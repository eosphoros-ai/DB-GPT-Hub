# Evaluation LLM For Text-to-SQL

This doc aims to summarize the performance of publicly available big language models when evaluated on the spider dev dataset. We hope it will provide a point of reference for folks using these big models for Text-to-SQL tasks. We'll keep sharing eval results from models we've tested and seen others use, and very welcome any contributions to make this more comprehensive.

## LLMs Text-to-SQL capability evaluation  before 20231104
 the follow  our experiment execution accuracy of Spider is base on the database which  is download from the  Spider official [website](https://yale-lily.github.io/spider) ,size only 95M.
| name                                | Execution Accuracy | reference                                                                                                                                                                                                   |
| ----------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GPT-4**                           | **0.762**          | [numbersstation-eval-res](https://www.numbersstation.ai/post/nsql-llama-2-7b)                                                                                                                               |
| ChatGPT                             | 0.728              | [numbersstation-eval-res](https://www.numbersstation.ai/post/nsql-llama-2-7b)                                                                                                                               |
| **CodeLlama-13b-Instruct-hf_lora**  | **0.789**          | sft train by our this project,only used spider train dataset, the same eval way in this project with lora SFT. The [weights](https://huggingface.co/Wangzaistone123/CodeLlama-13b-sql-lora) has pulished .  |
| **CodeLlama-13b-Instruct-hf_qlora** | **0.825**          | sft train by our this project, used around 50 thousand pieces of text-to-sql data. The same eval way in this project with lora SFT, and we make sure the training set has filtered the spider eval dataset. |
| CodeLlama-13b-Instruct-hf_qlora     | 0.774              | sft train by our this project, only used spider train dataset, the same eval way in this project with qlora and nf4, bit4 SFT.                                                                              |
| CodeLlama-7b-Instruct-hf_qlora      | 0.623              | sft train by this project, which only used **Spider** train dataset, the same eval way in this project with qlora and nf4, bit4 SFT.                                                                        |
| wizardcoder                         | 0.610              | [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder/tree/main)                                                                                                                       |
| CodeLlama-13b-Instruct-hf           | 0.556              | eval in this project default param                                                                                                                                                                          |
| Baichuan2-13B-Chat                  | 0.392              | eval in this project default param                                                                                                                                                                          |
| llama2_13b_hf                       | 0.449              | [numbersstation-eval-res](https://www.numbersstation.ai/post/nsql-llama-2-7b)                                                                                                                               |
| llama2_13b_hf_lora_best             | 0.744              | sft train by our this project,only used spider train dataset, the same eval way in this project.                                                                                                            |





It's important to note that our evaluation results are obtained based on the current project's relevant parameters. We strive to provide objective assessments, but due to variations in certain parameters like the temperature value, different individuals may derive different results using different methods. These results should be taken as **reference only**. We welcome more peers to contribute your evaluation results (along with the corresponding parameter values).  

If you have improved methods for objective evaluation, we warmly welcome contributions to the project's codebase.


## LLMs Text-to-SQL capability evaluation  before 20231208 
 the follow  our experiment execution accuracy of Spider,  this time is base on the database which  is download from the   [the Spider-based test-suite](https://github.com/taoyds/test-suite-sql-eval) ,size of 1.27G,  diffrent from Spider official [website](https://yale-lily.github.io/spider) ,size only 95M. 
the model 
 
 <table>
<tr>
<th>﻿Model</th>
<th>Method</th>
<th>EX</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<td>Llama2-7B-Chat</td>
<td>base</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.887</td>
<td>0.641</td>
<td>0.489</td>
<td>0.331</td>
<td>0.626</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.847</td>
<td>0.623</td>
<td>0.466</td>
<td>0.361</td>
<td>0.608</td>
</tr>
<tr>
<td>Llama2-13B-Chat</td>
<td>base</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.907</td>
<td>0.729</td>
<td>0.552</td>
<td>0.343</td>
<td>0.68</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.911</td>
<td>0.7</td>
<td>0.552</td>
<td>0.319</td>
<td>0.664</td>
</tr>
<tr>
<td>CodeLlama-7B-Instruct</td>
<td>base</td>
<td>0.214</td>
<td>0.177</td>
<td>0.092</td>
<td>0.036</td>
<td>0.149</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.923</td>
<td>0.756</td>
<td>0.586</td>
<td>0.349</td>
<td>0.702</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.911</td>
<td>0.751</td>
<td>0.598</td>
<td>0.331</td>
<td>0.696</td>
</tr>
<tr>
<td>CodeLlama-13B-Instruct</td>
<td>base</td>
<td>0.698</td>
<td>0.601</td>
<td>0.408</td>
<td>0.271</td>
<td>0.539</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.94</td>
<td>0.789</td>
<td>0.684</td>
<td>0.404</td>
<td>0.746</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.94</td>
<td>0.774</td>
<td>0.626</td>
<td>0.392</td>
<td>0.727</td>
</tr>
<tr>
<td>Baichuan2-7B-Chat</td>
<td>base</td>
<td>0.577</td>
<td>0.352</td>
<td>0.201</td>
<td>0.066</td>
<td>335</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.871</td>
<td>0.63</td>
<td>0.448</td>
<td>0.295</td>
<td>0.603</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.891</td>
<td>0.637</td>
<td>0.489</td>
<td>0.331</td>
<td>0.624</td>
</tr>
<tr>
<td>Baichuan2-13B-Chat</td>
<td>base</td>
<td>0.581</td>
<td>0.413</td>
<td>0.264</td>
<td>0.187</td>
<td>0.392</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.903</td>
<td>0.702</td>
<td>0.569</td>
<td>0.392</td>
<td>0.678</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.895</td>
<td>0.675</td>
<td>0.58</td>
<td>0.343</td>
<td>0.659</td>
</tr>
<tr>
<td>Qwen-7B-Chat</td>
<td>base</td>
<td>0.395</td>
<td>0.256</td>
<td>0.138</td>
<td>0.042</td>
<td>0.235</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.855</td>
<td>0.688</td>
<td>0.575</td>
<td>0.331</td>
<td>0.652</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.911</td>
<td>0.675</td>
<td>0.575</td>
<td>0.343</td>
<td>0.662</td>
</tr>
<tr>
<td>Qwen-14B-Chat</td>
<td>base</td>
<td>0.871</td>
<td>0.632</td>
<td>0.368</td>
<td>0.181</td>
<td>0.573</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.895</td>
<td>0.702</td>
<td>0.552</td>
<td>0.331</td>
<td>0.663</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.919</td>
<td>0.744</td>
<td>0.598</td>
<td>0.367</td>
<td>0.701</td>
</tr>
<tr>
<td>ChatGLM3-6b</td>
<td>base</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>lora</td>
<td>0.855</td>
<td>0.605</td>
<td>0.477</td>
<td>0.271</td>
<td>0.59</td>
</tr>
<tr>
<td></td>
<td>qlora</td>
<td>0.843</td>
<td>0.603</td>
<td>0.506</td>
<td>0.211</td>
<td>0.581</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
 

1、All the models lora and qlora are trained by default based on the spider dataset training set.   
2、All candidate models adopt the same evaluation method and prompt. The prompt has explicitly required the model to output only sql. The base evaluation results of Llama2-7B-Chat, Llama2-13B-Chat, and ChatGLM3-6b are 0. After analysis, we see that there are many errors because content other than sql has been generated.


## 2. Acknowledgements
Thanks to the following open source projects.

*  [text-to-sql-wizardcoder](https://github.com/cuplv/text-to-sql-wizardcoder)
*  [nsql-llama-2-7b](https://www.numbersstation.ai/post/nsql-llama-2-7b)
