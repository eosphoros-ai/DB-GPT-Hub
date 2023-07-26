import re
import os
import torch
import transformers
from transformers import AutoTokenizer
from train.train_qlora import \
(
    ModelArguments, DataArguments, TrainingArguments, GenerationArguments, 
    extract_alpaca_dataset, extract_sql_dataset, 
    local_dataset, load_dataset, 
    get_accelerate_model, 
    SQL_PROMPT_DICT, ALPACA_PROMPT_DICT, 
)


model_path = os.path.join("./model", os.listdir("model")[1])
checkpoint_dir = [os.path.join("./adapter", folder) for folder in os.listdir("./adapter") if "checkpoint" in folder][0]
dataset_format = "spider"
dataset = "spider"

def predict():
    # Parse arguments
    hfparser = transformers.HfArgumentParser((
        ModelArguments, DataArguments, TrainingArguments, GenerationArguments
    ))
    model_args, data_args, training_args, generation_args = \
        hfparser.parse_args_into_dataclasses()
    training_args.generation_config = transformers.GenerationConfig(**vars(generation_args))
    import argparse
    args = argparse.Namespace(
        **vars(model_args), **vars(data_args), **vars(training_args), **vars(generation_args)
    )
    device = torch.device("cuda:0")
    model,tokenizer = get_accelerate_model(args, checkpoint_dir)
    model.config.use_cache = False
    model.to(device)
   

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
            return load_dataset("json", data_files="sql_fintune_data.json")
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
    dataset = dataset["train"]["input"]

    result = []
    predict_batchsize = 24
    idx = 0
    while idx < len(dataset):
        if idx + predict_batchsize < len(dataset):
            inputs = dataset[idx: idx+predict_batchsize]
            idx += predict_batchsize
        else:
            inputs = dataset[idx: len(dataset)]
            idx = len(dataset)
        encoded_inputs = tokenizer.batch_encode_plus(inputs, 
                                                     return_tensors="pt", 
                                                     padding=True, truncation=True, 
                                                     max_length=512
                                                    )
        encoded_inputs = {name: tensor.to(device) for name, tensor in encoded_inputs.items()}
        outputs = model.generate(**encoded_inputs, max_length=512)
        for output in outputs:
            prediction = tokenizer.decode(output, skip_special_tokens=True)
            response = re.split(r"Response:\s*", prediction)[-1]
            result.append(response.replace("\n", ""))
        print(result)
        print(idx)
    return args.dataset, result




if __name__ == "__main__":

    dataset_name, result = predict()

    with open('data/'+ dataset_name +'/dev_pred.sql', 'w') as f:
        for p in result:
            f.write(p + "\n")
