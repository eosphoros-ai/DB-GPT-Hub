# DB-GPT-Hub:利用LLMs实现Text-to-SQL

<div align="center">
  <p>
    <a href="https://github.com/eosphoros-ai/DB-GPT">
        <img alt="stars" src="https://img.shields.io/github/stars/eosphoros-ai/db-gpt-hub?style=social" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT-Hub">
        <img alt="forks" src="https://img.shields.io/github/forks/eosphoros-ai/db-gpt-hub?style=social" />
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT-Hub/releases">
      <img alt="Release Notes" src="https://img.shields.io/github/release/eosphoros-ai/DB-GPT-Hub" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT-Hub/issues">
      <img alt="Open Issues" src="https://img.shields.io/github/issues-raw/eosphoros-ai/DB-GPT-Hub" />
    </a>
    <a href="https://discord.gg/7uQnPuveTY">
      <img alt="Discord" src="https://dcbadge.vercel.app/api/server/7uQnPuveTY?compact=true&style=flat" />
    </a>
  </p>


[**英文**](README.md) | [**Discord**](https://discord.gg/7uQnPuveTY) | [**Wechat**](https://github.com/eosphoros-ai/DB-GPT/blob/main/README.zh.md#%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC) | [**Huggingface**](https://huggingface.co/eosphoros) | [**Community**](https://github.com/eosphoros-ai/community)
</div>


## Baseline
- 更新日期: 2023/12/08
- 评价指标: execution accuracy (ex)
- 详情参考[docs/eval-llm-result.md](https://github.com/eosphoros-ai/DB-GPT-Hub/blob/main/docs/eval_llm_result.md)

<table style="text-align: center;">
  <tr>
    <th style="text-align: center;">Model</th>
    <th>Method</th>
    <th>Easy</th>
    <th>Medium</th>
    <th>Hard</th>
    <th>Extra</th>
    <th>All</th>
  </tr>
  <tr >
    <td></td>
    <td>base</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Llama2-7B-Chat</td>
    <td>lora</td>
    <td>0.887</td>
    <td>0.641</td>
    <td>0.489</td>
    <td>0.331</td>
    <td>0.626</td>
  </tr>
  <tr>
    <td></td>
    <td>qlora</td>
    <td>0.847</td>
    <td>0.623</td>
    <td>0.466</td>
    <td>0.361</td>
    <td>0.608</td>
  </tr>
  <tr>
    <td></td>
    <td>base</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Llama2-13B-Chat</td>
    <td>lora</td>
    <td>0.907</td>
    <td>0.729</td>
    <td>0.552</td>
    <td>0.343</td>
    <td>0.68</td>
  </tr>
  <tr>
    <td></td>
    <td>qlora</td>
    <td>0.911</td>
    <td>0.7</td>
    <td>0.552</td>
    <td>0.319</td>
    <td>0.664</td>
  </tr>
  <tr>
    <td></td>
    <td>base</td>
    <td>0.214</td>
    <td>0.177</td>
    <td>0.092</td>
    <td>0.036</td>
    <td>0.149</td>
  </tr>
  <tr>
  <td>CodeLlama-7B-Instruct</td>
    <td>lora</td>
    <td>0.923</td>
    <td>0.756</td>
    <td>0.586</td>
    <td>0.349</td>
    <td>0.702</td>
  </tr>
  <tr>
    <td></td>
    <td>qlora</td>
    <td>0.911</td>
    <td>0.751</td>
    <td>0.598</td>
    <td>0.331</td>
    <td>0.696</td>
  </tr>
  <tr>
    <td></td>
    <td>base</td>
    <td>0.698</td>
    <td>0.601</td>
    <td>0.408</td>
    <td>0.271</td>
    <td>0.539</td>
  </tr>
  <tr>
    <td>CodeLlama-13B-Instruct</td>
    <td>lora</td>
    <td>0.94</td>
    <td>0.789</td>
    <td>0.684</td>
    <td>0.404</td>
    <td>0.746</td>
  </tr>
  <tr>
    <td></td>
    <td>qlora</td>
    <td>0.94</td>
    <td>0.774</td>
    <td>0.626</td>
    <td>0.392</td>
    <td>0.727</td>
  </tr>
  <tr>
    <td></td>
    <td>base</td>
    <td>0.577</td>
    <td>0.352</td>
    <td>0.201</td>
    <td>0.066</td>
    <td>0.335</td>
  </tr>
  <tr>
    <td>Baichuan2-7B-Chat</td>
    <td>lora</td>
    <td>0.871</td>
    <td>0.63</td>
    <td>0.448</td>
    <td>0.295</td>
    <td>0.603</td>
  </tr>
  <tr>
  <td></td>
    <td>qlora</td>
    <td>0.891</td>
    <td>0.637</td>
    <td>0.489</td>
    <td>0.331</td>
    <td>0.624</td>
  </tr>
  <tr>
    <td></td>
    <td>base</td>
    <td>0.581</td>
    <td>0.413</td>
    <td>0.264</td>
    <td>0.187</td>
    <td>0.392</td>
  </tr>
    <tr>
    <td>Baichuan2-13B-Chat</td>
    <td>lora</td>
    <td>0.903</td>
    <td>0.702</td>
    <td>0.569</td>
    <td>0.392</td>
    <td>0.678</td>
    </tr>
  <tr>
  <td></td>
    <td>qlora</td>
    <td>0.895</td>
    <td>0.675</td>
    <td>0.58</td>
    <td>0.343</td>
    <td>0.659</td>
  </tr>
  <tr>
  <td></td>
  <td>base</td>
  <td>0.395</td>
  <td>0.256</td>
  <td>0.138</td>
  <td>0.042</td>
  <td>0.235</td>
  </tr>
<tr>
<td>Qwen-7B-Chat</td>
  <td>lora</td>
  <td>0.855</td>
  <td>0.688</td>
  <td>0.575</td>
  <td>0.331</td>
  <td>0.652</td>
  </tr>
  <tr>
    <td></td>
    <td>qlora</td>
    <td>0.911</td>
    <td>0.675</td>
    <td>0.575</td>
    <td>0.343</td>
    <td>0.662</td>
  </tr>
  <tr>
  <td></td>
  <td>base</td>
  <td>0.871</td>
  <td>0.632</td>
  <td>0.368</td>
  <td>0.181</td>
  <td>0.573</td>
  </tr>
  <tr>
    <td>Qwen-14B-Chat</td>
    <td>lora</td>
    <td>0.895</td>
    <td>0.702</td>
    <td>0.552</td>
    <td>0.331</td>
    <td>0.663</td>
  </tr>
  <tr>
    <td></td>
    <td>qlora</td>
    <td>0.919</td>
    <td>0.744</td>
    <td>0.598</td>
    <td>0.367</td>
  <td>0.701</td>
  </tr>
    <tr>
    <td></td>
    <td>base</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>ChatGLM3-6b</td>
    <td>lora</td>
    <td>0.855</td>
    <td>0.605</td>
    <td>0.477</td>
    <td>0.271</td>
    <td>0.59</td>
  </tr>
  <tr>
    <td></td>
    <td>qlora</td>
    <td>0.843</td>
    <td>0.603</td>
    <td>0.506</td>
    <td>0.211</td>
    <td>0.581</td>
  </tr>
</table>
 
## Contents
- [DB-GPT-Hub:利用LLMs实现Text-to-SQL](#db-gpt-hub利用llms实现text-to-sql)
  - [Baseline](#baseline)
  - [Contents](#contents)
  - [一、简介](#一简介)
  - [二、Text-to-SQL微调](#二text-to-sql微调)
    - [2.1、数据集](#21数据集)
    - [2.2、基座模型](#22基座模型)
  - [三、使用方法](#三使用方法)
    - [3.1、环境准备](#31环境准备)
    - [3.2、数据准备](#32数据准备)
    - [3.2 快速开始](#32-快速开始)
    - [3.3、模型微调](#33模型微调)
    - [3.4、模型预测](#34模型预测)
    - [3.5、模型权重](#35模型权重)
      - [3.5.1 模型和微调权重合并](#351-模型和微调权重合并)
    - [3.6、模型评估](#36模型评估)
  - [四、发展路线](#四发展路线)
  - [五、贡献](#五贡献)
  - [六、感谢](#六感谢)
  - [七、引用](#七引用)
  - [八、Licence](#八licence)
  - [九、我们的联系方式](#九我们的联系方式)

## 一、简介

DB-GPT-Hub是一个利用LLMs实现Text-to-SQL解析的实验项目，主要包含数据集收集、数据预处理、模型选择与构建和微调权重等步骤，通过这一系列的处理可以在提高Text-to-SQL能力的同时降低模型训练成本，让更多的开发者参与到Text-to-SQL的准确度提升工作当中，最终实现基于数据库的自动问答能力，让用户可以通过自然语言描述完成复杂数据库的查询操作等工作。     
目前我们已经基于多个大模型打通从数据处理、模型SFT训练、预测输出和评估的整个流程，**代码在本项目中均可以直接复用**。   
截止20231010，我们利用本项目基于开源的13B大小的模型微调，结合更多相关数据，在零样本提示下，基于Spider的[test-suite](https://github.com/taoyds/test-suite-sql-eval)中的数据库(大小1.27G)执行准确率可以达到**0.764**，基于Spider[官方网站](https://yale-lily.github.io/spider)指向的数据库(大小95M)的执行准确率为0.825。
部分实验结果已汇总到了本项目的相关[文档](docs/eval_llm_result.md) ，可供参考。

## 二、Text-to-SQL微调

 我们基于大语言模型的SFT来提升Text-to-SQL的效果。

### 2.1、数据集

本项目案例数据主要以**Spider**数据集为示例 ：
- [Spider](https://yale-lily.github.io/spider): 一个跨域的复杂text2sql数据集，包含了10,181条自然语言问句、分布在200个独立数据库中的5,693条SQL，内容覆盖了138个不同的领域。[下载链接](https://drive.google.com/uc?export=download&id=1TqleXec_OykOYFREKKtschzY29dUcVAQ)

其他数据集：  

- [WikiSQL:](https://github.com/salesforce/WikiSQL) 一个大型的语义解析数据集，由80,654个自然语句表述和24,241张表格的sql标注构成。WikiSQL中每一个问句的查询范围仅限于同一张表，不包含排序、分组、子查询等复杂操作。
- [CHASE](https://xjtu-intsoft.github.io/chase/): 一个跨领域多轮交互text2sql中文数据集，包含5459个多轮问题组成的列表，一共17940个<query, SQL>二元组，涉及280个不同领域的数据库。
- [BIRD-SQL：](https://bird-bench.github.io/)数据集是一个英文的大规模跨领域文本到SQL基准测试，特别关注大型数据库内容。该数据集包含12,751对文本到SQL数据对和95个数据库，总大小为33.4GB，跨越37个职业领域。BIRD-SQL数据集通过探索三个额外的挑战，即处理大规模和混乱的数据库值、外部知识推理和优化SQL执行效率，缩小了文本到SQL研究与实际应用之间的差距。
- [CoSQL:](https://yale-lily.github.io/cosql)是一个用于构建跨域对话文本到sql系统的语料库。它是Spider和SParC任务的对话版本。CoSQL由30k+回合和10k+带注释的SQL查询组成，这些查询来自Wizard-of-Oz的3k个对话集合，查询了跨越138个领域的200个复杂数据库。每个对话都模拟了一个真实的DB查询场景，其中一个工作人员作为用户探索数据库，一个SQL专家使用SQL检索答案，澄清模棱两可的问题，或者以其他方式通知。
- 按照[NSQL](https://github.com/NumbersStationAI/NSQL)的处理模板，对数据集做简单处理，共得到约[20w条训练数据](https://huggingface.co/datasets/Healthy13/Text2SQL/tree/main)



### 2.2、基座模型

DB-GPT-HUB目前已经支持的base模型有：

  - [x] CodeLlama
  - [x] Baichuan2 
  - [x] LLaMa/LLaMa2
  - [x] Falcon
  - [x] Qwen
  - [x] XVERSE
  - [x] ChatGLM2
  - [x] ChatGLM3
  - [x] internlm
  - [x] Falcon
  - [x] sqlcoder-7b(mistral)
  - [x] sqlcoder2-15b(starcoder)



模型可以基于quantization_bit为4的量化微调(QLoRA)所需的最低硬件资源,可以参考如下：

| 模型参数 | GPU RAM | CPU RAM | DISK   |
| -------- | ------- | ------- | ------ |
| 7b       | 6GB     | 3.6GB   | 36.4GB |
| 13b      | 13.4GB  | 5.9GB   | 60.2GB |

其中相关参数均设置的为最小，batch_size为1，max_length为512。根据经验，如果计算资源足够，为了效果更好，建议相关长度值设置为1024或者2048。  

## 三、使用方法

### 3.1、环境准备

```
git clone https://github.com/eosphoros-ai/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub python=3.10 
conda activate dbgpt_hub
pip install poetry
poetry install
```

### 3.2、数据准备

DB-GPT-Hub使用的是信息匹配生成法进行数据准备，即结合表信息的 SQL + Repository 生成方式，这种方式结合了数据表信息，能够更好地理解数据表的结构和关系，适用于生成符合需求的 SQL 语句。 
从[spider数据集链接](https://drive.google.com/uc?export=download&id=1TqleXec_OykOYFREKKtschzY29dUcVAQ) 下载spider数据集，默认将数据下载解压后，放在目录dbgpt_hub/data下面，即路径为`dbgpt_hub/data/spider`。 

数据预处理部分，**只需运行如下脚本**即可：
```bash
## 生成train数据 和dev(eval)数据,
poetry run sh dbgpt_hub/scripts/gen_train_eval_data.sh
```
在`dbgpt_hub/data/`目录你会得到新生成的训练文件example_text2sql_train.json 和测试文件example_text2sql_dev.json ，数据量分别为8659和1034条。 对于后面微调时的数据使用在dbgpt_hub/data/dataset_info.json中将参数`file_name`值给为训练集的文件名，如example_text2sql_train.json。

生成的json中的数据形如：  
```
    {
        "db_id": "department_management",
        "instruction": "I want you to act as a SQL terminal in front of an example database, you need only to return the sql command to me.Below is an instruction that describes a task, Write a response that appropriately completes the request.\n\"\n##Instruction:\ndepartment_management contains tables such as department, head, management. Table department has columns such as Department_ID, Name, Creation, Ranking, Budget_in_Billions, Num_Employees. Department_ID is the primary key.\nTable head has columns such as head_ID, name, born_state, age. head_ID is the primary key.\nTable management has columns such as department_ID, head_ID, temporary_acting. department_ID is the primary key.\nThe head_ID of management is the foreign key of head_ID of head.\nThe department_ID of management is the foreign key of Department_ID of department.\n\n",
        "input": "###Input:\nHow many heads of the departments are older than 56 ?\n\n###Response:",
        "output": "SELECT count(*) FROM head WHERE age  >  56",
        "history": []
    }, 
```     
项目的数据处理代码中已经嵌套了`chase` 、`cosql`、`sparc`的数据处理，可以根据上面链接将数据集下载到data路径后，在`dbgpt_hub/configs/config.py`中将 `SQL_DATA_INFO`中对应的代码注释松开即可。  

### 3.2 快速开始

首先，用如下命令安装`dbgpt-hub`：

`pip install dbgpt-hub`

然后，指定参数并用几行代码完成整个Text2SQL fine-tune流程：
```python
from dbgpt_hub_sql.data_process import preprocess_sft_data
from dbgpt_hub_sql.train import start_sft
from dbgpt_hub_sql.predict import start_predict
from dbgpt_hub_sql.eval import start_evaluate

# 配置训练和验证集路径和参数
data_folder = "dbgpt_hub/data"
data_info = [
        {
            "data_source": "spider",
            "train_file": ["train_spider.json", "train_others.json"],
            "dev_file": ["dev.json"],
            "tables_file": "tables.json",
            "db_id_name": "db_id",
            "is_multiple_turn": False,
            "train_output": "spider_train.json",
            "dev_output": "spider_dev.json",
        }
]

# 配置fine-tune参数
train_args = {
            "model_name_or_path": "codellama/CodeLlama-13b-Instruct-hf",
            "do_train": True,
            "dataset": "example_text2sql_train",
            "max_source_length": 2048,
            "max_target_length": 512,
            "finetuning_type": "lora",
            "lora_target": "q_proj,v_proj",
            "template": "llama2",
            "lora_rank": 64,
            "lora_alpha": 32,
            "output_dir": "dbgpt_hub/output/adapter/CodeLlama-13b-sql-lora",
            "overwrite_cache": True,
            "overwrite_output_dir": True,
            "per_device_train_batch_size": 1,
            "gradient_accumulation_steps": 16,
            "lr_scheduler_type": "cosine_with_restarts",
            "logging_steps": 50,
            "save_steps": 2000,
            "learning_rate": 2e-4,
            "num_train_epochs": 8,
            "plot_loss": True,
            "bf16": True,
}

# 配置预测参数
predict_args = {
            "model_name_or_path": "codellama/CodeLlama-13b-Instruct-hf",
            "template": "llama2",
            "finetuning_type": "lora",
            "checkpoint_dir": "dbgpt_hub/output/adapter/CodeLlama-13b-sql-lora",
            "predict_file_path": "dbgpt_hub/data/eval_data/dev_sql.json",
            "predict_out_dir": "dbgpt_hub/output/",
            "predicted_out_filename": "pred_sql.sql",
}

# 配置评估参数
evaluate_args =  {
            "input": "./dbgpt_hub/output/pred/pred_sql_dev_skeleton.sql",
            "gold": "./dbgpt_hub/data/eval_data/gold.txt",
            "gold_natsql": "./dbgpt_hub/data/eval_data/gold_natsql2sql.txt",
            "db": "./dbgpt_hub/data/spider/database",
            "table": "./dbgpt_hub/data/eval_data/tables.json",
            "table_natsql": "./dbgpt_hub/data/eval_data/tables_for_natsql2sql.json",
            "etype": "exec",
            "plug_value": True,
            "keep_distict": False,
            "progress_bar_for_each_datapoint": False,
            "natsql": False,
}

# 执行整个Fine-tune流程
preprocess_sft_data(
      data_folder = data_folder,
      data_info = data_info
)

start_sft(train_args)
start_predict(predict_args)
start_evaluate(evaluate_args)
```

### 3.3、模型微调

本项目微调不仅能支持QLoRA和LoRA法，还支持deepseed。 可以运行以下命令来微调模型，默认带着参数`--quantization_bit `为QLoRA的微调方式，如果想要转换为lora的微调，只需在脚本中去掉quantization_bit参数即可。
默认QLoRA微调，运行命令：

```bash
poetry run sh dbgpt_hub/scripts/train_sft.sh
```
微调后的模型权重会默认保存到adapter文件夹下面，即dbgpt_hub/output/adapter目录中。  
**如果使用多卡训练，想要用deepseed** ，则将train_sft.sh中默认的内容进行更改，
调整为：

```
CUDA_VISIBLE_DEVICES=0 python dbgpt_hub/train/sft_train.py \
    --quantization_bit 4 \
    ...
```    
更改为： 
```
deepspeed --num_gpus 2  dbgpt_hub/train/sft_train.py \
    --deepspeed dbgpt_hub/configs/ds_config.json \
    --quantization_bit 4 \
    ...
```   
如果需要指定对应的显卡id而不是默认的前两个如3,4，可以如下
```
deepspeed --include localhost:3,4  dbgpt_hub/train/sft_train.py \
    --deepspeed dbgpt_hub/configs/ds_config.json \
    --quantization_bit 4 \
    ...
```    

其他省略(...)的部分均保持一致即可。 如果想要更改默认的deepseed配置，进入 `dbgpt_hub/configs` 目录，在ds_config.json 更改即可，默认为stage2的策略。

脚本中微调时不同模型对应的关键参数lora_target 和 template，如下表：

| 模型名                                                   | lora_target     | template  |
| -------------------------------------------------------- | --------------- | --------- |
| [LLaMA-2](https://huggingface.co/meta-llama)             | q_proj,v_proj   | llama2    |
| [CodeLlama-2](https://huggingface.co/codellama/)         | q_proj,v_proj   | llama2    |
| [Baichuan2](https://github.com/baichuan-inc/Baichuan2)   | W_pack          | baichuan2 |
| [Qwen](https://github.com/QwenLM/Qwen-7B)                | c_attn          | chatml    |
| [sqlcoder-7b](https://huggingface.co/defog/sqlcoder-7b)  | q_proj,v_proj   | mistral   |
| [sqlcoder2-15b](https://huggingface.co/defog/sqlcoder2)  | c_attn          | default   |
| [InternLM](https://github.com/InternLM/InternLM)         | q_proj,v_proj   | intern    |
| [XVERSE](https://github.com/xverse-ai/XVERSE-13B)        | q_proj,v_proj   | xverse    |
| [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B)         | query_key_value | chatglm2  |
| [LLaMA](https://github.com/facebookresearch/llama)       | q_proj,v_proj   | -         |
| [BLOOM](https://huggingface.co/bigscience/bloom)         | query_key_value | -         |
| [BLOOMZ](https://huggingface.co/bigscience/bloomz)       | query_key_value | -         |
| [Baichuan](https://github.com/baichuan-inc/baichuan-13B) | W_pack          | baichuan  |
| [Falcon](https://huggingface.co/tiiuae/falcon-7b)        | query_key_value | -         |


`train_sft.sh`中其他关键参数含义：
> quantization_bit：是否量化，取值为[4或者8]   
> model_name_or_path：  LLM模型的路径   
> dataset： 取值为训练数据集的配置名字，对应在dbgpt_hub/data/dataset_info.json 中外层key值，如example_text2sql。   
> max_source_length： 输入模型的文本长度，如果计算资源支持，可以尽能设大，如1024或者2048。  
> max_target_length： 输出模型的sql内容长度，设置为512一般足够。   
> output_dir ： SFT微调时Peft模块输出的路径，默认设置在dbgpt_hub/output/adapter/路径下 。  
> per_device_train_batch_size ： batch的大小，如果计算资源支持，可以设置为更大，默认为1。   
> gradient_accumulation_steps ： 梯度更新的累计steps值 
> save_steps ： 模型保存的ckpt的steps大小值，默认可以设置为100。  
> num_train_epochs ： 训练数据的epoch数   




### 3.4、模型预测
项目目录下`./dbgpt_hub/`下的`output/pred/`，此文件路径为关于模型预测结果默认输出的位置(如果没有则建上)。   
预测运行命令：
```bash
poetry run sh ./dbgpt_hub/scripts/predict_sft.sh
```   
脚本中默认带着参数`--quantization_bit `为QLoRA的预测，去掉即为LoRA的预测方式。  
其中参数`predicted_input_filename`  为要预测的数据集文件， `--predicted_out_filename` 的值为模型预测的结果文件名。默认结果保存在`dbgpt_hub/output/pred`目录。


### 3.5、模型权重
可以从Huggingface查看我们社区上传的第二版Peft模块权重[huggingface地址](https://huggingface.co/Wangzaistone123/CodeLlama-13b-sql-lora) (202310) ,在spider评估集上的执行准确率达到0.789。    

#### 3.5.1 模型和微调权重合并
如果你需要将训练的基础模型和微调的Peft模块的权重合并，导出一个完整的模型。则运行如下模型导出脚本：  
```bash
poetry run sh ./dbgpt_hub/scripts/export_merge.sh
```
注意将脚本中的相关参数路径值替换为你项目所对应的路径。      


### 3.6、模型评估
对于模型在数据集上的效果评估,默认为在`spider`数据集上。
运行以下命令来：

```bash
poetry run python dbgpt_hub/eval/evaluation.py --plug_value --input  Your_model_pred_file
```
你可以在[这里](docs/eval_llm_result.md)找到我们最新的评估和实验结果。
**注意**： 默认的代码中指向的数据库为从[Spider官方网站](https://yale-lily.github.io/spider)下载的大小为95M的database，如果你需要使用基于Spider的[test-suite](https://github.com/taoyds/test-suite-sql-eval)中的数据库(大小1.27G)，请先下载链接中的数据库到自定义目录，并在上述评估命令中增加参数和值，形如`--db Your_download_db_path`。

## 四、发展路线    
整个过程我们会分为三个阶段：

* 阶段一:
  * 搭建基本框架，基于数个大模型打通从数据处理、模型SFT训练、预测输出和评估的整个流程，截止`20230804`我们已经整个打通。
  我们现在支持 
  - [x] CodeLlama
  - [x] Baichuan2 
  - [x] LLaMa/LLaMa2
  - [x] Falcon
  - [x] Qwen
  - [x] XVERSE
  - [x] ChatGLM2
  - [x] ChatGLM3
  - [x] internlm    
  - [x] sqlcoder-7b(mistral)
  - [x] sqlcoder2-15b(starcoder)
  
* 阶段二:
  - [x]  优化模型效果，支持更多不同模型进行不同方式的微调。截止`20231010`，我们已经完成对项目代码的重构，支持更多的模型。
  - [x] 对`prompt`优化
  - [x] 放出评估效果，和优化后的还不错的模型，并且给出复现教程(见我们微信公众号EosphorosAI)    
      
* 阶段三：
  - [ ] 推理速度优化提升
  - [ ] 业务场景和中文效果针对性优化提升
  - [ ] 基于更多论文进行优化，如`RESDSQL`等，结合我们社区的兄弟项目[Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL)进行更多的优化；  

  **如果你觉得我们的工作对你有那么点帮助，还请给我们个star鼓励下，我们会有更多动力去放出更多相关工作。**

## 五、贡献

欢迎更多小伙伴在数据集、模型微调、效果评测、论文推荐与复现等方面参与和反馈，如提issues或者pr反馈，我们会积极给出回应。提交代码前请先将代码按black格式化，运行下`black .`。

## 六、感谢

我们的工作主要是在众多开源工作的基础上开展的，非常感谢以下开源项目。

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
* [LLaMa-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning) 

非常感谢所有的contributors! 
 **20231104** ,尤其感谢 @[JBoRu](https://github.com/JBoRu) 提的[issue](https://github.com/eosphoros-ai/DB-GPT-Hub/issues/119)， 指出我们的之前按照官方网站的95M的数据库去评估的方式的不足，如论文《SQL-PALM: IMPROVED LARGE LANGUAGE MODEL ADAPTATION FOR TEXT-TO-SQL》 指出的 "We consider two commonly-used evaluation metrics: execution accuracy (EX) and test-suite accuracy (TS) [32]. EX measures whether SQL execution outcome matches ground truth (GT), whereas TS measures whether the SQL passes all EX evaluation for multiple tests, generated by database-augmentation. Since EX contains false positives, we consider TS as a more reliable evaluation metric" 。

## 七、引用
如果您觉得我们的项目对您的科研项目或者实际生产项目有帮助，请考虑在您的参考文献里引用`DB-GPT-Hub`:

```bibtex
@software{db-gpt-hub,
    author = {DB-GPT-Hub Team},
    title = {{DB-GPT-Hub}},
    url = {https://github.com/eosphoros-ai/DB-GPT-Hub},
    year = {2023}
}
```

## 八、Licence

The MIT License (MIT)

## 九、我们的联系方式
我们是一个社区一起合作，如果你对我们的社区工作有任何建议，随时可以联系我们。如果你对DB-GPT-Hub子项目的深入实验和优化感兴趣，可以联系微信群里的wangzai，我们欢迎大家共同努力，使它变得更好。
[![](https://dcbadge.vercel.app/api/server/7uQnPuveTY?compact=true&style=flat)](https://discord.gg/7uQnPuveTY)


[![Star History Chart](https://api.star-history.com/svg?repos=eosphoros-ai/DB-GPT-Hub&type=Date)](https://star-history.com/#eosphoros-ai/DB-GPT-Hub)
