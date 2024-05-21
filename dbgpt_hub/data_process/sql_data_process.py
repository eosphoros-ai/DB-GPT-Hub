import os
import json
from dbgpt_hub.data_process.data_utils import extract_most_similar_idx
import jsonlines
import sys
import re
import argparse
import pickle

from sentence_transformers import SentenceTransformer

ROOT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_PATH)

from tqdm import tqdm

from dbgpt_hub.configs.config import (SQL_DATA_INFO, DATA_PATH, INPUT_PROMPT,
                                      INSTRUCTION_PROMPT,
                                      INSTRUCTION_ONE_SHOT_PROMPT,
                                      INSTRUCTION_THREE_SHOT_PROMPT)


class ProcessSqlData:

    def __init__(self,
                 train_file=None,
                 dev_file=None,
                 num_shot=0,
                 code_representation=False,
                 table_ranking=False,
                 column_ranking=False,
                 primary_keys=False,
                 tips=False,
                 top_k=25) -> None:
        self.train_file = train_file
        self.dev_file = dev_file
        self.num_shot = num_shot
        self.code_representation = code_representation
        self.table_ranking = table_ranking
        self.column_ranking = column_ranking
        self.primary_keys = primary_keys
        self.tips = tips
        self.top_k = top_k

    def decode_json_file(
        self,
        data_file_list,
        table_file,
        db_folder_path,
        db_id_name,
        output_name,
        is_multiple_turn=False,
        tab_emb_file=None,
        col_emb_file=None,
        has_evidence=False,
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
        db_tab_dict = {}
        db_foreign_key_dict = {}
        for item in tables:
            tables_names = item["table_names_original"]
            coloumns = item["column_names_original"][1:]
            primary_key = item["primary_keys"]
            foreign_keys = item["foreign_keys"]
            source = ("The database " + item["db_id"] +
                      " contains tables such as " + ", ".join(tables_names) +
                      ". ")

            tab_dict = {}
            for i, name in enumerate(tables_names):
                cols = coloumns
                data = [col[1] for col in cols if col[0] == i]
                tab_cols = ("Table " + name + " has columns such as " +
                            ", ".join(data) + ". ")
                tab_dict[name] = [tab_cols]
                source += tab_cols

                # get primary key info
                primary_key_str = ""
                for j in range(len(primary_key)):
                    if type(primary_key[j]) == int:
                        if coloumns[primary_key[j] - 1][0] == i:
                            primary_key_str += (
                                coloumns[primary_key[j] - 1][1] +
                                " is the primary key." + "\n")
                    # combination primary key
                    elif type(primary_key[j]) == list:
                        combine_p = "The combination of ("
                        keys = []
                        for k in range(len(primary_key[j])):
                            if coloumns[primary_key[j][k] - 1][0] == i:
                                keys.append(coloumns[primary_key[j][k] - 1][1])
                        if not keys:
                            continue
                        primary_key_str += (combine_p + ", ".join(keys) +
                                            ") are the primary key." + "\n")
                    else:
                        print("not support type", type(primary_key[j]))
                        continue
                source += primary_key_str
                tab_dict[name].append(primary_key_str)

            # get foreign key info
            foreign_keys_str = ""
            for key in foreign_keys:
                foreign_keys_str += ("The " + coloumns[key[0] - 1][1] +
                                     " of " +
                                     tables_names[coloumns[key[0] - 1][0]] +
                                     " is the foreign key of " +
                                     coloumns[key[1] - 1][1] + " of " +
                                     tables_names[coloumns[key[1] - 1][0]] +
                                     ". ")
            db_foreign_key_dict[item["db_id"]] = foreign_keys_str + "\n"
            source += db_foreign_key_dict[item["db_id"]]

            db_dict[item["db_id"]] = source
            db_tab_dict[item["db_id"]] = tab_dict

        res = []
        base_instruction = INSTRUCTION_PROMPT
        if self.num_shot == 1:
            base_instruction = INSTRUCTION_ONE_SHOT_PROMPT
        elif self.num_shot == 3:
            base_instruction = INSTRUCTION_THREE_SHOT_PROMPT
        if self.column_ranking or self.table_ranking:
            assert (
                self.column_ranking
                != self.table_ranking), "Ranking by table or column, not both."
        if self.column_ranking:
            # TODO(yeounoh) we can use hosted embeddings API, but have to pay
            # May consider that option for the submission, since the test data
            # is hidden.
            assert col_emb_file is not None
            with open(col_emb_file, 'rb') as file:
                db_emb_dict = pickle.load(file)
            model_id = "sentence-transformers/sentence-t5-base"
            model = SentenceTransformer(model_id)
        elif self.table_ranking:
            assert tab_emb_file is not None
            with open(tab_emb_file, 'rb') as file:
                db_emb_dict = pickle.load(file)
            model_id = "sentence-transformers/sentence-t5-base"
            model = SentenceTransformer(model_id)

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
                            # top-k most relevant columns and foreign keys.
                            q_emb = model.encode(data["question"])
                            col_embs = [
                                t[1] for t in db_emb_dict[data[db_id_name]]
                            ]
                            k_similar_idx = extract_most_similar_idx(
                                q_emb, col_embs, top_k=self.top_k)

                            table_columns = [
                                db_emb_dict[data[db_id_name]][idx][0]
                                for idx in k_similar_idx
                            ]
                            table_to_column_dict = {}
                            for p in table_columns:
                                t_name = p.split(" ")[1]
                                c_name = p.split("\"")[1]
                                if t_name in table_to_column_dict:
                                    table_to_column_dict[t_name].append(c_name)
                                else:
                                    table_to_column_dict[t_name] = [c_name]
                            instruction = ""
                            for t_name, col_list in table_to_column_dict.items(
                            ):
                                instruction += f"Table {t_name} has columns such as "
                                instruction += ", ".join(col_list) + ". "
                            instruction += (
                                " \n" + db_foreign_key_dict[data[db_id_name]]
                                if data[db_id_name] in db_foreign_key_dict else
                                "")
                        elif self.table_ranking:
                            # top-k most relevant columns and foreign keys.
                            q_emb = model.encode(data["question"])
                            tab_embs = [
                                t[1] for t in db_emb_dict[data[db_id_name]]
                            ]
                            k_similar_idx = extract_most_similar_idx(
                                q_emb, tab_embs, top_k=self.top_k)

                            tables = [
                                db_emb_dict[data[db_id_name]][idx][0]
                                for idx in k_similar_idx
                            ]
                            instruction = ""
                            for t_name in tables:
                                instruction += db_tab_dict[
                                    data[db_id_name]][t_name][0]
                                if self.primary_keys:
                                    instruction += db_tab_dict[
                                        data[db_id_name]][t_name][1]
                            instruction += (
                                " \n" + db_foreign_key_dict[data[db_id_name]]
                                if data[db_id_name] in db_foreign_key_dict else
                                "")
                        else:
                            # all tables and columns with primary and foreign keys.
                            instruction = db_dict[data[db_id_name]]

                        if has_evidence and data["evidence"]:
                            instruction += (
                                "Here is some useful hints to generate the output: "
                                + data["evidence"] + ".\n")
                        if self.tips:
                            instruction += (
                                "Here are additional instructions: "
                                "1) -- is used to mark comment; "
                                "2) use nested SQL query when needed; "
                                "3) use the `date` function when comparing dates; "
                                "4) when dealing with ratios, cast the calculated values as REAL.\n"
                            )
                        input_instruction = base_instruction.format(
                            instruction)

                        input = {
                            "db_id": data[db_id_name],
                            "instruction": input_instruction,
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
                    tab_emb_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["train_tab_emb_file"],
                    ) if self.table_ranking else None,
                    col_emb_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["train_col_emb_file"],
                    ) if self.column_ranking else None,
                    has_evidence=data_info["data_source"] == "bird",
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
                    tab_emb_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["dev_tab_emb_file"],
                    ) if self.table_ranking else None,
                    col_emb_file=os.path.join(
                        DATA_PATH,
                        data_info["data_source"],
                        data_info["dev_col_emb_file"],
                    ) if self.column_ranking else None,
                    has_evidence=data_info["data_source"] == "bird",
                ))
        with open(self.train_file, "w", encoding="utf-8") as s:
            json.dump(train_data, s, indent=4, ensure_ascii=False)
        with open(self.dev_file, "w", encoding="utf-8") as s:
            json.dump(dev_data, s, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--code_representation",
                        help="Enable code representation",
                        default=False)
    parser.add_argument("--table_ranking",
                        help='Enable similarity-based table retrieval.')
    parser.add_argument("--column_ranking",
                        help="Enable similarity-based column retrieval.")
    parser.add_argument("--top_k",
                        help="Number of tables or columns to retrieve.",
                        default=15)
    parser.add_argument("--primary_keys",
                        help="Include table primary keys.",
                        default=False)
    parser.add_argument("--num_shot", default=0)
    parser.add_argument("--tips", default=False)
    args = parser.parse_args()

    all_in_one_train_file = os.path.join(DATA_PATH,
                                         "example_text2sql_train.json")
    all_in_one_dev_file = os.path.join(DATA_PATH, "example_text2sql_dev.json")
    precess = ProcessSqlData(train_file=all_in_one_train_file,
                             dev_file=all_in_one_dev_file,
                             code_representation=args.code_representation,
                             table_ranking=args.table_ranking,
                             column_ranking=args.column_ranking,
                             primary_keys=args.primary_keys,
                             tips=args.tips,
                             top_k=int(args.top_k) if args.top_k else 25)
    precess.create_sft_raw_data()

    # one-shot
    one_shot_all_in_one_train_file = os.path.join(
        DATA_PATH, "example_text2sql_train_three_shot.json")
    one_shot_all_in_one_dev_file = os.path.join(
        DATA_PATH, "example_text2sql_dev_three_shot.json")
    one_shot_precess = ProcessSqlData(
        train_file=one_shot_all_in_one_train_file,
        dev_file=one_shot_all_in_one_dev_file,
        num_shot=3,
        code_representation=args.code_representation,
        table_ranking=args.table_ranking,
        column_ranking=args.column_ranking,
        primary_keys=args.primary_keys,
        tips=args.tips,
        top_k=int(args.top_k) if args.top_k else 25)
    one_shot_precess.create_sft_raw_data()
