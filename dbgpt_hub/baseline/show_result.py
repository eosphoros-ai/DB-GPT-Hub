import os
import sys
import json
from typing import Optional, Dict, Any
from prettytable.colortable import ColorTable, Theme

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)


MYTHEME = Theme(
    default_color="96",  # blue
    vertical_color="31",  # red
    horizontal_color="33",  # yellow
    junction_color="97",  # white
)
HEADER = [
    "dataset",
    "model",
    "method",
    "prompt",
    "etype",
    "easy",
    "medium",
    "hard",
    "extra",
    "all",
]

MYTHEME = Theme(
    default_color="96",  # blue
    vertical_color="31",  # red
    horizontal_color="33",  # yellow
    junction_color="97",  # white
)
HEADER = [
    "dataset",
    "model",
    "method",
    "prompt",
    "etype",
    "easy",
    "medium",
    "hard",
    "extra",
    "all",
]
baseline_file = "./dbgpt_hub/baseline/baseline.json"


with open(baseline_file, "r") as file:
    baseline_json = json.load(file)


def print_color_table_score(acc_data, dataset, model, method, prompt):
    model_data = [dataset, model, method, prompt]
    print_table_scores = ColorTable(theme=MYTHEME)
    print_table_scores.field_names = HEADER
    model_ex = get_model_score(acc_data, "ex", model_data)
    model_em = get_model_score(acc_data, "em", model_data)
    print_table_scores.add_rows([model_em, model_ex])
    print(print_table_scores, "\n")


def table_add_row(table_scores, acc_data, dataset, model, method, prompt):
    model_data = [dataset, model, method, prompt]
    model_ex = get_model_score(acc_data, "ex", model_data)
    model_em = get_model_score(acc_data, "em", model_data)
    table_scores.add_rows([model_em, model_ex])
    return table_scores


def add_scores_to_table(
    table, json_data, dataset, model=None, method=None, prompt=None
):
    if model is None:
        for model_key in json_data.keys():
            add_scores_to_table(
                table, json_data[model_key], dataset, model_key, method, prompt
            )
    elif method is None:
        for method_key in json_data.keys():
            add_scores_to_table(
                table, json_data[method_key], dataset, model, method_key, prompt
            )
    elif prompt is None:
        for prompt_key in json_data.keys():
            add_scores_to_table(
                table, json_data[prompt_key], dataset, model, method, prompt_key
            )
    else:
        acc_data = json_data["acc"]
        table_add_row(table, acc_data, dataset, model, method, prompt)


def show_score(dataset=None, model=None, method=None, prompt=None):
    """
    Displays the model baseline score information for a given dataset, model, method and prompt.

    Args:
        dataset (str, optional): The dataset to be used for scoring.
        model (str, optional): The model to be scored on the dataset.
        method (str, optional): The training method to us.
        prompt (str, optional): Additional information or context prompt.

    Returns:
        model baseline score.


    Examples
    >>> from dbgpt_hub.baseline import show_score
    >>> show_score(dataset="spider", model="llama2-7b-hf", method="base", prompt="alpaca")

    """
    if dataset is None:
        raise ValueError("dataset cannot be None!")
    elif model is None:
        json_data = baseline_json[dataset]
    elif method is None:
        json_data = baseline_json[dataset][model]
    elif prompt is None:
        json_data = baseline_json[dataset][model][method]
    else:
        json_data = baseline_json[dataset][model][method][prompt]
    table_scores = ColorTable(theme=MYTHEME)
    table_scores.field_names = HEADER
    add_scores_to_table(table_scores, json_data, dataset, model, method, prompt)
    print(table_scores)


def show_score_api(dataset=None, model=None, method=None, prompt=None):
    show_score(dataset, model, method, prompt)


def get_model_score(acc_data, etype, model_data):
    etype_score = [etype] + [acc_data[etype][key] for key in acc_data[etype].keys()]
    model_score = model_data + etype_score
    return model_score


def show_scores():
    """
    Displays baseline score information for all models.

    Args:
        None

    Returns:
        model baseline score.


    Examples
    >>> from dbgpt_hub.baseline import show_scores
    >>> show_scores()

    """
    datasets = baseline_json.keys()
    table_scores = ColorTable(theme=MYTHEME)
    table_scores.field_names = HEADER
    for dataset in datasets:
        models = baseline_json[dataset].keys()
        for model in models:
            methods = baseline_json[dataset][model].keys()
            for method in methods:
                prompts = baseline_json[dataset][model][method].keys()
                for prompt in prompts:
                    acc_data = baseline_json[dataset][model][method][prompt]["acc"]
                    table_scores = table_add_row(
                        table_scores, acc_data, dataset, model, method, prompt
                    )
    print(table_scores, "\n")


def show_scores_api():
    show_scores()


if __name__ == "__main__":
    show_scores()
    show_score(dataset="spider", model="llama2-7b-hf", method="base", prompt="alpaca")
