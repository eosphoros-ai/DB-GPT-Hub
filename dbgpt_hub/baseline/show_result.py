import os
import sys
import json
from typing import Optional, Dict, Any
from prettytable import PrettyTable


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

baseline_file = "./dbgpt_hub/baseline/baseline.json"
# read json
with open(baseline_file, 'r') as file:
    baseline_json = json.load(file)

def print_models_info(dataset, model, method, prompt):
    print_table_models = PrettyTable()
    models_header = ['dataset', 'model', 'method', 'prompt']
    models_info = [dataset, model, method, prompt]
    print_table_models.field_names = models_header
    print_table_models.add_rows([models_info])
    return print_table_models


def print_scores_info(acc_data):
    print_table_scores = PrettyTable()
    scores_header = ['etype', 'easy', 'medium', 'hard', 'extra', 'all']
    print_table_scores.field_names = scores_header
    eytpe = "ex"
    ex_score = [acc_data[eytpe][key] for key in acc_data[eytpe].keys()]
    ex_score.insert(0, eytpe)
    eytpe = "em"
    em_score = [acc_data[eytpe][key] for key in acc_data[eytpe].keys()]
    em_score.insert(0, eytpe)
    print_table_scores.add_rows(
        [
            ex_score,
            em_score 
        ]
    )
    return print_table_scores

def show_model(
    dataset,
    model,
    method,
    prompt
    ):

    # 1.get res
    acc_data = baseline_json[dataset][model][method][prompt]['acc']

    # 2.print models info
    print_table_models = print_models_info(dataset, model, method, prompt)
    print(print_table_models)

    # 3.print scores info
    print_table_scores = print_scores_info(acc_data)
    print(print_table_scores)

def show_model_api(args: Optional[Dict[str, Any]] = None):
    dataset = args["dataset"]
    model = args["model"]
    method = args["method"]
    prompt = args["prompt"]

    show_model(
        dataset, 
        model, 
        method, 
        prompt
    )

def show_all():
    datasets = baseline_json.keys()
    for dataset in datasets:
        models = baseline_json[dataset].keys()
        for model in models:
            methods = baseline_json[dataset][model].keys()
            for method in methods:
                prompts = baseline_json[dataset][model][method].keys()
                for prompt in prompts:
                    # 1.get scores info
                    acc_data = baseline_json[dataset][model][method][prompt]['acc']

                    # 2.print models info
                    print_table_models = print_models_info(dataset, model, method, prompt)
                    print(print_table_models)

                    # 3.print scores info
                    print_table_scores = print_scores_info(acc_data)
                    print(print_table_scores)



            
def show_all_api():
   show_all()



# def update():
#     # todo : 更新baseline.json
#     #  


if __name__ == "__main__":
    # args
    show_args = {
        "dataset" : "spider",
        "model" : "llama2-7b-hf",
        "method" : "lora",
        "prompt" : "alpaca",
    }
    show_model(show_args)
    
    show_all()
    
