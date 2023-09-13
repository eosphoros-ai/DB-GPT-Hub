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

默认将数据下载后，放在一级目录data下面，如data/spider .

### 2.2、模型

DB-GPT-HUB目前支持的base模型有：

* LLaMa/LLaMa2系列
  * CodeLlama（在refactor分支）
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
sh scripts/lora/lora.sh 或者  sh scripts/lora/lora_ds.sh
```
其中lora.sh和lora_ds.sh的区别主要是用deepspeed(ds)版本。
## 三、使用方法

### 3.1、环境准备

```
git clone https://github.com/eosphoros-ai/DB-GPT-Hub.git
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
{"instruction": "department_management contains tables such as department, head, management. Table department has columns such as department_id, name, creation, ranking, budget_in_billions, num_employees. department_id is the primary key. Table head has columns such as head_id, name, born_state, age. head_id is the primary key. Table management has columns such as department_id, head_id, temporary_acting. department_id is the primary key. The head_id of management is the foreign key of head_id of head. The department_id of management is the foreign key of department_id of department.",
"input": "How many heads of the departments are older than 56 ?",
"output": "select count(*) from head where age > 56"}

```

以上数据预处理部分的代码实现如下：

```bash
## 生成train数据
python dbgpt_hub/utils/sql_data_process.py 

## 生成dev数据
python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json \
```
如果你不想做这一步，你可以[下载](https://drive.google.com/drive/folders/1MkNSJgJn9mTH5TTjdn@6gf5N3ghG1wnn?usp-drive_link)我们已经处理过的数据集，然后把它放在该项目文件夹下即可

在模型微调时，我们还定制了prompt dict以优化输入：

```python
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

如果需要将微调权重合并到base模型中，可以执行以下命令

```bash
python dbgpt_hub/utils/merge_peft_adapters.py --peft_model_path Your_adapter_model
```

### 3.4、预测
项目目录下建`./data/out_pred/`文件夹，此文件夹为默认输出的位置。

- 基于基础模型的直接预测
```bash
sh scripts/no_peft/get_predict_no_peft_llama2_13b_hf.sh
```

- 基于LoRA的预测
执行如下脚本命令
```bash
sh scripts/lora/get_predict_lora.sh
```
相关默认输入输出可见， ./data/out_pred/
- 基于QLoRA的预测
执行如下脚本命令
```bash
sh scripts/qlora/get_predict_qlora.sh
```

### 3.5 、模型评估
对于模型在数据集上的效果评估,默认为在`spider`数据集上。
运行以下命令来：

```bash
python eval/evaluation.py --plug_value --input  Your_model_pred_file
```
你可以在[这里](docs/eval_llm_result.md)找到我们最新的审查结果。
## 四、发展路线

整个过程我们会分为三个阶段：

* 阶段一:
  * 搭建基本框架，基于数个大模型打通从数据处理、模型SFT训练、预测输出和评估的整个流程，截止`20230804`我们已经整个打通。
  我们现在支持  
  - [x] CodeLlama（在refactor分支）
  - [x] LLaMa/LLaMa
  - [x] Falcon
  - [x] ChatGLM
  - [x] BLOOM 

  后续初步计划支持如下：
  - [ ] CodeGeeX
  - [ ] WizardLM
  最近我们也在重构代码，关于CodeLlama的支持和实验结果我们放到了refactore分支中。  
  
  **如果你觉得有帮助，给我们的项目点个star是对我们的最好鼓励，也是我们放出更多代码和实验结果的动力。谢谢你的鼓励！**



* 阶段二:
  * 优化模型效果，支持更多不同模型进行不同方式的微调。
  * 对`prompt`优化
  * 放出评估效果，优化后`DB-GPT-SFT`模型
* 阶段三：
  * 基于更多论文进行优化，如`RESDSQL`等；

## 五、贡献

欢迎更多小伙伴在数据集、模型微调、效果评测、论文推荐与复现等方面参与和反馈，如提issues或者pr反馈，我们会积极给出回应。

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
* [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder)
* [test-suite-sql-eval](https://github.com/taoyds/test-suite-sql-eval)

