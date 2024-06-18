import sqlite3
from dbgpt_hub.configs.config import CHECKER_TEMPLATE, LITERAL_ERROR_TEMPLATE, SYNTAX_FIXER_TEMPLATE, VERIFICATION_TEMPLATE
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
        # 1.0-pro finetuned model
        # sft_job = sft.SupervisedTuningJob(
        #     "projects/400355794761/locations/us-central1/tuningJobs/6853268654671265792"
        # )
        # self.model = GenerativeModel(
        #     model_name=sft_job.tuned_model_endpoint_name)
        self.model = GenerativeModel(model_name="gemini-1.5-pro-preview-0514")
        self.model2 = GenerativeModel(
            model_name="gemini-1.5-flash-preview-0514")

        self.template = get_template(self.data_args.template)
        self.system_prompt = self.data_args.system_prompt

    def _generate_sql(self,
                      query,
                      temperature=0.,
                      retry=True,
                      use_flash=False):
        model = self.model2 if use_flash else self.model
        try:
            resp = model.generate_content(query,
                                          generation_config={
                                              "temperature": temperature
                                          },
                                          safety_settings={
                                              0: HarmBlockThreshold.BLOCK_NONE,
                                              1: HarmBlockThreshold.BLOCK_NONE,
                                              2: HarmBlockThreshold.BLOCK_NONE,
                                              3: HarmBlockThreshold.BLOCK_NONE,
                                              4: HarmBlockThreshold.BLOCK_NONE,
                                          }).text.replace("```sql",
                                                          "").replace(
                                                              "```", "\n")
            if "<FINAL_ANSWER>" in resp:
                resp = resp.split("<FINAL_ANSWER>")[1].split("</FINAL_ANSWER>")[0]
        except:
            logging.error(
                f"\n===========\nSQL generation failed for: {query}\n")
            if retry:
                logging.info("Retrying...")
                return self._generate_sql(query,
                                          retry=False,
                                          use_flash=use_flash)
            return ""
        resp = re.sub(r"ite\s*\n?\s*SELECT", "SELECT", resp)
        resp = re.sub('\s+', ' ', resp).strip()
        return resp

    def verify_and_correct(self, query, sql, db_folder_path):

        def syntax_fix(s):
            pattern = r"(?<!\\)'"

            def replace_func(match):
                return match.group().replace("'", '"')

            modified_sql = re.sub(pattern, replace_func, r"{}".format(s))
            return modified_sql

        def verify_answer(s):
            context_str = query[query.find("###Table creation statements###"
                                           ):query.find("###Question###")]
            input_str = query[query.find("###Question###"):]
            new_prompt = VERIFICATION_TEMPLATE.format(context_str, input_str,
                                                      s)
            return self._generate_sql(new_prompt)

        def fix_error(s, err):
            context_str = query[query.find("###Table creation statements###"
                                           ):query.find("###Question###")]
            input_str = query[query.find("###Question###"):]
            new_prompt = CHECKER_TEMPLATE.format(context_str, input_str, s,
                                                 err)
            new_sql = self._generate_sql(new_prompt, use_flash=False)
            if s != new_sql:
                logging.info(f"\n*** verify and update, from {s} to {new_sql}")
            return new_sql

        def fix_literal_error(s):
            context_str = query[query.find("###Table creation statements###"
                                           ):query.find("###Question###")]
            input_str = query[query.find("###Question###"):]
            new_prompt = LITERAL_ERROR_TEMPLATE.format(context_str, input_str, s)
            new_sql = self._generate_sql(new_prompt, use_flash=False)
            logging.info(f"\n*** Fixing literal error, from {s} to {new_sql}")
            return new_sql

        def isValidSQL(sql, db):
            conn = sqlite3.connect(db)
            cursor = conn.cursor()

            err = ""
            rows = []
            is_valid = True
            try:
                rows = cursor.execute(sql).fetchall()
                if len(rows) == 0:
                    is_valid = False
                    err = "empty results"
            except sqlite3.Warning as warning:
                logging.error(f"SQLite Warning: {warning}")
                err = str(warning)
                is_valid = False
            except sqlite3.Error as e:
                logging.error(e)
                err = str(e)
                is_valid = False
            finally:
                if conn:
                    conn.close()
            return is_valid, err, len(rows)


        db_name = query.split("The database (\"")[1].split("\") structure")[0]
        db_path = os.path.join(db_folder_path, db_name) + f"/{db_name}.sqlite"
        logging.info("Connecting to " + db_path)

        _sql = sql
        #_sql = verify_answer(sql)
        _sql = syntax_fix(_sql)
        retry_cnt, max_retries = 0, 2
        valid, err, row_cnt = isValidSQL(_sql, db_path)

        while not valid and retry_cnt < max_retries:
            if row_cnt == 0:
                _sql = fix_literal_error(_sql)
            else:
                _sql = fix_error(_sql, err)
            #_sql = verify_answer(_sql) # this is too expensive to repeat
            _sql = syntax_fix(_sql)
            valid, err, row_cnt = isValidSQL(_sql, db_path)
            retry_cnt += 1
        if retry_cnt == max_retries:
            logging.info(f"Correction failed due to {err}, query: {_sql}")
        else:
            logging.info(f"New query: {_sql}")
        return _sql

    @torch.inference_mode()
    def chat(self,
             query: str,
             history: Optional[List[Tuple[str, str]]] = None,
             system: Optional[str] = None,
             **input_kwargs) -> Tuple[str, Tuple[int, int]]:
        try:
            resp = self._generate_sql(query, use_flash=False)
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
