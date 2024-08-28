
START_INDEX=0 CUDA_VISIBLE_DEVICES=0 python ./dbgpt_hub_nlu/ner.py \
--base_model_name_or_path Qwen/Qwen2-1.5B-Instruct \
--dataset intent \
--adapter_name_or_path


