import os

### path config
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ROOT_PATH = "/root/autodl-tmp"
# MODELS_PARENT_PATH = "/home/model_files/codellama/"
# DEFAULT_FT_MODEL_NAME = "CodeLlama-7b-Instruct-hf"
MODELS_PARENT_PATH = "/home/model/"
DEFAULT_FT_MODEL_NAME = "Baichuan2-13B-Chat"
MODEL_PATH = os.path.join(MODELS_PARENT_PATH, DEFAULT_FT_MODEL_NAME)

# MODEL_PATH = os.path.join(ROOT_PATH, "model")
ADAPTER_PATH = os.path.join(ROOT_PATH, "dbgpt_hub_gql/output/adapter")
MERGED_MODELS = os.path.join(ROOT_PATH, "dbgpt_hub_gql/output/merged_models")

# DATA_PATH = "/root/autodl-tmp/data/spider/pre_processed_data"
# OUT_DIR= "/root/autodl-tmp/codellama"

DATA_PATH = os.path.join(ROOT_PATH, "dbgpt_hub_gql/data")
PREDICTED_DATA_PATH = os.path.join(
    ROOT_PATH, "dbgpt_hub_gql/data/tugraph-db-example/dev.json"
)
PREDICTED_OUT_FILENAME = "pred_gql.txt"
# OUT_DIR = os.path.join(DATA_PATH, "out_pred")
OUT_DIR = os.path.join(ROOT_PATH, "dbgpt_hub_gql/output/")

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

INSTRUCTION_PROMPT = """\
I want you to act as a GQL terminal in front of an example database, \
you need only to return the gql command to me.Below is an instruction that describes a task, \
Write a response that appropriately completes the request.\n"
##Instruction:\n{}\n"""
INPUT_PROMPT = "###Input:\n{}\n\n###Response:"
