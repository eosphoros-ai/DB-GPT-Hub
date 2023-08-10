#!/bin/bash
start_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "[INFO] date:${start_time} "


CUDA_VISIBLE_DEVICES=4,5 python ./predict_no_peft_llama2_13b_hf_new.py

end_time=`date +"%Y-%m-%d %H:%M:%S"`
echo "finished"
echo "[INFO] date:${end_time} "
