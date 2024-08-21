# DB-GPT-GQL

DB-GPT-GQL是一个面向图数据库查询语言的，利用LLMs实现Text-to-GQL翻译的模块。主要包含模型微调、Text-to-GQL推理，推理结果评估等步骤。关系型数据库领域的Text-to-SQL翻译任务发展至如今已经拥有了大量的数据集以及多维度的翻译结果评估流程。不同于已经逐渐成熟的Text-to-SQL翻译任务，Text-to-GQL翻译任务由于图查询语言缺乏统一规范、目标成为国际标准的ISOGQL尚未真正落地等原因，使得建立属于各类图查询语言的完整语料数据集和建立Text-to-GQL翻译结果评估机制成为了两个颇具挑战性的任务。

DB-GPT-GQL不仅支持了基于多个大模型的微调、推理流程，在翻译结果评估方面也提供了两种评估方式，第一种是基于翻译结果与标准答案之间近似程度的文本相似度评估，这一评估方式适用于任何图查询语言，第二种则是基于不同图查询语言的语法解析器对翻译结果进行语法解析的语法正确性评估，目前已支持tugraph-db与tugraph-analytics两个数据库的图查询语言。

未来DB-GPT-GQL将会实现基于翻译结果的执行计划正确性评估（不需要实际数据），以及更进一步的执行正确性评估（需要实际数据），并参考Text-to-SQL领域的spider数据集中的方法实现对数据集中查询语言复杂程度的分级。

## Baseline
<table style="text-align: center;">
  <tr>
    <th style="text-align: center;">Language</th>
    <th style="text-align: center;">Model</th>
    <th>Method</th>
    <th>Similarity</th>
    <th>Grammar</th>
  </tr>
  <tr >
    <td></td>
    <td></td>
    <td>base</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>tugraph-db</td>
    <td>CodeLlama-7B-Instruct</td>
    <td>lora</td>
    <td>0.901</td>
    <td>0.892</td>
  </tr>
  <tr >
    <td></td>
    <td></td>
    <td>base</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>tugraph-analytics</td>
    <td>CodeLlama-7B-Instruct</td>
    <td>lora</td>
    <td>0.934</td>
    <td>0.990</td>
  </tr>
</table>

## 快速开始
本章将以仓库中自带的`/dbgpt_hub_gql/data/tugraph-db-example`文件夹中共计185条语料以及`CodeLlama-7B-Instruct`（需要额外下载）为样例，展示DB-GPT-GQL的完整功能。

### 环境准备

克隆项目并创建 conda 环境，
```bash
git clone https://github.com/eosphoros-ai/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub python=3.10 
conda activate dbgpt_hub
pip install poetry
poetry install
```

进入DB-GPT-GQL项目目录，并使用poetry安装依赖
```bash
cd src/dbgpt-hub-gql
pip install poetry
poetry install
```

### 模型下载
创建并进入codellama模型存放目录
```bash
mkdir codellama
cd ./codellama
```

在`codellama`文件夹下创建`download.py`文件并将如下内容复制进入python文件中
```python
from modelscope import snapshot_download

model_dir = snapshot_download("AI-ModelScope/CodeLlama-7b-Instruct-hf")
```

安装python依赖并下载模型
```bash
pip install modelscope
python3 download.py
```

下载完成后，将模型文件软链接到`codellama`目录下
```bash
ln -s /root/.cache/modelscope/hub/AI-ModelScope/CodeLlama-7b-Instruct-hf ./
```

### 微调
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
poetry run sh dbgpt_hub_gql/scripts/train_sft.sh
```

### 推理

在`./dbgpt_hub_gql/scripts/predict_sft.sh`中设置需要推理的数据集，模型，模型微调结果路径以及推理结果路径，当前默认值适配`./dbgpt_hub_gql/data/tugraph-db-example`中的开发数据集以及LoRA方法微调后的`CodeLlama-7B-Instruct`模型

```shell script
CUDA_VISIBLE_DEVICES=0,1  python dbgpt_hub_gql/predict/predict.py \
    --model_name_or_path codellama/CodeLlama-7b-Instruct-hf \
    --template llama2 \
    --finetuning_type lora \
    --predicted_input_filename dbgpt_hub_gql/data/tugraph-db-example/dev.json \
    --checkpoint_dir dbgpt_hub_gql/output/adapter/CodeLlama-7b-gql-lora \
    --predicted_out_filename dbgpt_hub_gql/output/pred/tugraph_db_example_dev.txt >> ${pred_log}
```

运行推理脚本，获取推理结果

```bash
poetry run sh ./dbgpt_hub_gql/scripts/predict_sft.sh
```

### 评估

目前版本支持两种预测结果评估方法，第一种是基于Jaro–Winkler distance的文本相似度评估，第二种是基于`.g4`语法文件或图数据库现有语法解析器的语法正确性评估。

#### 文本相似度评估

文本相似度评估直接统计推理结果与标准结果的Jaro–Winkler distance

```bash
poetry run python dbgpt_hub_gql/eval/evaluation.py  --input ./dbgpt_hub_gql/output/pred/tugraph_db_example_dev.txt --gold ./dbgpt_hub_gql/data/tugraph-db-example/gold_dev.txt --etype similarity
```

#### 语法正确性评估

`./dbgpt_hub_gql/data/tugraph-db-example`是符合`tugraph-db`的LCypher语法规则的语料数据集，语法正确性评估使用ANTLR4工具，基于`./dbgpt_hub_gql/eval/evaluator/impl/tugraph-db/Lcypher.g4`文件生成了语法解析器，用于评估模型推理结果的语法正确性。

```bash
poetry run python dbgpt_hub_gql/eval/evaluation.py  --input ./dbgpt_hub_gql/output/pred/tugraph_db_example_dev.txt --gold ./dbgpt_hub_gql/data/tugraph-db-example/gold_dev.txt --etype grammar --impl tugraph-db
```

### 权重合并

如果你需要将训练的基础模型和微调的Peft模块的权重合并，导出一个完整的模型。则运行如下模型导出脚本：

```bash
poetry run sh ./dbgpt_hub_gql/scripts/export_merge.sh
```

## 数据集

当前版本提供了`tugraph-db`与`tugraph-analytics`两个数据库的语料数据集，下载方式如下，下载完成后可以参考快速开始中的样例修改运行参数并完成微调->推理->评估的流程

### 数据集下载

#### tugraph-analytics
在当前文档所在的目录下执行以下命令
```bash
cd ./dbgpt_hub_gql/data
wget https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/text2gql/tugraph-analytics/tugraph-analytics.zip
unzip tugraph-analytics.zip
rm -f ./tugraph-analytics.zip 
cd ../..
```

## 参与贡献

欢迎更多小伙伴在数据集、模型微调、效果评测、论文推荐与复现等方面参与和反馈，如提issues或者pr反馈，我们会积极给出回应。提交代码前请先将代码按black格式化，运行下black。