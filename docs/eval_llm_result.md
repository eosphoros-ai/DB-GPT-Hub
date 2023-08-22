# Evaluation LLM For Text-to-SQL

This doc aims to summarize the performance of publicly available big language models when evaluated on the spider dataset. We hope it will provide a point of reference for folks using these big models for Text-to-SQL tasks. We'll keep sharing eval results from models we've tested and seen others use, and very welcome any contributions to make this more comprehensive.

## 1.LLMs Text-to-SQL capability evaluation
| name               | Execution Accuracy | reference                                                           |
| ------------------ | ------------------ | ------------------------------------------------------------------- |
| ChatGPT            | 0.728              | [quote](https://www.numbersstation.ai/post/nsql-llama-2-7b)         |
| GPT 4              | 0.762              | [quote](https://www.numbersstation.ai/post/nsql-llama-2-7b)         |
| wizardcoder        | 0.610              | [quote](https://github.com/cuplv/text-to-sql-wizardcoder/tree/main) |
| llama2_13b_hf      | 0.252              | run in this project,default param set                               |
| llama2_13b_hf_lora | 0.622              | run in this project,default param set                               |



## 2. Acknowledgements
Thanks to the following open source projects.

*  [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder)
*  [nsql-llama-2-7b](https://www.numbersstation.ai/post/nsql-llama-2-7b)
