# base_model="/data/models/chinese-roberta-wwm-ext"
base_model="/data/models/gte-large-zh"

python main.py \
--base_model_name_or_path $base_model \
--per_device_train_batch_size 4096 \
--model_name_or_path ./output \
--do_infer \
--input_text "请问安泰集团在2021年的营业成本是多少元"                     

