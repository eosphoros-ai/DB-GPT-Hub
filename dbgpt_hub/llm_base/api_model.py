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

    def _generate_sql(self, query, temperature=0.):
        resp = self.model.generate_content(
                query,
                generation_config={"temperature": temperature},
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
          err = ""
          try:
              cursor.execute(sql)
          except sqlite3.Error as e:
              logging.error(e)
              err = str(e)
              return False, err
          finally:
              if conn:
                conn.close()
          return True, err
        db_name = query.split("### Context:\n")[1].split(" contains tables ")[0].split("database ")[1]
        db_path = os.path.join(db_folder_path, db_name) + f"/{db_name}.sqlite"
        logging.info("Connecting to " + db_path)

        _sql = sql
        retry_cnt = 0
        valid, err = isValidSQL(_sql, db_path)


        while not valid and retry_cnt < 5:
            logging.info(f"{_sql} , failed due to {err}")
            if "no such column" in err:
                col_name = err.split(".")[-1]
                wrong_table_name = err.split(".")[0].split(" ")[-1]
                wrong_table_name = _sql.split(f" AS {wrong_table_name}")[0].split(" ")[-1]
                new_prompt = (f"Your previously generated SQL query, {_sql}, is not valid for this reason: {err}. "
                              f"\"{wrong_table_name}\" doesn't have column \"{col_name}\". Please make sure you associate \"{col_name}\" with the correct table. \n\n")
                logging.info("*** trying with this prompt: " + new_prompt)
                new_prompt += f"Now try again: {query}"
            else:
                new_prompt = (f"Your previously generated SQL query, {_sql}, is not valid for this reason: {err}. "
                              "Here are some useful tips: "
                              "1) Table Aliases: Use aliases to avoid duplicate table name conflicts; "
                              "2) Column References: Verify column names and use table_name.column_name format; "
                              "3) use the date function when comparing dates; "
                              "4) when dealing with ratios, cast the calculated values as REAL; "
                              "5) Table Joins: Ensure table names are correct and use appropriate joins.\n\n")
                new_prompt += f"Try again, and remember that  request {query}"
            _sql = self._generate_sql(new_prompt, temperature=0.2)
            valid, err = isValidSQL(_sql, db_path)
            retry_cnt += 1
        if retry_cnt == 5:
            logging.info(f"Failed to generate a valid query, had {_sql}")
            return _sql
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
