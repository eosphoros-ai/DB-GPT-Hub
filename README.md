# DB-GPT-Hub: Text-to-SQL parsing with LLMs

[**简体中文**](README.zh.md) |[**Discord**](https://discord.gg/FMGwbRQrM)|[**Wechat**](https://github.com/eosphoros-ai/DB-GPT/blob/main/README.zh.md#%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC)|[**Huggingface**](https://huggingface.co/eosphoros)

## Contents
- [1. Introduction](#1-what-is-db-gpt-hub)
- [2. Text2SQL Finetune](#2-fine-tuning-text-to-sql)
  - [2.1 Dataset](#21-dataset)
  - [2.2 BaseModel](#22-model)
  - [2.3 Finetune methods](#23-fine-tuning-methods)
- [3. Usage](#3-usage)
  - [3.1 Environment preparation](#31-environment-preparation)
  - [3.2 Data preparation](#32-data-preparation)
  - [3.3 Model fine-tuning](#33-model-fine-tuning)
  - [3.4 Model Predict](#34-model-predict)
  - [3.5 Model Weights](#35-model-weights)
  - [3.6 Model Evaluation](#36-model-evaluation)
- [4. roadmap](#4-roadmap)
- [5. contributions](#5-contributions)
- [6. acknowledgements](#6-acknowledgements)

## 1. What is DB-GPT-Hub

DB-GPT-Hub is an experimental project utilizing LLMs (Large Language Models) to achieve Text-to-SQL parsing. The project primarily encompasses data collection, data preprocessing, model selection and building, and fine-tuning of weights. Through this series of processes, we aim to enhance Text-to-SQL capabilities while reducing the model training costs, allowing more developers to contribute to the improvement of Text-to-SQL accuracy. Our ultimate goal is to realize automated question-answering capabilities based on databases, enabling users to execute complex database queries through natural language descriptions.    

So far, we have successfully integrated multiple large models and established a complete workflow, including data processing, model SFT (Supervised Fine-Tuning) training, prediction output, and evaluation. The code is readily reusable within this project.    

As of October 10, 2023, by fine-tuning an open-source model of 13 billion parameters using this project, **the execution accuracy on the Spider evaluation dataset has surpassed that of GPT-4!**  

Part of the experimental results have been compiled into the [document](docs/eval_llm_result.md) in this project. By utilizing this project and combining more related data, the execution accuracy on the Spider evaluation set has already reached **0.825**.

## 2. Fine-tuning Text-to-SQL

We enhance the Text-to-SQL performance by applying Supervised Fine-Tuning (SFT) on large language models.   

### 2.1. Dataset

The primary dataset for this project's examples is the **Spider** dataset:

- [SPIDER](https://yale-lily.github.io/spider): A complex text2sql dataset across domains, containing 10,181 natural language queries, 5,693 SQL distributed across 200 separate databases, covering 138 different domains.[download link](https://drive.google.com/uc?export=download&id=1TqleXec_OykOYFREKKtschzY29dUcVAQ)  

Other text2sql datasets available:   

- [WikiSQL:](https://github.com/salesforce/WikiSQL) A large semantic parsing dataset consisting of 80,654 natural statement expressions and sql annotations of 24,241 tables. Each query in WikiSQL is limited to the same table and does not contain complex operations such as sorting, grouping The queries in WikiSQL are limited to the same table and do not include complex operations such as sorting, grouping, subqueries, etc.
- [CHASE](https://xjtu-intsoft.github.io/chase/): A cross-domain multi-round interactive text2sql Chinese dataset containing a list of 5,459 multi-round questions consisting of 17,940 <query, SQL> binary groups across 280 different domain databases.
- [BIRD-SQL:](https://bird-bench.github.io/) A large-scale cross-domain text-to-SQL benchmark in English, with a particular focus on large database content. The dataset contains 12,751 text-to-SQL data pairs and 95 databases with a total size of 33.4 GB across 37 occupational domains. The BIRD-SQL dataset bridges the gap between text-to-SQL research and real-world applications by exploring three additional challenges, namely dealing with large and messy database values, external knowledge inference and optimising SQL execution efficiency.
- [CoSQL:](https://yale-lily.github.io/cosql) A corpus for building cross-domain conversational text-to-SQL systems. It is a conversational version of the Spider and SParC tasks. CoSQL consists of 30k+ rounds and 10k+ annotated SQL queries from Wizard-of-Oz's collection of 3k conversations querying 200 complex databases across 138 domains. Each conversation simulates a realistic DB query scenario in which a staff member explores the database as a user and a SQL expert uses SQL to retrieve answers, clarify ambiguous questions, or otherwise inform.

- Following the processing template of [NSQL](https://github.com/NumbersStationAI/NSQL), the dataset underwent basic processing, yielding approximately [20K dataset](https://huggingface.co/datasets/Healthy13/Text2SQL/tree/main)



### 2.2. Model

DB-GPT-Hub currently supports the following base models:

  - [x] CodeLlama
  - [x] Baichuan2 
  - [x] LLaMa/LLaMa2
  - [x] Falcon
  - [x] Qwen
  - [x] XVERSE
  - [x] ChatGLM2
  - [x] internlm


The model is fine-tuned based on a quantization bit of 4 using Quantized Learning over Redundant Architecture (QLoRA). The minimum hardware requirements for this can be referred to as follows:   

| Model Parameters | GPU RAM         | CPU RAM | DISK   |
| -------- | --------------- | ------- | ------ |
| 7b       | 6GB | 3.6GB   | 36.4GB |
| 13b      | 13.4GB | 5.9GB   | 60.2GB | 
  
All the related parameters are set to the minimum, with a batch size of 1 and max length of 512. Based on experience, for better performance, it is recommended to set the related length values to 1024 or 2048.


## 3. Usage

### 3.1. Environment preparation

```
git clone https://github.com/eosphoros-ai/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub python=3.10 
conda activate dbgpt_hub
pip install -r requirements.txt 
mkdir model 
```

### 3.2. Data preparation

DB-GPT-Hub uses the information matching generation method for data preparation, i.e. the SQL + Repository generation method that combines table information. This method combines data table information to better understand the structure and relationships of the data table, and is suitable for generating SQL statements that meet the requirements.  

Download the [Spider dataset]((https://drive.google.com/uc?export=download&id=1TqleXec_OykOYFREKKtschzY29dUcVAQ)) from the Spider dataset link. By default, after downloading and extracting the data, place it in the dbgpt_hub/data directory, i.e., the path should be `dbgpt_hub/data/spider`.  

For the data preprocessing part, simply **run the following script** :
```bash
## generate train and dev(eval) data
sh dbgpt_hub/scripts/gen_train_eval_data.sh
```

In the directory `dbgpt_hub/data/`, you will find the newly generated training file example_text2sql_train.json and testing file example_text2sql_dev.json, containing 8659 and 1034 entries respectively.


The data in the generated JSON looks something like this:
```
    {
        "db_id": "department_management",
        "instruction": "I want you to act as a SQL terminal in front of an example database, you need only to return the sql command to me.Below is an instruction that describes a task, Write a response that appropriately completes the request.\n\"\n##Instruction:\ndepartment_management contains tables such as department, head, management. Table department has columns such as Department_ID, Name, Creation, Ranking, Budget_in_Billions, Num_Employees. Department_ID is the primary key.\nTable head has columns such as head_ID, name, born_state, age. head_ID is the primary key.\nTable management has columns such as department_ID, head_ID, temporary_acting. department_ID is the primary key.\nThe head_ID of management is the foreign key of head_ID of head.\nThe department_ID of management is the foreign key of Department_ID of department.\n\n",
        "input": "###Input:\nHow many heads of the departments are older than 56 ?\n\n###Response:",
        "output": "SELECT count(*) FROM head WHERE age  >  56",
        "history": []
    }, 
```  


### 3.3. Model fine-tuning

The model fine-tuning supports both LoRA and QLoRA methods. We can run the following command to fine-tune the model. By default, with the parameter --quantization_bit, it uses the QLoRA fine-tuning method. To switch to LoRAs, simply remove the related parameter from the script.
Run the command:

```bash
sh dbgpt_hub/scripts/train_sft.sh
```

After fine-tuning, the model weights will be saved by default in the adapter folder, specifically in the dbgpt_hub/output/adapter directory.   

If you're using **multi-GPU training and want to utilize deepseed**, you should modify the default content in train_sft.sh. The change  is:

```
CUDA_VISIBLE_DEVICES=0 python dbgpt_hub/train/sft_train.py \
    --quantization_bit 4 \
    ...
```    
change to ： 
```
deepspeed --num_gpus 2  dbgpt_hub/train/sft_train.py \
    --deepspeed dbgpt_hub/configs/ds_config.json \
    --quantization_bit 4 \
    ...
```    

The other parts that are omitted (…) can be kept consistent. If you want to change the default deepseed configuration, go into the `dbgpt_hub/configs` directory and make changes to ds_config.json as needed.   

In the script, during fine-tuning, different models correspond to key parameters lora_target and template, as shown in the following table:   

| model name                                                   |  lora_target           | template |
| -------------------------------------------------------- |  ----------------- |----------|
| [LLaMA-2](https://huggingface.co/meta-llama)             |  q_proj,v_proj     | llama2   |
| [CodeLlama-2](https://huggingface.co/codellama/)             |  q_proj,v_proj     | llama2   |
| [Baichuan2](https://github.com/baichuan-inc/Baichuan2)   |  W_pack            | baichuan2 |
| [InternLM](https://github.com/InternLM/InternLM)         | q_proj,v_proj     | intern   |
| [Qwen](https://github.com/QwenLM/Qwen-7B)                | c_attn            | chatml   |
| [XVERSE](https://github.com/xverse-ai/XVERSE-13B)        | q_proj,v_proj     | xverse   |
| [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B)         | query_key_value   | chatglm2 |
| [LLaMA](https://github.com/facebookresearch/llama)       |  q_proj,v_proj     | -        |
| [BLOOM](https://huggingface.co/bigscience/bloom)         |  query_key_value   | -        |
| [BLOOMZ](https://huggingface.co/bigscience/bloomz)       |  query_key_value   | -        |
| [Baichuan](https://github.com/baichuan-inc/baichuan-13B) | W_pack            | baichuan |
| [Falcon](https://huggingface.co/tiiuae/falcon-7b)        | query_key_value   | -        |

 In `train_sft.sh` , other key parameters are as follows:

 > quantization_bit: Indicates whether quantization is applied, with valid values being [4 or 8].   
> model_name_or_path: The path of the LLM (Large Language Model).   
> dataset: Specifies the name of the training dataset configuration, corresponding to the outer key value in dbgpt_hub/data/dataset_info.json, such as example_text2sql.  
> max_source_length: The length of the text input into the model. If computing resources allow, it can be set as large as possible, like 1024 or 2048.      
> max_target_length: The length of the SQL content output by the model; 512 is generally sufficient.   
> output_dir: The output path of the Peft module during SFT (Supervised Fine-Tuning), set by default to `dbgpt_hub/output/adapter/` .     
> per_device_train_batch_size: The size of the batch. If computing resources allow, it can be set larger; the default is 1.   
> gradient_accumulation_steps: The number of steps for accumulating gradients before an update.   
> save_steps: The number of steps at which model checkpoints are saved; it can be set to 100 by default.  
> num_train_epochs: The number of epochs for training the dataset.   


### 3.4. Model Predict

Under the project directory ./dbgpt_hub/output/pred/, this folder is the default output location for model predictions(if not exist, just mkdir).

```bash
sh ./dbgpt_hub/scripts/predict_sft.sh
```

In the script, by default with the parameter `--quantization_bit`, it predicts using QLoRA. Removing it switches to the LoRA prediction method.
The value of the parameter  `--predicted_out_filename` is the file name of the model's predicted results, which can be found in the   `dbgpt_hub/output/pred` directory.

### 3.5 Model Weights
You can find the corresponding model weights we uploaded in August from Huggingface.[hg-eosphoros-ai
](https://huggingface.co/eosphoros)   

 We will soon release new model and improved weights that outperform GPT-4 in accuracy on the spider evaluation set.

#### 3.5.1 Model and fine-tuned weight merging 

If you need to merge the weights of the trained base model and the fine-tuned Peft module to export a complete model, execute the following model export script:   

```bash
sh ./dbgpt_hub/scripts/export_merge.sh
```

Be sure to replace the parameter path values in the script with the paths corresponding to your project.  

### 3.6 Model Evaluation
To evaluate model performance on the dataset, default is spider dev dataset.
Run the following command:
```bash
python dbgpt_hub/eval/evaluation.py --plug_value --input Your_model_pred_file
```
You can find the results of our latest review and part of experiment results [here](docs/eval_llm_result.md)

## 4. RoadMap 

The whole process we will divide into three phases:

* Stage 1:
  * Set up the basic framework, enabling end-to-end workflow from data processing, model SFT training, prediction output to evaluation based on multiple large models. As of 20230804, the entire pipeline has been established.
  now,we has supported as follows:
  - [x] CodeLlama
  - [x] Baichuan2 
  - [x] LLaMa/LLaMa2
  - [x] Falcon
  - [x] Qwen
  - [x] XVERSE
  - [x] ChatGLM2
  - [x] internlm

* Stage 2:
  * Optimize model performance, and support fine-tuning more different models in various ways before  `20231010`
  * Optimize `prompts`
  * Release evaluation results, and optimized   models open to peers.
* Stage 3:
  * Optimized based on more papers, such as RESDSQL and others. Combined with our community's sibling project[Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL)for further enhancements..

## 5. Contributions

We welcome more folks to participate and provide feedback in areas like datasets, model fine-tuning, performance evaluation, paper recommendations, code reproduction, etc. Feel free to open issues or PRs and we'll actively respond.Before submitting the code, please format it using the black style.

## 6. Acknowledgements

Our work is primarily based on the foundation of numerous open-source contributions. Thanks to the following open source projects

* [Spider](https://github.com/ElementAI/spider)
* [CoSQL](https://yale-lily.github.io/cosql)
* [Chase](https://xjtu-intsoft.github.io/chase/)
* [BIRD-SQL](https://bird-bench.github.io/)
* [LLaMA](https://github.com/facebookresearch/llama/tree/main)
* [BLOOM](https://huggingface.co/spaces/bigscience/license)
* [Falcon](https://github.com/hiyouga/LLaMA-Efficient-Tuning/blob/main/LICENSE)
* [ChatGLM](https://github.com/search?q=ChatGLM&type=repositories)
* [WizardLM](https://github.com/nlpxucan/WizardLM)
* [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder)
* [test-suite-sql-eval](https://github.com/taoyds/test-suite-sql-eval)
* [LLaMa-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning) 
