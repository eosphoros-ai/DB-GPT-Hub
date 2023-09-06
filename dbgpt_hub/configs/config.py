import os
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(ROOT_PATH, "model")
ADAPTER_PATH = os.path.join(ROOT_PATH, "adapter")
MERGED_MODELS = os.path.join(ROOT_PATH, "merged_models")
DATA_PATH = os.path.join(ROOT_PATH, "data")
OUT_DIR = os.path.join(DATA_PATH, "out_pred")


DEFAULT_FT_MODEL_NAME = "CodeLlama-7b-hf"

