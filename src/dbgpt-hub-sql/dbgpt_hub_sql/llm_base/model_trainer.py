import json
import math
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, Tuple, Union

import jieba
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
from peft import PeftModel
from rouge_chinese import Rouge
from transformers import Seq2SeqTrainer
from transformers.generation.logits_process import LogitsProcessor
from transformers.generation.utils import LogitsProcessorList
from transformers.modeling_utils import (
    PreTrainedModel,
    load_sharded_checkpoint,
    unwrap_model,
)
from transformers.trainer import (
    TRAINER_STATE_NAME,
    TRAINING_ARGS_NAME,
    WEIGHTS_INDEX_NAME,
    WEIGHTS_NAME,
)
from trl import PreTrainedModelWrapper

from ..configs.config import FINETUNING_ARGS_NAME, IGNORE_INDEX, VALUE_HEAD_FILE_NAME
from .config_parser import get_state_dict, get_train_args, load_trainable_params
from .load_tokenizer import load_model_and_tokenizer
from .loggings import get_logger

if TYPE_CHECKING:
    from transformers import PreTrainedTokenizer, Seq2SeqTrainingArguments, TrainerState
    from transformers.trainer import PredictionOutput

    from ..configs.model_args import FinetuningArguments


logger = get_logger(__name__)


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


@dataclass
class ComputeMetrics:
    r"""
    Wraps the tokenizer into metric functions, used in Seq2SeqPeftTrainer.
    """

    tokenizer: "PreTrainedTokenizer"

    def __call__(
        self, eval_preds: Sequence[Union[np.ndarray, Tuple[np.ndarray]]]
    ) -> Dict[str, float]:
        r"""
        Uses the model predictions to compute metrics.
        """
        preds, labels = eval_preds
        score_dict = {"rouge-1": [], "rouge-2": [], "rouge-l": [], "bleu-4": []}

        preds = np.where(preds != IGNORE_INDEX, preds, self.tokenizer.pad_token_id)
        labels = np.where(labels != IGNORE_INDEX, labels, self.tokenizer.pad_token_id)

        decoded_preds = self.tokenizer.batch_decode(preds, skip_special_tokens=True)
        decoded_labels = self.tokenizer.batch_decode(labels, skip_special_tokens=True)

        for pred, label in zip(decoded_preds, decoded_labels):
            hypothesis = list(jieba.cut(pred))
            reference = list(jieba.cut(label))

            if (
                len(" ".join(hypothesis).split()) == 0
                or len(" ".join(reference).split()) == 0
            ):
                result = {
                    "rouge-1": {"f": 0.0},
                    "rouge-2": {"f": 0.0},
                    "rouge-l": {"f": 0.0},
                }
            else:
                rouge = Rouge()
                scores = rouge.get_scores(" ".join(hypothesis), " ".join(reference))
                result = scores[0]

            for k, v in result.items():
                score_dict[k].append(round(v["f"] * 100, 4))

            bleu_score = sentence_bleu(
                [list(label)],
                list(pred),
                smoothing_function=SmoothingFunction().method3,
            )
            score_dict["bleu-4"].append(round(bleu_score * 100, 4))

        return {k: float(np.mean(v)) for k, v in score_dict.items()}


# Avoid runtime error in model.generate(do_sample=True).
class InvalidScoreLogitsProcessor(LogitsProcessor):
    def __call__(
        self, input_ids: torch.LongTensor, scores: torch.FloatTensor
    ) -> torch.FloatTensor:
        if torch.isnan(scores).any() or torch.isinf(scores).any():
            scores.zero_()
            scores[..., 0] = 1.0
        return scores


def get_logits_processor() -> LogitsProcessorList:
    logits_processor = LogitsProcessorList()
    logits_processor.append(InvalidScoreLogitsProcessor())
    return logits_processor


# metric used
def smooth(scalars: List[float]) -> List[float]:
    r"""
    EMA implementation according to TensorBoard.
    """
    last = scalars[0]
    smoothed = list()
    weight = 1.8 * (
        1 / (1 + math.exp(-0.05 * len(scalars))) - 0.5
    )  # a sigmoid function
    for next_val in scalars:
        smoothed_val = last * weight + (1 - weight) * next_val
        smoothed.append(smoothed_val)
        last = smoothed_val
    return smoothed


def plot_loss(
    save_dictionary: os.PathLike, keys: Optional[List[str]] = ["loss"]
) -> None:
    with open(
        os.path.join(save_dictionary, TRAINER_STATE_NAME), "r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    for key in keys:
        steps, metrics = [], []
        for i in range(len(data["log_history"])):
            if key in data["log_history"][i]:
                steps.append(data["log_history"][i]["step"])
                metrics.append(data["log_history"][i][key])

        if len(metrics) == 0:
            logger.warning(f"No metric {key} to plot.")
            continue

        plt.figure()
        plt.plot(steps, metrics, alpha=0.4, label="original")
        plt.plot(steps, smooth(metrics), label="smoothed")
        plt.title("training {} of {}".format(key, save_dictionary))
        plt.xlabel("step")
        plt.ylabel(key)
        plt.legend()
        plt.savefig(
            os.path.join(save_dictionary, "training_{}.png".format(key)),
            format="png",
            dpi=100,
        )
        print(
            "Figure saved:",
            os.path.join(save_dictionary, "training_{}.png".format(key)),
        )


def export_model(
    args: Optional[Dict[str, Any]] = None, max_shard_size: Optional[str] = "10GB"
):
    model_args, _, training_args, finetuning_args, _ = get_train_args(
        args, data_args_init=False
    )
    model, tokenizer = load_model_and_tokenizer(model_args, finetuning_args)
    model.save_pretrained(training_args.output_dir, max_shard_size=max_shard_size)
    try:
        tokenizer.save_pretrained(training_args.output_dir)
    except:
        logger.warning("Cannot save tokenizer, please copy the files manually.")
