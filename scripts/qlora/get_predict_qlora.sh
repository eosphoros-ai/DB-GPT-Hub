#!/bin/bash

python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json \

CUDA_VISIBLE_DEVICES=2,3 python ./../predict_qlora.py \

