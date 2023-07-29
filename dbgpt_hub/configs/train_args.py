from dataclasses import dataclass, field
from typing import Optional
from transformers import TrainingArguments


@dataclass
class TrainingArguments(TrainingArguments):
    cache_dir: Optional[str] = field(default=None)
    full_finetune: bool = field(
        default=False,
        metadata={'help': 'Finetune the entire model without adapters.'})
    do_train: bool = field(
        default=True,
        metadata={'help': 'To train or not to train, that is the question?'})
    do_eval: bool = field(
        default=False,
        metadata={'help': 'To train or not to train, that is the question?'})
    do_mmlu_eval: Optional[bool] = field(
        default=False,
        metadata={'help': 'Whether to run the MMLU evaluation.'})
    mmlu_dataset: Optional[str] = field(
        default='mmlu-fs',
        metadata={
            'help':
            'MMLU dataset to use: options are `mmlu-zs` for zero-shot or `mmlu-fs` for few shot.'
        })
    mmlu_split: Optional[str] = field(
        default='eval', metadata={'help': 'The MMLU split to run on'})
    max_mmlu_samples: Optional[int] = field(
        default=None,
        metadata={
            'help':
            'If set, only evaluates on `max_mmlu_samples` of the MMMLU dataset.'
        })
    mmlu_source_max_len: int = field(
        default=2048,
        metadata={'help': 'Maximum source sequence length for mmlu.'})
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
        default=1024,
        metadata={
            'help':
            'Maximum sequence length. Sequences will be right padded (and possibly truncated).'
        },
    )
