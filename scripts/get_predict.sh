#!/bin/bash


python src/predict.py \
    --model_name_or_path model/vicuna-7b-delta-v1.3 \
    --checkpoint_dir adapter/checkpoint-7000 \
    --dataset_format spider \
    --dataset spider \
