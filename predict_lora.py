import re
import os
import torch
import transformers
from transformers import AutoTokenizer
import logging
from typing import  Dict

# LoraArguments need to import from train_lora,otherwise report bug 
from train_qlora import \
(
     DataArguments, ModelArguments,TrainingArguments, GenerationArguments, get_accelerate_model
)
from train_lora import load_model_tokenizer,LoraArguments
## todo merge different LoraArguments  definition, and adapte default value for two qlora and lora case


from datasets import load_dataset, Dataset

# LLM path
model_path = os.path.join("./model", os.listdir("model")[1])
# qlora adapter outputer path
checkpoint_dir = [os.path.join("./adapter", folder) for folder in os.listdir("./adapter") if "checkpoint" in folder][0]
dataset_format = "spider"
dataset = "spider"


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
        "I want you to act as a SQL terminal in front of an example database. "
        "Below is an instruction that describes a task, Write a response that appropriately completes the request.\n\n"
        "###Instruction:\n{instruction}\n\n###Input:\n{input}\n\n###Response: "
    ),
    "prompt_no_input": (
        "I want you to act as a SQL terminal in front of an example database. "
        "Below is an instruction that describes a task, Write a response that appropriately completes the request.\n\n"
        "###Instruction:\n{instruction}\n\n### Response: "
    ),
}


def extract_alpaca_dataset(example):
    if example.get("input", "") != "":
        prompt_format = ALPACA_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = ALPACA_PROMPT_DICT["prompt_no_input"]
    return {'input': prompt_format.format(**example)}

def extract_sql_dataset(example):
    if example.get("input", "") != "":
        prompt_format = SQL_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = SQL_PROMPT_DICT["prompt_no_input"]
    return {'input': prompt_format.format(**example)}

def local_dataset(dataset_name):
    if dataset_name.endswith('.json'):
        full_dataset = Dataset.from_json(path_or_paths=dataset_name)
    elif dataset_name.endswith('.jsonl'):
        full_dataset = Dataset.from_json(filename=dataset_name, format='jsonlines')
    elif dataset_name.endswith('.csv'):
        full_dataset = Dataset.from_pandas(pd.read_csv(dataset_name))
    elif dataset_name.endswith('.tsv'):
        full_dataset = Dataset.from_pandas(pd.read_csv(dataset_name, delimiter='\t'))
    else:
        raise ValueError(f"Unsupported dataset format: {dataset_name}")

    split_dataset = full_dataset.train_test_split(test_size=0.1)
    return split_dataset







def smart_tokenizer_and_embedding_resize(
    special_tokens_dict: Dict,
    tokenizer: transformers.PreTrainedTokenizer,
    model: transformers.PreTrainedModel,
):
    """Resize tokenizer and embedding.

    Note: This is the unoptimized version that may make your embedding size not be divisible by 64.
    """
    num_new_tokens = tokenizer.add_special_tokens(special_tokens_dict)
    model.resize_token_embeddings(len(tokenizer))
    
    if num_new_tokens > 0:
        input_embeddings_data = model.get_input_embeddings().weight.data
        output_embeddings_data = model.get_output_embeddings().weight.data

        input_embeddings_avg = input_embeddings_data[:-num_new_tokens].mean(dim=0, keepdim=True)
        output_embeddings_avg = output_embeddings_data[:-num_new_tokens].mean(dim=0, keepdim=True)

        input_embeddings_data[-num_new_tokens:] = input_embeddings_avg
        output_embeddings_data[-num_new_tokens:] = output_embeddings_avg


def predict():
    # Parse arguments
    hfparser = transformers.HfArgumentParser((
        ModelArguments, DataArguments, TrainingArguments, GenerationArguments,LoraArguments
    ))
    model_args, data_args, training_args, generation_args, lora_args= \
        hfparser.parse_args_into_dataclasses()
    training_args.generation_config = transformers.GenerationConfig(**vars(generation_args))
    import argparse
    args = argparse.Namespace(
        **vars(model_args), **vars(data_args), **vars(training_args), **vars(generation_args),**vars(lora_args)
    )
    # device = torch.device("cuda:0")
    # model,tokenizer = get_accelerate_model(args, checkpoint_dir) # qlora的
    # model.config.use_cache = False
    # model.to(device)

    # load model and tokenizer
    model, tokenizer = load_model_tokenizer(args=args)
    # tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    # tokenizer.pad_token = tokenizer.eos_token
    
    if 'llama' in args.model_name_or_path and tokenizer.pad_token is None:
        tokenizer.add_special_tokens({"pad_token": "[PAD]"})

    # # ## todo带测试
    # DEFAULT_PAD_TOKEN = "[PAD]"
    # if tokenizer._pad_token is None:
    #     smart_tokenizer_and_embedding_resize(
    #         special_tokens_dict=dict(pad_token=DEFAULT_PAD_TOKEN),
    #         tokenizer=tokenizer,
    #         model=model,
    #     )
        
    logging.warning('Successfully loaded model and tokenizer.')
    model.config.use_cache = False

   
    # Load dataset.
    def load_data(dataset_name):
        if dataset_name == 'alpaca':
            return load_dataset("tatsu-lab/alpaca")
        elif dataset_name == 'alpaca-clean':
            return load_dataset("yahma/alpaca-cleaned")
        elif dataset_name == 'chip2':
            return load_dataset("laion/OIG", data_files='unified_chip2.jsonl')
        elif dataset_name == 'self-instruct':
            return load_dataset("yizhongw/self_instruct", name='self_instruct')
        elif dataset_name == 'hh-rlhf':
            return load_dataset("Anthropic/hh-rlhf")
        elif dataset_name == 'longform':
            return load_dataset("akoksal/LongForm")
        elif dataset_name == 'oasst1':
            return load_dataset("timdettmers/openassistant-guanaco")
        elif dataset_name == 'vicuna':
            raise NotImplementedError("Vicuna data was not released.")
        elif dataset_name == 'spider':
            # return load_dataset("json", data_files="sql_fintune_data.json")
            return load_dataset("json", data_files="sql_finetune_data.json")
        else:
            if os.path.exists(dataset_name):
                try:
                    args.dataset_format = args.dataset_format if args.dataset_format else "input-output"
                    full_dataset = local_dataset(dataset_name)
                    return full_dataset
                except:
                    raise ValueError(f"Error loading dataset from {dataset_name}")
            else:
                raise NotImplementedError(f"Dataset {dataset_name} not implemented yet.")


    def format_dataset(dataset, dataset_format):
        if (
            dataset_format == 'alpaca' or dataset_format == 'alpaca-clean' or 
            (dataset_format is None and args.dataset in ['alpaca', 'alpaca-clean'])
        ):
            dataset = dataset.map(extract_alpaca_dataset, remove_columns=['instruction'])
        elif dataset_format == 'spider':
            dataset = dataset.map(extract_sql_dataset, remove_columns=['instruction'])
        elif dataset_format == 'chip2' or (dataset_format is None and args.dataset == 'chip2'):
            dataset = dataset.map(lambda x: {
                'input': x['text'].split('\n<bot>: ')[0].replace('<human>: ', ''),
                'output': x['text'].split('\n<bot>: ')[1],
            })
        elif dataset_format == 'self-instruct' or (dataset_format is None and args.dataset == 'self-instruct'):
            for old, new in [["prompt", "input"], ["completion", "output"]]:
                dataset = dataset.rename_column(old, new)
        elif dataset_format == 'hh-rlhf' or (dataset_format is None and args.dataset == 'hh-rlhf'):
            dataset = dataset.map(lambda x: {
                'input': '',
                'output': x['chosen']
            })
        elif dataset_format == 'oasst1' or (dataset_format is None and args.dataset == 'oasst1'):
            dataset = dataset.map(lambda x: {
                'input': '',
                'output': x['text'],
            })
        elif dataset_format == 'input-output':
            pass
        dataset = dataset.remove_columns(
            [col for col in dataset.column_names['train'] if col not in ['input', 'output']]
        )
        return dataset


     # Load dataset.
    dataset = load_data(args.dataset)
    dataset = format_dataset(dataset, args.dataset_format)
    dataset_labels = dataset["train"]["output"] #self

    dataset = dataset["train"]["input"]
    ## test
    result = []
    predict_batchsize = 2
    idx = 0
    print("just test show ,limit 100 examples\n")
    nums_examples =len(dataset)
    if nums_examples >10:
        nums_examples =10
    # print("an example as follows ")

    dataset_labels = dataset_labels[:nums_examples] #self zw

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

        ## add branch for different type model ,
        if re.search(r'(?i)falcon', model_path) in model_path:
            generate_kwargs = {
              "input_ids": encoded_inputs["input_ids"], 
              "attention_mask": encoded_inputs["attention_mask"]
            }
            outputs = model.generate(**generate_kwargs, max_length=512)
        elif  re.search(r'(?i)llama', model_path):
            outputs = model.generate(**encoded_inputs, max_length=512)
        else:
            print("right now,not support well")

        ## support the compared format directly ,like origin inputs: \n   orgin outputs labels \n  predict;
        for i,output in  enumerate(outputs):
            input_idx = idx-predict_batchsize+i
            prediction = tokenizer.decode(output, skip_special_tokens=True)
            response = re.split(r"Response:\s*", prediction)[-1]
            compose_i = "origin inputs:\t"+ dataset[input_idx].replace("\n", "") + "\n"+"orgin   outputs labels:\t" + dataset_labels[input_idx].replace("\n", "") + "\n"+"predict outputs labels:\t"+ response.replace("\n", "")
            result.append(compose_i)
        ## origin only predict format
        # for output in outputs:
        #     prediction = tokenizer.decode(output, skip_special_tokens=True)
        #     response = re.split(r"Response:\s*", prediction)[-1]
        #     result.append(response.replace("\n", ""))
        print(result)
        print(idx)
    return args.dataset, result




if __name__ == "__main__":

    dataset_name, result = predict()

    with open('data/'+ dataset_name +'/Llama2_dev_lora_pred_test6.sql', 'w') as f:
        for p in result:
            f.write(p + "\n")
