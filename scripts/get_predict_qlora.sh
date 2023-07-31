#!/bin/bash


CUDA_VISIBLE_DEVICES=2,3 python ./../predict_qlora.py \
    --model_name_or_path model/vicuna-7b-delta-v1.3 \
    --checkpoint_dir adapter/checkpoint-7000 \
    --dataset_format spider \
    --dataset spider \
