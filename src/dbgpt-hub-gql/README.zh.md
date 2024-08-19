# DB-GPT-GQL

适用于中文、英文在在零样本条件下进行文本理解任务，如信息抽取、文本分类等。

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
    <td>tugraph-analytics</td>
    <td>CodeLlama-7B-Instruct</td>
    <td>lora</td>
    <td>0.934</td>
    <td>0.990</td>
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
</table>

## 使用方法

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

### 微调

```bash
poetry run sh dbgpt_hub_gql/scripts/train_sft.sh
```

### 推理

```bash
poetry run sh ./dbgpt_hub_gql/scripts/predict_sft.sh
```

### 评估
文本相似度评估

```bash
poetry run python dbgpt_hub_gql/eval/evaluation.py  --input ./dbgpt_hub_gql/output/pred/tugraph_analytics_dev.txt --gold ./dbgpt_hub_gql/data/tugraph-analytics/gold_dev.txt --etype similarity --impl tugraph_analytics
```

语法正确性评估
```bash
poetry run python dbgpt_hub_gql/eval/evaluation.py  --input ./dbgpt_hub_gql/output/pred/tugraph_analytics_dev.txt --gold ./dbgpt_hub_gql/data/tugraph-analytics/gold_dev.txt --etype grammar --impl tugraph-analytics
```

### 权重合并
```bash
poetry run sh ./dbgpt_hub_gql/scripts/export_merge.sh
```


## 参与贡献

欢迎更多小伙伴在数据集、模型微调、效果评测、论文推荐与复现等方面参与和反馈，如提issues或者pr反馈，我们会积极给出回应。提交代码前请先将代码按black格式化，运行下black。