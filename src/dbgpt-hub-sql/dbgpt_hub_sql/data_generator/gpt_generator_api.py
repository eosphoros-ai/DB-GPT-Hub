import os
import sys
from typing import Any, Dict, Optional

from .gpt_generator import GPTGenerator
from .utils import COT_PROMPT

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)


def generate_dataset_with_gpt(args: Optional[Dict[str, Any]] = None):
    # Default Arguments
    if args is None:
        args = {
            "model": "gpt-3.5-turbo-16k",
            "prompt": COT_PROMPT,
            "num_text2sql_pair_each_db": 1,
            "table_file_path": os.path.join(
                ROOT_PATH, "dbgpt_hub_sql/data/spider/tables.json"
            ),
            "output_path": os.path.join(
                ROOT_PATH, "dbgpt_hub_sql/data/spider/synthetic_data_with_gpt.json"
            ),
        }
    else:
        args = args

    # Run GPT Generator
    gpt_generator = GPTGenerator(
        model=args["model"],
        prompt=args["prompt"],
        num_text2sql_pair_each_db=args["num_text2sql_pair_each_db"],
        table_file_path=args["table_file_path"],
        output_path=args["output_path"],
    )
    gpt_generator.generate_synthetic_dataset()


if __name__ == "__main__":
    generate_dataset_with_gpt()
