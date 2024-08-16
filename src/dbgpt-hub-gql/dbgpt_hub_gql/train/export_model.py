import os
import sys

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)
from dbgpt_hub_gql.llm_base.model_trainer import export_model


def main():
    export_model()


if __name__ == "__main__":
    main()
