import os
from typing import Any, Dict, Optional

from dbgpt_hub_gql.train import sft_train


def start_sft(
    args: Optional[Dict[str, Any]] = None, cuda_visible_devices: Optional[str] = "0"
):
    # Setting CUDA Device
    os.environ["CUDA_VISIBLE_DEVICES"] = cuda_visible_devices

    # Default Arguments
    if args is None:
        args = {
            "model_name_or_path": "codellama/CodeLlama-13b-Instruct-hf",
            "do_train": True,
            "dataset": "tugraph_db_train",
            "max_source_length": 2048,
            "max_target_length": 512,
            "finetuning_type": "lora",
            "lora_target": "q_proj,v_proj",
            "template": "llama2",
            "lora_rank": 64,
            "lora_alpha": 32,
            "output_dir": "dbgpt_hub_gql/output/adapter/CodeLlama-13b-gql-lora",
            "overwrite_cache": True,
            "overwrite_output_dir": True,
            "per_device_train_batch_size": 1,
            "gradient_accumulation_steps": 16,
            "lr_scheduler_type": "cosine_with_restarts",
            "logging_steps": 50,
            "save_steps": 2000,
            "learning_rate": 2e-4,
            "num_train_epochs": 8,
            "plot_loss": True,
            "bf16": True,
        }
    else:
        args = args

    # Run SFT
    sft_train.train(args)


if __name__ == "__main__":
    start_sft()
