import os
from dataclasses import dataclass, field
from typing import List, Optional

import yaml


@dataclass
class DatasetAttr(object):

    dataset_name: Optional[str] = None
    hf_hub_url: Optional[str] = None
    local_path: Optional[str] = None
    dataset_format: Optional[str] = None
    dataset_sha1: Optional[str] = None
    load_from_local: bool = False
    multi_turn: Optional[bool] = False

    def __repr__(self) -> str:
        rep = (f'dataset_name: {self.dataset_name} || '
               f'hf_hub_url: {self.hf_hub_url} || '
               f'local_path: {self.local_path} \n'
               f'data_formate: {self.dataset_format}  || '
               f'load_from_local: {self.load_from_local} || '
               f'multi_turn: {self.multi_turn}')
        return rep

    def __post_init__(self):
        self.prompt_column = 'instruction'
        self.query_column = 'input'
        self.response_column = 'output'
        self.history_column = None


@dataclass
class DataArguments:
    dataset_name: Optional[str] = field(
        default='spider',
        metadata={
            'help': 'Which dataset to finetune on. See datamodule for options.'
        })

    dataset_dir: str = field(
        default=None,
        metadata={
            'help':
            'where is dataset in local dir. See datamodule for options.'
        })
    instruction_template: str = field(
        default='default',
        metadata={
            'help':
            'Which template to use for constructing prompts in training and inference.'
        })
    conversation_template: str = field(
        default='default',
        metadata={
            'help':
            'Which template to use for constructing prompts in multi-turn dataset training and inference.'
        })
    eval_dataset_size: Optional[float] = field(
        default=0.1, metadata={'help': 'Size of validation dataset.'})

    max_train_samples: Optional[int] = field(
        default=None,
        metadata={
            'help':
            'For debugging purposes or quicker training, truncate the number of training examples to this '
            'value if set.'
        },
    )
    source_max_len: int = field(
        default=1024,
        metadata={"help": "Maximum source sequence length. Sequences will be right padded (and possibly truncated)."},
    )
    target_max_len: int = field(
        default=256,
        metadata={"help": "Maximum target sequence length. Sequences will be right padded (and possibly truncated)."},
    )
    dataset: str = field(
        default='spider',
        metadata={"help": "Which dataset to finetune on. See datamodule for options."}
    )
    dataset_format: Optional[str] = field(
        default="spider",
        metadata={"help": "Which dataset format is used. [alpaca|chip2|self-instruct|hh-rlhf]"}
    )

    max_eval_samples: Optional[int] = field(
        default=None,
        metadata={
            'help':
            'For debugging purposes or quicker training, truncate the number of evaluation examples to this '
            'value if set.'
        },
    )

    def init_for_training(self):  # support mixing multiple datasets
        dataset_names = [ds.strip() for ds in self.dataset_name.split(',')]
        this_dir = os.path.dirname(os.path.abspath(__file__))
        datasets_info_path = os.path.join(this_dir, '../..', 'data','data_info.yaml')
        with open(datasets_info_path, 'r') as f:
            datasets_info = yaml.safe_load(f)

        self.datasets_list: List[DatasetAttr] = []
        for i, name in enumerate(dataset_names):
            if name not in datasets_info:
                raise ValueError('Undefined dataset {} in {}'.format(
                    name, datasets_info_path))

            dataset_attr = DatasetAttr()
            dataset_attr.dataset_name = name
            dataset_attr.dataset_format = datasets_info[name].get(
                'dataset_format', None)
            dataset_attr.hf_hub_url = datasets_info[name].get(
                'hf_hub_url', None)
            dataset_attr.local_path = datasets_info[name].get(
                'local_path', None)
            dataset_attr.multi_turn = datasets_info[name].get(
                'multi_turn', False)

            if datasets_info[name]['local_path'] and os.path.exists(
                    datasets_info[name]['local_path']):
                dataset_attr.load_from_local = True
            else:
                dataset_attr.load_from_local = False
                raise Warning(
                    'You have set local_path for {} but it does not exist! Will load the data from {}'
                    .format(name, dataset_attr.hf_hub_url))

            if 'columns' in datasets_info[name]:
                dataset_attr.prompt_column = datasets_info[name][
                    'columns'].get('prompt', None)
                dataset_attr.query_column = datasets_info[name]['columns'].get(
                    'query', None)
                dataset_attr.response_column = datasets_info[name][
                    'columns'].get('response', None)
                dataset_attr.history_column = datasets_info[name][
                    'columns'].get('history', None)

            self.datasets_list.append(dataset_attr)
