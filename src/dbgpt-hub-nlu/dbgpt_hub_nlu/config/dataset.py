import os
from dataclasses import dataclass, field
from typing import Optional


import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DataArguments:
    dataset: str = field(
        default="financial_report",
        metadata={"help": "The name of the dataset to use."},
    )
    dataset_dir: str = field(
        default="./datasets",
        metadata={"help": "The name of the folder containing datasets."},
    )
    preprocess_batch_size: int = field(
        default=8, metadata={"help": "Batch size for data preprocess"}
    )
    max_train_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of training examples to this "
            "value if set."
        },
    )

    max_val_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of validation or test examples to this "
            "value if set."
        },
    )

    def get_dataset_path(self):
        if os.path.exists(self.dataset):
            abs_path = os.path.abspath(self.dataset)
            return abs_path
        abs_path = os.path.abspath(os.path.join(self.dataset_dir, self.dataset))
        return abs_path


@dataclass
class InferArguments:
    do_infer: bool = field(
        default=False,
        metadata={"help": "Whether to perform inference."},
    )
    input_text: Optional[str] = field(
        default=None,
        metadata={"help": "The text to perform inference on."},
    )
