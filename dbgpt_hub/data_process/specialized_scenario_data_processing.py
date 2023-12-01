# -*- encoding: utf-8 -*-
import os
import csv

from typing import Any, Optional
from sklearn.model_selection import train_test_split

from .table_meta_data_processor import TableMetaDataProcessor
from connectors.anydb_connector import AnyDBConnector


class SpecialScenarioDataProcessor(object):
    def __init__(
        self,
        db_type: str = "mysql",
        host: str = "127.0.0.1",
        port: str = 3306,
        user: Optional[str] = None,
        passwd: Optional[str] = None,
    ) -> Any:
        self.db_type = db_type
        self.connector = AnyDBConnector(
            db_type=db_type, host=host, port=port, user=user, passwd=passwd
        )

    def generate_spider_nl2sql_metadata(
        self,
        input_folder: str = "",
        output_folder: str = "",
        training_ratio: float = 0.7,
        valid_ratio: float = 0.3,
        test_ratio: float = 0.0,
    ):
        # Generate table.json file according to Database Info
        """
        TO DO:
        1. need to solve config data
        """
        table_meta_data_processor = TableMetaDataProcessor(
            conn=self.connector, config_data=None
        )
        spider_table_metadata = (
            table_meta_data_processor.generate_spider_table_metadata()
        )

        with open(
            os.path.join(output_folder, "tables.json"), "w", encoding="utf-8"
        ) as json_file:
            json.dump(spider_table_metadata, json_file, ensure_ascii=False, indent=4)

        text2sql_pairs = self._parse_text2sql_pairs(input_folder=input_folder)

        metadata_with_tokens = self._parse_tokens(text2sql_pairs=text2sql_pairs)

        # split metadata into training valid and test data
        train_data, remain_data = train_test_split(
            metadata_with_tokens, test_size=(1 - training_ratio), random_state=42
        )

        if test_ratio > 0:
            valid_data, test_data = train_test_split(
                remain_data,
                test_size=test_ratio / (valid_ratio + test_ratio),
                random_state=42,
            )

            with open(
                os.path.join(output_folder, "train.json"), "w", encoding="utf-8"
            ) as json_file:
                json.dump(train_data, json_file, ensure_ascii=False, indent=4)

            with open(
                os.path.join(output_folder, "valid.json"), "w", encoding="utf-8"
            ) as json_file:
                json.dump(valid_data, json_file, ensure_ascii=False, indent=4)

            with open(
                os.path.join(output_folder, "test.json"), "w", encoding="utf-8"
            ) as json_file:
                json.dump(test_data, json_file, ensure_ascii=False, indent=4)
        else:
            with open(
                os.path.join(output_folder, "train.json"), "w", encoding="utf-8"
            ) as json_file:
                json.dump(train_data, json_file, ensure_ascii=False, indent=4)

            with open(
                os.path.join(output_folder, "valid.json"), "w", encoding="utf-8"
            ) as json_file:
                json.dump(remain_data, json_file, ensure_ascii=False, indent=4)

    def _parse_text2sql_pairs(
        self,
        input_folder: Optional[str] = None,
    ) -> Optional[Dict[str, str]]:
        """
        input_folder: the path of input folder

        TO DO: split NL and SQL tokens and tokens without values
        """

        # Initialize an empty list to store the dictionaries
        data_list = []

        # Iterate through all files in the folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".csv"):
                file_path = os.path.join(input_folder, filename)

                # Open and read the CSV file
                with open(file_path, "r", encoding="utf-8") as csv_file:
                    csv_reader = csv.DictReader(csv_file)

                    # Iterate through each row in the CSV file
                    for row in csv_reader:
                        db_name = row["db_name"]
                        nl_question = row["nl_question"]
                        query = row["query"]

                        # Create a dictionary for the current row and append it to the list
                        data_list.append(
                            {"db_id": db_name, "question": nl_question, "query": query}
                        )

        # Now, data_list contains all the rows from all CSV files as dictionaries
        return data_list

    def _parse_tokens(self, text2sql_pairs: Optional[Dict] = None) -> Any:
        """
        TO DO:
        need to parse SQL and NL into list of tokens
        """
        pass


if __name__ == "__main__":
    data_processor = SpecialScenarioDataProcessor()
    data_processor.generate_spider_nl2sql_metadata()
