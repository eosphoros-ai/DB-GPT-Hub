import os
import json
import jsonlines
import sys
import re
import argparse

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

from tqdm import tqdm

from dbgpt_hub.configs.config import (
    SQL_DATA_INFO,
    DATA_PATH,
    INPUT_PROMPT,
    INSTRUCTION_PROMPT,
    INSTRUCTION_ONE_SHOT_PROMPT,
)


class ProcessSqlData:
    def __init__(
        self, train_file=None, dev_file=None, num_shot=0, code_representation=False
    ) -> None:
        self.train_file = train_file
        self.dev_file = dev_file
        self.num_shot = num_shot
        self.code_representation = code_representation

    def decode_json_file(
        self,
        data_file_list,
        table_file,
        db_folder_path,
        db_id_name,
        output_name,
        is_multiple_turn=False,
    ):
        """
        TO DO:
            1.将相关prompt放入config中
            2.将不同数据来源的字段信息放入config中
        """

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
            print("Unsupported file types")
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
                    if type(primary_key[j]) == int:
                        if coloumns[primary_key[j] - 1][0] == i:
                            source += (
                                coloumns[primary_key[j] - 1][1]
                                + " is the primary key."
                                + "\n"
                            )
                    # combination primary key
                    elif type(primary_key[j]) == list:
                        combine_p = "The combination of ("
                        keys = []
                        for k in range(len(primary_key[j])):
                            if coloumns[primary_key[j][k] - 1][0] == i:
                                keys.append(coloumns[primary_key[j][k] - 1][1])
                        source += (
                            combine_p
                            + ", ".join(keys)
                            + ") are the primary key."
                            + "\n"
                        )
                    else:
                        print("not support type", type(primary_key[j]))
                        continue

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
        base_instruction = INSTRUCTION_PROMPT
        if self.num_shot == 1:
            base_instruction = INSTRUCTION_ONE_SHOT_PROMPT

        for data in tqdm(datas):
            if data[db_id_name] in db_dict.keys():
                if is_multiple_turn:  # 多轮
                    history = []
                    for interaction in data["interaction"]:
                        input = {
                            "db_id": data[db_id_name],
                            "instruction": base_instruction.format(
                                db_dict[data[db_id_name]]
                            ),
                            "input": INPUT_PROMPT.format(interaction["utterance"]),
                            "output": interaction[output_name],
                            "history": history,
                        }
                        res.append(input)
                        history.append(
                            (
                                INPUT_PROMPT.format(interaction["utterance"]),
                                interaction[output_name],
                            )
                        )
                else:  # 单轮
                    if self.code_representation:
                        db_path = os.path.join(db_folder_path, data[db_id_name])
                        sql_file_path = next(
                            (
                                file
                                for file in os.listdir(db_path)
                                if file.endswith(".sql")
                            ),
                            None,
                        )
                        if sql_file_path is None:
                            continue  # 提前结束迭代
                        schema_file_path = os.path.join(db_path, sql_file_path)
                        with open(schema_file_path, "r") as file:
                            schema_content = file.read()
                        create_statements = re.findall(
                            r"CREATE\s.*?;", schema_content, re.DOTALL|re.IGNORECASE
                        )
                        input = {
                            "db_id": data[db_id_name],
                            "instruction": INSTRUCTION_PROMPT.format(create_statements),
                            "input": INPUT_PROMPT.format(data["question"]),
                            "output": data[output_name],
                            "history": [],
                        }
                        res.append(input)
                    else:
                        input = {
                            "db_id": data[db_id_name],
                            "instruction": base_instruction.format(
                                db_dict[data[db_id_name]]
                            ),
                            "input": INPUT_PROMPT.format(data["question"]),
                            "output": data[output_name],
                            "history": [],
                        }
                        res.append(input)
        return res

    def create_sft_raw_data(self):
        train_data = []
        dev_data = []
        for data_info in SQL_DATA_INFO:
            train_data_file_list = [
                os.path.join(DATA_PATH, data_info["data_source"], file)
                for file in data_info["train_file"]
            ]
            train_data.extend(
                self.decode_json_file(
                    data_file_list=train_data_file_list,
                    table_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["train_tables_file"],
                    ),
                    db_folder_path=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        "database",
                    ),
                    db_id_name=data_info["db_id_name"],
                    output_name=data_info["output_name"],
                    is_multiple_turn=data_info["is_multiple_turn"],
                )
            )

            dev_data_file_list = [
                os.path.join(DATA_PATH, data_info["data_source"], file)
                for file in data_info["dev_file"]
            ]
            dev_data.extend(
                self.decode_json_file(
                    data_file_list=dev_data_file_list,
                    table_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["dev_tables_file"],
                    ),
                    db_folder_path=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        "database",
                    ),
                    db_id_name=data_info["db_id_name"],
                    output_name=data_info["output_name"],
                    is_multiple_turn=data_info["is_multiple_turn"],
                )
            )
        with open(self.train_file, "w", encoding="utf-8") as s:
            json.dump(train_data, s, indent=4, ensure_ascii=False)
        with open(self.dev_file, "w", encoding="utf-8") as s:
            json.dump(dev_data, s, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--code_representation", help="Enable code representation", default=False
    )
    args = parser.parse_args()

    all_in_one_train_file = os.path.join(DATA_PATH, "example_text2sql_train.json")
    all_in_one_dev_file = os.path.join(DATA_PATH, "example_text2sql_dev.json")
    precess = ProcessSqlData(
        train_file=all_in_one_train_file,
        dev_file=all_in_one_dev_file,
        code_representation=args.code_representation,
    )
    precess.create_sft_raw_data()

    # one-shot
    one_shot_all_in_one_train_file = os.path.join(
        DATA_PATH, "example_text2sql_train_one_shot.json"
    )
    one_shot_all_in_one_dev_file = os.path.join(
        DATA_PATH, "example_text2sql_dev_one_shot.json"
    )
    one_shot_precess = ProcessSqlData(
        train_file=one_shot_all_in_one_train_file,
        dev_file=one_shot_all_in_one_dev_file,
        num_shot=1,
        code_representation=args.code_representation,
    )
    one_shot_precess.create_sft_raw_data()
