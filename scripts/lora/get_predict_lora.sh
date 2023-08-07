#!/bin/bash

# prepare dev data
python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json \

# get lora predict 
# CUDA_VISIBLE_DEVICES=3
python predict_lora.py \


