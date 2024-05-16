import os

### path config
ROOT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ROOT_PATH = "/root/autodl-tmp"
# MODELS_PARENT_PATH = "/home/model_files/codellama/"
# DEFAULT_FT_MODEL_NAME = "CodeLlama-7b-Instruct-hf"
MODELS_PARENT_PATH = "/home/model/"
DEFAULT_FT_MODEL_NAME = "Baichuan2-13B-Chat"
MODEL_PATH = os.path.join(MODELS_PARENT_PATH, DEFAULT_FT_MODEL_NAME)

# MODEL_PATH = os.path.join(ROOT_PATH, "model")
ADAPTER_PATH = os.path.join(ROOT_PATH, "dbgpt_hub/output/adapter")
MERGED_MODELS = os.path.join(ROOT_PATH, "dbgpt_hub/output/merged_models")

# DATA_PATH = "/root/autodl-tmp/data/spider/pre_processed_data"
# OUT_DIR= "/root/autodl-tmp/codellama"

DATA_PATH = os.path.join(ROOT_PATH, "dbgpt_hub/data")
PREDICTED_DATA_PATH = os.path.join(ROOT_PATH,
                                   "dbgpt_hub/data/eval_data/dev_sql.json")
PREDICTED_OUT_FILENAME = "pred_sql.sql"
# OUT_DIR = os.path.join(DATA_PATH, "out_pred")
OUT_DIR = os.path.join(ROOT_PATH, "dbgpt_hub/output/")

## model constants
IGNORE_INDEX = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "<s>"
DEFAULT_UNK_TOKEN = "<unk>"

LOG_FILE_NAME = "trainer_log.jsonl"

# head_state_dict,model save name
VALUE_HEAD_FILE_NAME = "value_head.bin"

# output ,finetuning_args save_to_json name
FINETUNING_ARGS_NAME = "finetuning_args.json"

#  when prepare_model_for_training ,layer_norm_names
LAYERNORM_NAMES = ["norm", "ln_f", "ln_attn", "ln_mlp"]
EXT2TYPE = {"csv": "csv", "json": "json", "jsonl": "json", "txt": "text"}

# text2sql dataset information for processing sql data
# TODO: BIRD \ WiKiSQL \ ...
SQL_DATA_INFO = [
    # {
    #     "data_source": "spider",
    #     "train_file": ["train_spider.json", "train_others.json"],
    #     "dev_file": ["dev.json"],
    #     "train_tables_file": "tables.json",
    #     "dev_tables_file": "tables.json",
    #     "db_id_name": "db_id",
    #     "output_name": "query",
    #     "is_multiple_turn": False,
    #     "train_tab_emb_file": "train_tab_emb.pickle",
    # "dev_tab_emb_file": "dev_tab_emb.pickle",
    # "train_col_emb_file": "train_col_emb.pickle",
    # "dev_col_emb_file": "dev_col_emb.pickle",
    # }
    {
        "data_source": "bird",
        "train_file": ["train/train.json"],
        "dev_file": ["dev/dev.json"],
        "train_tables_file": "train/train_tables.json",
        "dev_tables_file": "dev/dev_tables.json",
        "db_id_name": "db_id",
        "output_name": "SQL",
        "is_multiple_turn": False,
        "train_tab_emb_file": "train_tab_emb.pickle",
        "dev_tab_emb_file": "dev_tab_emb.pickle",
        "train_col_emb_file": "train_col_emb.pickle",
        "dev_col_emb_file": "dev_col_emb.pickle",
    }
    # ,
    # {
    #     "data_source": "chase",
    #     "train_file": ["Chase/chase_train.json"],
    #     "dev_file": ["Chase/chase_dev.json"],
    #     "tables_file": "Chase/chase_tables.json",
    #     "db_id_name": "database_id",
    #     "is_multiple_turn": True,
    # }
    # ,
    # {
    #     "data_source": "cosql_dataset",
    #     "train_file": ["sql_state_tracking/cosql_train.json"],
    #     "dev_file": ["sql_state_tracking/cosql_dev.json"],
    #     "tables_file": "tables.json",
    #     "db_id_name": "database_id",
    #     "is_multiple_turn": True,
    # }
    # ,
    # {
    # {
    #     "data_source": "sparc",
    #     "train_file": ["train.json"],
    #     "train_tables_file": "tables.json",
    #     "dev_tables_file": "tables.json",
    #     "dev_file": ["dev.json"],
    #     "db_id_name": "database_id",
    #     "is_multiple_turn": True,
    #     "output_name": "query",
    # }
]

#### SPIDER ####
INSTRUCTION_PROMPT = """\
I want you to act as a SQL terminal in front of an example database, \
you need only to return the sql command to me.Below is an instruction that describes a task, \
Write a response that appropriately completes the request. \n"
### New Instruction:\n{}\n"""
INPUT_PROMPT = "###Input:\n{}\n\n###Response:"

INSTRUCTION_ONE_SHOT_PROMPT = """\
I want you to act as a SQL terminal in front of an example database. \
You need only to return the sql command to me. \
First, I will show you few examples of an instruction followed by the correct SQL response. \
Then, I will give you a new instruction, and you should write the SQL response that appropriately completes the request. \
\n### Example1 Instruction:
The database contains tables such as employee, salary, and position. \
Table employee has columns such as employee_id, name, age, and position_id. employee_id is the primary key. \
Table salary has columns such as employee_id, amount, and date. employee_id is the primary key. \
Table position has columns such as position_id, title, and department. position_id is the primary key. \
The employee_id of salary is the foreign key of employee_id of employee. \
The position_id of employee is the foreign key of position_id of position.\
\n### Example1 Input:\nList the names and ages of employees in the 'Engineering' department. \
\n### Example1 Response:\nSELECT employee.name, employee.age FROM employee JOIN position ON employee.position_id = position.position_id WHERE position.department = 'Engineering' \
\n\n### New Instruction:\n{}\n"""

INSTRUCTION_THREE_SHOT_PROMPT = """\
I want you to act as a SQL terminal in front of an example database. \
You need only to return the sql command to me. \
First, I will show you few examples of an instruction followed by the correct SQL response. \
Then, I will give you a new instruction, and you should write the SQL response that appropriately completes the request. \
\n### Example1 Instruction: \
retail_complains contains tables such as state, callcenterlogs, client, district, events, reviews. \
Table state has columns such as StateCode, State, Region. StateCode is the primary key.\nTable callcenterlogs \
has columns such as Date received, Complaint ID, rand client, phonefinal, vru+line, call_id, priority, type, outcome, server, ser_start, ser_exit, ser_time. \
Complaint ID is the primary key.\nTable client has columns such as client_id, sex, day, month, year, age, social, first, middle, last, phone, email, address_1, address_2, city, state, zipcode, district_id. client_id is the primary key. \
\nTable district has columns such as district_id, city, state_abbrev, division. district_id is the primary key.\nTable events has columns such as Date received, Product, Sub-product, Issue, Sub-issue, Consumer complaint narrative, \
Tags, Consumer consent provided?, Submitted via, Date sent to company, Company response to consumer, Timely response?, Consumer disputed?, Complaint ID, Client_ID. The combination of (Complaint ID, Client_ID) are the primary key. \
\nTable reviews has columns such as Date, Stars, Reviews, Product, district_id. Date is the primary key.\nThe rand client of callcenterlogs is the foreign key of client_id of client. The district_id of client is the foreign key of \
district_id of district. The state_abbrev of district is the foreign key of StateCode of state. The Client_ID of events is the foreign key of client_id of client. The Complaint ID of events is the foreign key of Complaint ID of callcenterlogs. \
The district_id of reviews is the foreign key of district_id of district. \nHere is some useful hints to generate the output: percentage = MULTIPLY(DIVIDE(SUM(\"Consumer disputed?\" = 'Yes' AND city = 'Houston'), COUNT(client_id)), 1.0); Houston refers to city = 'Houston';. \
\n### Example1 Input:\nWhat percentage of consumers from Houston disputed complaints? \
\n### Example1 Response:\nSELECT CAST(SUM(CASE WHEN T2.`Consumer disputed?` = 'Yes' AND T1.city = 'Houston' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.client_id) FROM client AS T1 INNER JOIN events AS T2 ON T1.client_id = T2.Client_ID \
\n\n### Example2 Instruction: \
movie_3 contains tables such as film_text, actor, address, category, city, country, customer, \
film, film_actor, film_category, inventory, language, payment, rental, staff, store. Table film_text \
has columns such as film_id, title, description. film_id is the primary key.\nTable actor has columns \
such as actor_id, first_name, last_name, last_update. actor_id is the primary key.\nTable address has \
columns such as address_id, address, address2, district, city_id, postal_code, phone, last_update. address_id \
is the primary key.\nTable category has columns such as category_id, name, last_update. category_id is the primary key. \
\nTable city has columns such as city_id, city, country_id, last_update. city_id is the primary key.\nTable country \
has columns such as country_id, country, last_update. country_id is the primary key.\nTable customer has columns such as \
customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update. customer_id is the primary \
key.\nTable film has columns such as film_id, title, description, release_year, language_id, original_language_id, rental_duration, \
rental_rate, length, replacement_cost, rating, special_features, last_update. film_id is the primary key.\nTable film_actor has columns \
such as actor_id, film_id, last_update. The combination of (actor_id, film_id) are the primary key.\nTable film_category has columns such as \
film_id, category_id, last_update. The combination of (film_id, category_id) are the primary key.\nTable inventory has columns such as inventory_id, \
film_id, store_id, last_update. inventory_id is the primary key.\nTable language has columns such as language_id, name, last_update. language_id is \
the primary key.\nTable payment has columns such as payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update. payment_id is the \
primary key.\nTable rental has columns such as rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update. rental_id is the \
primary key.\nTable staff has columns such as staff_id, first_name, last_name, address_id, picture, email, store_id, active, username, password, \
last_update. staff_id is the primary key.\nTable store has columns such as store_id, manager_staff_id, address_id, last_update. store_id is the primary \
key.\n\nHere is some useful hints to generate the output: over 4.99 refers to amount > 4.99. \
\n### Example2 Input:\nAmong the payments made by Mary Smith, how many of them are over 4.99? \
\n### Example2 Response:\nSELECT COUNT(T1.amount) FROM payment AS T1 INNER JOIN customer AS T2 ON T1.customer_id = T2.customer_id WHERE T2.first_name = 'MARY' AND T2.last_name = 'SMITH' AND T1.amount > 4.99 \
\n\n### Example3 Instruction: \
movie_3 contains tables such as film_text, actor, address, category, city, country, customer, film, film_actor, \
film_category, inventory, language, payment, rental, staff, store. Table film_text has columns such as film_id, \
title, description. film_id is the primary key.\nTable actor has columns such as actor_id, first_name, last_name, \
last_update. actor_id is the primary key.\nTable address has columns such as address_id, address, address2, district, \
city_id, postal_code, phone, last_update. address_id is the primary key.\nTable category has columns such as category_id, \
name, last_update. category_id is the primary key.\nTable city has columns such as city_id, city, country_id, last_update. \
city_id is the primary key.\nTable country has columns such as country_id, country, last_update. country_id is the primary key.\n \
Table customer has columns such as customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update. \
customer_id is the primary key.\nTable film has columns such as film_id, title, description, release_year, language_id, original_language_id, \
rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update. film_id is the primary key.\nTable film_actor has columns such as actor_id, \
film_id, last_update. The combination of (actor_id, film_id) are the primary key.\nTable film_category has columns such as film_id, category_id, last_update. \
The combination of (film_id, category_id) are the primary key.\nTable inventory has columns such as inventory_id, film_id, store_id, last_update. \
inventory_id is the primary key.\nTable language has columns such as language_id, name, last_update. language_id is the primary key.\nTable payment \
has columns such as payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update. payment_id is the primary key.\nTable rental has columns such \
as rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update. rental_id is the primary key.\nTable staff has columns such as staff_id, \
first_name, last_name, address_id, picture, email, store_id, active, username, password, last_update. staff_id is the primary key.\nTable store has columns such as store_id, \
manager_staff_id, address_id, last_update. store_id is the primary key.\n\nHere is some useful hints to generate the output: Italy refers to country = 'Italy'; \
average amount = divide(sum(amount), count(customer_id)) where country = 'Italy'. \
\n### Example3 Input:\nWhat is the average amount of money spent by a customer in Italy on a single film rental? \
\n### Example3 Response:\SELECT AVG(T5.amount) FROM address AS T1 INNER JOIN city AS T2 ON T1.city_id = T2.city_id INNER JOIN country AS T3 ON T2.country_id = T3.country_id INNER JOIN customer AS T4 ON T1.address_id = T4.address_id INNER JOIN payment AS T5 ON T4.customer_id = T5.customer_id WHERE T3.country = 'Italy' \
\n\n### New Instruction:\n{}\n"""

# EXAMPLES =[EXAMPLE1, EXAMPLE1]

# EXAMPLE1 = "\n### Example1 Input:\nList the names and ages of employees in the 'Engineering' department.\n\
# \n### Example1 Response:\nSELECT employee.name, employee.age FROM employee JOIN position ON employee.position_id = position.position_id WHERE position.department = 'Engineering';\
# \n###New Instruction:\n{}\n"

### test--------------------

# METHODS = ["full", "freeze", "lora"]

# STAGES = ["SFT", "Reward Modeling", "PPO", "DPO", "Pre-Training"]

# DATASET_STAGE_MAP = {
#     "SFT": "sft",
#     "Pre-Training": "pt",
#     "Reward Modeling": "rm",
#     "PPO": "sft",
#     "DPO": "rm",
# }

# SUPPORTED_MODELS = {
#     "LLaMA-7B": "huggyllama/llama-7b",
#     "LLaMA-13B": "huggyllama/llama-13b",
#     "LLaMA-30B": "huggyllama/llama-30b",
#     "LLaMA-65B": "huggyllama/llama-65b",
#     "LLaMA2-7B": "meta-llama/Llama-2-7b-hf",
#     "LLaMA2-13B": "meta-llama/Llama-2-13b-hf",
#     "LLaMA2-70B": "meta-llama/Llama-2-70b-hf",
#     "LLaMA2-7B-Chat": "meta-llama/Llama-2-7b-chat-hf",
#     "LLaMA2-13B-Chat": "meta-llama/Llama-2-13b-chat-hf",
#     "LLaMA2-70B-Chat": "meta-llama/Llama-2-70b-chat-hf",
#     "ChineseLLaMA2-7B": "ziqingyang/chinese-llama-2-7b",
#     "ChineseLLaMA2-13B": "ziqingyang/chinese-llama-2-13b",
#     "ChineseLLaMA2-7B-Chat": "ziqingyang/chinese-alpaca-2-7b",
#     "ChineseLLaMA2-13B-Chat": "ziqingyang/chinese-alpaca-2-13b",
#     "BLOOM-560M": "bigscience/bloom-560m",
#     "BLOOM-3B": "bigscience/bloom-3b",
#     "BLOOM-7B1": "bigscience/bloom-7b1",
#     "BLOOMZ-560M": "bigscience/bloomz-560m",
#     "BLOOMZ-3B": "bigscience/bloomz-3b",
#     "BLOOMZ-7B1-mt": "bigscience/bloomz-7b1-mt",
#     "Falcon-7B": "tiiuae/falcon-7b",
#     "Falcon-7B-Chat": "tiiuae/falcon-7b-instruct",
#     "Falcon-40B": "tiiuae/falcon-40b",
#     "Falcon-40B-Chat": "tiiuae/falcon-40b-instruct",
#     "Baichuan-7B": "baichuan-inc/Baichuan-7B",
#     "Baichuan-13B": "baichuan-inc/Baichuan-13B-Base",
#     "Baichuan-13B-Chat": "baichuan-inc/Baichuan-13B-Chat",
#     "Baichuan2-7B": "baichuan-inc/Baichuan2-7B-Base",
#     "Baichuan2-13B": "baichuan-inc/Baichuan2-13B-Base",
#     "Baichuan2-7B-Chat": "baichuan-inc/Baichuan2-7B-Chat",
#     "Baichuan2-13B-Chat": "baichuan-inc/Baichuan2-13B-Chat",
#     "InternLM-7B": "internlm/internlm-7b",
#     "InternLM-7B-Chat": "internlm/internlm-chat-7b",
#     "Qwen-7B": "Qwen/Qwen-7B",
#     "Qwen-7B-Chat": "Qwen/Qwen-7B-Chat",
#     "XVERSE-13B": "xverse/XVERSE-13B",
#     "ChatGLM2-6B-Chat": "THUDM/chatglm2-6b",
#     "ChatGLM3-6B-Base": "THUDM/chatglm3-6b-base",
#     "ChatGLM3-6B-Chat": "THUDM/chatglm3-6b"
# }

# DEFAULT_MODULE = {
#     "LLaMA": "q_proj,v_proj",
#     "LLaMA2": "q_proj,v_proj",
#     "ChineseLLaMA2": "q_proj,v_proj",
#     "BLOOM": "query_key_value",
#     "BLOOMZ": "query_key_value",
#     "Falcon": "query_key_value",
#     "Baichuan": "W_pack",
#     "Baichuan2": "W_pack",
#     "InternLM": "q_proj,v_proj",
#     "Qwen": "c_attn",
#     "XVERSE": "q_proj,v_proj",
#     "ChatGLM2": "query_key_value",
#     "ChatGLM3": "query_key_value",

# }

# DEFAULT_TEMPLATE = {
#     "LLaMA2": "llama2",
#     "ChineseLLaMA2": "llama2_zh",
#     "Baichuan": "baichuan",
#     "Baichuan2": "baichuan2",
#     "InternLM": "intern",
#     "Qwen": "chatml",
#     "ChatGLM2": "chatglm2",
#     "ChatGLM3": "chatglm3",

# }
