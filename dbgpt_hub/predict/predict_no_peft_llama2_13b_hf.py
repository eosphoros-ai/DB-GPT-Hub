"""predict only base model ,no peft sft"""
import re
import os
import torch
import argparse
import transformers
from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer, LlamaTokenizer
from dbgpt_hub.configs import GenerationArguments, ModelInferenceArguments
from dbgpt_hub.configs.config import MODEL_PATH, OUT_DIR, DEFAULT_FT_MODEL_NAME
from dbgpt_hub.utils.model_utils import get_logits_processor
from dbgpt_hub.utils.model_utils import smart_tokenizer_and_embedding_resize
from dbgpt_hub.configs.data_args import DEFAULT_PROMPT_DICT,ALPACA_PROMPT_DICT,SQL_PROMPT_DICT


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base_model_name_or_path",
        type=str,
        default=os.path.join(MODEL_PATH, DEFAULT_FT_MODEL_NAME),
    )
    parser.add_argument("--input_data_json", type=str, default="dev_sql.json")
    parser.add_argument(
        "--output_name",
        type=str,
        default=OUT_DIR + "/predict_no_peft_llama2_13b_hf_new.sql",
    )

    return parser.parse_args()


local_parser = get_args()




def extract_sql_dataset(example):
    if example.get("input", "") != "":
        prompt_format = SQL_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = SQL_PROMPT_DICT["prompt_no_input"]
    return {"input": prompt_format.format(**example)}


def predict():
    # parameters
    parser = transformers.HfArgumentParser(
        (ModelInferenceArguments, GenerationArguments)
    )
    model_server_args, generation_args = parser.parse_args_into_dataclasses()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading base model: {model_server_args.model_name_or_path}")

    base_model = AutoModelForCausalLM.from_pretrained(
        local_parser.base_model_name_or_path,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16,
        device_map={"": 0},
    )

    model = base_model

    tokenizer = AutoTokenizer.from_pretrained(
        local_parser.base_model_name_or_path,
        trust_remote_code=True,
        use_fast=False,
    )
    if tokenizer._pad_token is None:
        smart_tokenizer_and_embedding_resize(
            special_tokens_dict=dict(pad_token="[PAD]"),
            tokenizer=tokenizer,
            model=model,
        )
    if "llama" in model_server_args.model_name_or_path or isinstance(
        tokenizer, LlamaTokenizer
    ):
        # LLaMA tokenizer may not have correct special tokens set.
        # Check and add them if missing to prevent them from being parsed into different tokens.
        # Note that these are present in the vocabulary.
        # Note also that `model.config.pad_token_id` is 0 which corresponds to `<unk>` token.
        print("Adding special tokens.")
        tokenizer.add_special_tokens(
            {
                "eos_token": tokenizer.convert_ids_to_tokens(model.config.eos_token_id),
                "bos_token": tokenizer.convert_ids_to_tokens(model.config.bos_token_id),
                "unk_token": tokenizer.convert_ids_to_tokens(
                    model.config.pad_token_id
                    if model.config.pad_token_id != -1
                    else tokenizer.pad_token_id
                ),
            }
        )
    model.config.use_cache = False
    # model.to(device)

    # Load dataset.
    dataset = load_dataset("json", data_files=local_parser.input_data_json)
    dataset = dataset.map(extract_sql_dataset, remove_columns=["instruction"])
    dataset = dataset["train"]["input"]

    result = []
    predict_batchsize = 1
    idx = 0
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
        outputs = model.generate(
            **encoded_inputs,
            **generation_args.to_dict(),
            logits_processor=get_logits_processor(),
        )

        # support the compared format directly ,like origin inputs: \n   orgin outputs labels \n  predict;
        for output in outputs:
            prediction = tokenizer.decode(output, skip_special_tokens=True)
            response = re.split(r"Response:\s*", prediction)[-1]
            print("response replace \n", response.replace("\n", ""))
            result.append(response.replace("\n", ""))

    return result


if __name__ == "__main__":
    result = predict()

    # Judge path exists, if not need create
    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)

    with open(local_parser.output_name, "w") as f:
        for p in result:
            f.write(p + "\n")
