#!/bin/bash

python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json \
    
python predict.py \
    --model_name_or_path merged_model \

