#!/bin/bash

start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "
# current_dir=$(pwd)
# parent_dir=$(dirname $current_dir)

# python dbgpt_hub/utils/sql_data_process.py \
#     --data_filepaths data/spider/dev.json \
#     --output_file dev_sql.json 

# start_time=`date +"%Y-%m-%d %H:%M:%S"`
# echo "[INFO] date:${start_time} "


export PYTHONPATH=$PYTHONPATH:/home/LLM/code_llama09/DB-GPT-Hub


model_dir=/home/model_files/codellama/CodeLlama-7b-Instruct-hf


CUDA_VISIBLE_DEVICES=2,3 python dbgpt_hub/predict/predict_qlora_nf4_bit4.py 

    # --base_model_name_or_path model_dir \
    # --peft_ckpt_path output_pred/qlora_bit4/checkpoint-500 \
    # --input_data_json dev_sql.json \
    # --output_name output_pred/qlora_bit4/pred/qlora_64_nf4_bit4.sql

end_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "finished"
echo "[INFO] date:${end_time} "