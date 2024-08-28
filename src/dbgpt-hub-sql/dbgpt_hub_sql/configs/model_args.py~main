import json
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, Literal, Optional

import torch
from transformers import Seq2SeqTrainingArguments

from .config import ADAPTER_PATH


@dataclass
class ModelArguments:
    r"""
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune.
    """
    model_name_or_path: str = field(
        metadata={
            "help": "Path to pretrained model or model identifier from huggingface.co/models."
        }
    )
    cache_dir: Optional[str] = field(
        default=None,
        metadata={
            "help": "Where to store the pretrained models downloaded from huggingface.co."
        },
    )
    use_fast_tokenizer: Optional[bool] = field(
        default=False,
        metadata={
            "help": "Whether to use one of the fast tokenizer (backed by the tokenizers library) or not."
        },
    )
    use_auth_token: Optional[bool] = field(
        default=False,
        metadata={
            "help": "Will use the token generated when running `huggingface-cli login`."
        },
    )
    model_revision: Optional[str] = field(
        default="main",
        metadata={
            "help": "The specific model version to use (can be a branch name, tag name or commit id)."
        },
    )
    padding_side: Optional[Literal["left", "right"]] = field(
        default="left",
        metadata={"help": "The side on which the model should have padding applied."},
    )
    quantization_bit: Optional[int] = field(
        default=None, metadata={"help": "The number of bits to quantize the model."}
    )
    quantization_type: Optional[Literal["fp4", "nf4"]] = field(
        default="nf4",
        metadata={"help": "Quantization data type to use in int4 training."},
    )
    double_quantization: Optional[bool] = field(
        default=True,
        metadata={
            "help": "Whether to use double quantization in int4 training or not."
        },
    )
    rope_scaling: Optional[Literal["linear", "dynamic"]] = field(
        default=None, metadata={"help": "Adopt scaled rotary positional embeddings."}
    )
    checkpoint_dir: Optional[str] = field(
        default=None,
        metadata={
            "help": "Path to the directory(s) containing the delta model checkpoints as well as the configurations."
        },
    )
    # reward_model: Optional[str] = field(
    #     default=None,
    #     metadata={"help": "Path to the directory containing the checkpoints of the reward model."}
    # )
    plot_loss: Optional[bool] = field(
        default=False,
        metadata={
            "help": "Whether to plot the training loss after fine-tuning or not."
        },
    )
    hf_auth_token: Optional[str] = field(
        default=None, metadata={"help": "Auth token to log in with Hugging Face Hub."}
    )
    compute_dtype: Optional[torch.dtype] = field(
        default=None,
        metadata={
            "help": "Used in quantization configs. Do not specify this argument manually."
        },
    )
    model_max_length: Optional[int] = field(
        default=None,
        metadata={
            "help": "Used in rope scaling. Do not specify this argument manually."
        },
    )
    hf_hub_token: Optional[str] = field(
        default=None, metadata={"help": "Auth token to log in with Hugging Face Hub."}
    )
    split_special_tokens: Optional[bool] = field(
        default=False,
        metadata={
            "help": "Whether or not the special tokens should be split during the tokenization process."
        },
    )

    def __post_init__(self):
        if self.compute_dtype is not None or self.model_max_length is not None:
            raise ValueError("These arguments cannot be specified.")

        if self.checkpoint_dir is not None:  # support merging multiple lora weights
            self.checkpoint_dir = [cd.strip() for cd in self.checkpoint_dir.split(",")]

        if self.quantization_bit is not None:
            assert self.quantization_bit in [
                4,
                8,
            ], "We only accept 4-bit or 8-bit quantization."

        if self.use_auth_token == True and self.hf_auth_token is not None:
            from huggingface_hub.hf_api import HfFolder  # lazy load

            HfFolder.save_token(self.hf_auth_token)


@dataclass
class GeneratingArguments:
    r"""
    Arguments pertaining to specify the decoding parameters.
    """
    do_sample: Optional[bool] = field(
        default=True,
        metadata={
            "help": "Whether or not to use sampling, use greedy decoding otherwise."
        },
    )
    temperature: Optional[float] = field(
        default=0.95,
        metadata={"help": "The value used to modulate the next token probabilities."},
    )
    top_p: Optional[float] = field(
        default=0.7,
        metadata={
            "help": "The smallest set of most probable tokens with probabilities that add up to top_p or higher are kept."
        },
    )
    top_k: Optional[int] = field(
        default=50,
        metadata={
            "help": "The number of highest probability vocabulary tokens to keep for top-k filtering."
        },
    )
    num_beams: Optional[int] = field(
        default=1,
        metadata={"help": "Number of beams for beam search. 1 means no beam search."},
    )
    max_length: Optional[int] = field(
        default=None,
        metadata={
            "help": "The maximum length the generated tokens can have. It can be overridden by max_new_tokens."
        },
    )
    max_new_tokens: Optional[int] = field(
        default=512,
        metadata={
            "help": "The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt."
        },
    )
    repetition_penalty: Optional[float] = field(
        default=1.0,
        metadata={
            "help": "The parameter for repetition penalty. 1.0 means no penalty."
        },
    )
    length_penalty: Optional[float] = field(
        default=1.0,
        metadata={
            "help": "Exponential penalty to the length that is used with beam-based generation."
        },
    )

    def to_dict(self) -> Dict[str, Any]:
        args = asdict(self)
        if args.get("max_new_tokens", None):
            args.pop("max_length", None)
        return args


@dataclass
class FinetuningArguments:
    r"""
    Arguments pertaining to which techniques we are going to fine-tuning with.
    """
    stage: Optional[Literal["sft", "rm"]] = field(
        default="sft", metadata={"help": "Which stage will be performed in training."}
    )
    finetuning_type: Optional[Literal["lora", "freeze", "full", "none"]] = field(
        default="lora", metadata={"help": "Which fine-tuning method to use."}
    )
    num_hidden_layers: Optional[int] = field(
        default=32,
        metadata={
            "help": 'Number of decoder blocks in the model for partial-parameter (freeze) fine-tuning. \
                  LLaMA choices: ["32", "40", "60", "80"], \
                  LLaMA-2 choices: ["32", "40", "80"], \
                  BLOOM choices: ["24", "30", "70"], \
                  Falcon choices: ["32", "60"], \
                  Baichuan choices: ["32", "40"] \
                  Qwen choices: ["32"], \
                  XVERSE choices: ["40"], \
                  ChatGLM2 choices: ["28"],\
                  ChatGLM3 choices: ["28"]'
        },
    )
    num_layer_trainable: Optional[int] = field(
        default=3,
        metadata={
            "help": "Number of trainable layers for partial-parameter (freeze) fine-tuning."
        },
    )
    name_module_trainable: Optional[
        Literal["mlp", "self_attn", "self_attention"]
    ] = field(
        default="mlp",
        metadata={
            "help": 'Name of trainable modules for partial-parameter (freeze) fine-tuning. \
                  LLaMA choices: ["mlp", "self_attn"], \
                  BLOOM & Falcon & ChatGLM2   & ChatGLM3choices: ["mlp", "self_attention"], \
                  Baichuan choices: ["mlp", "self_attn"], \
                  Qwen choices: ["mlp", "attn"], \
                  LLaMA-2, InternLM, XVERSE choices: the same as LLaMA.'
        },
    )
    lora_rank: Optional[int] = field(
        default=8, metadata={"help": "The intrinsic dimension for LoRA fine-tuning."}
    )
    lora_alpha: Optional[float] = field(
        default=32.0,
        metadata={
            "help": "The scale factor for LoRA fine-tuning (similar with the learning rate)."
        },
    )
    lora_dropout: Optional[float] = field(
        default=0.1, metadata={"help": "Dropout rate for the LoRA fine-tuning."}
    )
    lora_target: Optional[str] = field(
        default=None,
        metadata={
            "help": 'Name(s) of target modules to apply LoRA. Use commas to separate multiple modules. \
                  LLaMA choices: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"], \
                  BLOOM & Falcon & ChatGLM2  & ChatGLM3 choices: ["query_key_value", "self_attention.dense", "mlp.dense"], \
                  Baichuan choices: ["W_pack", "o_proj", "gate_proj", "up_proj", "down_proj"], \
                  Qwen choices: ["c_attn", "attn.c_proj", "w1", "w2", "mlp.c_proj"], \
                  LLaMA-2, InternLM, XVERSE choices: the same as LLaMA.'
        },
    )
    resume_lora_training: Optional[bool] = field(
        default=True,
        metadata={
            "help": "Whether to resume training from the last LoRA weights or create new weights after merging them."
        },
    )
    ppo_score_norm: Optional[bool] = field(
        default=False, metadata={"help": "Use score normalization in PPO Training."}
    )
    dpo_beta: Optional[float] = field(
        default=0.1, metadata={"help": "The beta parameter for the DPO loss."}
    )

    def __post_init__(self):
        if isinstance(
            self.lora_target, str
        ):  # support custom target modules/layers of LoRA
            self.lora_target = [
                target.strip() for target in self.lora_target.split(",")
            ]

        if (
            self.num_layer_trainable > 0
        ):  # fine-tuning the last n layers if num_layer_trainable > 0
            trainable_layer_ids = [
                self.num_hidden_layers - k - 1 for k in range(self.num_layer_trainable)
            ]
        else:  # fine-tuning the first n layers if num_layer_trainable < 0
            trainable_layer_ids = [k for k in range(-self.num_layer_trainable)]

        self.trainable_layers = [
            "{:d}.{}".format(idx, self.name_module_trainable)
            for idx in trainable_layer_ids
        ]

        assert self.finetuning_type in [
            "lora",
            "freeze",
            "full",
            "none",
        ], "Invalid fine-tuning method."

    def save_to_json(self, json_path: str):
        r"""Saves the content of this instance in JSON format inside `json_path`."""
        json_string = json.dumps(asdict(self), indent=2, sort_keys=True) + "\n"
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(json_string)

    @classmethod
    def load_from_json(cls, json_path: str):
        r"""Creates an instance from the content of `json_path`."""
        with open(json_path, "r", encoding="utf-8") as f:
            text = f.read()
        return cls(**json.loads(text))


@dataclass
class TrainingArguments(Seq2SeqTrainingArguments):
    cache_dir: Optional[str] = field(default=None)
    train_on_source: Optional[bool] = field(
        default=False,
        metadata={
            "help": "Whether to train on the input in addition to the target text."
        },
    )
    full_finetune: bool = field(
        default=False, metadata={"help": "Finetune the entire model without adapters."}
    )
    do_train: bool = field(
        default=True,
        metadata={"help": "To train or not to train, that is the question?"},
    )
    sample_generate: bool = field(
        default=False, metadata={"help": "If do sample generation on evaluation."}
    )
    optim: str = field(
        default="paged_adamw_32bit", metadata={"help": "The optimizer to be used"}
    )
    max_grad_norm: float = field(
        default=0.3,
        metadata={
            "help": "Gradient clipping max norm. This is tuned and works well for all models tested."
        },
    )
    gradient_checkpointing: bool = field(
        default=True,
        metadata={"help": "Use gradient checkpointing. You want to use this."},
    )
    predict_with_generate: bool = field(
        default=False,
        metadata={
            "help": "Group sequences into batches with same length. Saves memory and speeds up training considerably."
        },
    )
    model_max_length: int = field(
        default=2048,
        metadata={
            "help": "Maximum sequence length. Sequences will be right padded (and possibly truncated)."
        },
    )
    output_dir: str = field(
        default=ADAPTER_PATH,
        metadata={"help": "The output dir for logs and checkpoints"},
    )
    per_device_train_batch_size: int = field(
        default=1,
        metadata={
            "help": "The training batch size per GPU. Increase for better speed."
        },
    )
    gradient_accumulation_steps: int = field(
        default=16,
        metadata={
            "help": "How many gradients to accumulate before to perform an optimizer step"
        },
    )
    max_steps: int = field(
        default=10000, metadata={"help": "How many optimizer update steps to take"}
    )
    # use lora dropout instead for regularization if needed
    weight_decay: float = field(
        default=0.0, metadata={"help": "The L2 weight decay rate of AdamW"}
    )
    learning_rate: float = field(default=0.0002, metadata={"help": "The learnign rate"})
    remove_unused_columns: bool = field(
        default=False,
        metadata={"help": "Removed unused columns. Needed to make this codebase work."},
    )
    lr_scheduler_type: str = field(
        default="constant",
        metadata={
            "help": "Learning rate schedule. Constant a bit better than cosine, and has advantage for analysis"
        },
    )
    warmup_ratio: float = field(
        default=0.03, metadata={"help": "Fraction of steps to do a warmup for"}
    )
    logging_steps: int = field(
        default=10,
        metadata={"help": "The frequency of update steps after which to log the loss"},
    )
    group_by_length: bool = field(
        default=True,
        metadata={
            "help": "Group sequences into batches with same length. Saves memory and speeds up training considerably."
        },
    )
    save_strategy: str = field(
        default="steps", metadata={"help": "When to save checkpoints"}
    )
    save_steps: int = field(default=250, metadata={"help": "How often to save a model"})
    save_total_limit: int = field(
        default=40,
        metadata={
            "help": "How many checkpoints to save before the oldest is overwritten"
        },
    )
