# DB-GPT-NLU：开箱即用的文本理解大模型组件

适用于中文、英文在在零样本条件下进行文本理解任务，如信息抽取、文本分类等。

## 使用方法

### 环境准备

克隆项目并创建 conda 环境，
```bash
git clone https://github.com/eosphoros-ai/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub python=3.10 
conda activate dbgpt_hub
```

从源码安装 DB-GPT-NLU，

```bash
cd src/dbgpt-hub-nlu
pip install -e .
```

### 微调

```bash
# 假设后续使用 bge-large-zh-v1.5 作为基础模型
export base_model="/data/models/bge-large-zh-v1.5"

python main.py \
--dataset financial_report \
--dataset_dir ./datasets \
--base_model_name_or_path $base_model \
--preprocess_batch_size 64 \
--per_device_train_batch_size 1024 \
--output_dir ./output \
--num_train_epochs 5 \
--gradient_accumulation_steps 16 \
--learning_rate 0.001 \
--logging_steps 100 \
--eval_strategy "steps" \
--eval_steps 100 \
--save_strategy "steps" \
--save_steps 200 \
--do_train \
--do_eval
```

### 评估

```bash
python main.py \
--dataset financial_report \
--dataset_dir ./datasets \
--base_model_name_or_path $base_model \
--preprocess_batch_size 64 \
--per_device_train_batch_size 1024 \
--output_dir ./output \
--do_eval
```

### 推理

```bash
python main.py \
--dataset financial_report \
--dataset_dir ./datasets \
--base_model_name_or_path $base_model \
--preprocess_batch_size 64 \
--per_device_train_batch_size 1024 \
--output_dir ./output \
--do_infer \
--input_text "请问安泰集团在2021年的营业成本是多少元"
```

## 参与贡献

提交 PR 或 Issue。

提交代码之前请执行下面命令格式化代码，

```bash
make fmt
```