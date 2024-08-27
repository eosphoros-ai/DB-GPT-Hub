import os
import sys
from typing import Any, Dict, Optional, Tuple

import datasets
import torch
import transformers
from transformers import HfArgumentParser, Seq2SeqTrainingArguments
from transformers.modeling_utils import load_sharded_checkpoint
from transformers.trainer import WEIGHTS_INDEX_NAME, WEIGHTS_NAME
from transformers.trainer_utils import get_last_checkpoint

from ..configs.data_args import DataArguments
from ..configs.model_args import (
    FinetuningArguments,
    GeneratingArguments,
    ModelArguments,
)
from .loggings import get_logger

logger = get_logger(__name__)


def get_state_dict(model: torch.nn.Module) -> Dict[str, torch.Tensor]:
    state_dict: Dict[str, torch.Tensor] = model.state_dict()
    filtered_state_dict = {}

    for k, v in model.named_parameters():
        if v.requires_grad:
            filtered_state_dict[k] = state_dict[k].cpu().clone().detach()

    return filtered_state_dict


def load_trainable_params(model: torch.nn.Module, checkpoint_dir: os.PathLike) -> bool:
    weights_file = os.path.join(checkpoint_dir, WEIGHTS_NAME)
    if os.path.exists(weights_file):
        model_state_dict = torch.load(weights_file, map_location="cpu")
        model.load_state_dict(model_state_dict, strict=False)  # skip missing keys
    elif os.path.exists(os.path.join(checkpoint_dir, WEIGHTS_INDEX_NAME)):
        load_sharded_checkpoint(model, checkpoint_dir, strict=False)
    else:
        logger.warning(
            "Provided path ({}) does not contain pre-trained weights.".format(
                checkpoint_dir
            )
        )
        return False
    return True


def _parse_args(
    parser: HfArgumentParser, args: Optional[Dict[str, Any]] = None
) -> Tuple[Any]:
    if args is not None:
        return parser.parse_dict(args)
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".yaml"):
        return parser.parse_yaml_file(os.path.abspath(sys.argv[1]))
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        return parser.parse_json_file(os.path.abspath(sys.argv[1]))
    else:
        return parser.parse_args_into_dataclasses()


def parse_train_args(
    args: Optional[Dict[str, Any]] = None
) -> Tuple[
    ModelArguments,
    DataArguments,
    Seq2SeqTrainingArguments,
    FinetuningArguments,
    GeneratingArguments,
]:
    parser = HfArgumentParser(
        (
            ModelArguments,
            DataArguments,
            Seq2SeqTrainingArguments,
            FinetuningArguments,
            GeneratingArguments,
        )
    )
    return _parse_args(parser, args)


def parse_infer_args(
    args: Optional[Dict[str, Any]] = None
) -> Tuple[ModelArguments, DataArguments, FinetuningArguments, GeneratingArguments]:
    parser = HfArgumentParser(
        (ModelArguments, DataArguments, FinetuningArguments, GeneratingArguments)
    )
    return _parse_args(parser, args)


def get_train_args(
    args: Optional[Dict[str, Any]] = None, data_args_init: bool = True
) -> Tuple[
    ModelArguments,
    DataArguments,
    Seq2SeqTrainingArguments,
    FinetuningArguments,
    GeneratingArguments,
]:
    (
        model_args,
        data_args,
        training_args,
        finetuning_args,
        generating_args,
    ) = parse_train_args(args)

    # Setup logging
    if training_args.should_log:
        # The default of training_args.log_level is passive, so we set log level at info here to have that default.
        transformers.utils.logging.set_verbosity_info()

    log_level = training_args.get_process_log_level()
    datasets.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.enable_default_handler()
    transformers.utils.logging.enable_explicit_format()

    # Check arguments (do not check finetuning_args since it may be loaded from checkpoints)
    if data_args_init:
        data_args.init_for_training()

    if training_args.max_steps == -1 and data_args.streaming:
        raise ValueError("Please specify `max_steps` in streaming mode.")

    if data_args.val_size > 1e-6 and data_args.val_size < 1 and data_args.streaming:
        raise ValueError("Streaming mode should have an integer val size.")

    if training_args.do_train and training_args.predict_with_generate:
        raise ValueError(
            "`predict_with_generate` cannot be set as True while training."
        )

    if (
        training_args.do_train
        and finetuning_args.finetuning_type == "lora"
        and finetuning_args.lora_target is None
    ):
        raise ValueError("Please specify `lora_target` in LoRA training.")

    if (
        model_args.quantization_bit is not None
        and finetuning_args.finetuning_type != "lora"
    ):
        raise ValueError("Quantization is only compatible with the LoRA method.")

    if model_args.checkpoint_dir is not None:
        if finetuning_args.finetuning_type != "lora":
            if len(model_args.checkpoint_dir) != 1:
                raise ValueError("Only LoRA tuning accepts multiple checkpoints.")
        elif (
            model_args.quantization_bit is not None
            and len(model_args.checkpoint_dir) != 1
        ):
            raise ValueError("Quantized model only accepts a single checkpoint.")

    if model_args.quantization_bit is not None and (not training_args.do_train):
        logger.warning("Evaluating model in 4/8-bit mode may cause lower scores.")

    if training_args.do_train and (not training_args.fp16) and (not training_args.bf16):
        logger.warning("We recommend enable mixed precision training.")

    # postprocess data_args
    if data_args.max_samples is not None and data_args.streaming:
        logger.warning(
            "`max_samples` is incompatible with `streaming`. Disabling max_samples."
        )
        data_args.max_samples = None

    # postprocess training_args
    if (
        training_args.local_rank != -1
        and training_args.ddp_find_unused_parameters is None
        and finetuning_args.finetuning_type == "lora"
    ):
        logger.warning(
            "`ddp_find_unused_parameters` needs to be set as False for LoRA in DDP training."
        )
        training_args_dict = training_args.to_dict()
        training_args_dict.update(dict(ddp_find_unused_parameters=False))
        training_args = Seq2SeqTrainingArguments(**training_args_dict)

    if (
        training_args.resume_from_checkpoint is None
        and training_args.do_train
        and os.path.isdir(training_args.output_dir)
        and not training_args.overwrite_output_dir
    ):
        last_checkpoint = get_last_checkpoint(training_args.output_dir)
        if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
            raise ValueError(
                "Output directory already exists and is not empty. Use `overwrite_output_dir`."
            )

        if last_checkpoint is not None:
            training_args_dict = training_args.to_dict()
            training_args_dict.update(dict(resume_from_checkpoint=last_checkpoint))
            training_args = Seq2SeqTrainingArguments(**training_args_dict)
            logger.info(
                "Resuming from checkpoint. Change `output_dir` or use `overwrite_output_dir` to avoid."
            )

    # postprocess model_args
    if training_args.bf16:
        if not torch.cuda.is_bf16_supported():
            raise ValueError("Current device does not support bf16 training.")
        model_args.compute_dtype = torch.bfloat16
    else:
        model_args.compute_dtype = torch.float16

    model_args.model_max_length = (
        data_args.max_source_length + data_args.max_target_length
    )

    # Log on each process the small summary:
    logger.info(
        "Process rank: {}, device: {}, n_gpu: {}\n  distributed training: {}, compute dtype: {}".format(
            training_args.local_rank,
            training_args.device,
            training_args.n_gpu,
            bool(training_args.local_rank != -1),
            str(model_args.compute_dtype),
        )
    )
    logger.info(f"Training/evaluation parameters {training_args}")

    # Set seed before initializing model.
    transformers.set_seed(training_args.seed)

    return model_args, data_args, training_args, finetuning_args, generating_args


def get_infer_args(
    args: Optional[Dict[str, Any]] = None
) -> Tuple[ModelArguments, DataArguments, FinetuningArguments, GeneratingArguments]:
    model_args, data_args, finetuning_args, generating_args = parse_infer_args(args)

    if (
        model_args.quantization_bit is not None
        and finetuning_args.finetuning_type != "lora"
    ):
        raise ValueError("Quantization is only compatible with the LoRA method.")

    if model_args.checkpoint_dir is not None:
        if finetuning_args.finetuning_type != "lora":
            if len(model_args.checkpoint_dir) != 1:
                raise ValueError("Only LoRA tuning accepts multiple checkpoints.")
        elif (
            model_args.quantization_bit is not None
            and len(model_args.checkpoint_dir) != 1
        ):
            raise ValueError("Quantized model only accepts a single checkpoint.")

    return model_args, data_args, finetuning_args, generating_args
