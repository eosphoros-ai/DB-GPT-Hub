python dbgpt_hub/train/export_model.py \
    --model_name_or_path /home/model/Baichuan2-13B-Chat \
    --template baichuan2_eval \
    --finetuning_type lora \
    --checkpoint_dir dbgpt_hub/output/adapter/baichuan2-13b-qlora/checkpoint-100 \
    --output_dir dbgpt_hub/output/merge_model/baichuan2-13b-qlora_merge \
    --fp16
    # --bf16
