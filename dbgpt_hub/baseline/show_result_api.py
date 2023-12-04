from typing import Optional, Dict, Any

from dbgpt_hub.baseline import show_result


def show_all():
    show_result.show_all_api()

def show_model(
    args: Optional[Dict[str, Any]] = None
):
     # Arguments for show result
    if args is None:
        args = {
           "dataset":"spider",
           "model":"llama2-7b-hf",
           "sft":"lora",
           "prompt":"alpaca",
        }
    else:
        args = args

    show_result.show_model_api(args)



if __name__ == "__main__":
    show_all()

    show_args = {
    "dataset" : "spider",
    "model" : "llama2-7b-hf",
    "method" : "lora",
    "prompt" : "alpaca"
    }
    show_model(show_args)
