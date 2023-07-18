#!/bin/bash

python src/sql_data_process.py 

python src/train/train_qlora.py \
    --output_dir ./adapter \
    --dataset spider \
    --do_train True \
    --do_eval False \
    --do_merge True \ 
    --source_max_len 384 \
    --target_max_len 128 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --logging_steps 2 \
    --max_steps 10 \
    --save_strategy steps \
    --data_seed 42 \
    --save_steps 1000 \
    --save_total_limit 40 \
    --evaluation_strategy steps \
    --eval_dataset_size 1024 \
    --max_eval_samples 1000 \
    --eval_steps 10 \
    --optim paged_adamw_32bit \

python src/utils/merge_peft_adapters.py
