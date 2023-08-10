python dbgpt_hub/utils/sql_data_process.py 

python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json 

start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "

CUDA_VISIBLE_DEVICES=0 torchrun --nproc_per_node=1 train_lora.py \
    --model_name_or_path meta-llama/Llama-2-7b-hf \
    --data_path sql_finetune_data.json \
    --output_dir adapter \
    --num_train_epochs 3 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 500 \
    --save_total_limit 5 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --optim "adamw_torch" \
    --lr_scheduler_type "cosine" \
    --model_max_length 2048 \
    --logging_steps 1 \
    --do_train \
    --do_eval \
    --gradient_checkpointing True \
    --deepspeed "scripts/ds_config/zero3_auto.json"

end_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "finished"
echo "[INFO] date:${end_time} "
    
# python dbgpt_hub/utils/merge_peft_adapters.py