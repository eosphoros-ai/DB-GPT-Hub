import hashlib
import os
from itertools import chain
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    Tuple,
    Union,
)

import numpy as np
import pandas as pd
import tiktoken
from datasets import (
    Dataset,
    DatasetDict,
    concatenate_datasets,
    interleave_datasets,
    load_dataset,
)

from ..configs.config import EXT2TYPE, IGNORE_INDEX
from ..configs.data_args import (
    ALPACA_PROMPT_DICT,
    DEFAULT_PROMPT_DICT,
    SQL_PROMPT_DICT,
    Llama2Template,
    Template,
)

if TYPE_CHECKING:
    pass

from dbgpt_hub_gql.llm_base.loggings import get_logger

logger = get_logger(__name__)


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


def extract_sql_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
    if example.get("input", "") != "":
        prompt_format = SQL_PROMPT_DICT["prompt_input"]
    else:
        prompt_format = SQL_PROMPT_DICT["prompt_no_input"]
    return {"input": prompt_format.format(**example)}


def infer_max_len(
    source_len: int, target_len: int, data_args: "DataArguments"
) -> Tuple[int, int]:
    max_target_len = int(
        data_args.cutoff_len * (target_len / (source_len + target_len))
    )
    max_target_len = max(max_target_len, data_args.reserved_label_len)
    max_source_len = data_args.cutoff_len - max_target_len
    return max_source_len, max_target_len


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


templates: Dict[str, Template] = {}


def get_template_and_fix_tokenizer(
    name: str, tokenizer: "PreTrainedTokenizer"
) -> Template:
    template = templates.get(name, None)
    assert template is not None, "Template {} does not exist.".format(name)

    additional_special_tokens = template.stop_words

    if tokenizer.eos_token_id is None:
        tokenizer.eos_token = "<|endoftext|>"
        logger.info("Add eos token: {}".format(tokenizer.eos_token))

    if tokenizer.pad_token_id is None:
        if tokenizer.unk_token_id is not None:
            tokenizer.pad_token = tokenizer.unk_token
        else:
            tokenizer.pad_token = tokenizer.eos_token
        logger.info("Add pad token: {}".format(tokenizer.pad_token))

    if name is None:
        return None

    tokenizer.add_special_tokens(
        dict(additional_special_tokens=additional_special_tokens),
        replace_additional_special_tokens=False,
    )
    return template


def register_template(
    name: str,
    prefix: List[Union[str, Dict[str, str]]],
    prompt: List[Union[str, Dict[str, str]]],
    system: str,
    sep: List[Union[str, Dict[str, str]]],
    stop_words: Optional[List[str]] = [],
    use_history: Optional[bool] = True,
) -> None:
    template_class = Llama2Template if "llama2" in name else Template
    templates[name] = template_class(
        prefix=prefix,
        prompt=prompt,
        system=system,
        sep=sep,
        stop_words=stop_words,
        use_history=use_history,
    )


r"""
Supports language model inference without histories.
"""
register_template(
    name="vanilla",
    prefix=[],
    prompt=["{{query}}"],
    system="",
    sep=[],
    use_history=False,
)

r"""
Supports language model for  mistral sqlcoder-7b
"""
register_template(
    name="mistral",
    prefix=["{{system}}"],
    prompt=["[INST] {{query}} [/INST]"],
    system="",
    sep=[],
)


r"""
Default template.
"""
register_template(
    name="default",
    prefix=["{{system}}"],
    prompt=["Human: {{query}}\nAssistant: "],
    system=(
        "A chat between a curious user and an artificial intelligence assistant. "
        "The assistant gives helpful, detailed, and polite answers to the user's questions."
    ),
    sep=["\n"],
)


r"""
Supports: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
          https://huggingface.co/meta-llama/Llama-2-13b-chat-hf
          https://huggingface.co/meta-llama/Llama-2-70b-chat-hf
"""
register_template(
    name="llama2",
    prefix=["<<SYS>>\n{{system}}\n<</SYS>>\n\n"],
    prompt=["[INST] {{query}} [/INST] "],
    system=(
        "You are a helpful, respectful and honest assistant. "
        "Always answer as helpfully as possible, while being safe.  "
        "Your answers should not include any harmful, unethical, "
        "racist, sexist, toxic, dangerous, or illegal content. "
        "Please ensure that your responses are socially unbiased and positive in nature.\n"
        "If a question does not make any sense, or is not factually coherent, "
        "explain why instead of answering something not correct. "
        "If you don't know the answer to a question, please don't share false information."
    ),
    sep=[],
)


r"""
Supports: https://github.com/ymcui/Chinese-LLaMA-Alpaca-2
          https://huggingface.co/ziqingyang/chinese-alpaca-2-7b
"""
register_template(
    name="llama2_zh",
    prefix=["<<SYS>>\n{{system}}\n<</SYS>>\n\n"],
    prompt=["[INST] {{query}} [/INST] "],
    system="You are a helpful assistant. 你是一个乐于助人的助手。",
    sep=[],
)


r"""
Supports: https://huggingface.co/tatsu-lab/alpaca-7b-wdiff
          https://github.com/ymcui/Chinese-LLaMA-Alpaca
"""
register_template(
    name="alpaca",
    prefix=["{{system}}"],
    prompt=["### Instruction:\n{{query}}\n\n### Response:\n"],
    system=(
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request."
    ),
    sep=["\n\n"],
)


r"""
Supports: https://huggingface.co/lmsys/vicuna-7b-delta-v1.1
          https://huggingface.co/lmsys/vicuna-13b-delta-v1.1
"""
register_template(
    name="vicuna",
    prefix=["{{system}}"],
    prompt=["USER: {{query}} ASSISTANT: "],
    system=(
        "A chat between a curious user and an artificial intelligence assistant. "
        "The assistant gives helpful, detailed, and polite answers to the user's questions."
    ),
    sep=[],
)


r"""
Supports: https://huggingface.co/BelleGroup/BELLE-LLaMA-EXT-13B
"""
register_template(
    name="belle",
    prefix=["{{system}}"],
    prompt=["Human: {{query}}\n\nBelle: "],
    system="",
    sep=["\n\n"],
)


r"""
Supports: https://github.com/CVI-SZU/Linly
"""
register_template(
    name="linly",
    prefix=["{{system}}"],
    prompt=["User: {{query}}\nBot: "],
    system="",
    sep=["\n"],
)


r"""
Supports: https://github.com/Neutralzz/BiLLa
"""
register_template(
    name="billa",
    prefix=["{{system}}"],
    prompt=["Human: {{query}}\nAssistant: "],
    system="",
    sep=["\n"],
)


r"""
Supports: https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1
"""
register_template(
    name="ziya",
    prefix=["{{system}}"],
    prompt=[{"token": "<human>"}, ":{{query}}\n", {"token": "<bot>"}, ":"],
    system="",
    sep=["\n"],
)


r"""
Supports: https://huggingface.co/qhduan/aquilachat-7b
"""
register_template(
    name="aquila",
    prefix=["{{system}}"],
    prompt=["Human: {{query}}###Assistant: "],
    system=(
        "A chat between a curious human and an artificial intelligence assistant. "
        "The assistant gives helpful, detailed, and polite answers to the human's questions."
    ),
    sep=["###"],
)


r"""
Supports: https://huggingface.co/internlm/internlm-chat-7b
"""
register_template(
    name="intern",
    prefix=["{{system}}"],
    prompt=["<|User|>:{{query}}", {"token": "<eoh>"}, "\n<|Bot|>:"],
    system="",
    sep=["\n"],
    stop_words=["</s>", "<eoa>"],  # internlm cannot replace eos token
)


r"""
Supports: https://huggingface.co/baichuan-inc/Baichuan-13B-Chat
Used for training and inference of the fine-tuned models.
"""
register_template(
    name="baichuan",
    prefix=["{{system}}"],
    prompt=[
        {"token": "<reserved_102>"},  # user token
        "{{query}}",
        {"token": "<reserved_103>"},  # assistant token
    ],
    system="",
    sep=[],
    stop_words=[],
)


r"""
Supports: https://huggingface.co/baichuan-inc/Baichuan-13B-Chat
Used for inference of the original model.
"""
register_template(
    name="baichuan_eval",
    prefix=["{{system}}", {"token": "<reserved_102>"}],  # user token
    prompt=["{{query}}", {"token": "<reserved_103>"}],  # assistant token
    system="",
    sep=[],
    stop_words=["<reserved_102>"],  # user token
)

r"""
Supports: https://huggingface.co/baichuan-inc/Baichuan2-7B-Chat
          https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat
Used for training and inference of the fine-tuned models.
"""
register_template(
    name="baichuan2",
    prefix=["{{system}}"],
    prompt=[
        {"token": "<reserved_106>"},  # user token
        "{{query}}",
        {"token": "<reserved_107>"},  # assistant token
    ],
    system="",
    sep=[],
)


r"""
Supports: https://huggingface.co/baichuan-inc/Baichuan2-7B-Chat
          https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat
Used for inference of the original model.
"""
register_template(
    name="baichuan2_eval",
    prefix=["{{system}}", {"token": "<reserved_106>"}],  # user token
    prompt=["{{query}}", {"token": "<reserved_107>"}],  # assistant token
    system="",
    sep=[],
    stop_words=["<reserved_106>"],  # user token
)


r"""
Supports: https://huggingface.co/HuggingFaceH4/starchat-alpha
          https://huggingface.co/HuggingFaceH4/starchat-beta

"""
register_template(
    name="starchat",
    prefix=[{"token": "<|system|>"}, "\n{{system}}", {"token": "<|end|>"}],
    prompt=[
        {"token": "<|user|>"},
        "\n{{query}}",
        {"token": "<|end|>"},
        "\n",
        {"token": "<|assistant|>"},
    ],
    system="",
    sep=["\n"],
    stop_words=["<|end|>"],
)


r"""
Supports: https://huggingface.co/Qwen/Qwen-7B-Chat
"""
register_template(
    name="chatml",
    prefix=[{"token": "<|im_start|>"}, "system\n{{system}}", {"token": "<|im_end|>"}],
    prompt=[
        {"token": "<|im_start|>"},
        "user\n{{query}}",
        {"token": "<|im_end|>"},
        "\n",
        {"token": "<|im_start|>"},
        "assistant\n",
    ],
    system="You are a helpful assistant.",
    sep=["\n"],
    stop_words=["<|im_end|>"],
)


r"""
Supports: https://huggingface.co/THUDM/chatglm2-6b
"""
register_template(
    name="chatglm2",
    prefix=[{"token": "[gMASK]"}, {"token": "sop"}, "{{system}}"],
    prompt=["[Round {{idx}}]\n\n问：{{query}}\n\n答："],
    system="",
    sep=["\n\n"],
)


r"""
Supports: https://huggingface.co/THUDM/chatglm3-6b
"""
register_template(
    name="chatglm3",
    prefix=[
        {"token": "[gMASK]"},
        {"token": "sop"},
        {"token": "<|system|>"},
        "\n",
        "{{system}}",
    ],
    prompt=[
        {"token": "<|user|>"},
        "\n",
        "{{query}}",
        {"token": "<|assistant|>"},
        "\n",  # add an extra newline to avoid error in ChatGLM's process_response method
    ],
    system=(
        "You are ChatGLM3, a large language model trained by Zhipu.AI. "
        "Follow the user's instructions carefully. Respond using markdown."
    ),
    sep=[],
    stop_words=["<|user|>", "<|observation|>"],
)

register_template(
    name="chatglm3_raw",  # the raw template for tool tuning
    prefix=[
        {"token": "[gMASK]"},
        {"token": "sop"},
        {"token": "<|system|>"},
        "\n",
        "{{system}}",
    ],
    prompt=[{"token": "<|user|>"}, "\n", "{{query}}", {"token": "<|assistant|>"}],
    system=(
        "You are ChatGLM3, a large language model trained by Zhipu.AI. "
        "Follow the user's instructions carefully. Respond using markdown."
    ),
    sep=[],
    stop_words=["<|user|>", "<|observation|>"],
)


r"""
Supports: https://huggingface.co/xverse/XVERSE-13B-Chat
"""
register_template(
    name="xverse",
    prefix=["{{system}}"],
    prompt=["Human: {{query}}\n\nAssistant: "],
    system="",
    sep=[],
)


def split_dataset(
    dataset: Union["Dataset", "IterableDataset"],
    data_args: "DataArguments",
    training_args: "TrainingArguments",
) -> Dict[str, "Dataset"]:
    if training_args.do_train:
        if data_args.val_size > 1e-6:  # Split the dataset
            if data_args.streaming:
                val_set = dataset.take(int(data_args.val_size))
                train_set = dataset.skip(int(data_args.val_size))
                dataset = dataset.shuffle(
                    buffer_size=data_args.buffer_size, seed=training_args.seed
                )
                return {"train_dataset": train_set, "eval_dataset": val_set}
            else:
                val_size = (
                    int(data_args.val_size)
                    if data_args.val_size > 1
                    else data_args.val_size
                )
                dataset = dataset.train_test_split(
                    test_size=val_size, seed=training_args.seed
                )
                return {
                    "train_dataset": dataset["train"],
                    "eval_dataset": dataset["test"],
                }
        else:
            if data_args.streaming:
                dataset = dataset.shuffle(
                    buffer_size=data_args.buffer_size, seed=training_args.seed
                )
            return {"train_dataset": dataset}
    else:  # do_eval or do_predict
        return {"eval_dataset": dataset}


def preprocess_dataset(
    dataset: Union["Dataset", "IterableDataset"],
    tokenizer: "PreTrainedTokenizer",
    data_args: "DataArguments",
    training_args: "Seq2SeqTrainingArguments",
    stage: Literal["pt", "sft", "rm", "ppo"],
) -> Union["Dataset", "IterableDataset"]:
    column_names = list(next(iter(dataset)).keys())
    template = get_template_and_fix_tokenizer(data_args.template, tokenizer)

    def construct_example(examples: Dict[str, List[Any]]) -> Generator[Any, None, None]:
        for i in range(len(examples["prompt"])):
            query, response = examples["prompt"][i], examples["response"][i]
            query = (
                query + "\n" + examples["query"][i]
                if "query" in examples and examples["query"][i]
                else query
            )
            history = examples["history"][i] if "history" in examples else None
            system = examples["system"][i] if "system" in examples else None
            yield query, response, history, system

    def preprocess_pretrain_dataset(examples: Dict[str, List[Any]]) -> Dict[str, Any]:
        # build grouped texts with format `X1 X2 X3 ...` (without <eos>)
        if isinstance(
            getattr(tokenizer, "tokenizer", None), tiktoken.Encoding
        ):  # for tiktoken tokenizer (Qwen)
            kwargs = dict(allowed_special="all")
        else:
            kwargs = dict(add_special_tokens=False)

        tokenized_examples = tokenizer(examples["prompt"], **kwargs)
        concatenated_examples = {
            k: list(chain(*tokenized_examples[k])) for k in tokenized_examples.keys()
        }
        total_length = len(concatenated_examples[list(concatenated_examples.keys())[0]])
        block_size = data_args.max_source_length
        # we drop the small remainder, and if the total_length < block_size, we exclude this batch
        total_length = (total_length // block_size) * block_size
        # split by chunks of max_source_length
        result = {
            k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
            for k, t in concatenated_examples.items()
        }
        return result

    def preprocess_supervised_dataset(examples: Dict[str, List[Any]]) -> Dict[str, Any]:
        # build inputs with format `<bos> X Y <eos>` and labels with format `<ignore> ... <ignore> Y <eos>`
        # for multiturn examples, we only mask the prompt part in each prompt-response pair.
        model_inputs = {"input_ids": [], "attention_mask": [], "labels": []}
        max_length = data_args.max_source_length + data_args.max_target_length

        for query, response, history, system in construct_example(examples):
            input_ids, labels = [], []

            for source_ids, target_ids in template.encode_multiturn(
                tokenizer, query, response, history, system
            ):
                if len(source_ids) > data_args.max_source_length:
                    source_ids = source_ids[: data_args.max_source_length]
                if len(target_ids) > data_args.max_target_length:
                    target_ids = target_ids[: data_args.max_target_length]

                if len(input_ids) + len(source_ids) + len(target_ids) > max_length:
                    break

                input_ids += source_ids + target_ids
                labels += [IGNORE_INDEX] * len(source_ids) + target_ids

            model_inputs["input_ids"].append(input_ids)
            model_inputs["attention_mask"].append([1] * len(input_ids))
            model_inputs["labels"].append(labels)

        return model_inputs

    def preprocess_unsupervised_dataset(
        examples: Dict[str, List[Any]]
    ) -> Dict[str, Any]:
        # build inputs with format `<bos> X` and labels with format `Y <eos>`
        model_inputs = {"input_ids": [], "attention_mask": [], "labels": []}

        for query, response, history, system in construct_example(examples):
            source_ids, target_ids = template.encode_oneturn(
                tokenizer, query, response, history, system
            )

            if len(source_ids) > data_args.max_source_length:
                source_ids = source_ids[: data_args.max_source_length]
            if len(target_ids) > data_args.max_target_length:
                target_ids = target_ids[: data_args.max_target_length]

            model_inputs["input_ids"].append(source_ids)
            model_inputs["attention_mask"].append([1] * len(source_ids))
            model_inputs["labels"].append(target_ids)

        return model_inputs

    def preprocess_pairwise_dataset(
        examples: Dict[str, List[Any]]
    ) -> Dict[str, List[List[int]]]:
        # build input pairs with format `<bos> X`, `Y1 <eos>` and `Y2 <eos>` for rm stage
        model_inputs = {"prompt_ids": [], "chosen_ids": [], "rejected_ids": []}
        for query, response, history, system in construct_example(examples):
            if not (
                isinstance(query, str)
                and isinstance(response, list)
                and query != ""
                and len(response) > 1
            ):
                continue

            prompt_ids, chosen_ids = template.encode_oneturn(
                tokenizer, query, response[0], history, system
            )
            _, rejected_ids = template.encode_oneturn(
                tokenizer, query, response[1], history, system
            )

            # if template.efficient_eos:
            chosen_ids += [tokenizer.eos_token_id]
            rejected_ids += [tokenizer.eos_token_id]

            source_len, target_len = len(prompt_ids), max(
                len(chosen_ids), len(rejected_ids)
            )
            max_source_len, max_target_len = infer_max_len(
                source_len, target_len, data_args
            )
            if source_len > max_source_len:
                prompt_ids = prompt_ids[:max_source_len]
            if target_len > max_target_len:
                chosen_ids = chosen_ids[:max_target_len]
                rejected_ids = rejected_ids[:max_target_len]

            model_inputs["prompt_ids"].append(prompt_ids)
            model_inputs["chosen_ids"].append(chosen_ids)
            model_inputs["rejected_ids"].append(rejected_ids)

        return model_inputs

    def print_pairwise_dataset_example(example: Dict[str, List[int]]) -> None:
        print("prompt_ids:\n{}".format(example["prompt_ids"]))
        print(
            "prompt:\n{}".format(
                tokenizer.decode(example["prompt_ids"], skip_special_tokens=False)
            )
        )
        print("chosen_ids:\n{}".format(example["chosen_ids"]))
        print(
            "chosen:\n{}".format(
                tokenizer.decode(example["chosen_ids"], skip_special_tokens=False)
            )
        )
        print("rejected_ids:\n{}".format(example["rejected_ids"]))
        print(
            "rejected:\n{}".format(
                tokenizer.decode(example["rejected_ids"], skip_special_tokens=False)
            )
        )

    def print_supervised_dataset_example(example):
        print("input_ids:\n{}".format(example["input_ids"]))
        print(
            "inputs:\n{}".format(
                tokenizer.decode(example["input_ids"], skip_special_tokens=False)
            )
        )
        print("label_ids:\n{}".format(example["labels"]))
        print(
            "labels:\n{}".format(
                tokenizer.decode(
                    [
                        token_id if token_id != IGNORE_INDEX else tokenizer.pad_token_id
                        for token_id in example["labels"]
                    ],
                    skip_special_tokens=False,
                )
            )
        )

    if stage == "pt":
        pass
    elif stage == "sft" and not training_args.predict_with_generate:
        preprocess_function = preprocess_supervised_dataset
        print_function = print_supervised_dataset_example
    elif stage == "rm":
        print(111111111111111111)
        preprocess_function = preprocess_pairwise_dataset
        print_function = print_pairwise_dataset_example
    else:
        pass

    with training_args.main_process_first(desc="dataset map pre-processing"):
        kwargs = {}
        if not data_args.streaming:
            kwargs = dict(
                num_proc=data_args.preprocessing_num_workers,
                load_from_cache_file=not data_args.overwrite_cache,
                desc="Running tokenizer on dataset",
            )

        dataset = dataset.map(
            preprocess_function, batched=True, remove_columns=column_names, **kwargs
        )

        print_function(next(iter(dataset)))
        return dataset


## used in get_dataset
def checksum(data_files: List[str], file_sha1: Optional[str] = None) -> None:
    if file_sha1 is None:
        logger.warning(
            "Checksum failed: missing SHA-1 hash value in dataset_info.json."
        )
        return

    if len(data_files) != 1:
        logger.warning("Checksum failed: too many files.")
        return

    with open(data_files[0], "rb") as f:
        sha1 = hashlib.sha1(f.read()).hexdigest()
        if sha1 != file_sha1:
            logger.warning(
                "Checksum failed: mismatched SHA-1 hash value at {}.".format(
                    data_files[0]
                )
            )


def get_dataset(
    model_args: "ModelArguments", data_args: "DataArguments"
) -> Union["Dataset", "IterableDataset"]:
    max_samples = data_args.max_samples
    all_datasets: List[
        Union["Dataset", "IterableDataset"]
    ] = []  # support multiple datasets

    for dataset_attr in data_args.dataset_list:
        logger.info("Loading dataset {}...".format(dataset_attr))

        if dataset_attr.load_from == "hf_hub":
            data_path = dataset_attr.dataset_name
            data_files = None
        elif dataset_attr.load_from == "script":
            data_path = os.path.join(data_args.dataset_dir, dataset_attr.dataset_name)
            data_files = None
        elif dataset_attr.load_from == "file":
            data_path = None
            data_files: List[str] = []

            if os.path.isdir(
                os.path.join(data_args.dataset_dir, dataset_attr.dataset_name)
            ):  # directory
                for file_name in os.listdir(
                    os.path.join(data_args.dataset_dir, dataset_attr.dataset_name)
                ):
                    data_files.append(
                        os.path.join(
                            data_args.dataset_dir, dataset_attr.dataset_name, file_name
                        )
                    )
                    if data_path is None:
                        data_path = EXT2TYPE.get(file_name.split(".")[-1], None)
                    else:
                        assert data_path == EXT2TYPE.get(
                            file_name.split(".")[-1], None
                        ), "file type does not match."
            elif os.path.isfile(
                os.path.join(data_args.dataset_dir, dataset_attr.dataset_name)
            ):  # single file
                data_files.append(
                    os.path.join(data_args.dataset_dir, dataset_attr.dataset_name)
                )
                data_path = EXT2TYPE.get(dataset_attr.dataset_name.split(".")[-1], None)
            else:
                raise ValueError("File not found.")

            assert data_path, "File extension must be txt, csv, json or jsonl."
            checksum(data_files, dataset_attr.dataset_sha1)
        else:
            raise NotImplementedError

        dataset = load_dataset(
            data_path,
            data_files=data_files,
            split=data_args.split,
            cache_dir=model_args.cache_dir,
            streaming=data_args.streaming,
            use_auth_token=True if model_args.use_auth_token else None,
        )

        if max_samples is not None:
            max_samples_temp = min(len(dataset), max_samples)
            dataset = dataset.select(range(max_samples_temp))

        for column_name in ["prompt", "query", "response", "history"]:  # align datasets
            if (
                getattr(dataset_attr, column_name)
                and getattr(dataset_attr, column_name) != column_name
            ):
                dataset = dataset.rename_column(
                    getattr(dataset_attr, column_name), column_name
                )

        if dataset_attr.system_prompt:  # add system prompt
            if data_args.streaming:
                dataset = dataset.map(lambda _: {"system": dataset_attr.system_prompt})
            else:
                dataset = dataset.add_column(
                    "system", [dataset_attr.system_prompt] * len(dataset)
                )

        all_datasets.append(dataset)

    if len(data_args.dataset_list) == 1:
        return all_datasets[0]
    elif data_args.mix_strategy == "concat":
        if data_args.streaming:
            logger.warning(
                "The samples between different datasets will not be mixed in streaming mode."
            )
        return concatenate_datasets(all_datasets)
    elif data_args.mix_strategy.startswith("interleave"):
        if not data_args.streaming:
            logger.warning(
                "We recommend using `mix_strategy=concat` in non-streaming mode."
            )
        stopping_strategy = (
            "first_exhausted"
            if data_args.mix_strategy.endswith("under")
            else "all_exhausted"
        )
        return interleave_datasets(
            all_datasets,
            data_args.interleave_probs,
            stopping_strategy=stopping_strategy,
        )
    else:
        raise ValueError("Unknown mixing strategy.")


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
