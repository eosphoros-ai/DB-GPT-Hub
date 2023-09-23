import os

### path config 
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ROOT_PATH = "/root/autodl-tmp"
# MODELS_PARENT_PATH = "/home/model_files/codellama/"
# DEFAULT_FT_MODEL_NAME = "CodeLlama-7b-Instruct-hf"
MODELS_PARENT_PATH="/home/model/"
DEFAULT_FT_MODEL_NAME="Baichuan2-13B-Chat"
MODEL_PATH = os.path.join(MODELS_PARENT_PATH, DEFAULT_FT_MODEL_NAME)

# MODEL_PATH = os.path.join(ROOT_PATH, "model")
ADAPTER_PATH = os.path.join(ROOT_PATH, "dbgpt_hub/output/adapter")
MERGED_MODELS = os.path.join(ROOT_PATH, "dbgpt_hub/output/merged_models")

# DATA_PATH = "/root/autodl-tmp/data/spider/pre_processed_data"
# OUT_DIR= "/root/autodl-tmp/codellama"

DATA_PATH = os.path.join(ROOT_PATH, "dbgpt_hub/data")
PREDICTED_DATA_PATH = os.path.join(ROOT_PATH, "dbgpt_hub/data/eval_data/dev_sql.json")
# OUT_DIR = os.path.join(DATA_PATH, "out_pred")
OUT_DIR = os.path.join(ROOT_PATH, "dbgpt_hub/output/")

## model constants 
IGNORE_INDEX = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "<s>"
DEFAULT_UNK_TOKEN = "<unk>"


LOG_FILE_NAME = "trainer_log.jsonl"

# head_state_dict,model save name
VALUE_HEAD_FILE_NAME = "value_head.bin"

# output ,finetuning_args save_to_json name 
FINETUNING_ARGS_NAME = "finetuning_args.json"

#  when prepare_model_for_training ,layer_norm_names
LAYERNORM_NAMES = ["norm", "ln_f", "ln_attn", "ln_mlp"]
EXT2TYPE = {"csv": "csv", "json": "json", "jsonl": "json", "txt": "text"}

# METHODS = ["full", "freeze", "lora"]

# STAGES = ["SFT", "Reward Modeling", "PPO", "DPO", "Pre-Training"]

# DATASET_STAGE_MAP = {
#     "SFT": "sft",
#     "Pre-Training": "pt",
#     "Reward Modeling": "rm",
#     "PPO": "sft",
#     "DPO": "rm",
# }

# SUPPORTED_MODELS = {
#     "LLaMA-7B": "huggyllama/llama-7b",
#     "LLaMA-13B": "huggyllama/llama-13b",
#     "LLaMA-30B": "huggyllama/llama-30b",
#     "LLaMA-65B": "huggyllama/llama-65b",
#     "LLaMA2-7B": "meta-llama/Llama-2-7b-hf",
#     "LLaMA2-13B": "meta-llama/Llama-2-13b-hf",
#     "LLaMA2-70B": "meta-llama/Llama-2-70b-hf",
#     "LLaMA2-7B-Chat": "meta-llama/Llama-2-7b-chat-hf",
#     "LLaMA2-13B-Chat": "meta-llama/Llama-2-13b-chat-hf",
#     "LLaMA2-70B-Chat": "meta-llama/Llama-2-70b-chat-hf",
#     "ChineseLLaMA2-7B": "ziqingyang/chinese-llama-2-7b",
#     "ChineseLLaMA2-13B": "ziqingyang/chinese-llama-2-13b",
#     "ChineseLLaMA2-7B-Chat": "ziqingyang/chinese-alpaca-2-7b",
#     "ChineseLLaMA2-13B-Chat": "ziqingyang/chinese-alpaca-2-13b",
#     "BLOOM-560M": "bigscience/bloom-560m",
#     "BLOOM-3B": "bigscience/bloom-3b",
#     "BLOOM-7B1": "bigscience/bloom-7b1",
#     "BLOOMZ-560M": "bigscience/bloomz-560m",
#     "BLOOMZ-3B": "bigscience/bloomz-3b",
#     "BLOOMZ-7B1-mt": "bigscience/bloomz-7b1-mt",
#     "Falcon-7B": "tiiuae/falcon-7b",
#     "Falcon-7B-Chat": "tiiuae/falcon-7b-instruct",
#     "Falcon-40B": "tiiuae/falcon-40b",
#     "Falcon-40B-Chat": "tiiuae/falcon-40b-instruct",
#     "Baichuan-7B": "baichuan-inc/Baichuan-7B",
#     "Baichuan-13B": "baichuan-inc/Baichuan-13B-Base",
#     "Baichuan-13B-Chat": "baichuan-inc/Baichuan-13B-Chat",
#     "Baichuan2-7B": "baichuan-inc/Baichuan2-7B-Base",
#     "Baichuan2-13B": "baichuan-inc/Baichuan2-13B-Base",
#     "Baichuan2-7B-Chat": "baichuan-inc/Baichuan2-7B-Chat",
#     "Baichuan2-13B-Chat": "baichuan-inc/Baichuan2-13B-Chat",
#     "InternLM-7B": "internlm/internlm-7b",
#     "InternLM-7B-Chat": "internlm/internlm-chat-7b",
#     "Qwen-7B": "Qwen/Qwen-7B",
#     "Qwen-7B-Chat": "Qwen/Qwen-7B-Chat",
#     "XVERSE-13B": "xverse/XVERSE-13B",
#     "ChatGLM2-6B-Chat": "THUDM/chatglm2-6b",
# }

# DEFAULT_MODULE = {
#     "LLaMA": "q_proj,v_proj",
#     "LLaMA2": "q_proj,v_proj",
#     "ChineseLLaMA2": "q_proj,v_proj",
#     "BLOOM": "query_key_value",
#     "BLOOMZ": "query_key_value",
#     "Falcon": "query_key_value",
#     "Baichuan": "W_pack",
#     "Baichuan2": "W_pack",
#     "InternLM": "q_proj,v_proj",
#     "Qwen": "c_attn",
#     "XVERSE": "q_proj,v_proj",
#     "ChatGLM2": "query_key_value",
# }

# DEFAULT_TEMPLATE = {
#     "LLaMA2": "llama2",
#     "ChineseLLaMA2": "llama2_zh",
#     "Baichuan": "baichuan",
#     "Baichuan2": "baichuan2",
#     "InternLM": "intern",
#     "Qwen": "chatml",
#     "ChatGLM2": "chatglm2",
# }
