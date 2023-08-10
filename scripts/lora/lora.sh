python dbgpt_hub/utils/sql_data_process.py 

start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "

CUDA_VISIBLE_DEVICES=3 python train_lora.py \
    --dataset_name spider \
    --model_name_or_path meta-llama/Llama-2-7b-hf \
    --output_dir adapter\lora \
    --num_train_epochs 1 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 250 \
    --max_steps 500 \
    --save_total_limit 5 \
    --learning_rate 0.0002 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --optim "adamw_torch" \
    --lora_r 8 \
    --lora_alpha 16 \
    --lora_dropout 0.1 \
    --lr_scheduler_type "constant" \
    --model_max_length 1024 \
    --logging_steps 20 \
    --do_train \
    --gradient_checkpointing True

end_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "finished"
echo "[INFO] date:${end_time} "
# python dbgpt_hub/utils/merge_peft_adapters.py
