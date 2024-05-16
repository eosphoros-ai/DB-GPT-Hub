import torch
import json
from typing import Any, Dict, Generator, List, Optional, Tuple
from threading import Thread

from dbgpt_hub.llm_base.config_parser import get_infer_args
from dbgpt_hub.data_process.data_utils import get_template
import vertexai
from vertexai.generative_models import GenerativeModel
from google.generativeai.types import HarmCategory, HarmBlockThreshold


class GeminiModel:

    def __init__(self, args: Optional[Dict[str, Any]] = None) -> None:
        (
            model_args,
            self.data_args,
            finetuning_args,
            self.generating_args,
        ) = get_infer_args(args)
        vertexai.init(project="400355794761", location="us-central1")
        self.model = GenerativeModel(model_name="gemini-1.0-pro-002")
        self.template = get_template(self.data_args.template)
        self.system_prompt = self.data_args.system_prompt

    @torch.inference_mode()
    def chat(self,
             query: str,
             history: Optional[List[Tuple[str, str]]] = None,
             system: Optional[str] = None,
             **input_kwargs) -> Tuple[str, Tuple[int, int]]:
        try:
            resp = self.model.generate_content(
                query,
                safety_settings={
                    HarmCategory(0): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(1): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(2): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(3): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(4): HarmBlockThreshold.BLOCK_NONE,
                }).text.replace("```sql","").replace("```","\n")
            import re
            resp = re.sub('\s+',' ', resp).strip()
        except:
            print(f'\n*** {query} resulted in API error...\n')
            resp = ""
        return resp, ()

    @torch.inference_mode()
    def stream_chat(self,
                    query: str,
                    history: Optional[List[Tuple[str, str]]] = None,
                    system: Optional[str] = None,
                    **input_kwargs) -> Generator[str, None, None]:
        raise NotImplementedError("stream_chat is not supported.")
