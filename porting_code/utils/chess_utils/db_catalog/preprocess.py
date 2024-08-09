import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.schema.document import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from .csv_utils import load_tables_description

load_dotenv(override=True)

EMBEDDING_FUNCTION = OpenAIEmbeddings(model="text-embedding-3-large")


def make_db_context_vec_db(db_directory_path: str, **kwargs) -> None:
  """Creates a context vector database for the specified database directory.

  Args:
      db_directory_path (str): The path to the database directory.
      **kwargs: Additional keyword arguments, including: - use_value_description
        (bool): Whether to include value descriptions (default is True).
  """
  db_id = Path(db_directory_path).name

  table_description = load_tables_description(
      db_directory_path, kwargs.get("use_value_description", True)
  )
  docs = []

  for table_name, columns in table_description.items():
    for column_name, column_info in columns.items():
      metadata = {
          "table_name": table_name,
          "original_column_name": column_name,
          "column_name": column_info.get("column_name", ""),
          "column_description": column_info.get("column_description", ""),
          "value_description": (
              column_info.get("value_description", "")
              if kwargs.get("use_value_description", True)
              else ""
          ),
      }
      for key in ["column_name", "column_description", "value_description"]:
        if column_info.get(key, "").strip():
          docs.append(
              Document(page_content=column_info[key], metadata=metadata)
          )

  logging.info(f"Creating context vector database for {db_id}")
  vector_db_path = Path(db_directory_path) / "context_vector_db"

  if vector_db_path.exists():
    os.system(f"rm -r {vector_db_path}")

  vector_db_path.mkdir(exist_ok=True)

  Chroma.from_documents(
      docs, EMBEDDING_FUNCTION, persist_directory=str(vector_db_path)
  )

  logging.info(f"Context vector database created at {vector_db_path}")
