import json
import os
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List, Literal, Optional, Tuple, Union

import tiktoken

if TYPE_CHECKING:
    from transformers import PreTrainedTokenizer


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
        "I want you to act as a GQL terminal in front of an example database, \
         you need only to return the gql command to me.Below is an instruction that describes a task, \
         Write a response that appropriately completes the request.\n"
        "##Instruction:\n{instruction}\n###Input:\n{input}\n\n###Response:"
    ),
    "prompt_no_input": (
        "I want you to act as a GQL terminal in front of an example database, \
        you need only to return the gql command to me.Below is an instruction that describes a task, \
        Write a response that appropriately completes the request.\n"
        "####Instruction:\n{instruction}\n\###Response: "
    ),
}


@dataclass
class DatasetAttr:
    load_from: str
    dataset_name: Optional[str] = None
    dataset_sha1: Optional[str] = None
    system_prompt: Optional[str] = None
    stage: Optional[str] = None

    def __repr__(self) -> str:
        return self.dataset_name

    def __post_init__(self):
        self.prompt = "instruction"
        self.query = "input"
        self.response = "output"
        self.history = None


@dataclass
class DataArguments:
    r"""
    Arguments pertaining to what data we are going to input our model for training and evaluation.
    """
    template: str = field(
        metadata={
            "help": "Which template to use for constructing prompts in training and inference."
        }
    )
    dataset: Optional[str] = field(
        default="tugraph_db_example_train",
        metadata={
            "help": "The name of provided dataset(s) to use. Use commas to separate multiple datasets."
        },
    )
    dataset_dir: Optional[str] = field(
        default="dbgpt_hub_gql/data/",
        metadata={"help": "The name of the folder containing datasets."},
    )
    cutoff_len: Optional[int] = field(
        default=1024,
        metadata={"help": "The maximum length of the model inputs after tokenization."},
    )
    reserved_label_len: Optional[int] = field(
        default=1,
        metadata={"help": "The maximum length reserved for label after tokenization."},
    )
    split: Optional[str] = field(
        default="train",
        metadata={"help": "Which dataset split to use for training and evaluation."},
    )
    streaming: Optional[bool] = field(
        default=False, metadata={"help": "Enable streaming mode."}
    )
    buffer_size: Optional[int] = field(
        default=16384,
        metadata={
            "help": "Size of the buffer to randomly sample examples from in streaming mode."
        },
    )
    mix_strategy: Optional[
        Literal["concat", "interleave_under", "interleave_over"]
    ] = field(default="concat", metadata={"help": "Strategy to use in dataset mixing."})
    interleave_probs: Optional[str] = field(
        default=None,
        metadata={
            "help": "Probabilities to sample data from datasets. Use commas to separate multiple datasets."
        },
    )
    overwrite_cache: Optional[bool] = field(
        default=False,
        metadata={"help": "Overwrite the cached training and evaluation sets."},
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "The number of processes to use for the preprocessing."},
    )
    max_source_length: Optional[int] = field(
        default=512,
        metadata={
            "help": "The maximum total input sequence length after tokenization."
        },
    )
    max_target_length: Optional[int] = field(
        default=512,
        metadata={
            "help": "The maximum total output sequence length after tokenization."
        },
    )
    max_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes, truncate the number of examples for each dataset."
        },
    )
    eval_num_beams: Optional[int] = field(
        default=None,
        metadata={
            "help": "Number of beams to use for evaluation. This argument will be passed to `model.generate`"
        },
    )
    ignore_pad_token_for_loss: Optional[bool] = field(
        default=True,
        metadata={
            "help": "Whether to ignore the tokens corresponding to padded labels in the loss computation or not."
        },
    )
    system_prompt: Optional[str] = field(
        default=None,
        metadata={
            "help": "System prompt to add before the user query. Use `|` to separate multiple prompts in training."
        },
    )
    val_size: Optional[float] = field(
        default=0,
        metadata={
            "help": "Size of the development set, should be an integer or a float in range `[0,1)`."
        },
    )
    predicted_input_filename: Optional[str] = field(
        default="dbgpt_hub_gql/data/tugraph-db-example/dev.json",
        metadata={"help": "Predict input filename to do pred "},
    )
    predicted_out_filename: Optional[str] = field(
        default="pred_gql.txt",
        metadata={"help": "Filename to save predicted outcomes"},
    )

    def init_for_training(self):  # support mixing multiple datasets
        dataset_names = [ds.strip() for ds in self.dataset.split(",")]
        with open(os.path.join(self.dataset_dir, "dataset_info.json"), "r") as f:
            dataset_info = json.load(f)

        prompt_list = self.system_prompt.split("|") if self.system_prompt else [None]
        prompt_list = prompt_list * (len(dataset_names) // len(prompt_list))
        assert len(prompt_list) == len(
            dataset_names
        ), "Number of system prompts should be equal to datasets or 1."

        if self.interleave_probs is not None:
            self.interleave_probs = [
                float(prob.strip()) for prob in self.interleave_probs.split(",")
            ]

        self.dataset_list: List[DatasetAttr] = []
        for i, name in enumerate(dataset_names):
            if name not in dataset_info:
                raise ValueError(
                    "Undefined dataset {} in dataset_info.json.".format(name)
                )

            if "hf_hub_url" in dataset_info[name]:
                dataset_attr = DatasetAttr(
                    "hf_hub",
                    dataset_name=dataset_info[name]["hf_hub_url"],
                    stage=dataset_info[name].get("stage", None),
                )
            elif "script_url" in dataset_info[name]:
                dataset_attr = DatasetAttr(
                    "script",
                    dataset_name=dataset_info[name]["script_url"],
                    stage=dataset_info[name].get("stage", None),
                )
            else:
                dataset_attr = DatasetAttr(
                    "file",
                    dataset_name=dataset_info[name]["file_name"],
                    dataset_sha1=dataset_info[name].get("file_sha1", None),
                    stage=dataset_info[name].get("stage", None),
                )

            if "columns" in dataset_info[name]:
                dataset_attr.prompt = dataset_info[name]["columns"].get("prompt", None)
                dataset_attr.query = dataset_info[name]["columns"].get("query", None)
                dataset_attr.response = dataset_info[name]["columns"].get(
                    "response", None
                )
                dataset_attr.history = dataset_info[name]["columns"].get(
                    "history", None
                )

            dataset_attr.system_prompt = prompt_list[i]
            self.dataset_list.append(dataset_attr)


@dataclass
class Template:
    prefix: List[Union[str, Dict[str, str]]]
    prompt: List[Union[str, Dict[str, str]]]
    system: str
    sep: List[Union[str, Dict[str, str]]]
    stop_words: List[str]
    use_history: bool

    def encode_oneturn(
        self,
        tokenizer: "PreTrainedTokenizer",
        query: str,
        resp: str,
        history: Optional[List[Tuple[str, str]]] = None,
        system: Optional[str] = None,
    ) -> Tuple[List[int], List[int]]:
        r"""
        Returns a single pair of token ids representing prompt and response respectively.
        """
        system, history = self._format(query, resp, history, system)
        encoded_pairs = self._encode(tokenizer, system, history)
        prompt_ids = []
        for query_ids, resp_ids in encoded_pairs[:-1]:
            prompt_ids = prompt_ids + query_ids + resp_ids
        prompt_ids, answer_ids = prompt_ids + encoded_pairs[-1][0], encoded_pairs[-1][1]
        return prompt_ids, answer_ids

    def encode_multiturn(
        self,
        tokenizer: "PreTrainedTokenizer",
        query: str,
        resp: str,
        history: Optional[List[Tuple[str, str]]] = None,
        system: Optional[str] = None,
    ) -> List[Tuple[List[int], List[int]]]:
        r"""
        Returns multiple pairs of token ids representing prompts and responses respectively.
        """
        system, history = self._format(query, resp, history, system)
        encoded_pairs = self._encode(tokenizer, system, history)
        return encoded_pairs

    def _format(
        self,
        query: str,
        resp: str,
        history: Optional[List[Tuple[str, str]]] = None,
        system: Optional[str] = None,
    ) -> Tuple[str, List[Tuple[str, str]]]:
        r"""
        Aligns inputs to the standard format.
        """
        system = system or self.system  # use system if provided
        history = history if (history and self.use_history) else []
        history = history + [(query, resp)]
        return system, history

    def _get_special_ids(
        self, tokenizer: "PreTrainedTokenizer"
    ) -> Tuple[List[int], List[int]]:
        if tokenizer.bos_token_id is not None and getattr(
            tokenizer, "add_bos_token", True
        ):  # baichuan-13b has no bos token
            bos_ids = [tokenizer.bos_token_id]
        else:
            bos_ids = []  # bos token is optional

        if tokenizer.eos_token_id is not None:
            eos_ids = [tokenizer.eos_token_id]
        else:
            raise ValueError("EOS token is required.")

        return bos_ids, eos_ids

    def _encode(
        self,
        tokenizer: "PreTrainedTokenizer",
        system: str,
        history: List[Tuple[str, str]],
    ) -> List[Tuple[List[int], List[int]]]:
        r"""
        Encodes formatted inputs to pairs of token ids.
        Turn 0: bos + prefix + sep + query    resp + eos
        Turn t: sep + bos + query             resp + eos
        """
        bos_ids, eos_ids = self._get_special_ids(tokenizer)
        sep_ids = self._convert_inputs_to_ids(tokenizer, context=self.sep)
        encoded_pairs = []
        for turn_idx, (query, resp) in enumerate(history):
            if turn_idx == 0:
                prefix_ids = self._convert_inputs_to_ids(
                    tokenizer, context=self.prefix, system=system
                )
                if len(prefix_ids) != 0:  # has prefix
                    prefix_ids = bos_ids + prefix_ids + sep_ids
                else:
                    prefix_ids = bos_ids
            else:
                prefix_ids = sep_ids + bos_ids

            query_ids = self._convert_inputs_to_ids(
                tokenizer, context=self.prompt, query=query, idx=str(turn_idx)
            )
            resp_ids = self._convert_inputs_to_ids(tokenizer, context=[resp])
            encoded_pairs.append((prefix_ids + query_ids, resp_ids + eos_ids))
        return encoded_pairs

    def _convert_inputs_to_ids(
        self,
        tokenizer: "PreTrainedTokenizer",
        context: List[Union[str, Dict[str, str]]],
        system: Optional[str] = None,
        query: Optional[str] = None,
        idx: Optional[str] = None,
    ) -> List[int]:
        r"""
        Converts context to token ids.
        """
        if isinstance(
            getattr(tokenizer, "tokenizer", None), tiktoken.Encoding
        ):  # for tiktoken tokenizer (Qwen)
            kwargs = dict(allowed_special="all")
        else:
            kwargs = dict(add_special_tokens=False)

        token_ids = []
        for elem in context:
            if isinstance(elem, str):
                elem = (
                    elem.replace("{{system}}", system, 1)
                    if system is not None
                    else elem
                )
                elem = (
                    elem.replace("{{query}}", query, 1) if query is not None else elem
                )
                elem = elem.replace("{{idx}}", idx, 1) if idx is not None else elem
                token_ids = token_ids + tokenizer.encode(elem, **kwargs)
            elif isinstance(elem, dict):
                token_ids = token_ids + [
                    tokenizer.convert_tokens_to_ids(elem.get("token"))
                ]
            else:
                raise NotImplementedError

        return token_ids


@dataclass
class Llama2Template(Template):
    def _encode(
        self,
        tokenizer: "PreTrainedTokenizer",
        system: str,
        history: List[Tuple[str, str]],
    ) -> List[Tuple[List[int], List[int]]]:
        r"""
        Encodes formatted inputs to pairs of token ids.
        Turn 0: bos + prefix + query    resp + eos
        Turn t: bos + query             resp + eos
        """
        bos_ids, eos_ids = self._get_special_ids(tokenizer)
        encoded_pairs = []
        for turn_idx, (query, resp) in enumerate(history):
            if turn_idx == 0:  # llama2 template has no sep_ids
                query = self.prefix[0].replace("{{system}}", system) + query
            query_ids = self._convert_inputs_to_ids(
                tokenizer, context=self.prompt, query=query
            )
            resp_ids = self._convert_inputs_to_ids(tokenizer, context=[resp])
            encoded_pairs.append((bos_ids + query_ids, resp_ids + eos_ids))
        return encoded_pairs


templates: Dict[str, Template] = {}
