import os
import json
import sys
from tqdm import tqdm

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)
from typing import List, Dict

from dbgpt_hub.data_process.data_utils import extract_sql_prompt_dataset
from dbgpt_hub.llm_base.vllm_chat_model import ChatModel
from dbgpt_hub.configs.config import (
    PREDICTED_DATA_PATH,
    OUT_DIR,
    PREDICTED_OUT_FILENAME,
)

def prepare_dataset() -> List[Dict]:
    with open(PREDICTED_DATA_PATH, "r") as fp:
        data = json.load(fp)
    predict_data = [extract_sql_prompt_dataset(item) for item in data]
    return predict_data


def inference(model: ChatModel, predict_data: List[Dict], **input_kwargs):
    res = []
    # test
    # for item in predict_data[:20]:
    for item in tqdm(predict_data):
        response = model.chat(query=item["input"], history=[], **input_kwargs)
        res.append(response)
    return res


def main():
    predict_data = prepare_dataset()
    model = ChatModel()
    result = inference(model, predict_data)

    predict_out_dir = os.path.join(OUT_DIR, "pred")
    if not os.path.exists(predict_out_dir):
        os.mkdir(predict_out_dir)

    predict_output_dir_name = os.path.join(
        predict_out_dir, model.data_args.predicted_out_filename
    )
    print(f"predict_output_dir_name \t{predict_output_dir_name}")

    with open(predict_output_dir_name, "w") as f:
        for p in result:
            f.write(p.replace("\n", " ") + "\n")


if __name__ == "__main__":
    main()
