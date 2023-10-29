import copy
import logging
import datasets
import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset
from dataclasses import dataclass
from datasets import DatasetDict
from transformers.tokenization_utils import PreTrainedTokenizer
from dbgpt_hub.configs.config import IGNORE_INDEX
from typing import Dict, List


logger = logging.getLogger(__name__)


@dataclass
class SupervisedDataset(Dataset):
    """Dataset for supervised fine-tuning.

    Args:
        hf_dataset (dataset): The preprocesed dataset to load.
        tokenizer (PreTrainedTokenizer): The tokenizer to use when tokenizing the data.
        source_max_len (int): The maximum length allowed for the source text.
        target_max_len (int): The maximum length allowed for the target text.
        train_on_source (bool): If True, the model will be trained on the source text as well as the target text.
        predict_with_generate (bool): If True, the model will generate predictions instead of training.
    """

    def __init__(
        self,
        hf_dataset: datasets.DatasetDict,
        tokenizer: PreTrainedTokenizer,
        source_max_len: int,
        target_max_len: int,
        train_on_source: bool,
        predict_with_generate: bool = False,
    ):
        super(SupervisedDataset, self).__init__()
        # Load the dataset and format it
        self.dataset = hf_dataset
        self.tokenizer = tokenizer
        self.source_max_len = source_max_len
        self.target_max_len = target_max_len
        self.train_on_source = train_on_source
        self.predict_with_generate = predict_with_generate

    def __len__(self) -> int:
        """Return the length of the dataset."""
        return len(self.dataset)

    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        """Return an item from the dataset based on its index."""
        example = self.dataset[idx]
        # Tokenize the source text
        source_txt = f"{self.tokenizer.bos_token}{example['input']}"
        tokenized_source = self.tokenizer(
            source_txt,
            max_length=self.source_max_len,
            truncation=True,
            add_special_tokens=False,
        )
        # Tokenize the target text
        target_txt = f"{example['output']}{self.tokenizer.eos_token}"
        tokenized_target = self.tokenizer(
            target_txt,
            max_length=self.target_max_len,
            truncation=True,
            add_special_tokens=False,
        )
        src_ids = tokenized_source["input_ids"]
        tgt_ids = tokenized_target["input_ids"]
        if not self.predict_with_generate:
            # If not generating predictions, concatenate the input and target ids
            input_ids = torch.tensor(src_ids + tgt_ids)
            if not self.train_on_source:
                # If not training on the source text, set the labels to IGNORE_INDEX \
                # for the input ids and the target ids
                labels = torch.tensor(
                    [IGNORE_INDEX for _ in range(len(src_ids))] + copy.deepcopy(tgt_ids)
                )
            else:
                # If training on the source text, set the labels to the concatenated \
                # input and target ids
                labels = torch.tensor(copy.deepcopy(src_ids + tgt_ids))
        else:
            # If generating predictions, only use the source ids as input
            input_ids = torch.tensor(src_ids)
            labels = None

        # Construct data dictionary containing inputs and labels
        data_dict = {"input_ids": input_ids, "labels": labels}

        return data_dict


# ## TODO  增加 _pad_tensors_to_target_len 函数，并适配
