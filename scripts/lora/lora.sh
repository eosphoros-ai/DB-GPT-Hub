python dbgpt_hub/utils/sql_data_process.py 

python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json \
    
python train_lora.py \
    --dataset_name spider \
    --output_dir adapter \
    --num_train_epochs 3 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 500 \
    --save_total_limit 5 \
    --learning_rate 0.0001 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --optim "adamw_torch" \
    --lr_scheduler_type "cosine" \
    --model_max_length 1024 \
    --logging_steps 1 \
    --do_train \
    --gradient_checkpointing True

python dbgpt_hub/utils/merge_peft_adapters.py