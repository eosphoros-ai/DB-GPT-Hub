import argparse
import os
import warnings
import importlib
import torch
from packaging import version
from os.path import join
from typing import Optional, Tuple,Dict
import bitsandbytes as bnb
from peft import LoraConfig, PeftModel, get_peft_model, prepare_model_for_kbit_training
from transformers import PreTrainedModel, PreTrainedTokenizer
from peft.tuners.lora import LoraLayer
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    LlamaTokenizer,
)


import os
import math
import torch
from types import MethodType
from typing import TYPE_CHECKING, Literal, Optional, Tuple,List

from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    PretrainedConfig,
    PreTrainedModel,
    PreTrainedTokenizerBase,
)
from transformers.utils import check_min_version
from transformers.utils.versions import require_version
from transformers.deepspeed import is_deepspeed_zero3_enabled
from trl import AutoModelForCausalLMWithValueHead

from dbgpt_hub.llm_base.loggings import reset_logging, get_logger
# from llmtuner.extras.misc import count_parameters, prepare_model_for_training
from dbgpt_hub.configs.model_args import FinetuningArguments
from dbgpt_hub.llm_base.adapter import init_adapter
from dbgpt_hub.configs.config import LAYERNORM_NAMES,VALUE_HEAD_FILE_NAME

if TYPE_CHECKING:
    from transformers import PreTrainedTokenizer
    from dbgpt_hub.configs.model_args import ModelArguments


logger = get_logger(__name__)


check_min_version("4.29.1")
require_version("datasets>=2.12.0", "To fix: pip install datasets>=2.12.0")
require_version("accelerate>=0.21.0", "To fix: pip install accelerate>=0.21.0")
require_version("peft>=0.4.0", "To fix: pip install peft>=0.4.0")
require_version("trl>=0.5.0", "To fix: pip install trl>=0.5.0")


# from dbgpt_hub.utils.model_utils import (
#     smart_tokenizer_and_embedding_resize,
#     find_all_linear_names,
# )



def is_ipex_available():
    def get_major_and_minor_from_version(full_version):
        return (
            str(version.parse(full_version).major)
            + "."
            + str(version.parse(full_version).minor)
        )

    _torch_version = importlib.metadata.version("torch")
    if importlib.util.find_spec("intel_extension_for_pytorch") is None:
        return False
    _ipex_version = "N/A"
    try:
        _ipex_version = importlib.metadata.version("intel_extension_for_pytorch")
    except importlib.metadata.PackageNotFoundError:
        return False
    torch_major_and_minor = get_major_and_minor_from_version(_torch_version)
    ipex_major_and_minor = get_major_and_minor_from_version(_ipex_version)
    if torch_major_and_minor != ipex_major_and_minor:
        warnings.warn(
            f"Intel Extension for PyTorch {ipex_major_and_minor} needs to work with PyTorch {ipex_major_and_minor}.*,"
            f" but PyTorch {_torch_version} is found. Please switch to the matching version and run again."
        )
        return False
    return True


def smart_tokenizer_and_embedding_resize(
    special_tokens_dict: Dict[str, str],
    tokenizer: PreTrainedTokenizer,
    model: PreTrainedModel,
) -> None:
    """Resize tokenizer and embedding to accommodate new special tokens.
    改变tokenizer和embedding的尺寸。
    一般需要将tokenizer和embedding的尺寸设置为64的倍数，方便GPU加速。

    Args:
        special_tokens_dict (Dict[str, str]): A dictionary of special tokens to be added to the tokenizer.
        tokenizer (PreTrainedTokenizer): The tokenizer object to be resized.
        model (PreTrainedModel): The model object whose token embeddings are to be resized.

    Returns:
        None

    Note: This function resizes the tokenizer to accommodate additional special tokens and the
    embedding matrix of the model to match the new size of the tokenizer. If any new special tokens
    have been added, the function computes the average embedding values of the existing embeddings
    and sets those values for the new special token embeddings. This is done separately for the input
    embeddings and output embeddings of the model.
    """

    num_new_tokens = tokenizer.add_special_tokens(special_tokens_dict)
    model.resize_token_embeddings(len(tokenizer))

    if num_new_tokens > 0:
        input_embeddings_data = model.get_input_embeddings().weight.data
        output_embeddings_data = model.get_output_embeddings().weight.data

        # Compute average embeddings of existing tokens
        input_embeddings_avg = input_embeddings_data[:-num_new_tokens].mean(
            dim=0, keepdim=True
        )
        output_embeddings_avg = output_embeddings_data[:-num_new_tokens].mean(
            dim=0, keepdim=True
        )

        input_embeddings_data[-num_new_tokens:] = input_embeddings_avg
        output_embeddings_data[-num_new_tokens:] = output_embeddings_avg


def find_all_linear_names(
    args: argparse.Namespace, model: torch.nn.Module
) -> List[str]:
    """
    Returns a list of names of all linear layers present in the given model.
    Args:
        args (argparse.Namespace): A namespace containing arguments of the script.
        model (torch.nn.Module): The PyTorch model to extract linear layer names from.

    Returns:
        List[str]: A list of names of all linear layers present in the given model.

    Raises:
        TypeError: If `args` is not an instance of `argparse.Namespace`, or if `model` is not an instance \
            of `torch.nn.Module`.
        ValueError: If `args.bits` is not 4 or 8.

    Example Usage:
        >>> import argparse
        >>> parser = argparse.ArgumentParser()
        >>> parser.add_argument('--bits', type=int)
        >>> args = parser.parse_args(['--bits', '4'])
        >>> model = torch.nn.Sequential(torch.nn.Linear(10, 5), torch.nn.Linear(5, 1))
        >>> find_all_linear_names(args, model)
        ['0', '1']
    """
    # Determine the correct linear layer class based on the value of `args.bits`
    if args.bits == 4:
        cls = bnb.nn.Linear4bit
    elif args.bits == 8:
        cls = bnb.nn.Linear8bitLt
    else:
        torch.nn.Linear

    lora_module_names = set()
    for name, module in model.named_modules():
        # Check if the current module is an instance of the linear layer class
        if isinstance(module, cls):
            # If yes, split the name of the module into its component parts and add the first or last part to the set
            names = name.split(".")
            lora_module_names.add(names[0] if len(names) == 1 else names[-1])

    # Remove 'lm_head' from the set if present (needed for 16-bit)
    if "lm_head" in lora_module_names:
        lora_module_names.remove("lm_head")

    # Convert the set into a list and return it
    return list(lora_module_names)




## TODO 待将此处的所有调用都替换掉，过去在train_qlora和predict_qlora中用了，待替换，然后删除此处历史代码。
def get_accelerate_model(
    args: argparse.Namespace = None, checkpoint_dir: Optional[str] = None
):
    if torch.cuda.is_available():
        n_gpus = torch.cuda.device_count()
    if is_ipex_available() and torch.xpu.is_available():
        n_gpus = torch.xpu.device_count()

    max_memory = f"{args.max_memory_MB}MB"
    max_memory = {i: max_memory for i in range(n_gpus)}
    device_map = "auto"

    # if we are in a distributed setting, we need to set the device map and max memory per device
    if os.environ.get("LOCAL_RANK") is not None:
        local_rank = int(os.environ.get("LOCAL_RANK", "0"))
        device_map = {"": local_rank}
        max_memory = {"": max_memory[local_rank]}

    if args.full_finetune:
        assert args.bits in [16, 32]

    print(f"loading base model {args.model_name_or_path}...")
    compute_dtype = (
        torch.float16 if args.fp16 else (torch.bfloat16 if args.bf16 else torch.float32)
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        cache_dir=args.cache_dir,
        load_in_4bit=args.bits == 4,
        load_in_8bit=args.bits == 8,
        device_map=device_map,
        max_memory=max_memory,
        quantization_config=BitsAndBytesConfig(
            load_in_4bit=args.bits == 4,
            load_in_8bit=args.bits == 8,
            llm_int8_threshold=6.0,
            llm_int8_has_fp16_weight=False,
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=args.double_quant,
            bnb_4bit_quant_type=args.quant_type,
        ),
        torch_dtype=(
            torch.float32
            if args.fp16
            else (torch.bfloat16 if args.bf16 else torch.float32)
        ),
        trust_remote_code=args.trust_remote_code,
        use_auth_token=args.use_auth_token,
    )
    if compute_dtype == torch.float16 and args.bits == 4:
        if torch.cuda.is_bf16_supported():
            print("=" * 80)
            print(
                "Your GPU supports bfloat16, you can accelerate training with the argument --bf16"
            )
            print("=" * 80)

    if compute_dtype == torch.float16 and (
        is_ipex_available() and torch.xpu.is_available()
    ):
        compute_dtype = torch.bfloat16
        print("Intel XPU does not support float16 yet, so switching to bfloat16")

    setattr(model, "model_parallel", True)
    setattr(model, "is_parallelizable", True)

    model.config.torch_dtype = (
        torch.float32 if args.fp16 else (torch.bfloat16 if args.bf16 else torch.float32)
    )

    # Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name_or_path,
        cache_dir=args.cache_dir,
        padding_side="right",
        use_fast=False,  # Fast tokenizer giving issues.
        tokenizer_type="llama"
        if (
            "llama" in args.model_name_or_path or "CodeLlama" in args.model_name_or_path
        )
        else None,  # Needed for HF name change
        trust_remote_code=args.trust_remote_code,
        use_auth_token=args.use_auth_token,
    )
    if tokenizer._pad_token is None:
        smart_tokenizer_and_embedding_resize(
            special_tokens_dict=dict(pad_token="[PAD]"),
            tokenizer=tokenizer,
            model=model,
        )
    if "llama" in args.model_name_or_path or isinstance(tokenizer, LlamaTokenizer):
        # LLaMA tokenizer may not have correct special tokens set.
        # Check and add them if missing to prevent them from being parsed into different tokens.
        # Note that these are present in the vocabulary.
        # Note also that `model.config.pad_token_id` is 0 which corresponds to `<unk>` token.
        print("Adding special tokens.")
        tokenizer.add_special_tokens(
            {
                "eos_token": tokenizer.convert_ids_to_tokens(model.config.eos_token_id),
                "bos_token": tokenizer.convert_ids_to_tokens(model.config.bos_token_id),
                "unk_token": tokenizer.convert_ids_to_tokens(
                    model.config.pad_token_id
                    if model.config.pad_token_id != -1
                    else tokenizer.pad_token_id
                ),
            }
        )

    if not args.full_finetune:
        model = prepare_model_for_kbit_training(
            model, use_gradient_checkpointing=args.gradient_checkpointing
        )

    if not args.full_finetune:
        if checkpoint_dir is not None:
            print("Loading adapters from checkpoint.")
            model = PeftModel.from_pretrained(
                model, join(checkpoint_dir, "adapter_model"), is_trainable=True
            )
        else:
            print(f"adding LoRA modules...")
            modules = find_all_linear_names(args, model)
            config = LoraConfig(
                r=args.lora_r,
                lora_alpha=args.lora_alpha,
                target_modules=modules,
                lora_dropout=args.lora_dropout,
                bias="none",
                task_type="CAUSAL_LM",
            )
            model = get_peft_model(model, config)

    for name, module in model.named_modules():
        if isinstance(module, LoraLayer):
            if args.bf16:
                module = module.to(torch.bfloat16)
        if "norm" in name:
            module = module.to(torch.float32)
        if "lm_head" in name or "embed_tokens" in name:
            if hasattr(module, "weight"):
                if args.bf16 and module.weight.dtype == torch.float32:
                    module = module.to(torch.bfloat16)
    return model, tokenizer


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

    # Fix LM head (for ChatGLM2)
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

def dispatch_model(model: "PreTrainedModel") -> "PreTrainedModel":
    r"""
    Dispatches a pre-trained model to GPUs with balanced memory.
    Borrowed from: https://github.com/huggingface/transformers/blob/v4.31.0/src/transformers/modeling_utils.py#L2803
    """
    if getattr(model, "is_loaded_in_8bit", False) or getattr(model, "is_loaded_in_4bit", False): # do nothing
        return model

    if torch.cuda.device_count() > 1:
        from accelerate import dispatch_model
        from accelerate.utils import infer_auto_device_map, get_balanced_memory

        if model._no_split_modules is None:
            raise ValueError("The model class needs to implement the `_no_split_modules` attribute.")

        kwargs = {"dtype": model.dtype, "no_split_module_classes": model._no_split_modules}
        max_memory = get_balanced_memory(model, **kwargs)
        # Make sure tied weights are tied before creating the device map.
        model.tie_weights()
        device_map = infer_auto_device_map(model, max_memory=max_memory, **kwargs)
        return dispatch_model(model, device_map)
    else:
        return model.cuda()