### TODO 此处文件待作废。
import os
import torch
import argparse
import logging
import pathlib
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Union
from deepspeed import zero
from deepspeed.runtime.zero.partition_parameters import ZeroParamStatus
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    PreTrainedModel,
    PreTrainedTokenizer,
    Seq2SeqTrainer,
    deepspeed,
)

# TODO 待解决引用问题，白色的。0919
from dbgpt_hub.configs import DataArguments, ModelArguments, TrainingArguments
from dbgpt_hub.data_process import make_supervised_data_module
from dbgpt_hub.utils.model_utils import add_special_tokens_if_missing


@dataclass
class LoraArguments:
    lora_r: int = 32
    lora_alpha: int = 16
    lora_dropout: float = 0.05
    lora_target_modules: List[str] = field(
        default_factory=lambda: [
            "q_proj",
            "v_proj",
            "k_proj",
            "down_proj",
            "gate_proj",
            "up_proj",
        ]
    )
    lora_weight_path: str = ""
    lora_bias: str = "none"
    q_lora: bool = False


def maybe_zero_3(param: Union[torch.Tensor, object]) -> torch.Tensor:
    """
    Applies zero.GatheredParameters to gather the parameter if it has ds_id attribute,
    and clones and detaches the tensor data if ds_status is ZeroParamStatus.NOT_AVAILABLE.

    Args:
        param: The parameter to be processed.

    Returns:
        The modified parameter.

    Raises:
        AssertionError: If `param` has ds_id attribute but ds_status is not ZeroParamStatus.NOT_AVAILABLE.
    """
    if hasattr(param, "ds_id"):
        assert param.ds_status == ZeroParamStatus.NOT_AVAILABLE, "Invalid ds_status"

        with zero.GatheredParameters([param]):
            param = param.data.detach().cpu().clone()
    else:
        param = param.detach().cpu().clone()
    return param


# Borrowed from peft.utils.get_peft_model_state_dict
def get_peft_state_maybe_zero_3(
    named_params: List[Tuple[str, torch.Tensor]], bias: str
) -> Dict[str, torch.Tensor]:
    """
    Filters and processes named parameters based on the specified bias.

    Args:
        named_params: An iterable containing tuples of parameter names and their corresponding values.
        bias: The bias type.

    Returns:
        A dictionary containing the filtered and possibly modified named parameters.

    Raises:
        NotImplementedError: If an unsupported bias type is provided.
    """
    to_return: Dict[str, torch.Tensor] = {}

    if bias == "none":
        to_return = {k: t for k, t in named_params if "lora_" in k}
    elif bias == "all":
        to_return = {k: t for k, t in named_params if "lora_" in k or "bias" in k}
    elif bias == "lora_only":
        maybe_lora_bias: Dict[str, torch.Tensor] = {}
        lora_bias_names: set() = set()

        for k, t in named_params:
            if "lora_" in k:
                to_return[k] = t
                bias_name = k.split("lora_")[0] + "bias"
                lora_bias_names.add(bias_name)
            elif "bias" in k:
                maybe_lora_bias[k] = t

        for k, t in maybe_lora_bias.items():
            bias_name = k.split("bias")[0] + "bias"
            if bias_name in lora_bias_names:
                to_return[bias_name] = t
    else:
        raise NotImplementedError("Unsupported bias type")

    to_return = {k: maybe_zero_3(v) for k, v in to_return.items()}

    return to_return


def load_model_tokenizer(
    args: argparse.Namespace,
) -> Tuple[PreTrainedModel, PreTrainedTokenizer]:
    """
    Load a pre-trained model and tokenizer for natural language processing tasks.

    Args:
        args: An object containing the input arguments.

    Returns:
        A tuple containing the loaded model and tokenizer.
    """

    # Determine torch dtype for model based on arguments
    if args.fp16:
        compute_dtype = torch.float16
    elif args.bf16:
        compute_dtype = torch.bfloat16
    else:
        compute_dtype = torch.float32

    device_map: Union[str, None] = "auto"
    if args.q_lora:
        world_size = int(os.environ.get("WORLD_SIZE", 1))
        device_map = (
            {"": int(os.environ.get("LOCAL_RANK") or 0)} if world_size != 1 else None
        )
        if len(args.fsdp) > 0 or deepspeed.is_deepspeed_zero3_enabled():
            logging.warning(
                "FSDP and ZeRO3 are both currently incompatible with QLoRA."
            )

    # Set configuration kwargs for tokenizer.
    config_kwargs = {
        "cache_dir": args.cache_dir,
        "use_auth_token": args.use_auth_token,
        "trust_remote_code": args.trust_remote_code,
    }

    # support multi gpu
    if torch.cuda.is_available():
        n_gpus = torch.cuda.device_count()
    device_map = "auto"
    # if we are in a distributed setting, we need to set the device map and max memory per device
    if os.environ.get("LOCAL_RANK") is not None:
        local_rank = int(os.environ.get("LOCAL_RANK", "0"))
        device_map = {"": local_rank}

    # Load the pre-trained model
    print(f"Loading Model from {args.model_name_or_path}...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        device_map=device_map,
        quantization_config=BitsAndBytesConfig(
            load_in_4bit=True,
            llm_int8_threshold=6.0,
            llm_int8_has_fp16_weight=False,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=compute_dtype,
        )
        if args.q_lora
        else None,
        torch_dtype=compute_dtype,
        **config_kwargs,
    )

    # Add LoRA sparsity if specified
    logging.warning("Adding LoRA modules...")
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        target_modules=args.lora_target_modules,
        lora_dropout=args.lora_dropout,
        bias=args.lora_bias,
        task_type="CAUSAL_LM",
    )
    if args.q_lora:
        logging.warning("Preparemodel for kbit training!!!")
        model = prepare_model_for_kbit_training(
            model, use_gradient_checkpointing=args.gradient_checkpointing
        )
        if torch.cuda.device_count() > 1:
            # Keeps Trainer from trying its own DataParallelism when more than 1 GPU is available
            setattr(model, "model_parallel", True)
            setattr(model, "is_parallelizable", True)

    logging.warning("Get the get peft model...")
    model = get_peft_model(model, lora_config)
    if args.deepspeed is not None and args.local_rank == 0:
        model.print_trainable_parameters()

    if args.gradient_checkpointing:
        logging.warning("Using gradient checkpointing...")
        model.enable_input_require_grads()
        model.config.use_cache = (
            False  # Turn off when gradient checkpointing is enabled
        )

    # Load the tokenizer
    print(f"Loading tokenizer from {args.model_name_or_path}...")
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name_or_path,
        padding_side="right",
        use_fast=False,
        model_max_length=args.model_max_length,
        tokenizer_type="llama" if "llama" in args.model_name_or_path else None,
        **config_kwargs,
    )

    return model, tokenizer


def train() -> None:
    """Trains a language model using Hugging Face's Transformers library.

    Returns:
        None
    """
    parser = HfArgumentParser(
        (ModelArguments, DataArguments, TrainingArguments, LoraArguments)
    )
    (
        model_args,
        data_args,
        training_args,
        lora_args,
    ) = parser.parse_args_into_dataclasses()
    data_args.init_for_training()
    args = argparse.Namespace(
        **vars(model_args), **vars(data_args), **vars(training_args), **vars(lora_args)
    )
    # Log on each process the small summary:
    logging.warning(
        f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
    )
    logging.warning(
        f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
    )
    logging.warning(f"Training parameters {training_args}")

    # load model and tokenizer
    model, tokenizer = load_model_tokenizer(args=args)
    logging.warning("Successfully loaded model and tokenizer.")

    if "llama" in args.model_name_or_path or "baichuan" in args.model_name_or_path:
        logging.warning(f"Adding special tokens for {args.model_name_or_path}.")
        add_special_tokens_if_missing(tokenizer, model)

    # Create a supervised dataset and Trainer, then train the model
    logging.warning("Creating a supervised dataset and DataCollator...")
    args.instruction_template = "spider"
    data_module = make_supervised_data_module(tokenizer=tokenizer, args=args)

    # Create a Trainer object and start training
    logging.warning("Creating a Trainer...")
    trainer = Seq2SeqTrainer(
        model=model, tokenizer=tokenizer, args=training_args, **data_module
    )

    logging.warning("Starting training...")
    if training_args.resume_from_checkpoint and list(
        pathlib.Path(training_args.output_dir).glob("checkpoint-*")
    ):
        logging.warning("Resuming from checkpoint...")
        trainer.train(resume_from_checkpoint=True)
    else:
        trainer.train()

    trainer.save_state()
    # Save the trained model
    # check if zero3 mode enabled
    if deepspeed.is_deepspeed_zero3_enabled():
        # use deepspeed engine internal function to gather state dict
        # state_dict_zero3 contains whole parameters of base and lora adapters
        # we will not extract lora parameters since peft save_pretrained will do that
        # https://github.com/huggingface/peft/blob/3714aa2fff158fdfa637b2b65952580801d890b2/src/peft/peft_model.py#L125
        # https://github.com/huggingface/peft/blob/3714aa2fff158fdfa637b2b65952580801d890b2/src/peft/utils/save_and_load.py#L19
        state_dict_zero3 = trainer.model_wrapped._zero3_consolidated_16bit_state_dict()
        if training_args.local_rank == 0:
            state_dict = state_dict_zero3
    else:
        # in other mode we use original code from fastchat team, to make sure our change is minimum
        state_dict = get_peft_state_maybe_zero_3(
            model.named_parameters(), lora_args.lora_bias
        )

    if training_args.local_rank == 0:
        model.save_pretrained(training_args.output_dir, state_dict=state_dict)


if __name__ == "__main__":
    train()
