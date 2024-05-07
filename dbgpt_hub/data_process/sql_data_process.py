import os
import json
from dbgpt_hub.data_process.data_utils import extract_most_similar_idx
import jsonlines
import sys
import re
import argparse
import pickle

from sentence_transformers import SentenceTransformer

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

from tqdm import tqdm

from dbgpt_hub.configs.config import (
    INSTRUCTION_ONE_SHOT_CODE_PROMPT,
    SQL_DATA_INFO,
    DATA_PATH,
    INPUT_PROMPT,
    INSTRUCTION_PROMPT,
    INSTRUCTION_ONE_SHOT_PROMPT,
    INSTRUCTION_ONE_SHOT_COL_TYPE_PROMPT,
)


class ProcessSqlData:

    def __init__(self,
                 train_file=None,
                 dev_file=None,
                 num_shot=0,
                 code_representation=False,
                 column_type=False,
                 column_ranking=False,
                 top_k=25) -> None:
        self.train_file = train_file
        self.dev_file = dev_file
        self.num_shot = num_shot
        self.code_representation = code_representation
        self.column_type = column_type
        self.column_ranking = column_ranking
        self.top_k = top_k

    def decode_json_file(
        self,
        data_file_list,
        table_file,
        db_folder_path,
        db_id_name,
        output_name,
        is_multiple_turn=False,
        table_col_emb_file=None,
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
            tables_names = item["table_names_original"]
            coloumns = item["column_names_original"][1:]
            column_types = list()
            if self.column_type:
                for i, ctype in enumerate(item["column_types"][1:]):
                    column_types.append(
                        [coloumns[i][0], coloumns[i][1] + ":" + ctype]
                    )
            primary_key = item["primary_keys"]
            foreign_keys = item["foreign_keys"]
            source = (item["db_id"] + " contains tables such as " +
                      ", ".join(tables_names) + ". ")

            for i, name in enumerate(tables_names):
                data = [col[1] for col in column_types if col[0] == i]
                source += ("Table " + name + " has columns such as " +
                           ", ".join(data) + ". ")
                # get primary key info
                for j in range(len(primary_key)):
                    if type(primary_key[j]) == int:
                        if coloumns[primary_key[j] - 1][0] == i:
                            source += (coloumns[primary_key[j] - 1][1] +
                                       " is the primary key." + "\n")
                    # combination primary key
                    elif type(primary_key[j]) == list:
                        combine_p = "The combination of ("
                        keys = []
                        for k in range(len(primary_key[j])):
                            if coloumns[primary_key[j][k] - 1][0] == i:
                                keys.append(coloumns[primary_key[j][k] - 1][1])
                        source += (combine_p + ", ".join(keys) +
                                   ") are the primary key." + "\n")
                    else:
                        print("not support type", type(primary_key[j]))
                        continue

            # get foreign key info
            for key in foreign_keys:
                source += ("The " + coloumns[key[0] - 1][1] + " of " +
                           tables_names[coloumns[key[0] - 1][0]] +
                           " is the foreign key of " +
                           coloumns[key[1] - 1][1] + " of " +
                           tables_names[coloumns[key[1] - 1][0]] + ".\n")

            db_dict[item["db_id"]] = source

        res = []
        base_instruction = INSTRUCTION_PROMPT
        if self.num_shot == 1:
            if self.code_representation:
                base_instruction = INSTRUCTION_ONE_SHOT_CODE_PROMPT
            elif self.column_type:
                base_instruction = INSTRUCTION_ONE_SHOT_COL_TYPE_PROMPT
            else:
                base_instruction = INSTRUCTION_ONE_SHOT_PROMPT

        if self.column_ranking:
            # TODO(yeounoh) we can use hosted embeddings API, but have to pay
            # May consider that option for the submission, since the test data
            # is hidden.
            assert table_col_emb_file is not None
            with open(table_col_emb_file, 'rb') as file:
                db_emb_dict = pickle.load(file)

        for data in tqdm(datas):
            if data[db_id_name] in db_dict.keys():
                if is_multiple_turn:  # 多轮
                    history = []
                    for interaction in data["interaction"]:
                        input = {
                            "db_id":
                            data[db_id_name],
                            "instruction":
                            base_instruction.format(db_dict[data[db_id_name]]),
                            "input":
                            INPUT_PROMPT.format(interaction["utterance"]),
                            "output":
                            interaction[output_name],
                            "history":
                            history,
                        }
                        res.append(input)
                        history.append((
                            INPUT_PROMPT.format(interaction["utterance"]),
                            interaction[output_name],
                        ))
                else:  # 单轮
                    if self.code_representation:
                        db_path = os.path.join(db_folder_path,
                                               data[db_id_name])
                        sql_file_path = next(
                            (file for file in os.listdir(db_path)
                             if file.endswith(".sql")),
                            None,
                        )
                        if sql_file_path is None:
                            continue  # 提前结束迭代
                        schema_file_path = os.path.join(db_path, sql_file_path)
                        with open(schema_file_path, "r") as file:
                            schema_content = file.read()
                        create_statements = re.findall(r"CREATE\s.*?;",
                                                       schema_content,
                                                       re.DOTALL)
                        input = {
                            "db_id":
                            data[db_id_name],
                            "instruction":
                            base_instruction.format(create_statements),
                            "input":
                            INPUT_PROMPT.format(data["question"]),
                            "output":
                            data[output_name],
                            "history": [],
                        }
                        res.append(input)
                    else:
                        if self.column_ranking:
                            model_id = "sentence-transformers/sentence-t5-base"
                            model = SentenceTransformer(model_id)
                            q_emb = model.encode([data["question"]])[0]
                            col_embs = [t[1] for t in db_emb_dict[data[db_id_name]]]
                            k_similar_idx = extract_most_similar_idx(q_emb, col_embs, top_k=self.top_k)
                            source = (item["db_id"] + " contains multiple tables with multiple columns, "
                                      + "listed as follows in \'table_name.column_name\' format: "
                                      + ", ".join([db_emb_dict[data[db_id_name]][idx][0] for idx in k_similar_idx])
                                      +" \n")
                            input_instruction = base_instruction.format(source)
                        else:
                            input_instruction = base_instruction.format(db_dict[data[db_id_name]])

                        input = {
                            "db_id":
                            data[db_id_name],
                            "instruction":
                            input_instruction,
                            "input":
                            INPUT_PROMPT.format(data["question"]),
                            "output":
                            data[output_name],
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
                    table_col_emb_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["train_tables_emb_file"],
                    ) if self.column_ranking else None,
                ))

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
                    table_col_emb_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["dev_tables_emb_file"],
                    ) if self.column_ranking else None,
                ))
        with open(self.train_file, "w", encoding="utf-8") as s:
            json.dump(train_data, s, indent=4, ensure_ascii=False)
        with open(self.dev_file, "w", encoding="utf-8") as s:
            json.dump(dev_data, s, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--code_representation", help="Enable code representation", default=False
    )
    parser.add_argument(
        "--column_type", help="Enable column type annotation", default=False
    )
    parser.add_argument("--column_ranking", help="Enable similarity-based column retrieval.")
    args = parser.parse_args()

    all_in_one_train_file = os.path.join(DATA_PATH, "example_text2sql_train.json")
    all_in_one_dev_file = os.path.join(DATA_PATH, "example_text2sql_dev.json")
    precess = ProcessSqlData(
        train_file=all_in_one_train_file,
        dev_file=all_in_one_dev_file,
        code_representation=args.code_representation,
        column_type=args.column_type,
        column_ranking=args.column_ranking,
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
        column_type=args.column_type,
        column_ranking=args.column_ranking,
    )
    one_shot_precess.create_sft_raw_data()
