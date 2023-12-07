from typing import Optional, Dict, Any

from dbgpt_hub.baseline import show_result


def show_scores():
    show_result.show_scores_api()


def show_score(dataset=None, model=None, method=None, prompt=None):
    show_result.show_score_api(dataset, model, method, prompt)


if __name__ == "__main__":
    show_score(dataset="spider", model="llama2-7b-hf", method="base", prompt="alpaca")
