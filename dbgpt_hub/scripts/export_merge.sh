python dbgpt_hub/train/export_model.py \
    --model_name_or_path Your_base_model_path_like_Baichuan2-13B-Chat \
    --template Your_template_like_baichuan2_eval \
    --finetuning_type lora \
    --checkpoint_dir Your_ckpt_path_checkpoint-100 \
    --output_dir Your_export_model_like_output_merge_model_baichuan2-13b-qlora_merge \
    --fp16
    # --bf16
