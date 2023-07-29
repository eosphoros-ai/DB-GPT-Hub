from dataclasses import dataclass, field
from typing import Optional
import os
model_path = os.path.join("./model", os.listdir("model")[1])
@dataclass
class ModelArguments:
    model_name_or_path: Optional[str] = field(
        default=model_path,
        metadata={
            'help':
            ("The model checkpoint for weights initialization. Don't set if you want to\
              train a model from scratch.")
        },
    )
    tokenizer_name: Optional[str] = field(
        default=None,
        metadata={
            'help':
            'Pretrained tokenizer name or path if not the same as model_name'
        })
    model_revision: str = field(
        default='main',
        metadata={
            'help':
            'The specific model version to use (can be a branch name, tag name or commit id).'
        },
    )
    trust_remote_code: Optional[bool] = field(
        default=False,
        metadata={
            'help':
            'Enable unpickling of arbitrary code in AutoModelForCausalLM#from_pretrained.'
        })
    use_auth_token: Optional[bool] = field(
        default=False,
        metadata={
            'help':
            'Enables using Huggingface auth token from Git Credentials.'
        })
