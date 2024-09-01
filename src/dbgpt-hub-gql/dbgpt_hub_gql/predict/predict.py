import json
import os
import sys

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

from typing import Any, Dict, List, Optional

from dbgpt_hub_gql.data_process.data_utils import extract_sql_prompt_dataset
from dbgpt_hub_gql.llm_base.chat_model import ChatModel
from tqdm import tqdm


def prepare_dataset(
    predict_file_path: Optional[str] = None,
) -> List[Dict]:
    with open(predict_file_path, "r") as fp:
        data = json.load(fp)
    predict_data = [extract_sql_prompt_dataset(item) for item in data]
    return predict_data


def inference(model: ChatModel, predict_data: List[Dict], **input_kwargs):
    res = []
    # test
    # for item in predict_data[:20]:
    for item in tqdm(predict_data, desc="Inference Progress", unit="item"):
        print(f"item[input] \n{item['input']}")
        response, _ = model.chat(query=item["input"], history=[], **input_kwargs)
        res.append(response)
    return res


def predict(model: ChatModel):
    args = model.data_args
    ## predict file can be give by param --predicted_input_filename ,output_file can be gived by param predicted_out_filename
    predict_data = prepare_dataset(args.predicted_input_filename)
    result = inference(model, predict_data)

    with open(args.predicted_out_filename, "w") as f:
        for p in result:
            try:
                f.write(p.replace("\n", " ") + "\n")
            except:
                f.write("Invalid Output!\n")


if __name__ == "__main__":
    model = ChatModel()
    predict(model)
