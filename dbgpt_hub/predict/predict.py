import logging
import os
import json
import sys

ROOT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

from tqdm import tqdm
from typing import List, Dict, Optional, Any
from concurrent.futures import FIRST_COMPLETED, FIRST_EXCEPTION, ThreadPoolExecutor, as_completed, wait

from dbgpt_hub.data_process.data_utils import extract_sql_prompt_dataset
from dbgpt_hub.llm_base.chat_model import ChatModel
from dbgpt_hub.llm_base.api_model import GeminiModel

import torch.distributed as dist
import torch.multiprocessing as mp


def prepare_dataset(predict_file_path: Optional[str] = None, ) -> List[Dict]:
    with open(predict_file_path, "r") as fp:
        data = json.load(fp)
    predict_data = [extract_sql_prompt_dataset(item) for item in data]
    return predict_data

from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def inference_worker(model, item, input_kwargs):  # Worker function for a single inference task
    n_candidates = 1
    cands = []
    for i in range(n_candidates):
        response, _ = model.chat(query=item["input"], history=[], **input_kwargs)
        response = model.verify_and_correct(item["input"], response, db_folder_path)
        cands.append(response)
    if n_candidates == 1:
        return response
    else:
        query = item["input"].split('Also consider the "Rules" and some useful "Hints" if provided.')[1].split('Now generate SQLite SQL query to answer the given "Question".')[0]
        return model.majority_voting(query, cands)

def parallelized_inference(model: ChatModel, predict_data: List[Dict], **input_kwargs):
    num_threads = 5
    res_dict = {}
    success_count, failure_count = 0, 0

    # Initialization outside the executor
    pbar = tqdm(total=len(predict_data), desc="Inference Progress", unit="item")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(inference_worker, model, item, input_kwargs): i for i, item in enumerate(predict_data)}

        # Use 'as_completed' for smoother progress bar updates
        for future in tqdm(as_completed(futures, timeout=1800), total=len(futures), desc="Inference Progress", unit="item"):
            index = futures[future]
            result = future.result()
            res_dict[index] = result

            if result != "":
                success_count += 1
            else:
                failure_count += 1

    print(f"Successful inferences: {success_count}, Failed inferences: {failure_count}")
    return [res_dict[i] for i in range(len(predict_data))]


def inference(model: ChatModel, predict_data: List[Dict], **input_kwargs):
    res = []
    for item in tqdm(predict_data, desc="Inference Progress", unit="item"):
        n_candidates = 1
        cands = []
        for i in range(n_candidates):
            response, _ = model.chat(query=item["input"],
                                     history=[],
                                     **input_kwargs)
            response = model.verify_and_correct(item["input"], response,
                                                db_folder_path)
            cands.append(response)
        if n_candidates == 1:
            res.append(response)
        else:
            query = item["input"].split(
                'Also consider the "Rules" and some useful "Hints" if provided.'
            )[1].split(
                'Now generate SQLite SQL query to answer the given "Question".')[0]
            res.append(model.majority_voting(query, cands))
    return res


def predict(model: ChatModel):
    args = model.data_args
    ## predict file can be give by param --predicted_input_filename ,output_file can be gived by param predicted_out_filename
    predict_data = prepare_dataset(args.predicted_input_filename)
    result = parallelized_inference(model, predict_data)

    with open(args.predicted_out_filename, "w") as f:
        for p in result:
            try:
                f.write(p.replace("\n", " ") + "\n")
            except:
                f.write("Invalid Output!\n")


if __name__ == "__main__":
    model = GeminiModel()  #ChatModel()
    model._infer_args()
    db_folder_path = '/root/DB-GPT-Hub/dbgpt_hub/data/bird/dev/dev_databases'
    #db_folder_path = '/root/DB-GPT-Hub/dbgpt_hub/data/spider/database'
    predict(model)
