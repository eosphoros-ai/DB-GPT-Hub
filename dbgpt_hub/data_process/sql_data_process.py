import os
import json
import jsonlines

from tqdm import tqdm

from dbgpt_hub.configs.config import SQL_DATA_INFO, DATA_PATH, INPUT_PROMPT, INSTRUCTION_PROMPT

class ProcessSqlData:
    def __init__(self) -> None:
        pass

    # def decode_json_file(self, 
    #                      data_file: AnyStr, 
    #                      table_file: AnyStr, 
    #                      is_multiple_turn=False) -> None: 

    #     # load data form sql_data_info
        
    #     if data_file.endswith(".jsonl"):
    #         datas, tables = jsonlines.open(data_file), jsonlines.open(table_file)
    #     elif data_file.endswith(".json"):
    #         datas, tables = json.load(open(data_file)), json.load(open(table_file))
            
    #     """ get table info of table name and columns names, examples: 
    #         {
    #             'perpetrator': {
    #                 'tables': ['perpetrator', 'people'], 
    #                 'tables_and_columns': {
    #                     'perpetrator': ['Perpetrator_ID', 'People_ID', 'Date', 'Year', 'Location', 'Country', 'Killed', 'Injured'], 
    #                     'people': ['People_ID', 'Name', 'Height', 'Weight', 'Home Town']
    #                     },
    #                 'tables_and_primary_key': {
    #                     'perpetrator': 'Perpetrator_ID' , 
    #                     'people': 'People_ID',
    #                     },
    #             }
    #         }

    #     """

    #     db_dict = {}
    #     for item in tables[0:1]:

    #         db_dict[item["db_id"]] = {}
    #         db_dict[item["db_id"]]["tables"] = item["table_names_original"]
    #         db_dict[item["db_id"]]["tables_and_columns"] = {}
    #         db_dict[item["db_id"]]["tables_and_primary_key"] = {}
    #         db_dict[item["db_id"]]["tables_and_foreign_key"] = {}
    #         print(db_dict)

    #         coloumns = item["column_names_original"][1:]
    #         primary_key = item["primary_keys"]
    #         foreign_keys = item["foreign_keys"]
            
    #         for i, table_name in enumerate(item["table_names_original"]):
    #             coloumns_name = [col[1] for col in coloumns if col[0] == i]
    #             db_dict[item["db_id"]]["tables_and_columns"][table_name] = coloumns_name

    #             # get promary key info
    #             for j in range(len(primary_key)):
    #                 if coloumns[primary_key[j]-1][0] == i:
    #                     db_dict[item["db_id"]]["tables_and_primary_key"][table_name] = coloumns[primary_key[j]-1][1]
                
    #         for key in foreign_keys:
    #             source += "The " + coloumns[key[0]-1][1] + " of " + tables[coloumns[key[0]-1][0]] + " is the foreign key of " + coloumns[key[1]-1][1] + " of " + tables[coloumns[key[1]-1][0]] + ".\n"

    #     print(db_dict)

        # one-turn conversation
        # if not is_multiple_turn:

    def decode_json_file(self, data_file, table_file, out_file):
        """
            TO DO:
                1.将相关prompt放入config中
                2.将不同数据来源的字段信息放入config中
                3.支持多轮对话数据集
        """

        if data_file.endswith(".jsonl"):
            datas, tables = jsonlines.open(data_file), jsonlines.open(table_file)
        elif data_file.endswith(".json"):
            datas, tables = json.load(open(data_file)), json.load(open(table_file))
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
            source = item["db_id"] + " contains tables such as " + ", ".join(tables) + ". "
            for i, name in enumerate(tables):
                data = [coloumn[1] for coloumn in coloumns if coloumn[0] == i]
                source += "Table " + name +  " has columns such as " + ", ".join(data) + ". " 

                # get primary key info
                for j in range(len(primary_key)):
                    if coloumns[primary_key[j]-1][0] == i:
                        source += coloumns[primary_key[j]-1][1] + " is the primary key." + "\n"
            
            # get foreign key info 
            for key in foreign_keys:
                source += "The " + coloumns[key[0]-1][1] + " of " + tables[coloumns[key[0]-1][0]] + " is the foreign key of " + coloumns[key[1]-1][1] + " of " + tables[coloumns[key[1]-1][0]] + ".\n"

            db_dict[item["db_id"]] = source.format()
    
        # 单论对话
        res = []
        for data in tqdm(datas[0: 100]):
            if data["db_id"] in db_dict.keys():
                input = {
                    "db_id": data["db_id"],
                    "instruction": INSTRUCTION_PROMPT.format(db_dict[data["db_id"]]),
                    "input": INPUT_PROMPT.format(data["question"]),
                    "output": data["query"],
                    "history": []
                }
                res.append(input)
            
        with open(out_file, "w", encoding="utf-8") as s:
            json.dump(res, s, indent=4, ensure_ascii=False)


    def create_sft_raw_data(self):
        for data_info in SQL_DATA_INFO:
            self.decode_json_file(
                data_file=os.path.join(DATA_PATH, data_info["data_source"], data_info["train_file"]),
                table_file=os.path.join(DATA_PATH, data_info["data_source"], data_info["tables_file"]),
                out_file=os.path.join(DATA_PATH, "example_text2sql_train.json")
            )
            self.decode_json_file(
                data_file=os.path.join(DATA_PATH, data_info["data_source"], data_info["dev_file"]),
                table_file=os.path.join(DATA_PATH, data_info["data_source"], data_info["tables_file"]),
                out_file=os.path.join(DATA_PATH, "example_text2sql_dev.json")
            )


if __name__ == "__main__":
    precess = ProcessSqlData()
    precess.create_sft_raw_data()
    
       