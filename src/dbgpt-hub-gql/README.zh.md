# DB-GPT-GQL:利用LLMs实现Text-to-GQL

## Baseline

- 更新日期: 2024/08/26

<table style="text-align: center;">
  <tr>
    <th style="text-align: center;">Language</th>
    <th style="text-align: center;">Dataset</th>
    <th style="text-align: center;">Model</th>
    <th>Method</th>
    <th>Similarity</th>
    <th>Grammar</th>
    <th>Execution</th>
  </tr>
  <tr >
    <td></td>
    <td></td>
    <td></td>
    <td>base</td>
    <td>0.674</td>
    <td>0.653</td>
    <td>0.037</td>
  </tr>
  <tr>
    <td>Cypher <a href="https://github.com/TuGraph-family/tugraph-db">(tugraph-db)</a></td>
    <td><a href="https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/text2gql/tugraph-db/tugraph-db.zip">TuGraph-DB Cypher数据集</a></td>
    <td><a href="https://huggingface.co/tugraph/CodeLlama-7b-Cypher-hf/tree/1.0">CodeLlama-7B-Instruct</a></td>
    <td>lora</td>
    <td>0.922</td>
    <td>0.987</td>
    <td>0.507</td>
  </tr>
  <tr >
    <td></td>
    <td></td>
    <td></td>
    <td>base</td>
    <td>0.493</td>
    <td>0.002</td>
    <td>none</td>
  </tr>
  <tr>
    <td>GQL<a href="https://github.com/TuGraph-family/tugraph-analytics">(tugraph-analytics)</a></td>
    <td><a href="https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/text2gql/tugraph-analytics/tugraph-analytics.zip">TuGraph-Analytics GQL数据集</a></td>
    <td><a href="https://huggingface.co/tugraph/CodeLlama-7b-GQL-hf/tree/1.1">CodeLlama-7B-Instruct</a></td>
    <td>lora</td>
    <td>0.935</td>
    <td>0.984</td>
    <td>none</td>
  </tr>
  <tr >
    <td></td>
    <td></td>
    <td></td>
    <td>base</td>
    <td>0.769</td>
    <td>0.703</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td>Cypher <a href="https://github.com/TuGraph-family/tugraph-db">(tugraph-db-example)</a></td>
    <td><a href="https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/text2gql/tugraph-db-example/tugraph-db-example.zip">TuGraph-DB Cypher数据集</a></td>
    <td><a href="https://huggingface.co/tugraph/CodeLlama-7b-Cypher-hf/tree/1.0">CodeLlama-7B-Instruct</a></td>
    <td>lora</td>
    <td>0.928</td>
    <td>0.946</td>
    <td>0.476</td>
  </tr>
</table>

## Contents
- [DB-GPT-GQL](#db-gpt-gql利用llms实现text-to-gql)
  - [Baseline](#baseline)
  - [Contents](#contents)
  - [一、简介](#一简介)
  - [二、Text-to-GQL微调](#二text-to-gql微调)
    - [2.1、数据集](#21数据集)
    - [2.2、基座模型](#22基座模型)
  - [三、使用方法](#三使用方法)
    - [3.1、环境准备](#31环境准备)
    - [3.2、模型准备](#32模型准备)
    - [3.3、模型微调](#33模型微调)
    - [3.4、模型预测](#34模型预测)
    - [3.5、模型评估](#35模型评估)
      - [3.5.1、文本相似度评估](#351文本相似度评估)
      - [3.5.2、语法正确性评估](#352语法正确性评估)
      - [3.5.3、执行结果一致性评估](#353执行结果一致性评估)
        - [3.5.3.1、tugraph-db](#3531tugraph-db)
    - [3.6、模型权重合并](#36模型权重合并)

# 一、简介

DB-GPT-GQL是一个面向图数据库查询语言的，利用LLMs实现Text-to-GQL翻译的模块。主要包含模型微调、Text-to-GQL预测，预测结果评估等步骤。关系型数据库领域的Text-to-SQL翻译任务发展至如今已经拥有了大量的数据集以及多维度的翻译结果评估流程。不同于已经逐渐成熟的Text-to-SQL翻译任务，Text-to-GQL翻译任务由于图查询语言缺乏统一规范、目标成为国际标准的ISOGQL尚未真正落地等原因，使得建立属于各类图查询语言的完整语料数据集和建立Text-to-GQL翻译结果评估机制成为了两个颇具挑战性的任务。

DB-GPT-GQL不仅支持了基于多个大模型的微调、预测流程，在翻译结果评估方面也提供了两种评估方式，第一种是基于翻译结果与标准答案之间近似程度的文本相似度评估，这一评估方式适用于任何图查询语言，第二种则是基于不同图查询语言的语法解析器对翻译结果进行语法解析的语法正确性评估，目前已支持tugraph-db与tugraph-analytics两个数据库的图查询语言。

未来DB-GPT-GQL将会实现基于翻译结果的执行计划正确性评估（不需要实际数据），以及更进一步的执行正确性评估（需要实际数据），并参考Text-to-SQL领域的spider数据集中的方法实现对数据集中查询语言复杂程度的分级。

## 二、Text-to-GQL微调

 我们基于大语言模型的SFT来提升Text-to-GQL的效果。

### 2.1、数据集

本项目样例数据集为`Cypher(tugraph-db-example)`，其中包含tugraph-db提供的，可在tugraph-db上可执行的185条语料，存放在`/dbgpt_hub_gql/data/tugraph-db-example`文件夹中，当前可使用的数据集如下：

- [Cypher(tugraph-db)](https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/text2gql/tugraph-db/tugraph-db.zip)： 符合tugraph-db的Cypher语法的数据集，采用“ [语法制导的语料生成策略](https://mp.weixin.qq.com/s/rZdj8TEoHZg_f4C-V4lq2A)”，将查询语言模板结合多样化的schema生成查询语言，并使用大模型泛化与之对应的自然语言问题描述后生成的语料。[语料生成框架](https://github.com/TuGraph-contrib/Awesome-Text2GQL)现已开源，欢迎参与共建。

- [GQL(tugraph-analytics)](https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/text2gql/tugraph-analytics/tugraph-analytics.zip)： 符合tugraph-analytics的GQL语法的数据集，采用“ [语法制导的语料生成策略](https://mp.weixin.qq.com/s/rZdj8TEoHZg_f4C-V4lq2A)”，将查询语言模板结合多样化的schema生成查询语言，并使用大模型泛化与之对应的自然语言问题描述后生成的语料。

请将下载并解压完成后的数据集放置在`/dbgpt_hub_gql/data/`目录下使用。

### 2.2、基座模型

DB-GPT-GQL目前已经支持的base模型有：

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
本章将以仓库中自带的`/dbgpt_hub_gql/data/tugraph-db-example`文件夹中共计185条语料以及`CodeLlama-7B-Instruct`（需要额外下载）为样例，展示DB-GPT-GQL的完整功能。

### 3.1、环境准备

```bash
# 克隆项目并创建 conda 环境
git clone https://github.com/eosphoros-ai/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub_gql python=3.10 
conda activate dbgpt_hub_gql

# 进入DB-GPT-GQL项目目录，并使用poetry安装依赖
cd src/dbgpt-hub-gql
pip install -e .

# 创建输出及日志目录
mkdir dbgpt_hub_gql/output
mkdir dbgpt_hub_gql/output/logs
mkdir dbgpt_hub_gql/output/pred
```

### 3.2、模型准备

创建`download.py`文件并将如下内容复制进入python文件中
```python
from modelscope import snapshot_download

model_dir = snapshot_download("AI-ModelScope/CodeLlama-7b-Instruct-hf", cache_dir='./')
```
使用download.py下载模型
```bash
# 安装python依赖并下载模型
pip install modelscope
python3 download.py

# 下载完成后，将AI-ModelScope/CodeLlama-7b-Instruct-hf重命名为codellama/CodeLlama-7b-Instruct-hf
mv ./AI-ModelScope ./codellama
```

### 3.3、模型微调
开始语料微调前需要手动将训练数据集在`./dbgpt_hub_gql/data/dataset_info.json`中注册，`./dbgpt_hub_gql/data/tugraph-db-example`文件夹中的训练数据集已经注册在其中，格式如下

```json
"tugraph_db_example_train": {
    "file_name": "./tugraph-db-example/train.json",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output",
      "history": "history"
    }
  }
```

在`dbgpt_hub_gql/scripts/train_sft.sh`中设置数据集，模型，以及微调结果输出路径，当前默认值适配`./dbgpt_hub_gql/data/tugraph-db-example`中的训练数据集以及`CodeLlama-7B-Instruct`模型，使用LoRA方法微调

```shell script
dataset="tugraph_db_example_train"
model_name_or_path=${model_name_or_path-"codellama/CodeLlama-7b-Instruct-hf"}
output_dir="dbgpt_hub_gql/output/adapter/CodeLlama-7b-gql-lora"
```

运行微调脚本，开始微调
```bash
sh dbgpt_hub_gql/scripts/train_sft.sh
```

### 3.4、模型预测

在`./dbgpt_hub_gql/scripts/predict_sft.sh`中设置需要预测的数据集，模型，模型微调结果路径以及预测结果路径，当前默认值适配`./dbgpt_hub_gql/data/tugraph-db-example`中的开发数据集以及LoRA方法微调后的`CodeLlama-7B-Instruct`模型

```shell script
CUDA_VISIBLE_DEVICES=0,1  python dbgpt_hub_gql/predict/predict.py \
    --model_name_or_path codellama/CodeLlama-7b-Instruct-hf \
    --template llama2 \
    --finetuning_type lora \
    --predicted_input_filename dbgpt_hub_gql/data/tugraph-db-example/dev.json \
    --checkpoint_dir dbgpt_hub_gql/output/adapter/CodeLlama-7b-gql-lora \
    --predicted_out_filename dbgpt_hub_gql/output/pred/tugraph_db_example_dev.txt >> ${pred_log}
```

运行预测脚本，获取预测结果

```bash
sh dbgpt_hub_gql/scripts/predict_sft.sh
```

### 3.5、模型评估

目前版本支持三种预测结果评估方法，第一种是基于Jaro–Winkler distance的文本相似度评估，第二种是基于`.g4`语法文件或图数据库现有语法解析器的语法正确性评估，第三种则是基于查询语句返回结果比较大的执行一致性评估。

#### 3.5.1、文本相似度评估

文本相似度评估直接统计预测结果与标准结果的Jaro–Winkler distance

```bash
python dbgpt_hub_gql/eval/evaluation.py  --input ./dbgpt_hub_gql/output/pred/tugraph_db_example_dev.txt --gold ./dbgpt_hub_gql/data/tugraph-db-example/dev.json --etype similarity
```

#### 3.5.2、语法正确性评估

`tugraph-db-example`是符合`tugraph-db`的LCypher语法规则的语料数据集，语法正确性评估使用ANTLR4工具，基于`./dbgpt_hub_gql/eval/evaluator/impl/tugraph-db/Lcypher.g4`文件生成了语法解析器，用于评估模型预测结果的语法正确性。

```bash
python dbgpt_hub_gql/eval/evaluation.py  --input ./dbgpt_hub_gql/output/pred/tugraph_db_example_dev.txt --gold ./dbgpt_hub_gql/data/tugraph-db-example/dev.json --etype grammar --impl tugraph-db
```

#### 3.5.3、执行结果一致性评估

当前版本仅支持tugraph-db上的执行结果一致性评估，暂未支持tugraph-analytics上的执行结果一致性评估。

##### 3.5.3.1、tugraph-db

执行结果一致性评估需要实际运行tugraph-db，方便起见可以下载tugraph官方提供的runtime镜像。

```bash
# 下载并解压tugraph执行测试数据集
wget -P ./dbgpt_hub_gql/eval/evaluator/impl/tugraph-db https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/text2gql/tugraph-db-server/datasets.zip

unzip -d ./dbgpt_hub_gql/eval/evaluator/impl/tugraph-db  ./dbgpt_hub_gql/eval/evaluator/impl/tugraph-db/datasets.zip

# 下载并启动tugraph的runtime镜像
docker pull tugraph/tugraph-runtime-centos7

docker run -it -v ./:/root/dbgpt-hub-gql --name=tugraph-db_evaluation tugraph/tugraph-runtime-centos7 /bin/bash

cd /root

# 安装 miniconda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh --no-check-certificate
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
source ~/miniconda3/bin/activate

# 准备运行环境
cd /root/dbgpt-hub-gql/
conda create -n dbgpt_hub_gql python=3.10 
conda activate dbgpt_hub_gql
pip install -e .

# 执行评测
python dbgpt_hub_gql/eval/evaluation.py  --input ./dbgpt_hub_gql/output/pred/tugraph_db_example_dev.txt --gold ./dbgpt_hub_gql/data/tugraph-db-example/dev.json --etype execution --impl tugraph-db
```



### 3.6、模型权重合并

如果你需要将训练的基础模型和微调的Peft模块的权重合并，导出一个完整的模型。则运行如下模型导出脚本：

```bash
sh dbgpt_hub_gql/scripts/export_merge.sh
```
