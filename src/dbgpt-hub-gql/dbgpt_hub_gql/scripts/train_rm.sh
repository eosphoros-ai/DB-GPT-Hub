wandb offline # Close wandb
# a100 ,单卡
current_date=$(date +"%Y%m%d_%H%M")
train_log="dbgpt_hub_gql/output/logs/train_sft_test_${current_date}.log"
start_time=$(date +%s)
echo " Train Start time: $(date -d @$start_time +'%Y-%m-%d %H:%M:%S')" >>${train_log}

# the default param set could be run in a server with one a100(40G) gpu, if your server not support the set,you can set smaller param such as  lora_rank and use qlora with quant 4 eg...
deepspeed --num_gpus 4  dbgpt_hub_gql/train/rm_train.py \
    --deepspeed dbgpt_hub_gql/configs/ds_config.json \
    --stage rm \
    --model_name_or_path /home/CPF/LLM/qwen-7b-chat \
    --do_train \
    --dataset example_rm_train \
    --max_source_length 1024 \
    --max_target_length 512 \
    --finetuning_type lora \
    --lora_target c_attn \
    --template chatml \
    --lora_rank 64 \
    --lora_alpha 32 \
    --output_dir dbgpt_hub_gql/output/adapter/qwen-7b-rm-test \
    --overwrite_cache \
    --overwrite_output_dir \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --lr_scheduler_type cosine_with_restarts \
    --logging_steps 50 \
    --save_steps 2000 \
    --learning_rate 1e-6 \
    --num_train_epochs 0.05 \
    --plot_loss True \
    --quantization_bit 4 >> ${train_log}
    # --bf16  
    # --bf16#v100不支持bf16
    
echo "############train end###############" >>${train_log}
echo "Train End time: $(date)" >>${train_log}
end_time=$(date +%s)
duration=$((end_time - start_time))
hours=$((duration / 3600))
min=$(( (duration % 3600) / 60))
echo "Time elapsed: ${hour}  hour $min min " >>${train_log}