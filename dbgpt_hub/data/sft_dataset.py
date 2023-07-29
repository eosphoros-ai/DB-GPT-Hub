import copy
import logging
from dataclasses import dataclass
from typing import Dict, List

import datasets
import torch
from datasets import DatasetDict
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset
from transformers.tokenization_utils import PreTrainedTokenizer

from dbgpt_hub.data.data_utils import IGNORE_INDEX, make_data_module

logger = logging.getLogger(__name__)


class SFTInstructionDataset(Dataset):
    """
    Dataset for supervised fine-tuning of instruction following models.

    Converts raw dataset containing source/target instructions
    into tokenized input/target pairs with truncation and padding.

    Attributes:
        dataset: The raw dataset containing source/target examples
        tokenizer: Tokenizer to use for encoding text
        max_seq_len: Maximum sequence length for truncation

    """
    def __init__(self,
                 raw_data: DatasetDict,
                 tokenizer: PreTrainedTokenizer,
                 max_seq_len: int = 1024):
        """
        Initialize the dataset with the raw data and tokenizer.

        Args:
            raw_data: Raw dataset containing source/target examples
            tokenizer: Tokenizer to encode text
            max_seq_len: Max sequence length for truncation
        """
        self.dataset = raw_data
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __len__(self) -> int:
        """Return number of examples in dataset"""
        return len(self.dataset)

    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        """
        Convert an raw example into tokenized input/target pair.

        Args:
            idx: Index of the example in the dataset

        Returns:
            input_ids: tokenized input sequence
            labels: tokenized target sequence
        """

        example = self.dataset[idx]

        source_text = example['input']
        source_text = f'{self.tokenizer.bos_token}{source_text}{self.tokenizer.eos_token}'

        target_text = example['output']
        target_text = f'{target_text}{self.tokenizer.eos_token}'

        # Tokenize the source text
        tokenized_source = self.tokenizer(source_text,
                                          max_length=self.max_seq_len,
                                          truncation=True,
                                          add_special_tokens=False)
        # Tokenize the example and source text
        tokenized_target = self.tokenizer(target_text,
                                          max_length=self.max_seq_len,
                                          truncation=True,
                                          add_special_tokens=False)

        source_ids = tokenized_source['input_ids']
        target_ids = tokenized_target['input_ids']

        # Extract the input_ids tensor
        if len(source_ids) > self.max_seq_len:
            print(
                f'Source length {len(source_ids)} exceeds max seq length of {self.max_seq_len}'
            )
        # Create the labels tensor
        if len(target_ids) > self.max_seq_len:
            print(
                f'Target length {len(target_ids)} exceeds max seq length of {self.max_seq_len}'
            )

        input_ids = torch.tensor(source_ids + target_ids)
        labels = torch.tensor([IGNORE_INDEX for _ in range(len(source_ids))] +
                              copy.deepcopy(target_ids))

        # Construct data dictionary containing inputs and labels
        data_dict = {'input_ids': input_ids, 'labels': labels}

        return data_dict


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
        src_ids = tokenized_source['input_ids']
        tgt_ids = tokenized_target['input_ids']
        if not self.predict_with_generate:
            # If not generating predictions, concatenate the input and target ids
            input_ids = torch.tensor(src_ids + tgt_ids)
            if not self.train_on_source:
                # If not training on the source text, set the labels to IGNORE_INDEX \
                # for the input ids and the target ids
                labels = torch.tensor(
                    [IGNORE_INDEX
                     for _ in range(len(src_ids))] + copy.deepcopy(tgt_ids))
            else:
                # If training on the source text, set the labels to the concatenated \
                # input and target ids
                labels = torch.tensor(copy.deepcopy(src_ids + tgt_ids))
        else:
            # If generating predictions, only use the source ids as input
            input_ids = torch.tensor(src_ids)
            labels = None

        # Construct data dictionary containing inputs and labels
        data_dict = {'input_ids': input_ids, 'labels': labels}

        return data_dict


@dataclass
class DataCollatorForSupervisedDataset:
    """
    Collate and pad examples for supervised training.
    """

    tokenizer: PreTrainedTokenizer
    predict_with_generate: bool = False

    def __call__(
            self,
            examples: List[Dict[str,
                                torch.Tensor]]) -> Dict[str, torch.Tensor]:
        """
        Collate examples into dictionary for supervised training.

        Args:
            examples: List of examples, each containing 'input_ids' and 'labels'

        Returns:
            Dictionary with padded 'input_ids', 'attention_mask' and optionally 'labels'
        """

        # Extract input_ids and labels
        input_ids = [example['input_ids'] for example in examples]
        labels = [example['labels'] for example in examples]

        # Pad input sequences
        input_ids = pad_sequence(input_ids,
                                 batch_first=True,
                                 padding_value=0)

        # Pad labels if needed
        if not self.predict_with_generate:
            labels = pad_sequence(labels,
                                  batch_first=True,
                                  padding_value=IGNORE_INDEX)

        # Create attention mask based on padded input
        attention_mask = input_ids.ne(0)

        # Assemble final dict
        data_dict = {'input_ids': input_ids, 'attention_mask': attention_mask}
        if labels is not None:
            data_dict['labels'] = labels

        return data_dict


def make_instruction_data_module(tokenizer: PreTrainedTokenizer, args):
    train_dataset, eval_dataset = make_data_module(args)
    train_dataset = SupervisedDataset(
        train_dataset,
        tokenizer=tokenizer,
        source_max_len=args.source_max_len,
        target_max_len=args.target_max_len,
        train_on_source=args.train_on_source,
        predict_with_generate=args.predict_with_generate,
    ) if args.do_train else None

    eval_dataset = SupervisedDataset(
        eval_dataset,
        tokenizer=tokenizer,
        source_max_len=args.source_max_len,
        target_max_len=args.target_max_len,
        train_on_source=args.train_on_source,
        predict_with_generate=args.predict_with_generate,
    ) if args.do_eval else None

    print(
        f'train_dataset: {type(train_dataset)}, #length: {len(train_dataset)}'
    ) if args.do_train else None
    print(f'eval_dataset: {type(eval_dataset)}, #length: {len(eval_dataset)}'
          ) if args.do_eval else None
    print('Adding data collator: ', DataCollatorForSupervisedDataset)
    data_collator = DataCollatorForSupervisedDataset(
        tokenizer=tokenizer, predict_with_generate=args.predict_with_generate)

    return {
        'train_dataset': train_dataset,
        'eval_dataset': eval_dataset,
        'data_collator': data_collator
    }
