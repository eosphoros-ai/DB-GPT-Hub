# Environment preparation
Be consistent with the README.md document

# Data preprocessing
Be consistent with the README.md document

# Model fine-tuning
```python
# first set model_dir and output_dir in train_qlora_codellama.sh
model_dir=/root/autodl-tmp/CodeLlama-7b-hf
output_dir=/root/autodl-tmp/CodeLlama-7b-hf/output_pred

# second set DATA_PATH in dbgpt_hub/configs/config.py, data_info.yml is saved here
DATA_PATH = "/root/autodl-tmp/data/spider/pre_processed_data"

# then train with qlora method
sh train_qlora_codellama.sh
```