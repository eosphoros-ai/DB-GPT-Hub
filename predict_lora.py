import re
import os
import torch
import pandas as pd
import transformers
from transformers import AutoTokenizer
from transformers import (AutoModelForCausalLM, AutoTokenizer,  LlamaTokenizer)
from dbgpt_hub.configs import (GenerationArguments,ModelInferenceArguments)
from datasets import load_dataset, Dataset
from dbgpt_hub.utils.model_utils import get_logits_processor
from dbgpt_hub.utils.model_utils import smart_tokenizer_and_embedding_resize

SQL_PROMPT_DICT = {
    "prompt_input": (
        "I want you to act as a SQL terminal in front of an example database, you only need to return the sql command to me.Below is an instruction that describes a task, Write a response that appropriately completes the request.  The instruction is {instruction}, So please tell me {input} ###Response:"
    ),
    "prompt_no_input": (
        "I want you to act as a SQL terminal in front of an example database, you only need to return the sql command to me.Below is an instruction that describes a task, Write a response that appropriately completes the request.  The instruction is {instruction}, ###Response:"
    ),
}

def extract_sql_dataset(example):
    if example.get("input", "") != "":
        prompt_format = SQL_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = SQL_PROMPT_DICT["prompt_no_input"]
    return {'input': prompt_format.format(**example)}


def predict():
    # parameters 
    parser = transformers.HfArgumentParser(
        (ModelInferenceArguments, GenerationArguments))
    model_server_args, generation_args = parser.parse_args_into_dataclasses()

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = AutoModelForCausalLM.from_pretrained(
        model_server_args.model_name_or_path,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16,
        device_map={"":0})

    tokenizer = AutoTokenizer.from_pretrained(
        model_server_args.model_name_or_path,
        trust_remote_code=True,
        use_fast=False,
    )
    if tokenizer._pad_token is None:
        smart_tokenizer_and_embedding_resize(
            special_tokens_dict=dict(pad_token='[PAD]'),
            tokenizer=tokenizer,
            model=model,
        )
    if 'llama' in model_server_args.model_name_or_path or isinstance(tokenizer, LlamaTokenizer):
        # LLaMA tokenizer may not have correct special tokens set.
        # Check and add them if missing to prevent them from being parsed into different tokens.
        # Note that these are present in the vocabulary.
        # Note also that `model.config.pad_token_id` is 0 which corresponds to `<unk>` token.
        print('Adding special tokens.')
        tokenizer.add_special_tokens({
                "eos_token": tokenizer.convert_ids_to_tokens(model.config.eos_token_id),
                "bos_token": tokenizer.convert_ids_to_tokens(model.config.bos_token_id),
                "unk_token": tokenizer.convert_ids_to_tokens(
                    model.config.pad_token_id if model.config.pad_token_id != -1 else tokenizer.pad_token_id
                ),
        })
    model.config.use_cache = False
    # model.to(device)



    # Load dataset.
    dataset = load_dataset("json", data_files="dev_sql.json")
    dataset = dataset.map(extract_sql_dataset, remove_columns=['instruction'])
    # dataset_labels = dataset["train"]["output"] 
    dataset = dataset["train"]["input"]

    result = []
    predict_batchsize = 1
    idx = 0
    nums_examples =len(dataset)
    while idx < nums_examples:
        if idx + predict_batchsize < nums_examples:
            inputs = dataset[idx: idx+predict_batchsize]
            idx += predict_batchsize
        else:
            inputs = dataset[idx: nums_examples]
            idx = nums_examples
        encoded_inputs = tokenizer.batch_encode_plus(inputs, 
                                                     return_tensors="pt", 
                                                     padding=True, truncation=True, 
                                                     max_length=512
                                                    )
        encoded_inputs = {name: tensor.to(device) for name, tensor in encoded_inputs.items()}
        outputs = model.generate(
                **encoded_inputs, 
                **generation_args.to_dict(), 
                logits_processor=get_logits_processor()
            )
        # ## support different type LLM 
        # if re.search(r'(?i)falcon', model_path):
        #     generate_kwargs = {
        #       "input_ids": encoded_inputs["input_ids"], 
        #       "attention_mask": encoded_inputs["attention_mask"]
        #     }
        #     outputs = model.generate(**generate_kwargs, max_length=512)
        # elif  re.search(r'(?i)llama', model_path):
        #     outputs = model.generate(
        #         **encoded_inputs, 
        #         max_new_tokens=512, 
        #         generation_config = training_args.generation_config, 
        #         logits_processor=get_logits_processor()
        #     )
        # else:
        #     print("right now,not support well")

        ## support the compared format directly ,like origin inputs: \n   orgin outputs labels \n  predict;
        for output in  outputs:
            prediction = tokenizer.decode(output, skip_special_tokens=True)
            response = re.split(r"Response:\s*", prediction)[-1]
            result.append(response)
            print(response)
            print(idx)
        ## origin only predict format
        # for output in outputs:
        #     prediction = tokenizer.decode(output, skip_special_tokens=True)
        #     response = re.split(r"Response:\s*", prediction)[-1]
        #     result.append(response.replace("\n", ""))
    return result





if __name__ == "__main__":

    result = predict()

    with open('dev_pred.sql', 'w') as f:
        for p in result:
            f.write(p + "\n")
