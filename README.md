# DB-GPT-Hub: Text-to-SQL parsing with LLMs

[**简体中文**](README.zh.md) |[**Discord**](https://discord.gg/c2xxQ8Rq)|[**Wechat**](https://github.com/csunny/DB-GPT/blob/main/README.zh.md#%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC)

## 1. What is DB-GPT-Hub

DB-GPT-Hub is an experimental project to implement Text-to-SQL parsing using LLMs, which mainly includes dataset collection, data pre-processing, model selection and construction, and fine-tuning weights, etc. Through this series of processing, we can reduce the model training cost while improving Text-to-SQL capability, and allow more developers to participate in the work of improving the accuracy of Text-to-SQL, and finally realizing the automatic database based question and answer capability, allowing users to complete complex database query operations through natural language descriptions.

## 2. Fine-tuning Text-to-SQL

Large Language Models (LLMs) have achieved impressive results in existing benchmark tests of Text-to-SQL. However, these models remain challenging in the face of large databases and noisy content, and the mysteries behind the huge database values need external knowledge and reasoning to be revealed. We enhance Text-to-SQL based on a large language models sustained SFT

### 2.1. Dataset

The following publicly available text-to-sql datasets are used for this project:

- [WikiSQL:](https://github.com/salesforce/WikiSQL) A large semantic parsing dataset consisting of 80,654 natural statement expressions and sql annotations of 24,241 tables. Each query in WikiSQL is limited to the same table and does not contain complex operations such as sorting, grouping The queries in WikiSQL are limited to the same table and do not include complex operations such as sorting, grouping, subqueries, etc.
- [SPIDER](https://yale-lily.github.io/spider): A complex text2sql dataset across domains, containing 10,181 natural language queries, 5,693 SQL distributed across 200 separate databases, covering 138 different domains.
- [CHASE](https://xjtu-intsoft.github.io/chase/): A cross-domain multi-round interactive text2sql Chinese dataset containing a list of 5,459 multi-round questions consisting of 17,940 <query, SQL> binary groups across 280 different domain databases.
- [BIRD-SQL:](https://bird-bench.github.io/) A large-scale cross-domain text-to-SQL benchmark in English, with a particular focus on large database content. The dataset contains 12,751 text-to-SQL data pairs and 95 databases with a total size of 33.4 GB across 37 occupational domains. The BIRD-SQL dataset bridges the gap between text-to-SQL research and real-world applications by exploring three additional challenges, namely dealing with large and messy database values, external knowledge inference and optimising SQL execution efficiency.
- [CoSQL:](https://yale-lily.github.io/cosql) A corpus for building cross-domain conversational text-to-SQL systems. It is a conversational version of the Spider and SParC tasks. CoSQL consists of 30k+ rounds and 10k+ annotated SQL queries from Wizard-of-Oz's collection of 3k conversations querying 200 complex databases across 138 domains. Each conversation simulates a realistic DB query scenario in which a staff member explores the database as a user and a SQL expert uses SQL to retrieve answers, clarify ambiguous questions, or otherwise inform.


After the data is downloaded by default, it is placed under the first-level directory data, such as data/spider.

### 2.2. Model

DB-GPT-HUB currently supports the following base models:

* LLaMa/LLaMa2
  * alpaca
  * vicuna
  * guanaco

* Falcon
* BLOOM
* ChatGLM
* WizardLLM

The approximate hardware resources required to quantize and fine-tune the model are as follows:

| Model Parameters | GPU RAM        | CPU RAM | DISK   |
| ---------------- | -------------- | ------- | ------ |
| 7b               | 4.8GB (14.7GB) | 3.6GB   | 36.4GB |
| 13b              | 8.4GB (28.7GB) | 5.9GB   | 60.2GB |
| 33b              | 18.3GB (OOM)   | 8.4GB   | 122GB  |
| 65b              | 38.7GB (OOM)   | 13.1GB  | 434GB  |

### 2.3. Fine-tuning methods

#### Spider+QLoRA/LoRA+LLM(Falcon/Vicuna/Guanaco/LLaMa)

This experimental project builds a dataset by adding table structure information, adjusting the parameters of the language model and then fine-tuning the LLM with QLoRA/LoRA, aiming to reduce the cost of fine-tuning while increasing the accuracy and speed of SQL generation. This can be executed with the following command:

```shell
sh scripts/qlora/qlora.sh
sh scripts/lora/lora.sh
```

## 3. Usage

### 3.1. Environment preparation

```
git clone https://github.com/csunny/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub python=3.10 
conda activate dbgpt_hub
pip install -r requirements.txt 
mkdir model 
```
Put the model files under the new Model folder here

### 3.2. Data preparation

DB-GPT-HUB uses the information matching generation method for data preparation, i.e. the SQL + Repository generation method that combines table information. This method combines data table information to better understand the structure and relationships of the data table, and is suitable for generating SQL statements that meet the requirements.

Before running, you need to download the SQL data set and put it in this directory. Here, take the spider data set as an example. The spider data set consists of three main parts:

* train_spide.json: each text-to-SQL QA data and database related data is stored as a json file
  * db_id: the name of the database
  * question: the command issued to the database in natural language
  * query: sql code that accepts the natural language command and executes it exactly
* train_gold.slq: the real slq code for the question
* database: the database source file
  * schema.sql: the table build statement.
  * sqlite: the specifics of the database.

First we need to extract all the information from the above data such as QA, table structure and database content in the following format:

```
{
        "query": sample["query"].
        "question": sample["question"].
        "db_id": db_id.
        "db_path": db_path.
        "db_table_names": schema["table_names_original"].
        "db_column_names": [
            {"table_id": table_id, "column_name": column_name}
            for table_id, column_name in schema["column_names_original"]
        ].
        "db_column_types": schema["column_types"].
        "db_primary_keys": [{"column_id": column_id} for column_id in schema["primary_keys"]].
        "db_foreign_keys": [
            {"column_id": column_id, "other_column_id": other_column_id}
            for column_id, other_column_id in schema["foreign_keys"]
        ].
    }
```

This data is then expressed in natural language, e.g:

```
{"instruction": "department_management contains tables such as department, head, management. Table department has columns such as department_id, name, creation, ranking, budget_in_billions, num_employees. department_id is the primary key. Table head has columns such as head_id, name, born_state, age. head_id is the primary key. Table management has columns such as department_id, head_id, temporary_acting. department_id is the primary key. The head_id of management is the foreign key of head_id of head. The department_id of management is the foreign key of department_id of department.",
"input": "How many heads of the departments are older than 56 ?",
"output": "select count(*) from head where age > 56"}
```

The code implementation of the above data pre-processing section is as follows:

```bash
## Generate train data
python dbgpt_hub/utils/sql_data_process.py 

## Generate dev data
python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json \

```

When fine-tuning the model, we also customize the prompt dict to optimize the input: 

``` python
SQL_PROMPT_DICT = {
    "prompt_input": (
        "I want you to act as a SQL terminal in front of an example database, \
         you need only to return the sql command to me.Below is an instruction that describes a task, \
         Write a response that appropriately completes the request.\n"  \
         "##Instruction:\n{instruction}\n###Input:\n{input}\n\n###Response:"
    ),
    "prompt_no_input": (
        "I want you to act as a SQL terminal in front of an example database, \
        you need only to return the sql command to me.Below is an instruction that describes a task, \
        Write a response that appropriately completes the request.\n"  \
        "####Instruction:\n{instruction}\n\###Response: "
    ),
}

```

### 3.3. Model fine-tuning

Model fine-tuning uses the QLoRA/LoRA method, where we can run the following command to fine-tune the model:

```bash
python train_qlora.py --model_name_or_path <path_or_name>
```
The fine-tuned model weights are saved under the adapter folder by default. The full training script is in scripts/qlora/qlora.sh.For multi-card runs, scripts/spider_qlora_finetune.sh is based on QLoRA by default, so it is recommended to specify the GPU number to run at the beginning. e.g. from `python src/train/train_qlora.py` to `CUDA_VISIBLE_DEVICES=0,1,2,3 python src/train/train_qlora.py` 

```bash
python train_lora.py --model_name_or_path <path_or_name>
```
The full training script is in scripts/lora/.

### 3.4. Model Predict

Create the ./data/out_pred/ folder under the project directory. This is the default output location.
- Prediction based on LoRA
Run the following script:
```bash
sh scripts/lora/get_predict_lora.sh
```

- Prediction based on QLoRA
Run the following script:
```bash
sh scripts/qlora/get_predict_qlora.sh
```

### 3.5 Model Evaluation
To evaluate model performance on the dataset, default is spider dataset.
Run the following command:

```bash
python eval/evaluation.py --plug_value --input
```

## 4. RoadMap 

The whole process we will divide into three phases:

* Stage 1:
  * Set up the basic framework, enabling end-to-end workflow from data processing, model SFT training, prediction output to evaluation based on multiple large models. As of 20230804, the entire pipeline has been established.
  now,we has supported as follows:
  - [x] LLaMa/LLaMa
  - [x] Falcon
* Stage 2:
  * Optimize model performance, support fine-tuning more different models in various ways.
  * Optimize `prompts`
  * Release evaluation results, optimize `DB-GPT-SFT` models
* Stage 3:
  * Based on more papers, conduct optimizations, such as `RESDSQL`, etc.

## 5. Contributions

We welcome more folks to participate and provide feedback in areas like datasets, model fine-tuning, performance evaluation, paper recommendations, code reproduction, etc. Feel free to open issues or PRs and we'll actively respond.

## 6. Acknowledgements

Thanks to the following open source projects

* [Spider](https://github.com/ElementAI/spider)
* [CoSQL](https://yale-lily.github.io/cosql)
* [Chase](https://xjtu-intsoft.github.io/chase/)
* [BIRD-SQL](https://bird-bench.github.io/)
* [LLaMA](https://github.com/facebookresearch/llama/tree/main)
* [BLOOM](https://huggingface.co/spaces/bigscience/license)
* [Falcon](https://github.com/hiyouga/LLaMA-Efficient-Tuning/blob/main/LICENSE)
* [ChatGLM](https://github.com/search?q=ChatGLM&type=repositories)
* [WizardLM](https://github.com/nlpxucan/WizardLM)
*  [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder)
* [test-suite-sql-eval](https://github.com/taoyds/test-suite-sql-eval)

