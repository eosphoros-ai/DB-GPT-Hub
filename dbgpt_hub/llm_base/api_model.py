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
        sft_job = sft.SupervisedTuningJob(
            "projects/400355794761/locations/us-central1/tuningJobs/6853268654671265792"
        )
        self.model = GenerativeModel(
            model_name=sft_job.tuned_model_endpoint_name)
        #self.model = GenerativeModel(model_name="gemini-1.0-pro-002")
        "projects/400355794761/locations/us-central1/tuningJobs/6853268654671265792"
        self.template = get_template(self.data_args.template)
        self.system_prompt = self.data_args.system_prompt

    def _generate_sql(self, query, temperature=0.):
        resp = self.model.generate_content(query,
                                           generation_config={
                                               "temperature": temperature
                                           },
                                           safety_settings={
                                               HarmCategory(0):
                                               HarmBlockThreshold.BLOCK_NONE,
                                               HarmCategory(1):
                                               HarmBlockThreshold.BLOCK_NONE,
                                               HarmCategory(2):
                                               HarmBlockThreshold.BLOCK_NONE,
                                               HarmCategory(3):
                                               HarmBlockThreshold.BLOCK_NONE,
                                               HarmCategory(4):
                                               HarmBlockThreshold.BLOCK_NONE,
                                           }).text.replace("```sql",
                                                           "").replace(
                                                               "```", "\n")
        resp = re.sub('\s+', ' ', resp).strip()
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

        db_name = query.split("The database (\"")[1].split(
            "\") structure")[0]
        db_path = os.path.join(db_folder_path, db_name) + f"/{db_name}.sqlite"
        logging.info("Connecting to " + db_path)

        _sql = sql
        retry_cnt, max_retries = 0, 2
        valid, err = isValidSQL(_sql, db_path)

        while not valid and retry_cnt < max_retries:
            logging.info(f"{_sql} , failed due to {err}")
            if "no such column" in err:
                col_name = err.split(": ")[-1]
                col_name = col_name.split(".")[-1]
                context_str = query[query.find("###Table creation statements###"):query.
                                    find("###Question###")]
                input_str = query[query.find("###Question###"):]
                if context_str.find(f"\"{col_name}\"") == -1:
                    new_prompt = (
                        f"Read this text carefully that describes the tables and their associated columns: {context_str}\n\n"
                        f"The column name, \"{col_name}\" is not valid. "
                        f"Find the correct column name that should have been used instead of \"{col_name}\". "
                        "Be careful of any typo or missing spaces, prefer a correction with the minimum edit distance. "
                        "Just return the column name and no other characters or quotations."
                    )
                    col_name = self._generate_sql(new_prompt)
                new_prompt = (
                    f"You need to identify the correct table name for the column, \"{col_name}\". "
                    f"We can do this step-by-step. First, find all the tables that has \"{col_name}\" according to this instruction: {context_str}\n\n"
                    "Next, if there is only one candidate, just return that table. "
                    f"Otherwise, if there are multiple candidates identified in the previous step, then return the one that is most likely given the user question {input_str}. "
                    f"Note that the final table must have the column \"{col_name}\" according to according to the above instruction. "
                    "Always return the table name and no other chracters or quotations. "
                )
                table_name = self._generate_sql(new_prompt)
                new_prompt = (
                    f"This query, {_sql}, is not valid due to this error: {err}\n"
                    f"We can correct this taking some steps. "
                    f"First, understand the foreign key relationship between the tables by reading this: {context_str}\n\n"
                    f"Second, address the error using the correct column reference, {table_name + '.`' + col_name + '`'}\n"
                    "Beware of the table aliases in the query. "
                    f"Rewrite and correct the query, so that the column \"{col_name}\" is correctly referenced from the table \"{table_name}\", "
                    "and just return the corrected query."
                )
                _sql = self._generate_sql(new_prompt)

                if table_name not in _sql:
                    new_prompt = (
                        f"We need to use the column {table_name + '.`' + col_name + '`'} in the SQL query, {_sql}; "
                        f"however, {table_name} is not being used in the query. Introduce the table to the query using proper joins, "
                        f"according to this table and column and foreign key information: {context_str}\n\n"
                        "Return the corrected query. Always return just the SQL query."
                    )
                    _sql = self._generate_sql(new_prompt)
                logging.info(
                    f" *** Correcting {err} with {table_name + '.' + col_name} ...")
            else:
                new_prompt = (
                    f"Your previously generated SQL query, {_sql}, is not valid for this reason: {err}. "
                    "Here are some useful tips: "
                    "1) Table Aliases: Use aliases to avoid duplicate table name conflicts; "
                    "2) Column References: Verify column names and use table_name.column_name format; "
                    "3) use the date function when comparing dates; "
                    "4) when dealing with ratios, cast the calculated values as REAL; "
                    "5) Table Joins: Ensure table names are correct and use appropriate joins.\n\n"
                )
                new_prompt += f"Try again, and remember that  request {query}"
                _sql = self._generate_sql(new_prompt, temperature=0.2)
            valid, err = isValidSQL(_sql, db_path)
            retry_cnt += 1
        if retry_cnt == max_retries:
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
