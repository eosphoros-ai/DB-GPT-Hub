import os
import json
import torch
import numpy as np
import torch.nn as nn
from dbgpt_hub.configs.config import IGNORE_INDEX
from dbgpt_hub.llm_base.logging import get_logger
from dbgpt_hub.configs import VALUE_HEAD_FILE_NAME,FINETUNING_ARGS_NAME
from transformers import Seq2SeqTrainer
from transformers.trainer import TRAINING_ARGS_NAME, WEIGHTS_NAME
from transformers.modeling_utils import PreTrainedModel, unwrap_model,load_sharded_checkpoint
from transformers.trainer import WEIGHTS_NAME, WEIGHTS_INDEX_NAME
from peft import PeftModel
from trl import PreTrainedModelWrapper
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

if TYPE_CHECKING:
    from transformers import PreTrainedTokenizer, Seq2SeqTrainingArguments, TrainerState
    from transformers.trainer import PredictionOutput
    from dbgpt_hub.configs.model_args  import FinetuningArguments



logger = get_logger(__name__)


def get_state_dict(model: torch.nn.Module) -> Dict[str, torch.Tensor]:
    state_dict: Dict[str, torch.Tensor] = model.state_dict()
    filtered_state_dict = {}

    for k, v in model.named_parameters():
        if v.requires_grad:
            filtered_state_dict[k] = state_dict[k].cpu().clone().detach()

    return filtered_state_dict


def load_trainable_params(model: torch.nn.Module, checkpoint_dir: os.PathLike) -> bool:
    weights_file = os.path.join(checkpoint_dir, WEIGHTS_NAME)
    if os.path.exists(weights_file):
        model_state_dict = torch.load(weights_file, map_location="cpu")
        model.load_state_dict(model_state_dict, strict=False)  # skip missing keys
    elif os.path.exists(os.path.join(checkpoint_dir, WEIGHTS_INDEX_NAME)):
        load_sharded_checkpoint(model, checkpoint_dir, strict=False)
    else:
        logger.warning(
            "Provided path ({}) does not contain pre-trained weights.".format(
                checkpoint_dir
            )
        )
        return False
    return True



class PeftModelMixin:
    r"""
    Patches the save and load methods in Hugging Face Trainer for PeftModel and ModelWithValueHead.
    """

    def __init__(self) -> None:  # for type checking
        self.model: PreTrainedModel = None
        self.tokenizer: "PreTrainedTokenizer" = None
        self.args: "Seq2SeqTrainingArguments" = None
        self.finetuning_args: "FinetuningArguments" = None
        self.state: "TrainerState" = None
        raise AssertionError("Mixin should not be initialized.")

    def _save(
        self,
        output_dir: Optional[str] = None,
        state_dict: Optional[Dict[str, torch.Tensor]] = None,
    ) -> None:
        r"""
        Saves trainable parameters as model checkpoint.

        This function will only be executed at the process zero.

        Subclass and override to inject custom behavior. It should not be directly used by external scripts.
        """
        output_dir = output_dir if output_dir is not None else self.args.output_dir
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Saving model checkpoint to {output_dir}")

        model = unwrap_model(self.model)
        if isinstance(model, PreTrainedModelWrapper):
            # Custom state dict: https://github.com/lvwerra/trl/blob/v0.4.7/trl/models/modeling_value_head.py#L200
            model_state_dict = state_dict or model.state_dict()
            v_head_state_dict = {
                name.replace("v_head.", ""): model_state_dict[name]
                .cpu()
                .clone()
                .detach()
                for name in model_state_dict.keys()
                if name.startswith("v_head.")
            }

            torch.save(
                v_head_state_dict, os.path.join(output_dir, VALUE_HEAD_FILE_NAME)
            )
            model = model.pretrained_model

        state_dict = state_dict or get_state_dict(model)
        if isinstance(model, (PeftModel, PreTrainedModel)):
            model.config.use_cache = True
            model.save_pretrained(
                output_dir,
                state_dict=state_dict,
                safe_serialization=self.args.save_safetensors,
            )
            model.config.use_cache = False
        else:
            torch.save(state_dict, os.path.join(output_dir, WEIGHTS_NAME))

        if (
            self.finetuning_args.finetuning_type == "full"
            and self.tokenizer is not None
        ):
            try:
                self.tokenizer.save_pretrained(output_dir)
            except:
                logger.warning("Cannot save tokenizer, copy the files manually.")

        with open(
            os.path.join(output_dir, TRAINING_ARGS_NAME), "w", encoding="utf-8"
        ) as f:
            f.write(self.args.to_json_string() + "\n")

        self.finetuning_args.save_to_json(
            os.path.join(output_dir, FINETUNING_ARGS_NAME)
        )

    def _load_best_model(self):
        r"""
        Loads trainable parameters from model checkpoint.

        Subclass and override to inject custom behavior. It should not be directly used by external scripts.
        """
        logger.info(
            f"Loading best model from {self.state.best_model_checkpoint} (score: {self.state.best_metric})."
        )
        model = unwrap_model(self.model)

        if isinstance(model, PreTrainedModelWrapper):
            model.v_head.load_state_dict(
                torch.load(
                    os.path.join(
                        self.state.best_model_checkpoint, VALUE_HEAD_FILE_NAME
                    ),
                    map_location="cpu",
                )
            )
            model = model.pretrained_model

        if isinstance(model, PeftModel):
            model.load_adapter(self.state.best_model_checkpoint, model.active_adapter)
        else:  # freeze/full-tuning
            load_trainable_params(model, self.state.best_model_checkpoint)



class PeftTrainer(PeftModelMixin, Seq2SeqTrainer):
    r"""
    Inherits Seq2SeqTrainer to support parameter-efficient checkpoints.
    """

    def __init__(self, finetuning_args: "FinetuningArguments", **kwargs):
        Seq2SeqTrainer.__init__(self, **kwargs)
        self.finetuning_args = finetuning_args



class Seq2SeqPeftTrainer(PeftTrainer):
    r"""
    Inherits PeftTrainer to compute generative metrics such as BLEU and ROUGE.
    """

    def prediction_step(
        self,
        model: nn.Module,
        inputs: Dict[str, Union[torch.Tensor, Any]],
        prediction_loss_only: bool,
        ignore_keys: Optional[List[str]] = None,
    ) -> Tuple[Optional[float], Optional[torch.Tensor], Optional[torch.Tensor]]:
        r"""
        Removes the prompt part in the generated tokens.

        Subclass and override to inject custom behavior.
        """
        prompt_len, label_len = inputs["input_ids"].size(-1), inputs["labels"].size(-1)
        if prompt_len > label_len:
            inputs["labels"] = self._pad_tensors_to_target_len(
                inputs["labels"], inputs["input_ids"]
            )
        if label_len > prompt_len:
            inputs["input_ids"] = self._pad_tensors_to_target_len(
                inputs["input_ids"], inputs["labels"]
            )
            if "attention_mask" in inputs:
                inputs["attention_mask"] = self._pad_tensors_to_target_len(
                    inputs["attention_mask"], inputs["labels"], pad_token_id=0
                )
            if "position_ids" in inputs:
                inputs["position_ids"] = self._pad_tensors_to_target_len(
                    inputs["position_ids"], inputs["labels"], pad_token_id=0
                )

        loss, generated_tokens, labels = super().prediction_step(
            model,
            inputs,
            prediction_loss_only=prediction_loss_only,
            ignore_keys=ignore_keys,
        )
        if generated_tokens is not None:
            generated_tokens[
                :, : max(prompt_len, label_len)
            ] = self.tokenizer.pad_token_id * torch.ones_like(
                generated_tokens[:, : max(prompt_len, label_len)]
            )

        return loss, generated_tokens, labels

    def _pad_tensors_to_target_len(
        self,
        src_tensor: torch.Tensor,
        tgt_tensor: torch.Tensor,
        pad_token_id: Optional[int] = None,
    ) -> torch.Tensor:
        r"""
        Pads the tensor to the same length as the target tensor.

        Should only be called when predict_with_generate=True.
        """
        if pad_token_id is None:
            if self.tokenizer is not None and hasattr(self.tokenizer, "pad_token_id"):
                assert (
                    self.tokenizer.padding_side == "left"
                ), "This method only accepts left-padded tensor."
                pad_token_id = self.tokenizer.pad_token_id
            else:
                raise ValueError("PAD token is required.")

        padded_tensor = pad_token_id * torch.ones_like(tgt_tensor)
        padded_tensor[:, -src_tensor.shape[-1] :] = src_tensor  # adopt left-padding
        return padded_tensor.contiguous()  # in contiguous memory

    def save_predictions(self, predict_results: "PredictionOutput") -> None:
        r"""
        Saves model predictions to `output_dir`.

        A custom behavior that not contained in Seq2SeqTrainer.
        """
        if not self.is_world_process_zero():
            return

        output_prediction_file = os.path.join(
            self.args.output_dir, "generated_predictions.jsonl"
        )
        logger.info(f"Saving prediction results to {output_prediction_file}")

        preds = np.where(
            predict_results.predictions != IGNORE_INDEX,
            predict_results.predictions,
            self.tokenizer.pad_token_id,
        )
        labels = np.where(
            predict_results.label_ids != IGNORE_INDEX,
            predict_results.label_ids,
            self.tokenizer.pad_token_id,
        )

        decoded_preds = self.tokenizer.batch_decode(
            preds, skip_special_tokens=True, clean_up_tokenization_spaces=True
        )
        decoded_labels = self.tokenizer.batch_decode(
            labels, skip_special_tokens=True, clean_up_tokenization_spaces=True
        )

        with open(output_prediction_file, "w", encoding="utf-8") as writer:
            res: List[str] = []
            for pred, label in zip(decoded_preds, decoded_labels):
                res.append(
                    json.dumps({"label": label, "predict": pred}, ensure_ascii=False)
                )
            writer.write("\n".join(res))