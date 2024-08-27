# base_model="/data/models/chinese-roberta-wwm-ext"
base_model="/data/models/bge-large-zh-v1.5"

python main.py \
--dataset financial_report \
--dataset_dir ./datasets \
--base_model_name_or_path $base_model \
--preprocess_batch_size 64 \
--per_device_train_batch_size 1024 \
--output_dir ./output \
--do_infer \
--input_text "请问安泰集团在2021年的营业成本是多少元"
