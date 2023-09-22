import os
import json
# import sys
import sys
sys.path.append('/home/zw/explained/DB-GPT-Hub')
from typing import List, Dict

from dbgpt_hub.data_process.data_utils import extract_sql_prompt_dataset
from dbgpt_hub.llm_base.chat_model import ChatModel
from dbgpt_hub.configs.config import PREDICTED_DATA_PATH, OUT_DIR

def prepare_dataset() -> List[Dict]:
    with open(PREDICTED_DATA_PATH, "r") as fp:
        data = json.load(fp)
    predict_data = [extract_sql_prompt_dataset[item] for item in data] 
    return predict_data

def inference(model: ChatModel, predict_data: List[Dict], **input_kwargs):
    predict_out_dir = os.path.join(OUT_DIR, "pred")
    if not os.path.exists(predict_out_dir):
        os.mkdir(predict_out_dir)
    res = []
    for item in predict_data[0: 1]:
        response = model.chat(
            query=item["input"], 
            history=[],
            **input_kwargs)
        print(response)
        res.append(response)

def main():
    model = ChatModel()
    predict_data = prepare_dataset()
    inference(model, predict_data)

if __name__ == "__main__":
    main()
