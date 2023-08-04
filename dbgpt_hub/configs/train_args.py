from dataclasses import dataclass, field
from typing import Optional
from transformers import TrainingArguments


@dataclass
class TrainingArguments(transformers.Seq2SeqTrainingArguments):
    cache_dir: Optional[str] = field(default=None)
    train_on_source: Optional[bool] = field(
        default=False,
        metadata={"help": "Whether to train on the input in addition to the target text."}
    )
    full_finetune: bool = field(
        default=False,
        metadata={'help': 'Finetune the entire model without adapters.'})
    do_train: bool = field(
        default=True,
        metadata={'help': 'To train or not to train, that is the question?'})
    sample_generate: bool = field(
        default=False,
        metadata={'help': 'If do sample generation on evaluation.'})
    optim: str = field(default='paged_adamw_32bit',
                       metadata={'help': 'The optimizer to be used'})
    max_grad_norm: float = field(
        default=0.3,
        metadata={
            'help':
            'Gradient clipping max norm. This is tuned and works well for all models tested.'
        })
    gradient_checkpointing: bool = field(
        default=True,
        metadata={'help': 'Use gradient checkpointing. You want to use this.'})
    predict_with_generate: bool = field(
        default=False,
        metadata={
            'help':
            'Group sequences into batches with same length. Saves memory and speeds up training considerably.'
        })
    model_max_length: int = field(
        default=2048,
        metadata={
            'help':
            'Maximum sequence length. Sequences will be right padded (and possibly truncated).'
        },
    )
    output_dir: str = field(default='./adapter', metadata={"help": 'The output dir for logs and checkpoints'})
    per_device_train_batch_size: int = field(default=1, metadata={"help": 'The training batch size per GPU. Increase for better speed.'})
    gradient_accumulation_steps: int = field(default=16, metadata={"help": 'How many gradients to accumulate before to perform an optimizer step'})
    max_steps: int = field(default=10000, metadata={"help": 'How many optimizer update steps to take'})
    weight_decay: float = field(default=0.0, metadata={"help": 'The L2 weight decay rate of AdamW'}) # use lora dropout instead for regularization if needed
    learning_rate: float = field(default=0.0002, metadata={"help": 'The learnign rate'})
    remove_unused_columns: bool = field(default=False, metadata={"help": 'Removed unused columns. Needed to make this codebase work.'})
    lr_scheduler_type: str = field(default='constant', metadata={"help": 'Learning rate schedule. Constant a bit better than cosine, and has advantage for analysis'})
    warmup_ratio: float = field(default=0.03, metadata={"help": 'Fraction of steps to do a warmup for'})
    logging_steps: int = field(default=10, metadata={"help": 'The frequency of update steps after which to log the loss'})
    group_by_length: bool = field(default=True, metadata={"help": 'Group sequences into batches with same length. Saves memory and speeds up training considerably.'})
    save_strategy: str = field(default='steps', metadata={"help": 'When to save checkpoints'})
    save_steps: int = field(default=250, metadata={"help": 'How often to save a model'})
    save_total_limit: int = field(default=40, metadata={"help": 'How many checkpoints to save before the oldest is overwritten'})
