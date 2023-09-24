CUDA_VISIBLE_DEVICES=0,1  python dbgpt_hub/predict/predict.py \
    --model_name_or_path Llama-2-13b-chat-hf \
    --template llama2 \
    --finetuning_type lora \
    --checkpoint_dir dbgpt_hub/output/adapter