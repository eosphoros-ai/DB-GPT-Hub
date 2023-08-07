import re
import os
import torch
import transformers
from transformers import AutoTokenizer
from transformers import set_seed, Seq2SeqTrainer, GenerationConfig

from dbgpt_hub.configs import (
    DataArguments,
    GenerationArguments,
    LoraArguments,
    ModelArguments,
    QuantArguments,
    TrainingArguments,
)
from dbgpt_hub.model import get_accelerate_model

from datasets import load_dataset, Dataset
import pandas as pd
from peft import PeftModel
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base_model_name_or_path",
        type=str,
        default="/home/model_files/Llama-2-13b-chat-hf",
    )
    parser.add_argument(
        "--peft_ckpt_path", type=str, default="Your peft qlora ckpt path"
    )
    parser.add_argument("--input_data_json", type=str, default="dev_sql.json")
    parser.add_argument(
        "--output_name", type=str, default="./data/out_pred/qlora_8_lr_2e4_drop1e1.sql"
    )

    return parser.parse_args()


local_parser = get_args()


ALPACA_PROMPT_DICT = {
    "prompt_input": (
        "Below is an instruction that describes a task, paired with an input that provides further context. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response: "
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Response: "
    ),
}

SQL_PROMPT_DICT = {
    "prompt_input": (
        "I want you to act as a SQL terminal in front of an example database, \
         you need only to return the sql command to me.Below is an instruction that describes a task, \
         Write a response that appropriately completes the request.\n"
        "##Instruction:\n{instruction}\n###Input:\n{input}\n\n###Response:"
    ),
    "prompt_no_input": (
        "I want you to act as a SQL terminal in front of an example database, \
        you need only to return the sql command to me.Below is an instruction that describes a task, \
        Write a response that appropriately completes the request.\n"
        "####Instruction:\n{instruction}\n\###Response: "
    ),
}


def extract_alpaca_dataset(example):
    if example.get("input", "") != "":
        prompt_format = ALPACA_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = ALPACA_PROMPT_DICT["prompt_no_input"]
    return {"input": prompt_format.format(**example)}


def extract_sql_dataset(example):
    if example.get("input", "") != "":
        prompt_format = SQL_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = SQL_PROMPT_DICT["prompt_no_input"]
    return {"input": prompt_format.format(**example)}


def predict():
    # parameters
    parser = transformers.HfArgumentParser(
        (
            ModelArguments,
            DataArguments,
            TrainingArguments,
            LoraArguments,
            QuantArguments,
            GenerationArguments,
        )
    )
    (
        model_args,
        data_args,
        training_args,
        lora_args,
        quant_args,
        generation_args,
    ) = parser.parse_args_into_dataclasses()
    # Check arguments (do not check finetuning_args since it may be loaded from checkpoints)
    # data_args.init_for_training()
    training_args.generation_config = GenerationConfig(**vars(generation_args))
    import argparse

    args = argparse.Namespace(
        **vars(model_args),
        **vars(data_args),
        **vars(training_args),
        **vars(lora_args),
        **vars(quant_args),
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, tokenizer = get_accelerate_model(args, local_parser.peft_ckpt_path)
    model.config.use_cache = False

    def format_dataset(dataset, dataset_format):
        if (
            dataset_format == "alpaca"
            or dataset_format == "alpaca-clean"
            or (dataset_format is None and args.dataset in ["alpaca", "alpaca-clean"])
        ):
            dataset = dataset.map(
                extract_alpaca_dataset, remove_columns=["instruction"]
            )
        elif dataset_format == "spider":
            dataset = dataset.map(extract_sql_dataset, remove_columns=["instruction"])
        elif dataset_format == "chip2" or (
            dataset_format is None and args.dataset == "chip2"
        ):
            dataset = dataset.map(
                lambda x: {
                    "input": x["text"].split("\n<bot>: ")[0].replace("<human>: ", ""),
                    "output": x["text"].split("\n<bot>: ")[1],
                }
            )
        elif dataset_format == "self-instruct" or (
            dataset_format is None and args.dataset == "self-instruct"
        ):
            for old, new in [["prompt", "input"], ["completion", "output"]]:
                dataset = dataset.rename_column(old, new)
        elif dataset_format == "hh-rlhf" or (
            dataset_format is None and args.dataset == "hh-rlhf"
        ):
            dataset = dataset.map(lambda x: {"input": "", "output": x["chosen"]})
        elif dataset_format == "oasst1" or (
            dataset_format is None and args.dataset == "oasst1"
        ):
            dataset = dataset.map(
                lambda x: {
                    "input": "",
                    "output": x["text"],
                }
            )
        elif dataset_format == "input-output":
            pass
        dataset = dataset.remove_columns(
            [
                col
                for col in dataset.column_names["train"]
                if col not in ["input", "output"]
            ]
        )
        return dataset

    # Load dataset.
    dataset = load_dataset("json", data_files=local_parser.input_data_json)
    dataset = format_dataset(dataset, args.dataset_format)
    dataset_labels = dataset["train"]["output"]

    dataset = dataset["train"]["input"]

    result = []
    idx = 0
    predict_batchsize = 2
    nums_examples = len(dataset)
    # if nums_examples > 6:
    #     nums_examples = 6
    print(f"just test {nums_examples} examples\n")
    while idx < nums_examples:
        if idx + predict_batchsize < nums_examples:
            inputs = dataset[idx : idx + predict_batchsize]
            idx += predict_batchsize
        else:
            inputs = dataset[idx:nums_examples]
            idx = nums_examples
        encoded_inputs = tokenizer.batch_encode_plus(
            inputs, return_tensors="pt", padding=True, truncation=True, max_length=512
        )
        encoded_inputs = {
            name: tensor.to(device) for name, tensor in encoded_inputs.items()
        }

        # support different type LLM
        if re.search(r"(?i)falcon", local_parser.base_model_name_or_path):
            generate_kwargs = {
                "input_ids": encoded_inputs["input_ids"],
                "attention_mask": encoded_inputs["attention_mask"],
            }
            outputs = model.generate(**generate_kwargs, max_length=512)
        elif re.search(r"(?i)llama", local_parser.base_model_name_or_path):
            outputs = model.generate(**encoded_inputs, max_length=512)
        else:
            print("right now,not support well")

        # support the compared format directly ,like origin inputs: \n   orgin outputs labels \n  predict;
        for i, output in enumerate(outputs):
            input_idx = idx - predict_batchsize + i
            prediction = tokenizer.decode(output, skip_special_tokens=True)
            response = re.split(r"Response:\s*", prediction)[-1]
            # compose_i = "origin inputs:\t" + dataset[input_idx].replace("\n", "") + "\n"+"orgin   outputs labels:\t" + dataset_labels[input_idx].replace(
            # "\n", "") + "\n"+"predict outputs labels:\t" + response.replace("\n", "")
            # test
            compose_i = response.replace("\n", "")
            print(f"compos_i \t {compose_i}")
            result.append(compose_i)
        print(result)
        print(idx)
    return args.dataset, result


if __name__ == "__main__":
    dataset_name, result = predict()

    with open(local_parser.output_name, "w") as f:
        for p in result:
            f.write(p + "\n")
