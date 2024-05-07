wandb offline # Close wandb
# a100 ,单卡
current_date=$(date +"%Y%m%d_%H%M")
train_log="dbgpt_hub/output/logs/train_sft_test_${current_date}.log"
start_time=$(date +%s)
echo " Train Start time: $(date -d @$start_time +'%Y-%m-%d %H:%M:%S')" >>${train_log}

# default train , zero-shot,
num_shot=1

# one-shot train
# num_shot=1

dataset="example_text2sql_train"
if [ "$num_shot" -eq 1 ]; then
    dataset="example_text2sql_train_one_shot"
fi
# TODO(yeounoh) restore after enabling gemma-7b
model_name_or_path="google/gemma-7b" #"Your_download_CodeLlama-13b-Instruct-hf_path"
output_dir="dbgpt_hub/output/adapter/gemma-7b-1shot-col_type-sql-lora"

# the default param set could be run in a server with one a100(40G) gpu, if your server not support the set,you can set smaller param such as  lora_rank and use qlora with quant 4 eg...
# CUDA_VISIBLE_DEVICES=0 python dbgpt_hub/train/sft_train.py \
#     --model_name_or_path $model_name_or_path \
#     --do_train \
#     --dataset $dataset \
#     --max_source_length 2048 \
#     --max_target_length 512 \
#     --finetuning_type lora \
#     --lora_target q_proj,v_proj \
#     --template llama2 \
#     --lora_rank 64 \
#     --lora_alpha 32 \
#     --output_dir $output_dir \
#     --overwrite_cache \
#     --overwrite_output_dir \
#     --per_device_train_batch_size 1 \
#     --gradient_accumulation_steps 16 \
#     --lr_scheduler_type cosine_with_restarts \
#     --logging_steps 50 \
#     --save_steps 2000 \
#     --learning_rate 2e-4 \
#     --num_train_epochs 8 \
#     --plot_loss \
#     --bf16  >> ${train_log}
#     # --bf16#v100不支持bf16

# 多卡，deepseed启动，A100
deepspeed --num_gpus 8  dbgpt_hub/train/sft_train.py \
    --deepspeed dbgpt_hub/configs/ds_config.json \
    --quantization_bit 4 \
    --model_name_or_path $model_name_or_path \
    --do_train \
    --dataset $dataset \
    --max_source_length 2048 \
    --max_target_length 512 \
    --template mistral \
    --finetuning_type lora \
    --lora_rank 64 \
    --lora_alpha 32 \
    --lora_target q_proj,v_proj \
    --output_dir $output_dir \
    --overwrite_cache \
    --overwrite_output_dir \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --lr_scheduler_type cosine_with_restarts \
    --logging_steps 50 \
    --save_steps 2000 \
    --learning_rate 2e-4 \
    --num_train_epochs 9 \
    --plot_loss \
    2>&1 | tee ${train_log}

echo "############train end###############" >>${train_log}
echo "Train End time: $(date)" >>${train_log}
end_time=$(date +%s)
duration=$((end_time - start_time))
hours=$((duration / 3600))
min=$(( (duration % 3600) / 60))
echo "Time elapsed: ${hour}  hour $min min " >>${train_log}





# 多卡，deepseed，全量微调
# deepspeed --include localhost:4,5,6,7  dbgpt_hub/train/sft_train.py \
#     --dataset example_text2sql_train \
#     --model_name_or_path CodeLlama-7b-Instruct-hf \
#     --do_train \
#     --finetuning_type full \
#     --max_source_length 2048 \
#     --max_target_length 512 \
#     --template llama2 \
#     --output_dir dbgpt_hub/output/adapter/code-llama-7b-2048_epoch4_full \
#     --overwrite_cache \
#     --overwrite_output_dir \
#     --per_device_train_batch_size 4 \
#     --gradient_accumulation_steps 16 \
#     --lr_scheduler_type cosine_with_restarts \
#     --logging_steps 50 \
#     --learning_rate 2e-5 \
#     --num_train_epochs 4 \
#     --plot_loss \
#     --bf16 True\
#     --deepspeed dbgpt_hub/configs/stage3.json 2>&1 | tee ${train_log}
