import os
import numpy as np
import pandas as pd

from typing import Any, Dict, List, Optional, Tuple, Union
from datasets import Dataset, DatasetDict, concatenate_datasets, load_dataset

IGNORE_INDEX = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "<s>"
DEFAULT_UNK_TOKEN = "<unk>"

DEFAULT_PROMPT_DICT = {
    "prompt_input": ("{instruction}\n\n{input}\n\n"),
    "prompt_no_input": ("{instruction}\n\n"),
}

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


def extract_default_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
    # Not random, use pre-defined templates
    if example.get("input", "") != "":
        prompt_template = DEFAULT_PROMPT_DICT["prompt_input"]
    else:
        prompt_template = DEFAULT_PROMPT_DICT["prompt_no_input"]

    # Format prompt with example
    formated_prompt = prompt_template.format(**example)

    return {"input": formated_prompt}


def extract_alpaca_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
    if example.get("input", "") != "":
        prompt_format = ALPACA_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = ALPACA_PROMPT_DICT["prompt_no_input"]
    return {"input": prompt_format.format(**example)}


def extract_sql_dataset(example: Dict[str, Any]) -> Dict[str, str]:
    if example.get("input", "") != "":
        prompt_format = SQL_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = SQL_PROMPT_DICT["prompt_no_input"]
    return {"input": prompt_format.format(**example)}


def local_dataset(
    dataset_path: str, eval_dataset_size: float = 0.1
) -> Tuple[Dataset, Dataset]:
    """
    Reads in a dataset from a file and returns it as a split train-test dataset.

    Args:
        dataset_path (str): The name of the dataset file to read in. \
            The format is inferred based on the file extension.

    Returns:
        A tuple containing two datasets - the training subset and the testing subset.
    Raises:
        ValueError: If the specified file format is unsupported.

    """

    # Read in the full dataset from file based on the file format
    if dataset_path.endswith(".json"):
        full_dataset = load_dataset("json", data_files=dataset_path)
    elif dataset_path.endswith(".jsonl"):
        full_dataset = load_dataset("json", data_files=dataset_path)
    elif dataset_path.endswith(".csv"):
        full_dataset = Dataset.from_pandas(pd.read_csv(dataset_path))
    elif dataset_path.endswith(".tsv"):
        full_dataset = Dataset.from_pandas(pd.read_csv(dataset_path, delimiter="\t"))
    else:
        raise ValueError(f"Unsupported dataset format: {dataset_path}")
    if "train" not in full_dataset:
        split_dataset = full_dataset.train_test_split(test_size=eval_dataset_size)
        return split_dataset
    else:
        return full_dataset


def load_data(
    dataset_path: str, eval_dataset_size: float = 0.1
) -> Union[Dict[str, Dataset], None]:
    """
    Load a dataset based on its name.

    Args:
        dataset_path: A string representing the path to the dataset to be loaded.

    Returns:
        A dictionary containing the loaded dataset if the dataset exists.
        None if the dataset does not exist.

    Raises:
        NotImplementedError: If the dataset name provided is not implemented yet or if
            the dataset is not released.

    Examples:
        >>> load_data('alpaca')
        {'train': Dataset(...), 'validation': Dataset(...), 'test': Dataset(...)}

    """
    if not os.path.exists(dataset_path):
        # Download dataset from HuggingFace Datasets
        print(
            f"Lodding dataset from huggingface, please ref to https://huggingface.co/datasets/{dataset_path}"
        )
        dataset = load_dataset(dataset_path, cache_dir="~/.cache/huggingface/datasets")
        return dataset
    else:
        # Load dataset from local file
        try:
            print(f"Lodding dataset from local path: {dataset_path}")
            dataset = local_dataset(dataset_path, eval_dataset_size)
            return dataset
        except:
            raise ValueError(f"Error loading dataset from {dataset_path}")


def formate_instruction_dataset(
    dataset: Dataset,
    dataset_name: str,
    dataset_format: str,
    instruction_template: str = "default",
) -> Optional[Dict[str, Dataset]]:
    """
    Formats a given dataset based on its name and format.


    Removes unused columns, renames columns to 'input' and 'output',
    and applies dataset-specific formatting based on the dataset_name.

    Returns formatted dataset dict if dataset can be formatted, else None.

    Args:
        dataset: A dataset object to be formatted.
        dataset_name: A string representing the name of the dataset to be formatted.
        dataset_format: A string representing the name of the dataset format to be used.
        instruction_template: A string representing the name of the prompt template to be used.

    Returns:
        A dictionary containing the formatted dataset if the dataset exists in the
        specified format.
        None if the dataset does not exist or if the format is not recognized.
    """

    def _format_self_instruct(dataset: Dataset) -> Dataset:
        """Format Self-Instruct dataset.

        hf_url: https://huggingface.co/datasets/yizhongw/self_instruct/viewer/self_instruct/train
        """
        dataset = dataset.rename_column("prompt", "input")
        dataset = dataset.rename_column("completion", "output")
        return dataset

    def _remove_unused_columns(dataset):
        """Remove columns not named 'input' or 'output'."""
        dataset = dataset.remove_columns(
            [
                col
                for col in dataset.column_names["train"]
                if col not in ["input", "output"]
            ]
        )
        return dataset

    # Format dataset
    print(f"The {dataset_name} using {dataset_format} dataset format.")
    if dataset_format == "alpaca":
        print("By default, We support the Alpaca dataset format.")
    elif dataset_format == "spider":
        print("By default, We support the spider dataset format.")
    elif dataset_format == "self-instruct":
        dataset = _format_self_instruct(dataset)
    # elif dataset_format == "hh-rlhf":
    #     dataset = _format_hh_rlhf(dataset)
    # elif dataset_format == "oasst1":
    #     dataset = _format_oasst1(dataset)
    # elif dataset_format == "100PoisonMpts":
    #     dataset = _format_100Poison(dataset)
    # elif dataset_format == "dolly":
    #     dataset = _format_dolly15k(dataset)
    # elif dataset_format == "chip2":
    #     dataset = _format_chip2(dataset)
    else:
        raise NotImplementedError(
            f"Unsupported dataset format: {dataset_format},  Please add the formate function in data_utils.py"
        )
    # encode_instruction_example
    print(f"Applying instruction template: {instruction_template}")
    if instruction_template == "alpaca":
        dataset = dataset.map(extract_alpaca_prompt_dataset)
    # elif instruction_template == "spider":
    #     dataset = dataset.map(extract_sql_prompt_dataset)
    # elif instruction_template == "random":
    #     dataset = dataset.map(extract_random_prompt_dataset)
    else:
        dataset = dataset.map(extract_default_prompt_dataset)

    # Remove unused columns.
    print("Removing the unused columns, keep only 'input' and 'output'")
    dataset = _remove_unused_columns(dataset)

    return dataset


def split_train_eval(
    dataset: Dataset,
    do_eval: bool = False,
    eval_dataset_size: float = 0.1,
    max_eval_samples: int = None,
    do_train: bool = True,
    max_train_samples: int = None,
) -> Dict[str, Dataset]:
    """
    Prepare the training and evaluation datasets for a machine learning model.

    Args:
        dataset (DatasetDict): The complete dataset containing train, validation, and test splits.
        do_eval (bool, optional): Whether to use an evaluation dataset or not. Defaults to False.
        eval_dataset_size (float, optional): The size of the validation set if splitting from the training data.
            Ignored if `do_eval` is False. Defaults to 0.2.
        max_eval_samples (int, optional): The maximum number of samples to keep in the evaluation dataset.
            Ignored if `do_eval` is False or `None`. Defaults to None.
        do_train (bool, optional): Whether to use a training dataset or not. Defaults to True.
        max_train_samples (int, optional): The maximum number of samples to keep in the training dataset.
            Ignored if `do_train` is False or `None`. Defaults to None.

    Returns:
        Dict[str, Dataset]: A dictionary containing the prepared training and evaluation datasets
        (if used), where the keys are 'train' and 'eval', respectively.
    """
    if not isinstance(dataset, DatasetDict):
        raise TypeError("The 'dataset' argument must be a DatasetDict object.")

    train_dataset, eval_dataset = None, None
    # Prepare evaluation dataset
    if do_eval:
        if "eval" in dataset:
            eval_dataset = dataset["eval"]
        else:
            # Split train dataset in train and validation according to `eval_dataset_size`
            print(
                f"Splitting the dataset into train and validation according to `eval_dataset_size`:  {eval_dataset_size}"
            )
            dataset = dataset["train"].train_test_split(
                test_size=eval_dataset_size, shuffle=True, seed=42
            )
            eval_dataset = dataset["test"]

        # Reduce evaluation dataset size (if specified)
        print(
            f"You have set the max_eval_samples: {max_eval_samples}, will do sampling ..."
        )
        if max_eval_samples is not None and len(eval_dataset) > max_eval_samples:
            eval_dataset = eval_dataset.select(np.arange(max_eval_samples))

    # Prepare training dataset
    if do_train:
        train_dataset = dataset["train"]

        # Reduce training dataset size (if specified)
        print(
            f"You have set the max_train_samples: {max_train_samples}, will do sampling ..."
        )
        if max_train_samples is not None and len(train_dataset) > max_train_samples:
            train_dataset = train_dataset.select(np.arange(max_train_samples))

    return train_dataset, eval_dataset


def make_data_module(args):
    """
    Make dataset and collator for supervised fine-tuning.
    Datasets are expected to have the following columns: { `input`, `output` }

    Available datasets to be selected with `dataset` argument:
        - alpaca, 52002 examples
        - alpaca cleaned, 51942 examples
        - chip2 (OIG), 210289 examples
        - self-instruct, 82612 examples
        - hh-rlhf (Anthropic), 160800 examples
        - longform, 23.7k examples
        - oasst1 (OpenAssistant) primary message tree only, 9,846 examples

    Coming soon:
        - unnatural instructions core, 66010 examples
        - unnatural instructions full, 240670 examples
        - alpaca-gpt4, 52002 examples
        - unnatural-instructions-gpt4, 9000 examples
        - supernatural-instructions, 69624 examples (same as paper with 100 ex/task more can be used)
        - flan (FLAN v2), up to 20M examples available
        - vicuna

    """
    train_datasets: List[Dataset] = []
    eval_datasets: List[Dataset] = []
    dataset_name_list = args.dataset_name.split(",")
    print(f"Loading datasets: {dataset_name_list}")
    mutliturn_lst = [dataset_attr.multi_turn for dataset_attr in args.datasets_list]
    assert mutliturn_lst.count(mutliturn_lst[0]) == len(
        mutliturn_lst
    ), "All datasets should be multi-turn or single-turn. As follwing we will concat all datasets, so they should be in the same format."

    for dataset_attr in args.datasets_list:
        print("=" * 80)
        print("DatasetAttr: {}".format(dataset_attr))

        if dataset_attr.load_from_local:
            dataset_path = dataset_attr.local_path
        elif dataset_attr.hf_hub_url:
            dataset_path = dataset_attr.hf_hub_url
        else:
            raise ValueError("Please set the dataset path or hf_hub_url.")

        dataset = load_data(dataset_path, eval_dataset_size=args.eval_dataset_size)

        if not dataset_attr.multi_turn:
            dataset = formate_instruction_dataset(
                dataset,
                dataset_name=dataset_attr.dataset_name,
                dataset_format=dataset_attr.dataset_format,
                instruction_template=args.instruction_template,
            )

        train_dataset, eval_dataset = split_train_eval(
            dataset,
            do_eval=args.do_eval,
            eval_dataset_size=args.eval_dataset_size,
            max_eval_samples=args.max_eval_samples,
            do_train=args.do_train,
            max_train_samples=args.max_train_samples,
        )
        if train_dataset:
            print(
                "loaded dataset:",
                dataset_attr.dataset_name,
                " ",
                "#train data size:",
                len(train_dataset),
            )
            train_datasets.append(train_dataset)
        if eval_dataset:
            print(
                "loaded dataset:",
                dataset_attr.dataset_name,
                " " "#eval data size:",
                len(eval_dataset),
            )
            eval_datasets.append(eval_dataset)

    concate_train = concatenate_datasets(train_datasets) if train_datasets else None
    print(
        f"Concatenated dataset list: {dataset_name_list}, #train dataset size: {len(concate_train)}"
    ) if concate_train else None
    concate_eval = concatenate_datasets(eval_datasets) if eval_datasets else None
    print(
        f"Concatenated dataset list: {dataset_name_list}, #eval dataset size: {len(concate_eval)}"
    ) if concate_eval else None
    return concate_train, concate_eval, mutliturn_lst[0]
