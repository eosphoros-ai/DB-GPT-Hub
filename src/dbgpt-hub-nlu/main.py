import os
import sys
from typing import TYPE_CHECKING, Tuple

import torch
from datasets import DatasetDict, load_dataset
from dbgpt_hub_nlu.config.dataset import DataArguments, InferArguments
from dbgpt_hub_nlu.config.model_args import ModelArguments, NLUTrainingArguments
from dbgpt_hub_nlu.model.simple import SimpleIntentClassifier
from dbgpt_hub_nlu.trainer import NLUTrainer, _load_base_model
from transformers import HfArgumentParser

if TYPE_CHECKING:
    from datasets import Features


def _load_model(
    input_dim: int, num_classes: int, device: torch.device
) -> SimpleIntentClassifier:
    model = SimpleIntentClassifier(input_dim, num_classes)
    model.to(device)
    return model


def _load_dataset(
    tokenizer,
    model,
    data_args: DataArguments,
    training_args: NLUTrainingArguments,
    just_infer: bool = False,
) -> Tuple[int, int, "Features", DatasetDict]:
    from dbgpt_hub_nlu.model.simple import batch_sentence_embeddings

    def handle_fin_func(batch):
        return {
            "input_ids": batch_sentence_embeddings(
                batch["text"], tokenizer, model, training_args.device
            ),
            "intent_label_ids": batch["label"],
        }

    ds = load_dataset(data_args.get_dataset_path())
    # Just has train split
    ds = ds["train"]
    if data_args.max_train_samples:
        ds = ds.select(range(data_args.max_train_samples))

    label_features = ds.features["label"]
    num_classes = label_features.num_classes

    if just_infer:
        return 1, num_classes, label_features, ds

    dataset = ds.map(
        handle_fin_func, batched=True, batch_size=training_args.train_batch_size
    )
    dataset = dataset.remove_columns(["text", "label"])
    ds_train_devtest = dataset.train_test_split(test_size=0.2, seed=42)
    ds_devtest = ds_train_devtest["test"].train_test_split(test_size=0.5, seed=42)

    input_dim = len(ds_train_devtest["train"][0]["input_ids"])
    ds_splits = DatasetDict(
        {
            "train": ds_train_devtest["train"],
            "valid": ds_devtest["train"],
            "test": ds_devtest["test"],
        }
    )
    return input_dim, num_classes, label_features, ds_splits


def main() -> None:
    # See all possible arguments by passing the --help flag to this script.
    parser = HfArgumentParser(
        (ModelArguments, DataArguments, NLUTrainingArguments, InferArguments)
    )
    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        # If we pass only one argument to the script and it's the path to a json file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args, infer_args = parser.parse_json_file(
            json_file=os.path.abspath(sys.argv[1])
        )
    else:
        (
            model_args,
            data_args,
            training_args,
            infer_args,
        ) = parser.parse_args_into_dataclasses()

    just_infer = (
        infer_args.do_infer
        and not training_args.do_train
        and not training_args.do_eval
        and not training_args.do_predict
    )

    base_tokenizer, base_model = _load_base_model(model_args)
    base_model = base_model.to(training_args.device)
    input_dim, num_classes, label_features, dataset = _load_dataset(
        base_tokenizer, base_model, data_args, training_args, just_infer=just_infer
    )
    model = _load_model(input_dim, num_classes, training_args.device)
    trainer = NLUTrainer(dataset, model, training_args)
    if model_args.model_name_or_path:
        trainer.load_model(model_args.model_name_or_path)

    if training_args.do_train:
        trainer.train()

    if training_args.do_eval:
        trainer.evaluate()

    if infer_args.do_infer:
        from dbgpt_hub_nlu.model.simple import batch_sentence_embeddings

        input_text = infer_args.input_text
        input_ids = batch_sentence_embeddings(
            [input_text], base_tokenizer, base_model, training_args.device
        )
        trainer.infer(input_ids, label_features)


if __name__ == "__main__":
    main()
