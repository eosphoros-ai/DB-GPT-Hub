base_model="/data/models/chinese-roberta-wwm-ext"
# base_model="/data/models/gte-large-zh"

python main.py \
--dataset financial_report \
--dataset_dir ./datasets \
--base_model_name_or_path $base_model \
--per_device_train_batch_size 4096 \
--output_dir ./output \
--num_train_epochs 1000 \
--gradient_accumulation_steps 16 \
--learning_rate 0.001 \
--logging_steps 20 \
--eval_strategy "steps" \
--eval_steps 20 \
--save_steps 100 \
--do_train \
--do_eval