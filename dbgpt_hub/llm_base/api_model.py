import pickle
import sqlite3
from dbgpt_hub.configs.config import CHECKER_TEMPLATE, LITERAL_ERROR_TEMPLATE, MAJORITY_VOTING, NOT_NULL_TEMPLATE, SELECT_FIX_TEMPLATE, SYNTAX_FIXER_TEMPLATE, VERIFICATION_TEMPLATE
import torch
import json
import random
import numpy as np
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

    def __init__(self) -> None:
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

    def _infer_args(self, args: Optional[Dict[str, Any]] = None):
        (
            model_args,
            self.data_args,
            finetuning_args,
            self.generating_args,
        ) = get_infer_args(args)

    def _generate_sql(self,
                      query,
                      temperature=0.5,
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
                resp = resp.split("<FINAL_ANSWER>")[1].split(
                    "</FINAL_ANSWER>")[0]
        except:
            logging.error(
                f"\n===========\nSQL generation failed for: {query}\n")
            return ""
        resp = re.sub(r"ite\s*\n?\s*SELECT", "SELECT", resp)
        resp = re.sub('\s+', ' ', resp).strip()
        return resp

    def majority_voting(self, query, candidates):
        should_vote = False
        for c in candidates:
            if c != candidates[0]:
                should_vote = True
                break
        if not should_vote:
            return candidates[0]

        sql = self._generate_sql(MAJORITY_VOTING.format(input=query, candidates=candidates),
                                  use_flash=False)
        logging.info("Consensus: " + sql)
        return sql

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
            # this should capture the hints.
            input_str = query[query.find("###Question###"):query.find(
                "Now generate SQLite SQL query to answer the given")]
            new_prompt = VERIFICATION_TEMPLATE.format(context_str, input_str,
                                                      s)
            return self._generate_sql(new_prompt)

        def enforce_rules(s):
            context_str = query[query.find("###Table creation statements###"
                                           ):query.find("###Question###")]
            input_str = query[query.find("###Question###"):query.find(
                "Now generate SQLite SQL query to answer the given")]
            _sql = self._generate_sql(NOT_NULL_TEMPLATE.format(sql=s, question=input_str), use_flash=False)
            _sql = self._generate_sql(SELECT_FIX_TEMPLATE.format(sql=_sql, question=input_str, schema=context_str))
            return _sql

        def fix_error(s, err):
            context_str = query[query.find("###Table creation statements###"
                                           ):query.find("###Question###")]
            # this should capture the hints.
            input_str = query[query.find("###Question###"):query.find(
                "Now generate SQLite SQL query to answer the given")]
            new_prompt = CHECKER_TEMPLATE.format(context_str, input_str, s,
                                                 err)
            new_sql = self._generate_sql(new_prompt, use_flash=False)
            # if s != new_sql:
            #     logging.info(f"\n*** verify and update, from {s} to {new_sql}")
            return new_sql

        def fix_literal_error(s, db_id):
            if s == "":
                return fix_error(s, "INFO:root:")
            file_path = 'dbgpt_hub/data/dev_db_tbl_col_vals.pickle'
            with open(file_path, 'rb') as file:
                tbl_col_vals = pickle.load(file)[db_id]

            def validate_email(email):
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                return re.match(pattern, email) is not None

            def format_col_vals(tbl_col_vals):
                s = ""
                for tbl, col_vals in tbl_col_vals.items():
                    for col, vals in col_vals.items():
                        if len(vals) > 0 and validate_email(vals[0]):
                            continue
                        if len(vals) > 50 and np.mean(
                            [len(v) for v in random.sample(vals, 10)]) > 90:
                            continue
                        s += f'* `{tbl}`.`{col}`: [{",".join(vals[:1200])}]\n'
                return s

            col_vals = format_col_vals(tbl_col_vals)
            context_str = query[query.find("###Table creation statements###"
                                           ):query.find("###Question###")]
            # this should capture the hints.
            input_str = query[query.find("###Question###"):query.find(
                "Now generate SQLite SQL query to answer the given")]
            new_prompt = LITERAL_ERROR_TEMPLATE.format(context_str, col_vals,
                                                       input_str, s)
            new_sql = self._generate_sql(new_prompt, use_flash=False)
            #logging.info(f"\n*** Fixing literal error, from {s} to {new_sql}")
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
        _sql = enforce_rules(_sql)
        # if _sql != "":
        #     _sql = fix_literal_error(sql, db_name)  # verification
        #_sql = verify_answer(sql)
        #_sql = syntax_fix(_sql)
        retry_cnt, max_retries = 0, 2
        valid, err, row_cnt = isValidSQL(_sql, db_path)

        while not valid and retry_cnt < max_retries:
            if err == "empty results":
                _sql = fix_literal_error(_sql, db_name)
            else:
                _sql = fix_error(_sql, err)
                # _sql = fix_literal_error(_sql, db_name)  # verification
            #_sql = verify_answer(_sql) # this is too expensive to repeat
            #_sql = syntax_fix(_sql)
            _sql = enforce_rules(_sql)
            valid, err, row_cnt = isValidSQL(_sql, db_path)
            retry_cnt += 1
        if retry_cnt == max_retries:
            logging.info(f"Correction failed due to {err}")
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
