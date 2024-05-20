import sqlite3
import torch
import json
import os, re
from typing import Any, Dict, Generator, List, Optional, Tuple
from threading import Thread

from dbgpt_hub.llm_base.config_parser import get_infer_args
from dbgpt_hub.data_process.data_utils import get_template
import vertexai
from vertexai.preview.tuning import sft
from vertexai.generative_models import GenerativeModel
from google.generativeai.types import HarmCategory, HarmBlockThreshold

import logging
logging.basicConfig(level=logging.DEBUG)

class GeminiModel:

    def __init__(self, args: Optional[Dict[str, Any]] = None) -> None:
        (
            model_args,
            self.data_args,
            finetuning_args,
            self.generating_args,
        ) = get_infer_args(args)
        vertexai.init(project="400355794761", location="us-central1")
        sft_job = sft.SupervisedTuningJob("projects/400355794761/locations/us-central1/tuningJobs/6853268654671265792")
        self.model = GenerativeModel(model_name=sft_job.tuned_model_endpoint_name)
        #self.model = GenerativeModel(model_name="gemini-1.0-pro-002")
        "projects/400355794761/locations/us-central1/tuningJobs/6853268654671265792"
        self.template = get_template(self.data_args.template)
        self.system_prompt = self.data_args.system_prompt

    def _generate_sql(self, query):
        resp = self.model.generate_content(
                query,
                safety_settings={
                    HarmCategory(0): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(1): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(2): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(3): HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory(4): HarmBlockThreshold.BLOCK_NONE,
                }).text.replace("```sql","").replace("```","\n")
        resp = re.sub('\s+',' ', resp).strip()
        return resp

    def verify_and_correct(self, query, sql, db_folder_path):
        def isValidSQL(sql, db):
          conn = sqlite3.connect(db)
          cursor = conn.cursor()
          try:
              cursor.execute(sql)
          except:
              return False
          return True
        db_name = query.split("### New Instruction:\n")[1].split(" contains tables ")[0]
        db_path = os.path.join(db_folder_path, db_name) + f"/{db_name}.sqlite"
        logging.info(f"Connecting to database at {db_path}")

        _sql = sql
        retry_cnt = 0
        while not isValidSQL(_sql, db_path) and retry_cnt < 3:
            new_prompt = (f"Your previous answer, {sql}, was not a valid SQL query. "
                          "Here are some useful tips: 1) -- is used to mark comment; "
                          "2) use nested SQL query when needed; "
                          "3) use the `date` function when comparing dates; "
                          "4) when dealing with ratios, cast the calculated values as REAL;\n\n")
            new_prompt += f"Now, try to generate a new SQL query. Here is the instruction again, {query}"
            _sql = self._generate_sql(new_prompt)
            retry_cnt += 1
        if retry_cnt == 3:
            _sql = "SELECT *"  # failed to generate an executable query
        return _sql


    @torch.inference_mode()
    def chat(self,
             query: str,
             history: Optional[List[Tuple[str, str]]] = None,
             system: Optional[str] = None,
             **input_kwargs) -> Tuple[str, Tuple[int, int]]:
        try:
            resp = self._generate_sql(query)
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
