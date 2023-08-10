#!/bin/bash


# prepare dev data
python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json \

start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "

# get lora predict 
CUDA_VISIBLE_DEVICES=3 python ./predict_lora.py 

end_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "finished"
echo "[INFO] date:${end_time} "