# llama2 series
python dbgpt_hub/train/export_model.py \
    --model_name_or_path /home/LLM/CodeLlama-13b-Instruct-hf \
    --template llama2 \
    --finetuning_type lora \
    --checkpoint_dir dbgpt_hub/output/adapter/CodeLlama-13b-sql-lora \
    --output_dir dbgpt_hub/output/codellama-13b-sql-sft \
    --fp16


## Baichuan2
# python dbgpt_hub/train/export_model.py \
#     --model_name_or_path Your_base_model_path_like_Baichuan2-13B-Chat \
#     --template Your_template_like_baichuan2_eval \
#     --finetuning_type lora \
#     --checkpoint_dir Your_ckpt_path_checkpoint-100 \
#     --output_dir Your_export_model_like_output_merge_model_baichuan2-13b-qlora_merge \
#     --fp16
#     # --bf16