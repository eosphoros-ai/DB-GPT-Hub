import json
import os
import sys

import jsonlines

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

from typing import Any, Dict, List, Optional

from dbgpt_hub_gql.configs.config import INPUT_PROMPT, INSTRUCTION_PROMPT
from tqdm import tqdm


class SqlDataProcessor(object):
    def __init__(
        self, data_folder: Optional[str] = None, data_info: Optional[List[Dict]] = None
    ) -> Any:
        if data_folder is None:
            self.data_folder = os.path.join(ROOT_PATH, "dbgpt_hub_gql/data")
            print(
                "The user do not provide exact data folder, we take 'dbgpt_hub_gql/data' as the default folder"
            )
        else:
            self.data_folder = data_folder

        if data_info is None:
            print("Please provide at least one dataset information!")
            raise
        else:
            self.data_info = data_info

    def _decode_json_file(
        self,
        data_file_list: Optional[List] = [],
        table_file: Optional[str] = "",
        db_id_name: Optional[str] = "",
        is_multiple_turn=False,
    ) -> List:
        if table_file.endswith(".jsonl"):
            tables = jsonlines.open(table_file)
            datas = []
            for data_file in data_file_list:
                datas.extend(jsonlines.open(data_file))

        elif table_file.endswith(".json"):
            tables = json.load(open(table_file))
            datas = []
            for data_file in data_file_list:
                datas.extend(json.load(open(data_file)))
        else:
            print("Unsupported file types, please provide .json or .jsonl files!")
            raise

        # 先将db_id 的table和coloumns处理好
        db_dict = {}
        for item in tables:
            tables = item["table_names_original"]
            coloumns = item["column_names_original"][1:]
            primary_key = item["primary_keys"]
            foreign_keys = item["foreign_keys"]
            source = (
                item["db_id"] + " contains tables such as " + ", ".join(tables) + ". "
            )
            for i, name in enumerate(tables):
                data = [coloumn[1] for coloumn in coloumns if coloumn[0] == i]
                source += (
                    "Table " + name + " has columns such as " + ", ".join(data) + ". "
                )

                # get primary key info
                for j in range(len(primary_key)):
                    if coloumns[primary_key[j] - 1][0] == i:
                        source += (
                            coloumns[primary_key[j] - 1][1]
                            + " is the primary key."
                            + "\n"
                        )

            # get foreign key info
            for key in foreign_keys:
                source += (
                    "The "
                    + coloumns[key[0] - 1][1]
                    + " of "
                    + tables[coloumns[key[0] - 1][0]]
                    + " is the foreign key of "
                    + coloumns[key[1] - 1][1]
                    + " of "
                    + tables[coloumns[key[1] - 1][0]]
                    + ".\n"
                )

            db_dict[item["db_id"]] = source

        res = []
        for data in tqdm(datas):
            if data[db_id_name] in db_dict.keys():
                # Manage multiple turn dataset
                if is_multiple_turn:
                    history = []
                    for interaction in data["interaction"]:
                        input = {
                            "db_id": data[db_id_name],
                            "instruction": INSTRUCTION_PROMPT.format(
                                db_dict[data[db_id_name]]
                            ),
                            "input": INPUT_PROMPT.format(interaction["utterance"]),
                            "output": interaction["query"],
                            "history": history,
                        }
                        res.append(input)
                        history.append(
                            (
                                INPUT_PROMPT.format(interaction["utterance"]),
                                interaction["query"],
                            )
                        )
                else:
                    # Manage single turn dataset
                    input = {
                        "db_id": data[db_id_name],
                        "instruction": INSTRUCTION_PROMPT.format(
                            db_dict[data[db_id_name]]
                        ),
                        "input": INPUT_PROMPT.format(data["question"]),
                        "output": data["query"],
                        "history": [],
                    }
                    res.append(input)
        return res

    def _create_sft_raw_data(
        self,
    ) -> None:
        for data_info in self.data_info:
            train_data = []
            dev_data = []

            train_data_file_list = [
                os.path.join(self.data_folder, data_info["data_source"], file)
                for file in data_info["train_file"]
            ]
            train_data.extend(
                self._decode_json_file(
                    data_file_list=train_data_file_list,
                    table_file=os.path.join(
                        self.data_folder,
                        data_info["data_source"],
                        data_info["tables_file"],
                    ),
                    db_id_name=data_info["db_id_name"],
                    is_multiple_turn=data_info["is_multiple_turn"],
                )
            )

            dev_data_file_list = [
                os.path.join(self.data_folder, data_info["data_source"], file)
                for file in data_info["dev_file"]
            ]
            dev_data.extend(
                self._decode_json_file(
                    data_file_list=dev_data_file_list,
                    table_file=os.path.join(
                        self.data_folder,
                        data_info["data_source"],
                        data_info["tables_file"],
                    ),
                    db_id_name=data_info["db_id_name"],
                    is_multiple_turn=data_info["is_multiple_turn"],
                )
            )

            train_output_path = os.path.join(
                self.data_folder, data_info["train_output"]
            )
            dev_output_path = os.path.join(self.data_folder, data_info["dev_output"])
            with open(train_output_path, "w", encoding="utf-8") as s:
                json.dump(train_data, s, indent=4, ensure_ascii=False)
            with open(dev_output_path, "w", encoding="utf-8") as s:
                json.dump(dev_data, s, indent=4, ensure_ascii=False)

    def process_sft_data(
        self,
    ) -> None:
        self._create_sft_raw_data()


def preprocess_sft_data(
    data_folder: Optional[str] = "", data_info: Optional[List[Dict]] = None
) -> None:
    processor = SqlDataProcessor(data_folder=data_folder, data_info=data_info)
    processor.process_sft_data()


if __name__ == "__main__":
    data_folder = os.path.join(ROOT_PATH, "dbgpt_hub_gql/data")
    data_info = [
        {
            "data_source": "spider",
            "train_file": ["train_spider.json", "train_others.json"],
            "dev_file": ["dev.json"],
            "tables_file": "tables.json",
            "db_id_name": "db_id",
            "is_multiple_turn": False,
            "train_output": "example_train.json",
            "dev_output": "example_dev.json",
        }
    ]
    preprocess_sft_data(data_folder=data_folder, data_info=data_info)
