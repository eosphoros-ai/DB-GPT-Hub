import os
import torch
from dbgpt_hub.llm_base.logging import get_logger
from transformers.trainer import  WEIGHTS_NAME
from transformers.modeling_utils import load_sharded_checkpoint
from transformers.trainer import WEIGHTS_NAME, WEIGHTS_INDEX_NAME
from typing import Dict



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

