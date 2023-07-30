# DB-GPT-Hub:利用LLMs实现Text-to-SQL

[**英文**](README.md) |[**Discord**](https://discord.gg/c2xxQ8Rq)|[**Wechat**](https://github.com/csunny/DB-GPT/blob/main/README.zh.md#%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC)

## 一、什么是DB-GPT-Hub

DB-GPT-Hub是一个利用LLMs实现Text-to-SQL解析的实验项目，主要包含数据集收集、数据预处理、模型选择与构建和微调权重等步骤，通过这一系列的处理可以在提高Text-to-SQL能力的同时降低模型训练成本，让更多的开发者参与到Text-to-SQL的准确度提升工作当中，最终实现基于数据库的自动问答能力，让用户可以通过自然语言描述完成复杂数据库的查询操作等工作。

## 二、Text-to-SQL微调

大型语言模型（LLMs）在现有Text-to-SQL的基准测试中取得了令人印象深刻的成果。然而，这些模型在面对大型数据库和嘈杂内容时仍然存在挑战，而且巨大的数据库价值背后的奥秘需要外部知识和推理来揭示。 我们基于大语言模型持续的SFT来提升Text-to-SQL的效果

### 2.1、数据集

本项目主要使用了以下公开的text2sql数据集：

- [WikiSQL:](https://github.com/salesforce/WikiSQL) 一个大型的语义解析数据集，由80,654个自然语句表述和24,241张表格的sql标注构成。WikiSQL中每一个问句的查询范围仅限于同一张表，不包含排序、分组、子查询等复杂操作。
- [Spider](https://yale-lily.github.io/spider): 一个跨域的复杂text2sql数据集，包含了10,181条自然语言问句、分布在200个独立数据库中的5,693条SQL，内容覆盖了138个不同的领域。
- [CHASE](https://xjtu-intsoft.github.io/chase/): 一个跨领域多轮交互text2sql中文数据集，包含5459个多轮问题组成的列表，一共17940个<query, SQL>二元组，涉及280个不同领域的数据库。
- [BIRD-SQL：](https://bird-bench.github.io/)数据集是一个英文的大规模跨领域文本到SQL基准测试，特别关注大型数据库内容。该数据集包含12,751对文本到SQL数据对和95个数据库，总大小为33.4GB，跨越37个职业领域。BIRD-SQL数据集通过探索三个额外的挑战，即处理大规模和混乱的数据库值、外部知识推理和优化SQL执行效率，缩小了文本到SQL研究与实际应用之间的差距。
- [CoSQL:](https://yale-lily.github.io/cosql)是一个用于构建跨域对话文本到sql系统的语料库。它是Spider和SParC任务的对话版本。CoSQL由30k+回合和10k+带注释的SQL查询组成，这些查询来自Wizard-of-Oz的3k个对话集合，查询了跨越138个领域的200个复杂数据库。每个对话都模拟了一个真实的DB查询场景，其中一个工作人员作为用户探索数据库，一个SQL专家使用SQL检索答案，澄清模棱两可的问题，或者以其他方式通知。

### 2.2、模型

DB-GPT-HUB目前支持的base模型有：

* LLaMa/LLaMa2系列
  * alpaca
  * vicuna
  * guanaco

* Falcon系列
* BLOOM系列
* ChatGLM系列
* WizardLLM

模型量化微调所需的硬件资源大概如下：

| 模型参数 | GPU RAM         | CPU RAM | DISK   |
| -------- | --------------- | ------- | ------ |
| 7b       | 4.8GB（14.7GB） | 3.6GB   | 36.4GB |
| 13b      | 8.4GB（28.7GB） | 5.9GB   | 60.2GB |
| 33b      | 18.3GB（OOM）   | 8.4GB   | 122GB  |
| 65b      | 38.7GB（OOM）   | 13.1GB  | 434GB  |

### 2.3、微调方法

#### Spider+QLoRA/LoRA+LLM(Falcon/Vicuna/Guanaco/LLaMa)

该实验项目通过加入表结构信息、调整语言模型的参数等方式构建数据集，然后用QLoRA/LoRA对LLM模型进行微调，旨在降低微调成本的同时提高SQL生成的准确性和速度。可以通过以下命令来执行：

```shell
sh scripts/qlora/qlora.sh
sh scripts/lora/lora.sh
```

## 三、使用方法

### 3.1、环境准备

```
git clone https://github.com/csunny/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub python=3.10 
conda activate dbgpt_hub
pip install -r requirements.txt 
mkdir model 
```
你可以将下载的大模型文件放在新建model文件夹下面

### 3.2、数据准备

DB-GPT-HUB使用的是信息匹配生成法进行数据准备，即结合表信息的 SQL + Repository 生成方式，这种方式结合了数据表信息，能够更好地理解数据表的结构和关系，适用于生成符合需求的 SQL 语句。

运行前需要将SQL数据集下载后放在该目录下。这里以spider数据集为例，spider数据集主要包含三部分：

* train_spide.json：每条text-to-SQL的QA数据与数据库相关数据存储为json文件
  * db_id：数据库名称
  * question: 以自然语言的方式向数据库发出的指令
  * query：接受自然语言指令后，能够准确执行指令的sql代码
* train_gold.slq：question的真实slq代码
* database：数据库源文件
  * schema.sql: 建表语句。
  * sqlite: 数据库的具体内容。

首先我们需要将以上数据中的QA、表结构和数据库内容等都信息提取出来，格式如下：

```
{
        "query": sample["query"],
        "question": sample["question"],
        "db_id": db_id,
        "db_path": db_path,
        "db_table_names": schema["table_names_original"],
        "db_column_names": [
            {"table_id": table_id, "column_name": column_name}
            for table_id, column_name in schema["column_names_original"]
        ],
        "db_column_types": schema["column_types"],
        "db_primary_keys": [{"column_id": column_id} for column_id in schema["primary_keys"]],
        "db_foreign_keys": [
            {"column_id": column_id, "other_column_id": other_column_id}
            for column_id, other_column_id in schema["foreign_keys"]
        ],
    }
```

然后将该数据以自然语言的形式表述，例如：

```
{"instruction": "concert_singer contains tables such as stadium, singer, concert, singer_in_concert. Table stadium has columns such as stadium_id, location, name, capacity, highest, lowest, average. stadium_id is the primary key. Table singer has columns such as singer_id, name, country, song_name, song_release_year, age, is_male. singer_id is the primary key. Table concert has columns such as concert_id, concert_name, theme, stadium_id, year. concert_id is the primary key. Table singer_in_concert has columns such as concert_id, singer_id. concert_id is the primary key. The year of concert is the foreign key of location of stadium. The stadium_id of singer_in_concert is the foreign key of name of singer. The singer_id of singer_in_concert is the foreign key of concert_name of concert.", 
"input": "How many singers do we have?", 
"response": "concert_singer | select count(*) from singer"}
```

以上数据预处理部分的代码实现如下：

```bash
python dbgpt_hub/utils/sql_data_process.py
```

在模型微调时，我们还定制了prompt dict以优化输入：

```python
SQL_PROMPT_DICT = {
    "prompt_input": (
        "I want you to act as a SQL terminal in front of an example database. "
        "Below is an instruction that describes a task, Write a response that appropriately completes the request.\n\n"
        "###Instruction:\n{instruction}\n\n###Input:\n{input}\n\n###Response: "
    ),
    "prompt_no_input": (
        "I want you to act as a SQL terminal in front of an example database. "
        "Below is an instruction that describes a task, Write a response that appropriately completes the request.\n\n"
        "###Instruction:\n{instruction}\n\n### Response: "
    ),
}
```

### 3.3、模型微调

模型微调使用的是qlora和lora方法，我们可以运行以下命令来微调模型：

```bash
python train_qlora.py --model_name_or_path <path_or_name>
```

微调后的模型权重会默认保存到adapter文件夹下面。完整的训练脚本在scripts/qlora/qlora.sh中。
对于多卡运行，scripts/spider_qlora_finetune.sh中由于默认是基于QLoRA，建议在一开始就指定运行的GPU编号。如由`python src/train/train_qlora.py` 改为`CUDA_VISIBLE_DEVICES=0,1,2,3 python src/train/train_qlora.py` 。

当使用lora微调时，我们可以用以下指令：

```bash
python train_lora.py --model_name_or_path <path_or_name>
```
完整的训练脚本在scripts/lora/中。

### 3.4、合并权重

运行以下命令来生成最终合并的模型：

```bash
python dbgpt_hub/utils/merge_peft_adapters.py --base_model_name_or_path <path_or_name>
```
在3.3中生成的输出路径对应此3.4中的“--peft_model_path”参数，如其值默认为“./adapter/checkpoint-10/adapter_model”，其他相关参数的默认值也均在merge_peft_adapters.py中的get_arg函数中。

## 四、发展路线

整个过程我们会分为三个阶段：

* 阶段一：
  - [x] LLaMa/LLaMa2
    - [x] LoRA
    - [x] QLoRA
  - [x] Falcon
    - [x] LoRA
    - [x] QLoRA
  - [ ] ChatGLM
  - [ ] BLOOM
  - [ ] WizardLM
* 阶段二:
  * 优化模型效果，放出优化后DB-GPT-SFT模型
* 阶段三：
  * 评测数据集和方法标准

## 五、贡献

欢迎大家在数据集、模型微调、效果评测等方面积极参与并提供更多意见。

## 六、感谢

感谢以下开源项目

* [Spider](https://github.com/ElementAI/spider)
* [CoSQL](https://yale-lily.github.io/cosql)
* [Chase](https://xjtu-intsoft.github.io/chase/)
* [BIRD-SQL](https://bird-bench.github.io/)
* [LLaMA](https://github.com/facebookresearch/llama/tree/main)
* [BLOOM](https://huggingface.co/spaces/bigscience/license)
* [Falcon](https://github.com/hiyouga/LLaMA-Efficient-Tuning/blob/main/LICENSE)
* [ChatGLM](https://github.com/search?q=ChatGLM&type=repositories)
* [WizardLM](https://github.com/nlpxucan/WizardLM)

