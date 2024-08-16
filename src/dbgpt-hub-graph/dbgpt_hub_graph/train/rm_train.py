import json
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
import torch
from dbgpt_hub_gql.data_process.data_utils import (
    get_dataset,
    preprocess_dataset,
    split_dataset,
)
from dbgpt_hub_gql.llm_base.config_parser import get_train_args
from dbgpt_hub_gql.llm_base.load_tokenizer import load_model_and_tokenizer
from dbgpt_hub_gql.llm_base.loggings import LogCallback, get_logger
from dbgpt_hub_gql.llm_base.model_trainer import plot_loss
from transformers import (
    DataCollatorWithPadding,
    Seq2SeqTrainingArguments,
    Trainer,
    TrainerCallback,
    TrainerControl,
    TrainerState,
    TrainingArguments,
)
from transformers.modeling_utils import custom_object_save, unwrap_model
from transformers.trainer_utils import PREFIX_CHECKPOINT_DIR, has_length

if TYPE_CHECKING:
    from dbgpt_hub_gql.configs.data_args import DataArguments
    from dbgpt_hub_gql.configs.model_args import (
        FinetuningArguments,
        GeneratingArguments,
        ModelArguments,
    )
    from transformers.modeling_utils import PreTrainedModel
    from transformers.trainer import PredictionOutput
    from trl import AutoModelForCausalLMWithValueHead

logger = get_logger(__name__)


@dataclass
class PairwiseDataCollatorWithPadding(DataCollatorWithPadding):
    r"""
    Data collator for pairwise data.
    """

    def __call__(self, features: Sequence[Dict[str, Any]]) -> Dict[str, torch.Tensor]:
        r"""
        Pads batched data to the longest sequence in the batch.

        We generate 2 * n examples where the first n examples represent chosen examples and
        the last n examples represent rejected examples.
        """
        features = [
            {
                "input_ids": feature["prompt_ids"] + feature[key],
                "attention_mask": [1]
                * (len(feature["prompt_ids"]) + len(feature[key])),
            }
            for key in ("chosen_ids", "rejected_ids")
            for feature in features
        ]
        return super().__call__(features)


class PairwiseTrainer(Trainer):
    r"""
    Inherits PeftTrainer to compute pairwise loss.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.can_return_loss = True  # override property to return eval_loss

    def compute_loss(
        self,
        model: "PreTrainedModel",
        inputs: Dict[str, torch.Tensor],
        return_outputs: Optional[bool] = False,
    ) -> Union[torch.Tensor, Tuple[torch.Tensor, List[torch.Tensor]]]:
        r"""
        Computes pairwise loss. The first n examples are chosen and the last n examples are rejected.

        Subclass and override to inject custom behavior.

        Note that the first element will be removed from the output tuple.
        See: https://github.com/huggingface/transformers/blob/v4.30.2/src/transformers/trainer.py#L3509
        """
        # Compute rewards
        _, _, values = model(**inputs, output_hidden_states=True, return_dict=True)

        unwrapped_model: "PreTrainedModel" = self.accelerator.unwrap_model(self.model)
        if getattr(unwrapped_model.config, "model_type", None) == "chatglm":
            values = torch.transpose(values, 0, 1)

        # Split the inputs and rewards into two parts, chosen and rejected
        batch_size = inputs["input_ids"].size(0) // 2
        chosen_input_ids, rejected_input_ids = (
            inputs["input_ids"][:batch_size],
            inputs["input_ids"][batch_size:],
        )
        chosen_rewards, rejected_rewards = values[:batch_size], values[batch_size:]
        chosen_scores, rejected_scores = [], []

        # Compute pairwise loss. Only backprop on the different tokens before padding
        # Inspired by: https://github.com/CarperAI/trlx/blob/main/examples/summarize_rlhf/reward_model/reward_model.py
        loss = 0
        for i in range(batch_size):
            chosen_length = (
                chosen_input_ids[i] != self.tokenizer.pad_token_id
            ).nonzero()[-1] + 1
            rejected_length = (
                rejected_input_ids[i] != self.tokenizer.pad_token_id
            ).nonzero()[-1] + 1
            check_divergence = (chosen_input_ids[i] != rejected_input_ids[i]).nonzero()

            if len(check_divergence) == 0:
                end_index = chosen_length
                div_index = end_index - 1
            else:
                end_index = max(chosen_length, rejected_length)
                div_index = check_divergence[0]

            assert div_index > 0
            chosen_trunc_rewards = chosen_rewards[i, div_index:end_index]
            rejected_trunc_rewards = rejected_rewards[i, div_index:end_index]
            if (
                return_outputs
            ):  # use the score on the last token except pad token for inference
                chosen_scores.append(chosen_rewards[i, chosen_length - 1])
                rejected_scores.append(rejected_rewards[i, rejected_length - 1])
            loss += -torch.nn.functional.logsigmoid(
                chosen_trunc_rewards - rejected_trunc_rewards
            ).mean()

        loss = loss / batch_size
        if return_outputs:
            chosen_scores, rejected_scores = torch.stack(chosen_scores), torch.stack(
                rejected_scores
            )
            return loss, [loss, chosen_scores, rejected_scores]

        return loss

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
        chosen_scores, rejected_scores = predict_results.predictions

        with open(output_prediction_file, "w", encoding="utf-8") as writer:
            res: List[str] = []
            for c_score, r_score in zip(chosen_scores, rejected_scores):
                res.append(
                    json.dumps(
                        {
                            "chosen": round(float(c_score), 2),
                            "rejected": round(float(r_score), 2),
                        }
                    )
                )
            writer.write("\n".join(res))


class SavePeftModelCallback(TrainerCallback):
    def _save_model_with_valuehead(
        self, model: "AutoModelForCausalLMWithValueHead", output_dir: str
    ) -> None:
        model.pretrained_model.config.save_pretrained(output_dir)
        if model.pretrained_model.can_generate():
            model.pretrained_model.generation_config.save_pretrained(output_dir)
        if getattr(model, "is_peft_model", False):
            model.pretrained_model.save_pretrained(output_dir)
        elif getattr(
            model.pretrained_model, "_auto_class", None
        ):  # must not a peft model
            custom_object_save(
                model.pretrained_model, output_dir, config=model.pretrained_model.config
            )

    def on_save(
        self,
        args: "TrainingArguments",
        state: "TrainerState",
        control: "TrainerControl",
        **kwargs,
    ):
        r"""
        Event called after a checkpoint save.
        """
        if args.should_save:
            self._save_model_with_valuehead(
                model=unwrap_model(kwargs.pop("model")),
                output_dir=os.path.join(
                    args.output_dir,
                    "{}-{}".format(PREFIX_CHECKPOINT_DIR, state.global_step),
                ),
            )

    def on_train_end(
        self,
        args: "TrainingArguments",
        state: "TrainerState",
        control: "TrainerControl",
        **kwargs,
    ):
        r"""
        Event called at the end of training.
        """

        if args.should_save:
            self._save_model_with_valuehead(
                model=unwrap_model(kwargs.pop("model")), output_dir=args.output_dir
            )


def compute_accuracy(
    eval_preds: Sequence[Union[np.ndarray, Tuple[np.ndarray]]]
) -> Dict[str, float]:
    preds, _ = eval_preds
    return {"accuracy": (preds[0] > preds[1]).sum() / len(preds[0])}


def run_rm(
    model_args: "ModelArguments",
    data_args: "DataArguments",
    training_args: "Seq2SeqTrainingArguments",
    finetuning_args: "FinetuningArguments",
    callbacks: Optional[List["TrainerCallback"]] = None,
):
    dataset = get_dataset(model_args, data_args)
    model, tokenizer = load_model_and_tokenizer(
        model_args, finetuning_args, training_args.do_train, add_valuehead=True
    )
    dataset = preprocess_dataset(
        dataset, tokenizer, data_args, training_args, stage="rm"
    )
    data_collator = PairwiseDataCollatorWithPadding(tokenizer, pad_to_multiple_of=8)

    # Update arguments
    training_args_dict = training_args.to_dict()
    training_args_dict.update(
        dict(remove_unused_columns=False)
    )  # important for pairwise dataset
    training_args = Seq2SeqTrainingArguments(**training_args_dict)

    # Initialize our Trainer
    trainer = PairwiseTrainer(
        model=model,
        args=training_args,
        tokenizer=tokenizer,
        data_collator=data_collator,
        callbacks=callbacks + [SavePeftModelCallback()],
        compute_metrics=compute_accuracy,
        **split_dataset(dataset, data_args, training_args),
    )

    # Training
    if training_args.do_train:
        train_result = trainer.train(
            resume_from_checkpoint=training_args.resume_from_checkpoint
        )
        trainer.save_model()
        trainer.log_metrics("train", train_result.metrics)
        trainer.save_metrics("train", train_result.metrics)
        trainer.save_state()
        if trainer.is_world_process_zero() and model_args.plot_loss:
            plot_loss(training_args.output_dir, keys=["loss", "eval_loss"])

    # Evaluation
    if training_args.do_eval:
        metrics = trainer.evaluate(metric_key_prefix="eval")
        trainer.log_metrics("eval", metrics)
        trainer.save_metrics("eval", metrics)

    # Predict
    if training_args.do_predict:
        predict_results = trainer.predict(dataset, metric_key_prefix="predict")
        trainer.log_metrics("predict", predict_results.metrics)
        trainer.save_metrics("predict", predict_results.metrics)
        trainer.save_predictions(predict_results)


def train(
    args: Optional[Dict[str, Any]] = None,
    callbacks: Optional[List["TrainerCallback"]] = None,
):
    (
        model_args,
        data_args,
        training_args,
        finetuning_args,
        generating_args,
    ) = get_train_args(args)
    callbacks = [LogCallback()] if callbacks is None else callbacks

    run_rm(
        model_args,
        data_args,
        training_args,
        finetuning_args,
        callbacks,
    )


if __name__ == "__main__":
    train()
