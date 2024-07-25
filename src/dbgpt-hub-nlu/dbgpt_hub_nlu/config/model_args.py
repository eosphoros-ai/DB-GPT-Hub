from dataclasses import dataclass, field
from typing import Optional

from transformers import TrainingArguments


@dataclass
class NLUTrainingArguments(TrainingArguments):
    output_dir: str = field(
        default="output",
        metadata={
            "help": "The output directory where the model predictions and checkpoints will be written."
        },
    )
    num_train_epochs: int = field(
        default=5, metadata={"help": "Specify number of epochs, default 5"}
    )
    per_device_train_batch_size: int = field(
        default=8, metadata={"help": "Specify number of batch size, default 8"}
    )
    learning_rate: float = field(
        default=1e-4, metadata={"help": "Specify learning rate, default 1e-4"}
    )
    weight_decay: float = field(
        default=0.01, metadata={"help": "Specify weight decay, default 0.01"}
    )
    do_train: bool = field(default=False, metadata={"help": "Whether to run training."})
    eval_strategy: str = field(
        default="no", metadata={"help": "The evaluation strategy to use."}
    )
    save_strategy: str = field(
        default="no",
        metadata={"help": "The save strategy to use."},
    )
    load_best_model_at_end: bool = field(
        default=True,
        metadata={"help": "Whether to load the best model at the end of training."},
    )


@dataclass
class ModelArguments:
    """Arguments pertaining to which model/config/tokenizer we are going to fine-tune from."""

    base_model_name_or_path: str = field(
        metadata={
            "help": "Path to pretrained model or model identifier from huggingface.co/models"
        }
    )

    base_tokenizer_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Base pretrained tokenizer name or path if not the same as model_name"
        },
    )

    config_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Pretrained config name or path if not the same as model_name"
        },
    )
    tokenizer_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Pretrained tokenizer name or path if not the same as model_name"
        },
    )
    cache_dir: Optional[str] = field(
        default=None,
        metadata={
            "help": "Where to store the pretrained models downloaded from huggingface.co"
        },
    )
    use_fast_tokenizer: bool = field(
        default=True,
        metadata={
            "help": "Whether to use one of the fast tokenizer (backed by the tokenizers library) or not."
        },
    )
    model_revision: str = field(
        default="main",
        metadata={
            "help": "The specific model version to use (can be a branch name, tag name or commit id)."
        },
    )
    use_auth_token: bool = field(
        default=False,
        metadata={
            "help": "Will use the token generated when running `transformers-cli login` (necessary to use this script "
            "with private models)."
        },
    )

    lora_r: int = field(
        default=8,
        metadata={"help": "Lora R dimension"},
    )
    lora_alpha: int = field(
        default=32,
        metadata={"help": "Lora alpha parameter"},
    )
    lora_dropout: float = field(
        default=0.1,
        metadata={"help": "Lora dropout probability"},
    )
    max_length: int = field(
        default=512,
        metadata={"help": "Maximum input sequence length"},
    )
