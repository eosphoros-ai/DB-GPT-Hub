#!/bin/bash



python dbgpt_hub/utils/sql_data_process.py \
    --data_filepaths data/spider/dev.json \
    --output_file dev_sql.json 

start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "

CUDA_VISIBLE_DEVICES=2,3 python predict_qlora.py 

end_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "finished"
echo "[INFO] date:${end_time} "