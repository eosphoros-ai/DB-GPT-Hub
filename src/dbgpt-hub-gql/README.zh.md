# DB-GPT-GQL

适用于中文、英文在在零样本条件下进行文本理解任务，如信息抽取、文本分类等。

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
语法正确性评估

```bash
poetry run python dbgpt_hub_graph/eval/evaluation.py  --input ./dbgpt_hub_graph/output/pred/tugraph_analytics_dev.txt --gold ./dbgpt_hub_graph/data/tugraph-analytics/gold_dev.txt --etype grammar --impl tugraph_analytics
```

### 权重合并
```bash
poetry run sh ./dbgpt_hub_gql/scripts/export_merge.sh
```


## 参与贡献

提交 PR 或 Issue。

提交代码之前请执行下面命令格式化代码，

```bash
make fmt
```