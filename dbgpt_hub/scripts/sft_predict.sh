## shijian llama2 test
# CUDA_VISIBLE_DEVICES=0,1  python dbgpt_hub/predict/predict.py \
#     --model_name_or_path Llama-2-13b-chat-hf \
#     --template llama2 \
#     --finetuning_type lora \
#     --checkpoint_dir dbgpt_hub/output/adapter

# # wangzai baichua2_eval test
CUDA_VISIBLE_DEVICES=0 python dbgpt_hub/predict/predict.py \
    --model_name_or_path /home/model/Baichuan2-13B-Chat \
    --template baichuan2_eval \
    --quantization_bit 4 \
    --finetuning_type lora \
    --checkpoint_dir dbgpt_hub/output/adapter

