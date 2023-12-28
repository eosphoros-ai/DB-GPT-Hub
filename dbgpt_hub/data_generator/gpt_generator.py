from openai import OpenAI

import os
import json

from tqdm import tqdm

from .llm_generator import LLMGenerator
from .utils import COT_PROMPT, FEW_SHOTS_EXAMPLE


class GPTGenerator(LLMGenerator):
    def __init__(
        self,
        model: str = "gpt-3.5-turbo-16k",
        model_temperature: int = 0,
        max_tokens: int = 2048,
        prompt: str = "",
        num_text2sql_pair_each_db: int = 10,
        table_file_path: str = "",
        output_path: str = "",
    ):
        if len(table_file_path) > 0:
            self.table_file_path = table_file_path
        else:
            self.table_file_path = "../data/spider/tables.json"

        if len(output_path) > 0:
            self.output_path = output_path
        else:
            self.output_path = "../data/spider/synthetic_data_with_gpt.json"

        if len(prompt) > 0:
            self.prompt = prompt
        else:
            self.prompt = COT_PROMPT
        self.model = model
        self.model_temperature = model_temperature
        self.max_tokens = max_tokens
        self.num_text2sql_pair_each_db = num_text2sql_pair_each_db

        self.synthetic_dataset = []

    def generate_synthetic_dataset(self):
        """Function for generating synthetic dataset.
        By default, we generate Spider-like synthetic dataset.
        """
        schema = ""
        synthetic_dataset = []

        tables = json.load(open(self.table_file_path))
        db_num = len(tables)
        easy_count = int(self.num_text2sql_pair_each_db / db_num)
        medium_count = int(self.num_text2sql_pair_each_db / db_num)
        hard_count = self.num_text2sql_pair_each_db - easy_count - medium_count

        db_dict = {}
        for item in tqdm(tables[:]):
            tables = item["table_names_original"]
            coloumns = item["column_names_original"][1:]
            primary_key = item["primary_keys"]
            foreign_keys = item["foreign_keys"]
            schema = (
                item["db_id"]
                + " database contains tables such as "
                + ", ".join(tables)
                + ". "
            )
            for i, name in enumerate(tables):
                data = [coloumn[1] for coloumn in coloumns if coloumn[0] == i]
                schema += (
                    "Table " + name + " has columns such as " + ", ".join(data) + ". "
                )

                # get primary key info
                for j in range(len(primary_key)):
                    if coloumns[primary_key[j] - 1][0] == i:
                        schema += (
                            coloumns[primary_key[j] - 1][1]
                            + " is the primary key."
                            + "\n"
                        )

                # get foreign key info
                for key in foreign_keys:
                    schema += (
                        "The "
                        + coloumns[key[0] - 1][1]
                        + " of "
                        + tables[coloumns[key[0] - 1][0]]
                        + " is the foreign key of "
                        + coloumns[key[1] - 1][1]
                        + " of "
                        + tables[coloumns[key[1] - 1][0]]
                        + ".\n"
                    )

            db_dict[item["db_id"]] = schema

            try:
                # Single generated data for one DB
                for k in range(self.num_text2sql_pair_each_db):
                    text2sql_pair = self._chat_llm(
                        self.prompt.format(
                            easy_count=easy_count,
                            medium_count=medium_count,
                            hard_count=hard_count,
                            schema=schema,
                            few_shots_example=FEW_SHOTS_EXAMPLE,
                        )
                    )
                    text2sql_pair = eval(text2sql_pair)
                    synthetic_dataset += text2sql_pair
            except:
                continue

        self.synthetic_dataset = synthetic_dataset
        self._writeout_dataset()

    def _chat_llm(self, prompt):
        client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
        )

        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
            temperature=self.model_temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return completion.choices[0].message.content

    def _writeout_dataset(self):
        with open(self.output_path, "w", encoding="utf-8") as s:
            json.dump(self.synthetic_dataset, s, indent=4, ensure_ascii=False)
