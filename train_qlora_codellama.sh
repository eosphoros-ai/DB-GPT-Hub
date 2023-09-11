#!/bin/bash

#python dbgpt_hub/utils/sql_data_process.py 

start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "


current_dir=$(pwd)
parent_dir=$(dirname $current_dir)

export PYTHONPATH=$PYTHONPATH:"../../../../.."
export PYTHONPATH=$PYTHONPATH:$parent_dir
export WANDB_DISABLED=true

echo $PYTHONPATH



model_dir=/root/autodl-tmp/CodeLlama-7b-hf
output_dir=/root/autodl-tmp/CodeLlama-7b-hf/output_pred


CUDA_VISIBLE_DEVICES=0,1 python ./dbgpt_hub/train/train_qlora.py \
    --model_name_or_path $model_dir \
    --output_dir $output_dir \
    --dataset_name spider \
    --use_auth \
    --logging_steps 10 \
    --save_strategy steps \
    --data_seed 42 \
    --save_steps 500 \
    --save_total_limit 40 \
    --evaluation_strategy steps \
    --max_eval_samples 1000 \
    --per_device_eval_batch_size 1 \
    --max_new_tokens 32 \
    --dataloader_num_workers 1 \
    --group_by_length \
    --logging_strategy steps \
    --remove_unused_columns False \
    --do_train \
    --lora_r 64 \
    --lora_alpha 16 \
    --double_quant \
    --quant_type nf4 \
    --bf16 \
    --bits 4 \
    --warmup_ratio 0.03 \
    --lr_scheduler_type constant \
    --gradient_checkpointing \
    --source_max_len 16 \
    --target_max_len 512 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --max_steps 1875 \
    --eval_steps 187 \
    --learning_rate 0.0002 \
    --adam_beta2 0.999 \
    --max_grad_norm 0.3 \
    --lora_dropout 0.1 \
    --weight_decay 0.0 \
    --seed 0 \
    2>&1 | tee $output_dir/log/log.txt
    
start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "
# python dbgpt_hub/utils/merge_peft_adapters.py
