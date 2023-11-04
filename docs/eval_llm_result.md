# Evaluation LLM For Text-to-SQL

This doc aims to summarize the performance of publicly available big language models when evaluated on the spider dev dataset. We hope it will provide a point of reference for folks using these big models for Text-to-SQL tasks. We'll keep sharing eval results from models we've tested and seen others use, and very welcome any contributions to make this more comprehensive.

## LLMs Text-to-SQL capability evaluation  before 20231104
 the follow  our experiment execution accuracy of Spider is base on the database which  is download from the  Spider official [website](https://yale-lily.github.io/spider) ,size only 95M.
| name                           | Execution Accuracy | reference                                                                          |
| ------------------------------ | ------------------ | ---------------------------------------------------------------------------------- |
| **GPT-4**                         | **0.762**              | [numbersstation-eval-res](https://www.numbersstation.ai/post/nsql-llama-2-7b)    |
| ChatGPT                        | 0.728              | [numbersstation-eval-res](https://www.numbersstation.ai/post/nsql-llama-2-7b)| 
| **CodeLlama-13b-Instruct-hf_lora** | **0.789**              | sft train by our this project,only used spider train dataset, the same eval way in this project with lora SFT. The [weights](https://huggingface.co/Wangzaistone123/CodeLlama-13b-sql-lora) has pulished . |
| **CodeLlama-13b-Instruct-hf_qlora** | **0.825**              | sft train by our this project, used around 50 thousand pieces of text-to-sql data. The same eval way in this project with lora SFT, and we make sure the training set has filtered the spider eval dataset. |
| CodeLlama-13b-Instruct-hf_qlora | 0.774              | sft train by our this project, only used spider train dataset, the same eval way in this project with qlora and nf4, bit4 SFT.|
| CodeLlama-7b-Instruct-hf_qlora | 0.623              | sft train by this project, which only used **Spider** train dataset, the same eval way in this project with qlora and nf4, bit4 SFT.|
| wizardcoder                    | 0.610              | [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder/tree/main)                |  
|CodeLlama-13b-Instruct-hf| 0.556 | eval in this project default param|
|Baichuan2-13B-Chat|0.392|  eval in this project default param|
| llama2_13b_hf                  | 0.449        | [numbersstation-eval-res](https://www.numbersstation.ai/post/nsql-llama-2-7b)  |
| llama2_13b_hf_lora_best             | 0.744           | sft train by our this project,only used spider train dataset, the same eval way in this project. |



It's important to note that our evaluation results are obtained based on the current project's relevant parameters. We strive to provide objective assessments, but due to variations in certain parameters like the temperature value, different individuals may derive different results using different methods. These results should be taken as **reference only**. We welcome more peers to contribute your evaluation results (along with the corresponding parameter values).  

If you have improved methods for objective evaluation, we warmly welcome contributions to the project's codebase.


## 2. Acknowledgements
Thanks to the following open source projects.

*  [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder)
*  [nsql-llama-2-7b](https://www.numbersstation.ai/post/nsql-llama-2-7b)
