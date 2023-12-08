import os
import torch
import math
from typing import Optional, Tuple, Dict, TYPE_CHECKING, Literal, List
from types import MethodType
from trl import AutoModelForCausalLMWithValueHead
from dbgpt_hub.llm_base.loggings import reset_logging, get_logger
from dbgpt_hub.configs.model_args import FinetuningArguments
from dbgpt_hub.llm_base.adapter import init_adapter
from dbgpt_hub.configs.config import LAYERNORM_NAMES, VALUE_HEAD_FILE_NAME

from transformers import PreTrainedModel, PreTrainedTokenizer
from transformers.utils import check_min_version
from transformers.utils.versions import require_version
from transformers.deepspeed import is_deepspeed_zero3_enabled
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    PretrainedConfig,
    PreTrainedModel,
    PreTrainedTokenizerBase,
)

if TYPE_CHECKING:
    from transformers import PreTrainedTokenizer
    from dbgpt_hub.configs.model_args import ModelArguments


logger = get_logger(__name__)


check_min_version("4.29.1")
require_version("datasets>=2.12.0", "To fix: pip install datasets>=2.12.0")
require_version("accelerate>=0.21.0", "To fix: pip install accelerate>=0.21.0")
require_version("peft>=0.4.0", "To fix: pip install peft>=0.4.0")
require_version("trl>=0.5.0", "To fix: pip install trl>=0.5.0")


def count_parameters(model: torch.nn.Module) -> Tuple[int, int]:
    r"""
    Returns the number of trainable parameters and number of all parameters in the model.
    """
    trainable_params, all_param = 0, 0
    for param in model.parameters():
        num_params = param.numel()
        # if using DS Zero 3 and the weights are initialized empty
        if num_params == 0 and hasattr(param, "ds_numel"):
            num_params = param.ds_numel

        # Due to the design of 4bit linear layers from bitsandbytes, multiply the number of parameters by 2
        if param.__class__.__name__ == "Params4bit":
            num_params = num_params * 2

        all_param += num_params
        if param.requires_grad:
            trainable_params += num_params

    return trainable_params, all_param


# Includes: (1) cast the layernorm in fp32 (2) make output embedding layer require grads (3) upcast the lm_head to fp32
# Inspired by: https://github.com/huggingface/peft/blob/c0209c35abbf88c63aa267800d98a8e212ed0a42/src/peft/utils/other.py#L35
def prepare_model_for_training(
    model: "PreTrainedModel",
    finetuning_type: str,
    output_layer_name: Optional[str] = "lm_head",
    use_gradient_checkpointing: Optional[bool] = True,
    layer_norm_names: Optional[List[str]] = LAYERNORM_NAMES,
) -> "PreTrainedModel":
    for name, param in model.named_parameters():
        if param.ndim == 1 and any(
            layer_norm_name in name for layer_norm_name in layer_norm_names
        ):
            param.data = param.data.to(torch.float32)

    if use_gradient_checkpointing:
        if hasattr(model, "enable_input_require_grads"):
            model.enable_input_require_grads()
        else:

            def make_inputs_require_grad(module, input, output):
                output.requires_grad_(True)

            model.get_input_embeddings().register_forward_hook(make_inputs_require_grad)

        model.gradient_checkpointing_enable()
        model.config.use_cache = (
            False  # turn off when gradient checkpointing is enabled
        )

    if finetuning_type != "full" and hasattr(model, output_layer_name):
        output_layer: torch.nn.Linear = getattr(model, output_layer_name)
        input_dtype = output_layer.weight.dtype

        class CastOutputToFloat(torch.nn.Sequential):
            def forward(self, x: torch.Tensor) -> torch.Tensor:
                return super().forward(x.to(input_dtype)).to(torch.float32)

        setattr(model, output_layer_name, CastOutputToFloat(output_layer))

    return model


def load_valuehead_params(model: torch.nn.Module, checkpoint_dir: os.PathLike) -> bool:
    valuehead_file = os.path.join(checkpoint_dir, VALUE_HEAD_FILE_NAME)
    if not os.path.exists(valuehead_file):
        logger.warning(
            "Provided path ({}) does not contain valuehead weights.".format(
                checkpoint_dir
            )
        )
        return False
    valuehead_state_dict = torch.load(valuehead_file, map_location="cpu")
    model.register_buffer("reward_head_weight", valuehead_state_dict["summary.weight"])
    model.register_buffer("reward_head_bias", valuehead_state_dict["summary.bias"])
    model.register_buffer(
        "default_head_weight", torch.zeros_like(valuehead_state_dict["summary.weight"])
    )
    model.register_buffer(
        "default_head_bias", torch.zeros_like(valuehead_state_dict["summary.bias"])
    )
    return True


def load_model_and_tokenizer(
    model_args: "ModelArguments",
    finetuning_args: "FinetuningArguments",
    is_trainable: Optional[bool] = False,
    stage: Optional[Literal["pt", "sft", "rm", "ppo"]] = "sft",
) -> Tuple[PreTrainedModel, "PreTrainedTokenizer"]:
    r"""
    Loads pretrained model and tokenizer.

    Support both training and inference.
    """
    if (not is_trainable) and model_args.checkpoint_dir is None:
        logger.warning(
            "Checkpoint is not found at evaluation, load the original model."
        )
        finetuning_args = FinetuningArguments(finetuning_type="none")

    config_kwargs = {
        "trust_remote_code": True,
        "cache_dir": model_args.cache_dir,
        "revision": model_args.model_revision,
        "use_auth_token": True if model_args.use_auth_token else None,
    }

    tokenizer = AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        use_fast=model_args.use_fast_tokenizer,
        padding_side=model_args.padding_side,
        **config_kwargs
    )

    if (
        finetuning_args.finetuning_type == "full"
        and model_args.checkpoint_dir is not None
    ):
        model_to_load = model_args.checkpoint_dir[0]
    else:
        model_to_load = model_args.model_name_or_path

    config = AutoConfig.from_pretrained(model_to_load, **config_kwargs)

    if hasattr(config, "fp16") and hasattr(config, "bf16"):  # fix Qwen config
        if model_args.compute_dtype == torch.bfloat16:
            setattr(config, "bf16", True)
        else:
            setattr(config, "fp16", True)

    # Set RoPE scaling
    if model_args.rope_scaling is not None:
        if hasattr(config, "use_dynamic_ntk"):  # for Qwen models
            if is_trainable:
                logger.warning("Qwen model does not support RoPE scaling in training.")
            else:
                setattr(config, "use_dynamic_ntk", True)
                setattr(config, "use_logn_attn", True)
                logger.info("Using dynamic NTK scaling.")

        elif hasattr(config, "rope_scaling"):  # for LLaMA models
            require_version(
                "transformers>=4.31.0", "RoPE scaling requires transformers>=4.31.0"
            )

            if is_trainable:
                if model_args.rope_scaling == "dynamic":
                    logger.warning(
                        "Dynamic NTK may not work well with fine-tuning. "
                        "See: https://github.com/huggingface/transformers/pull/24653"
                    )

                current_max_length = getattr(config, "max_position_embeddings", None)
                if (
                    current_max_length
                    and model_args.model_max_length > current_max_length
                ):
                    scaling_factor = float(
                        math.ceil(model_args.model_max_length / current_max_length)
                    )
                else:
                    logger.warning(
                        "Input length is smaller than max length. Consider increase input length."
                    )
                    scaling_factor = 1.0
            else:
                scaling_factor = 2.0

            setattr(
                config,
                "rope_scaling",
                {"type": model_args.rope_scaling, "factor": scaling_factor},
            )
            logger.info(
                "Using {} scaling strategy and setting scaling factor to {}".format(
                    model_args.rope_scaling, scaling_factor
                )
            )

        else:
            logger.warning("Current model does not support RoPE scaling.")

    # Quantization configurations (using bitsandbytes library).
    is_mergeable = True
    if model_args.quantization_bit is not None:
        if is_deepspeed_zero3_enabled():
            raise ValueError("DeepSpeed ZeRO-3 is incompatible with quantization.")

        if model_args.quantization_bit == 8:
            require_version(
                "bitsandbytes>=0.37.0", "To fix: pip install bitsandbytes>=0.37.0"
            )
            config_kwargs["load_in_8bit"] = True
            config_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)

        elif model_args.quantization_bit == 4:
            require_version(
                "bitsandbytes>=0.39.0", "To fix: pip install bitsandbytes>=0.39.0"
            )
            config_kwargs["load_in_4bit"] = True
            config_kwargs["quantization_config"] = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=model_args.compute_dtype,
                bnb_4bit_use_double_quant=model_args.double_quantization,
                bnb_4bit_quant_type=model_args.quantization_type,
            )

        is_mergeable = False
        config_kwargs["device_map"] = (
            {"": int(os.environ.get("LOCAL_RANK", "0"))} if is_trainable else "auto"
        )
        logger.info("Quantizing model to {} bit.".format(model_args.quantization_bit))

    # Load and prepare pre-trained models (without valuehead).
    model = AutoModelForCausalLM.from_pretrained(
        model_to_load,
        config=config,
        torch_dtype=model_args.compute_dtype,
        low_cpu_mem_usage=(not is_deepspeed_zero3_enabled()),
        **config_kwargs
    )

    # Disable custom generate method (for Qwen)
    if "GenerationMixin" not in str(model.generate.__func__):
        model.generate = MethodType(PreTrainedModel.generate, model)

    # Fix LM head (for ChatGLM2,ChatGLM3)
    if not hasattr(model, "lm_head") and hasattr(model, "transformer"):
        setattr(model, "lm_head", model.transformer.output_layer)

    # Register auto class to save the custom code files.
    if isinstance(config, PretrainedConfig) and "AutoConfig" in getattr(
        config, "auto_map", {}
    ):
        config.__class__.register_for_auto_class()
    if isinstance(model, PreTrainedModel) and "AutoModelForCausalLM" in getattr(
        config, "auto_map", {}
    ):
        model.__class__.register_for_auto_class()
    if isinstance(
        tokenizer, PreTrainedTokenizerBase
    ) and "AutoTokenizer" in tokenizer.init_kwargs.get("auto_map", {}):
        tokenizer.__class__.register_for_auto_class()

    # Initialize adapters
    model = (
        prepare_model_for_training(model, finetuning_args.finetuning_type)
        if is_trainable
        else model
    )
    model = init_adapter(model, model_args, finetuning_args, is_trainable, is_mergeable)

    # Prepare model with valuehead for RLHF
    if stage == "rm" or stage == "ppo":
        model: AutoModelForCausalLMWithValueHead = (
            AutoModelForCausalLMWithValueHead.from_pretrained(model)
        )
        reset_logging()
        if (
            stage == "rm" and model_args.checkpoint_dir is not None
        ):  # load valuehead weights to evaluate reward model
            logger.warning(
                "Only the last checkpoint containing valuehead will be loaded as the valuehead."
            )
            if load_valuehead_params(model, model_args.checkpoint_dir[-1]):
                model.v_head.load_state_dict(
                    {
                        "summary.weight": getattr(model, "reward_head_weight"),
                        "summary.bias": getattr(model, "reward_head_bias"),
                    }
                )

        if stage == "ppo":  # load reward model
            logger.info("Load reward model from {}".format(model_args.reward_model))
            model.pretrained_model.load_adapter(
                model_args.reward_model, "reward", is_trainable=False
            )
            assert load_valuehead_params(
                model, model_args.reward_model
            ), "Reward model is not correctly loaded."

    # Prepare model for inference
    if not is_trainable:
        model.requires_grad_(False)  # fix all model params
        infer_dtype = (
            torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        )  # detect cuda capability
        model = model.to(infer_dtype) if model_args.quantization_bit is None else model

    trainable_params, all_param = count_parameters(model)
    logger.info(
        "trainable params: {:d} || all params: {:d} || trainable%: {:.4f}".format(
            trainable_params, all_param, 100 * trainable_params / all_param
        )
    )

    return model, tokenizer


def dispatch_model(model: "PreTrainedModel") -> "PreTrainedModel":
    r"""
    Dispatches a pre-trained model to GPUs with balanced memory.
    Borrowed from: https://github.com/huggingface/transformers/blob/v4.31.0/src/transformers/modeling_utils.py#L2803
    """
    if getattr(model, "is_loaded_in_8bit", False) or getattr(
        model, "is_loaded_in_4bit", False
    ):  # do nothing
        return model

    if torch.cuda.device_count() > 1:
        from accelerate import dispatch_model
        from accelerate.utils import infer_auto_device_map, get_balanced_memory

        if model._no_split_modules is None:
            raise ValueError(
                "The model class needs to implement the `_no_split_modules` attribute."
            )

        kwargs = {
            "dtype": model.dtype,
            "no_split_module_classes": model._no_split_modules,
        }
        max_memory = get_balanced_memory(model, **kwargs)
        # Make sure tied weights are tied before creating the device map.
        model.tie_weights()
        device_map = infer_auto_device_map(model, max_memory=max_memory, **kwargs)
        return dispatch_model(model, device_map)
    else:
        return model.cuda()
