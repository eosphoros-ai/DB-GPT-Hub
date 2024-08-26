import os
from typing import Any, Dict, Optional

from dbgpt_hub_gql.predict import predict


def start_predict(
    args: Optional[Dict[str, Any]] = None, cuda_visible_devices: Optional[str] = "0"
):
    # Setting CUDA Device
    os.environ["CUDA_VISIBLE_DEVICES"] = cuda_visible_devices

    # Default Arguments
    if args is None:
        args = {
            "model_name_or_path": "codellama/CodeLlama-13b-Instruct-hf",
            "template": "llama2",
            "finetuning_type": "lora",
            "checkpoint_dir": "dbgpt_hub_gql/output/adapter/CodeLlama-13b-gql-lora",
            "predict_file_path": "dbgpt_hub_gql/data/tugraph-db-example/dev.json",
            "predict_out_dir": "dbgpt_hub_gql/output/",
            "predicted_out_filename": "pred_gql.txt",
        }
    else:
        args = args

    # Execute prediction
    predict.predict(args)


if __name__ == "__main__":
    start_predict()
