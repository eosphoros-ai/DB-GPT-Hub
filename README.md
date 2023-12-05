# DB-GPT-Hub: Text-to-SQL parsing with LLMs


<div align="center">
  <p>
    <a href="https://github.com/eosphoros-ai/DB-GPT">
        <img alt="stars" src="https://img.shields.io/github/stars/eosphoros-ai/db-gpt-hub?style=social" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT-Hub">
        <img alt="forks" src="https://img.shields.io/github/forks/eosphoros-ai/db-gpt-hub?style=social" />
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
    </a>
     <a href="https://github.com/eosphoros-ai/DB-GPT-Hub/releases">
      <img alt="Release Notes" src="https://img.shields.io/github/release/eosphoros-ai/DB-GPT-Hub" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT-Hub/issues">
      <img alt="Open Issues" src="https://img.shields.io/github/issues-raw/eosphoros-ai/DB-GPT-Hub" />
    </a>
    <a href="https://discord.gg/7uQnPuveTY">
      <img alt="Discord" src="https://dcbadge.vercel.app/api/server/7uQnPuveTY?compact=true&style=flat" />
    </a>
  </p>


[**简体中文**](README.zh.md) | [**Discord**](https://discord.gg/7uQnPuveTY) | [**Wechat**](https://github.com/eosphoros-ai/DB-GPT/blob/main/README.zh.md#%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC) | [**Huggingface**](https://huggingface.co/eosphoros) | [**Community**](https://github.com/eosphoros-ai/community)
</div>

## Contents
- [DB-GPT-Hub: Text-to-SQL parsing with LLMs](#db-gpt-hub-text-to-sql-parsing-with-llms)
  - [Contents](#contents)
  - [1. What is DB-GPT-Hub](#1-what-is-db-gpt-hub)
  - [2. Fine-tuning Text-to-SQL](#2-fine-tuning-text-to-sql)
    - [2.1. Dataset](#21-dataset)
    - [2.2. Model](#22-model)
  - [3. Usage](#3-usage)
    - [3.1. Environment preparation](#31-environment-preparation)
    - [3.2. Data preparation](#32-data-preparation)
    - [3.3. Model fine-tuning](#33-model-fine-tuning)
    - [3.4. Model Predict](#34-model-predict)
    - [3.5 Model Weights](#35-model-weights)
      - [3.5.1 Model and fine-tuned weight merging](#351-model-and-fine-tuned-weight-merging)
    - [3.6 Model Evaluation](#36-model-evaluation)
  - [4. RoadMap](#4-roadmap)
  - [5. Contributions](#5-contributions)
  - [6. Acknowledgements](#6-acknowledgements)
  - [7、Licence](#7licence)
  - [8、Contact Information](#8contact-information)

## 1. What is DB-GPT-Hub

DB-GPT-Hub is an experimental project that leverages Large Language Models (LLMs) to achieve Text-to-SQL parsing. The project encompasses various stages, including data collection, data preprocessing, model selection and construction, and fine-tuning of model weights. Through these processes, our aim is to enhance Text-to-SQL capabilities while reducing model training costs, thus enabling more developers to contribute to improving Text-to-SQL accuracy. Our ultimate goal is to realize automated question-answering capabilities based on databases, allowing users to execute complex database queries using natural language descriptions.

To date, we have successfully integrated multiple large models and established a comprehensive workflow that includes data processing, Supervised Fine-Tuning (SFT) model training, prediction output, and evaluation. The code developed for this project is easily reusable within the project itself.

As of October 10, 2023, we have used this project to fine-tune the open-source 13B-sized model, incorporating more relevant data. Under zero-shot prompts and utilizing [the Spider-based test-suite](https://github.com/taoyds/test-suite-sql-eval), we have achieved an execution accuracy rate of 0.764 for a database with a size of 1.27G. Additionally, the execution accuracy for the database pointed to by [the Spider official website](https://yale-lily.github.io/spider), with a size of 95M, stands at 0.825.


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

- Following the processing template of [NSQL](https://github.com/NumbersStationAI/NSQL), the dataset underwent basic processing, yielding approximately [20W dataset](https://huggingface.co/datasets/Healthy13/Text2SQL/tree/main)



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

| Model Parameters | GPU RAM | CPU RAM | DISK   |
| ---------------- | ------- | ------- | ------ |
| 7b               | 6GB     | 3.6GB   | 36.4GB |
| 13b              | 13.4GB  | 5.9GB   | 60.2GB |
  
All the related parameters are set to the minimum, with a batch size of 1 and max length of 512. Based on experience, for better performance, it is recommended to set the related length values to 1024 or 2048.


## 3. Usage

### 3.1. Environment preparation

```
git clone https://github.com/eosphoros-ai/DB-GPT-Hub.git
cd DB-GPT-Hub
conda create -n dbgpt_hub python=3.10 
conda activate dbgpt_hub
pip install poetry>=1.4.0
poetry install
```

### 3.2. Data preparation

DB-GPT-Hub uses the information matching generation method for data preparation, i.e. the SQL + Repository generation method that combines table information. This method combines data table information to better understand the structure and relationships of the data table, and is suitable for generating SQL statements that meet the requirements.  

Download the [Spider dataset]((https://drive.google.com/uc?export=download&id=1TqleXec_OykOYFREKKtschzY29dUcVAQ)) from the Spider dataset link. By default, after downloading and extracting the data, place it in the dbgpt_hub/data directory, i.e., the path should be `dbgpt_hub/data/spider`.  

For the data preprocessing part, simply **run the following script** :
```bash
## generate train and dev(eval) data
poetry run sh dbgpt_hub/scripts/gen_train_eval_data.sh
```

In the directory `dbgpt_hub/data/`, you will find the newly generated training file example_text2sql_train.json and testing file example_text2sql_dev.json, containing 8659 and 1034 entries respectively. For the data used in subsequent fine-tuning, set the parameter `file_name` value to the file name of the training set in dbgpt_hub/data/dataset_info.json, such as example_text2sql_train.json


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
The data processing code of `chase`, `cosql` and `sparc` has been embedded in the data processing code of the project. After downloading the data set according to the above link, you only need to add ` in `dbgpt_hub/configs/config.py` Just loosen the corresponding code comment in SQL_DATA_INFO`.   

### 3.3. Model fine-tuning

The model fine-tuning supports both LoRA and QLoRA methods. We can run the following command to fine-tune the model. By default, with the parameter --quantization_bit, it uses the QLoRA fine-tuning method. To switch to LoRAs, simply remove the related parameter from the script.
Run the command:

```bash
poetry run sh dbgpt_hub/scripts/train_sft.sh
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

The other parts that are omitted (…) can be kept consistent. If you want to change the default deepseed configuration, go into the `dbgpt_hub/configs` directory and make changes to ds_config.json as needed,the default is stage2.   

In the script, during fine-tuning, different models correspond to key parameters lora_target and template, as shown in the following table:   

| model name                                               | lora_target     | template  |
| -------------------------------------------------------- | --------------- | --------- |
| [LLaMA-2](https://huggingface.co/meta-llama)             | q_proj,v_proj   | llama2    |
| [CodeLlama-2](https://huggingface.co/codellama/)         | q_proj,v_proj   | llama2    |
| [Baichuan2](https://github.com/baichuan-inc/Baichuan2)   | W_pack          | baichuan2 |
| [InternLM](https://github.com/InternLM/InternLM)         | q_proj,v_proj   | intern    |
| [Qwen](https://github.com/QwenLM/Qwen-7B)                | c_attn          | chatml    |
| [XVERSE](https://github.com/xverse-ai/XVERSE-13B)        | q_proj,v_proj   | xverse    |
| [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B)         | query_key_value | chatglm2  |
| [LLaMA](https://github.com/facebookresearch/llama)       | q_proj,v_proj   | -         |
| [BLOOM](https://huggingface.co/bigscience/bloom)         | query_key_value | -         |
| [BLOOMZ](https://huggingface.co/bigscience/bloomz)       | query_key_value | -         |
| [Baichuan](https://github.com/baichuan-inc/baichuan-13B) | W_pack          | baichuan  |
| [Falcon](https://huggingface.co/tiiuae/falcon-7b)        | query_key_value | -         |

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
poetry run sh ./dbgpt_hub/scripts/predict_sft.sh
```

In the script, by default with the parameter `--quantization_bit`, it predicts using QLoRA. Removing it switches to the LoRA prediction method.
The value of the parameter  `--predicted_out_filename` is the file name of the model's predicted results, which can be found in the   `dbgpt_hub/output/pred` directory.

### 3.5 Model Weights
You can find the second corresponding model weights  from Huggingface [hg-eosphoros-ai
](https://huggingface.co/Wangzaistone123/CodeLlama-13b-sql-lora)  ,we uploaded the LoRA weights in October,which execution accuracy on the Spider evaluation set reached 0.789.    

#### 3.5.1 Model and fine-tuned weight merging 

If you need to merge the weights of the trained base model and the fine-tuned Peft module to export a complete model, execute the following model export script:   

```bash
poetry run sh ./dbgpt_hub/scripts/export_merge.sh
```

Be sure to replace the parameter path values in the script with the paths corresponding to your project.  
                                                    
### 3.6 Model Evaluation
To evaluate model performance on the dataset, default is spider dev dataset.
Run the following command:
```bash
poetry run python dbgpt_hub/eval/evaluation.py --plug_value --input Your_model_pred_file
```
You can find the results of our latest review and part of experiment results [here](docs/eval_llm_result.md)  
**Note**: The database pointed to by the default code is a 95M database downloaded from [Spider official website] (https://yale-lily.github.io/spider). If you need to use Spider database (size 1.27G) in [test-suite](https://github.com/taoyds/test-suite-sql-eval), please download the database in the link to the custom directory first, and run the above evaluation command which add parameters and values ​​like `--db Your_download_db_path`.

## 4. RoadMap 

The whole process we will divide into three phases:

* Stage 1:
  * Set up the foundational framework, enabling an end-to-end workflow that encompasses data processing, model SFT (Single Fine-Tuning) training, prediction output, and evaluation using multiple large language models (LLMs). As of August 4th, 2023, the entire pipeline has been successfully established.

  Currently, we offer support for the following features:
  - [x] CodeLlama
  - [x] Baichuan2 
  - [x] LLaMa/LLaMa2
  - [x] Falcon
  - [x] Qwen
  - [x] XVERSE
  - [x] ChatGLM2
  - [x] internlm

* Stage 2:
  - [x] Optidmize model performance, and support fine-tuning more different models in various ways before  `20231010`
  - [x] Optimize `prompts`
  - [x] Release evaluation results, and optimized   models open to peers.
* Stage 3:
  - [ ] Inference speed optimization and improvement   
  - [ ] Targeted optimization and improvement of business scenarios and Chinese effects   
  - [ ] Optimized based on more papers, such as RESDSQL and others. Combined with our community's sibling project[Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL)for further enhancements..  

**If our work has provided even a small measure of assistance to you, please consider giving us a star. Your feedback and support serve as motivation for us to continue releasing more related work and improving our efforts. Thank you!**   

## 5. Contributions

We warmly invite more individuals to join us and actively engage in various aspects of our project, such as datasets, model fine-tuning, performance evaluation, paper recommendations, and code reproduction. Please don't hesitate to open issues or pull requests (PRs), and we will be proactive in responding to your contributions.

Before submitting your code, please ensure that it is formatted according to the black style by using the following command: 
```
poetry run black dbgpt_hub
```

If you have more time to execute more detailed type checking and style checking of your code, please use the following commond:
```
poetry run pyright dbgpt_hub
poetry run pylint dbgpt_hub
```

If you have any questions or need further assistance, don't hesitate to reach out. We appreciate your involvement!

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

Thanks to all the contributors, especially @[JBoRu](https://github.com/JBoRu) who raised the [issue](https://github.com/eosphoros-ai/DB-GPT-Hub/issues/119) which reminded us to add a new promising evaluation way, i.e. Test Suite. As the paper 《SQL-PALM: IMPROVED LARGE LANGUAGE MODEL ADAPTATION FOR TEXT-TO-SQL》 mentioned, "We consider two commonly-used evaluation metrics: execution accuracy (EX) and test-suite accuracy (TS). EX measures whether the SQL execution outcome matches ground truth (GT), whereas TS measures whether the SQL passes all EX evaluations for multiple tests, generated by database augmentation. Since EX contains false positives, we consider TS as a more reliable evaluation metric".

## 7. Citation
Please consider citing our project if you find it useful:

```bibtex
@software{db-gpt-hub,
    author = {DB-GPT-Hub Team},
    title = {{DB-GPT-Hub}},
    url = {https://github.com/eosphoros-ai/DB-GPT-Hub},
    year = {2023}
}
```

## 8. Licence

The MIT License (MIT)

## 9. Contact Information
We are collaborating as a community, and if you have any ideas regarding our community work, please don't hesitate to get in touch with us. If you're interested in delving into an in-depth experiment and optimizing the DB-GPT-Hub subproject, you can reach out to 'wangzai' within the WeChat group. We wholeheartedly welcome your contributions to making it even better together! 
[![](https://dcbadge.vercel.app/api/server/7uQnPuveTY?compact=true&style=flat)](https://discord.gg/7uQnPuveTY)

<p align="center">
  <img src="assets/wechat.JPG" width="300px" />
</p>


[![Star History Chart](https://api.star-history.com/svg?repos=eosphoros-ai/DB-GPT-Hub&type=Date)](https://star-history.com/#eosphoros-ai/DB-GPT-Hub)
