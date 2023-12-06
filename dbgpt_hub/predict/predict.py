import os
import json
import sys

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

from tqdm import tqdm
from typing import List, Dict, Optional, Any

from dbgpt_hub.data_process.data_utils import extract_sql_prompt_dataset
from dbgpt_hub.llm_base.chat_model import ChatModel


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
        response, _ = model.chat(query=item["input"], history=[], **input_kwargs)
        res.append(response)
    return res


def predict(args: Optional[Dict[str, Any]] = None):
    predict_file_path = ""
    if args is None:
        predict_file_path = os.path.join(
            ROOT_PATH, "dbgpt_hub/data/eval_data/dev_sql.json"
        )
        predict_out_dir = os.path.join(
            os.path.join(ROOT_PATH, "dbgpt_hub/output/"), "pred"
        )
        if not os.path.exists(predict_out_dir):
            os.mkdir(predict_out_dir)
        predict_output_filename = os.path.join(predict_out_dir, "pred_sql.sql")
        print(f"predict_output_filename \t{predict_output_filename}")
    else:
        predict_file_path = os.path.join(ROOT_PATH, args["predict_file_path"])
        predict_out_dir = os.path.join(
            os.path.join(ROOT_PATH, args["predict_out_dir"]), "pred"
        )
        if not os.path.exists(predict_out_dir):
            os.mkdir(predict_out_dir)
        predict_output_filename = os.path.join(predict_out_dir, args["pred_sql.sql"])
        print(f"predict_output_filename \t{predict_output_filename}")

    predict_data = prepare_dataset(predict_file_path=predict_file_path)
    model = ChatModel()
    result = inference(model, predict_data)

    with open(predict_output_filename, "w") as f:
        for p in result:
            try:
                f.write(p.replace("\n", " ") + "\n")
            except:
                f.write("Invalid Output!\n")


if __name__ == "__main__":
    predict()
