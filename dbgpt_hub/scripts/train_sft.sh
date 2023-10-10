wandb offline
# v100 ,单卡
CUDA_VISIBLE_DEVICES=0 python dbgpt_hub/train/sft_train.py \
    --quantization_bit 4 \
    --model_name_or_path /home/model/Baichuan2-13B-Chat \
    --do_train \
    --dataset example_text2sql \
    --max_source_length 1024 \
    --max_target_length 512 \
    --template baichuan2 \
    --finetuning_type lora \
    --lora_rank 32 \
    --lora_alpha 8 \
    --lora_target W_pack \
    --output_dir dbgpt_hub/output/adapter/baichuan2-13b-qlora \
    --overwrite_cache \
    --overwrite_output_dir \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine_with_restarts \
    --logging_steps 10 \
    --save_steps 10 \
    --learning_rate 5e-5 \
    --num_train_epochs 0.2 \
    --plot_loss 
    # --bf16#v100不支持bf16
    # test  num_train_epochs set to 0.1

# 多卡，deepseed启动，A100
# deepspeed --num_gpus 2  dbgpt_hub/train/sft_train.py \
#     --deepspeed dbgpt_hub/configs/ds_config.json \
#     --quantization_bit 4 \
#     --model_name_or_path /home/model_files/Llama-2-13b-chat-hf \
#     --do_train \
#     --dataset example_text2sql_train \
#     --max_source_length 1024 \
#     --max_target_length 512 \
#     --template llama2 \
#     --finetuning_type lora \
#     --lora_rank 64 \
#     --lora_alpha 32 \
#     --lora_target q_proj,v_proj \
#     --output_dir dbgpt_hub/output/adapter/llama2-13b-qlora_1024_epoch1_debug1008_withDeepseed_mulitCard \
#     --overwrite_cache \
#     --overwrite_output_dir \
#     --per_device_train_batch_size 1 \
#     --gradient_accumulation_steps 16 \
#     --lr_scheduler_type cosine_with_restarts \
#     --logging_steps 25 \
#     --save_steps 20 \
#     --learning_rate 2e-4 \
#     --num_train_epochs 0.1 \
#     --plot_loss \
#     --bf16