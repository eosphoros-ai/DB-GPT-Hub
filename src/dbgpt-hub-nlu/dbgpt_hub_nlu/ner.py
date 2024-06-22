import ast

import evaluate
import numpy as np
import pandas as pd
import torch
from config.dataset import DataArguments, InferArguments
from config.model_args import ModelArguments, NLUTrainingArguments
from datasets import Dataset
from model.qwen import Qwen2ForTokenClassification
from peft import LoraConfig, PeftConfig, PeftModel, TaskType, get_peft_model
from transformers import (
    AutoTokenizer,
    DataCollatorForTokenClassification,
    HfArgumentParser,
    Trainer,
    pipeline,
)


def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_tokenizer(base_model_name_or_path):
    return AutoTokenizer.from_pretrained(base_model_name_or_path)


def load_dataset_from_excel(file_path):
    df = pd.read_excel(file_path)
    df["tokens"] = df["tokens"].apply(ast.literal_eval)
    df["labels"] = df["labels"].apply(ast.literal_eval)
    df["ner_tags"] = df["ner_tags"].apply(ast.literal_eval)
    dataset_dict = {
        "tokens": df["tokens"].tolist(),
        "labels": df["labels"].tolist(),
        "ner_tags": df["ner_tags"].tolist(),
    }
    return Dataset.from_dict(dataset_dict).train_test_split(test_size=0.2)


def prepare_model(args, label2id, id2label):
    model = Qwen2ForTokenClassification.from_pretrained(
        args.base_model_name_or_path,
        num_labels=len(label2id),
        id2label=id2label,
        label2id=label2id,
    ).bfloat16()

    peft_config = LoraConfig(
        task_type=TaskType.TOKEN_CLS,
        inference_mode=False,
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "up_proj",
            "gate_proj",
            "down_proj",
        ],
    )

    return get_peft_model(model, peft_config)


def tokenize_and_align_labels(examples, tokenizer, max_length):
    tokenized_inputs = tokenizer(
        examples["tokens"],
        is_split_into_words=True,
        padding="longest",
        max_length=max_length,
        truncation=True,
    )
    labels = []
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_ids.append(label[word_idx])
            else:
                label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs


def compute_metrics(p, label_list, seqeval):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)
    true_predictions = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    results = seqeval.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": results["overall_precision"],
        "recall": results["overall_recall"],
        "f1": results["overall_f1"],
        "accuracy": results["overall_accuracy"],
    }


def main():
    parser = HfArgumentParser(
        (ModelArguments, NLUTrainingArguments, DataArguments, InferArguments)
    )
    (
        model_args,
        training_args,
        data_args,
        infer_args,
    ) = parser.parse_args_into_dataclasses()

    device = get_device()
    print(f"Using device: {device}")

    tokenizer = load_tokenizer(model_args.base_model_name_or_path)
    seqeval = evaluate.load("seqeval")

    if data_args.dataset == "ner":
        label2id = {
            "O": 0,
            "B-CONT": 1,
            "I-CONT": 2,
            "B-EDU": 3,
            "I-EDU": 4,
            "B-LOC": 5,
            "I-LOC": 6,
            "B-NAME": 7,
            "I-NAME": 8,
            "B-ORG": 9,
            "I-ORG": 10,
            "B-PRO": 11,
            "I-PRO": 12,
            "B-RACE": 13,
            "I-RACE": 14,
            "B-TITLE": 15,
            "I-TITLE": 16,
        }
        ds = load_dataset_from_excel("./datasets/financial_report/data/ner.xlsx")
    else:
        raise NotImplementedError

    id2label = {v: k for k, v in label2id.items()}
    label_list = list(label2id.keys())

    if training_args.do_train:
        model = prepare_model(model_args, label2id, id2label)
        model.print_trainable_parameters()

        tokenized_ds = ds.map(
            lambda x: tokenize_and_align_labels(x, tokenizer, model_args.max_length),
            batched=True,
        )
        data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_ds["train"],
            eval_dataset=tokenized_ds["test"],
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics,
        )

        trainer.train()

    if infer_args.do_infer:
        adapter_path = "./output/checkpoint-500"
        tokenizer = AutoTokenizer.from_pretrained(adapter_path)
        peft_config = PeftConfig.from_pretrained(adapter_path)
        model = Qwen2ForTokenClassification.from_pretrained(
            peft_config.base_model_name_or_path,
            num_labels=len(label2id),
            id2label=id2label,
            label2id=label2id,
        )
        model = PeftModel.from_pretrained(model, adapter_path)
        # merge and unload is necessary for inference
        model = model.merge_and_unload()

        token_classifier = pipeline(
            "token-classification",
            model=model,
            tokenizer=tokenizer,
            aggregation_strategy="simple",
        )
        sentence = "康希诺生物股份公司在2020年的资产负债比率具体是多少?"
        tokens = token_classifier(sentence)
        print(tokens)


if __name__ == "__main__":
    main()
