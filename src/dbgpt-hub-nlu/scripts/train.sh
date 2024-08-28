base_model="/data/models/bge-large-zh-v1.5"
# base_model="/data/models/gte-large-zh"

python main.py \
--dataset financial_report \
--dataset_dir ./datasets \
--base_model_name_or_path $base_model \
--preprocess_batch_size 256 \
--per_device_train_batch_size 4096 \
--output_dir ./output \
--num_train_epochs 500 \
--gradient_accumulation_steps 16 \
--learning_rate 0.001 \
--logging_steps 100 \
--eval_strategy "steps" \
--eval_steps 50 \
--save_strategy "steps" \
--save_steps 50 \
--do_train \
--do_eval