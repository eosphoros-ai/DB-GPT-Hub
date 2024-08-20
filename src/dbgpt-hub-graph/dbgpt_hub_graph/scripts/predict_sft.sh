## shijian llama2 test

current_date=$(date +"%Y%m%d_%H%M")
pred_log="dbgpt_hub_gql/output/logs/pred_test_${current_date}.log"
start_time=$(date +%s)
echo " Pred Start time: $(date -d @$start_time +'%Y-%m-%d %H:%M:%S')" >>${pred_log}

# CUDA_VISIBLE_DEVICES=0,1  python dbgpt_hub_gql/predict/predict.py \
#     --model_name_or_path codellama/CodeLlama-7b-Instruct-hf \
#     --template llama2 \
#     --finetuning_type lora \
#     --predicted_input_filename dbgpt_hub_gql/data/tugraph-analytics/dev.json \
#     --checkpoint_dir dbgpt_hub_gql/output/adapter/CodeLlama-7b-gql-lora \
#     --predicted_out_filename dbgpt_hub_gql/output/pred/tugraph_analytics_dev.txt >> ${pred_log}

CUDA_VISIBLE_DEVICES=0,1  python dbgpt_hub_gql/predict/predict.py \
    --model_name_or_path codellama/CodeLlama-7b-Instruct-hf \
    --template llama2 \
    --finetuning_type lora \
    --predicted_input_filename dbgpt_hub_gql/data/tugraph-db-example/dev.json \
    --checkpoint_dir dbgpt_hub_gql/output/adapter/CodeLlama-7b-gql-lora \
    --predicted_out_filename dbgpt_hub_gql/output/pred/tugraph_db_dev.txt >> ${pred_log}

echo "############pred end###############" >>${pred_log}
echo "pred End time: $(date)" >>${pred_log}
end_time=$(date +%s)
duration=$((end_time - start_time))
hours=$((duration / 3600))
min=$(( (duration % 3600) / 60))
echo "Time elapsed: ${hour}  hour $min min " >>${pred_log}


# # wangzai baichua2_eval test
# CUDA_VISIBLE_DEVICES=0 python dbgpt_hub_gql/predict/predict.py \
#     --model_name_or_path /home/model/Baichuan2-13B-Chat \
#     --template baichuan2_eval \
#     --quantization_bit 4 \
#     --finetuning_type lora \
#     --checkpoint_dir dbgpt_hub_gql/output/adapter/baichuan2-13b-qlora 


## wangzai codellama2_pred test a100
# CUDA_VISIBLE_DEVICES=0,1  python dbgpt_hub_gql/predict/predict.py \
#     --model_name_or_path /home/model_files/codellama/CodeLlama-7b-Instruct-hf \
#     --template llama2 \
#     --finetuning_type lora \
#     --checkpoint_dir dbgpt_hub_gql/output/adapter/code_llama_7b-qlora