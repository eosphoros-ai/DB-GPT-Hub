from dataclasses import dataclass, field
from typing import Optional
import os

model_path = os.path.join("./model", os.listdir("model")[1])

@dataclass
class ModelInferenceArguments:
    cache_dir: Optional[str] = field(default=None)
    model_name_or_path: Optional[str] = field(
        default=model_path,
        metadata={'help': 'Path to pre-trained model'})
    model_max_length: int = field(
        default=2048,
        metadata={
            'help':
            'Maximum sequence length. Sequences will be right padded (and possibly truncated).'
        },
    )
    prompt_template: str = field(
        default='default',
        metadata={
            'help':
            'Prompt template name. Such as vanilla, alpaca, llama2, vicuna..., etc.'
        })
    source_prefix: Optional[str] = field(
        default=None,
        metadata={'help': 'Prefix to prepend to every source text.'})