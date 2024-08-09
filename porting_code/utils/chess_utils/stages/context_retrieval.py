import logging
from typing import Any, Dict, List

from langchain_chroma import Chroma
from nl2sql_eval.chess_utils.db_catalog.search import query_vector_db


def context_retrieval(
    task: Dict[str, str],
    keywords: List[str],
    vector_db: Chroma,
) -> Dict[str, Any]:
  """Retrieves context information based on the task's question and evidence.

  Args:
      task (Any): The task object containing the question and evidence.

  Returns:
      Dict[str, Any]: A dictionary containing the schema with descriptions.
  """
  logging.info("Starting context retrieval")

  top_k = 5

  retrieved_columns = _find_most_similar_columns(
      question=task["question"],
      evidence=task["hint"],
      keywords=keywords,
      vector_db=vector_db,
      top_k=top_k,
  )

  schema_with_descriptions = _format_retrieved_descriptions(retrieved_columns)
  result = {"schema_with_descriptions": schema_with_descriptions}

  logging.info("Context retrieval completed successfully")
  return result


### Context similarity ###


def _find_most_similar_columns(
    question: str,
    evidence: str,
    keywords: List[str],
    vector_db: Chroma,
    top_k: int,
) -> Dict[str, Dict[str, Dict[str, str]]]:
  """Finds the most similar columns based on the question and evidence.

  Args:
      question (str): The question string.
      evidence (str): The evidence string.
      keywords (List[str]): The list of keywords.
      top_k (int): The number of top similar columns to retrieve.

  Returns:
      Dict[str, Dict[str, Dict[str, str]]]: A dictionary containing the most
      similar columns with descriptions.
  """
  logging.info("Finding the most similar columns")
  tables_with_descriptions = {}

  for keyword in keywords:
    question_based_query = f"{question} {keyword}"
    evidence_based_query = f"{evidence} {keyword}"

    retrieved_question_based_query = query_vector_db(
        vector_db, question_based_query, top_k=top_k
    )
    retrieved_evidence_based_query = query_vector_db(
        vector_db, evidence_based_query, top_k=top_k
    )

    tables_with_descriptions = _add_description(
        tables_with_descriptions, retrieved_question_based_query
    )
    tables_with_descriptions = _add_description(
        tables_with_descriptions, retrieved_evidence_based_query
    )

  return tables_with_descriptions


def _add_description(
    tables_with_descriptions: Dict[str, Dict[str, Dict[str, str]]],
    retrieved_descriptions: Dict[str, Dict[str, Dict[str, str]]],
) -> Dict[str, Dict[str, Dict[str, str]]]:
  """Adds descriptions to tables from retrieved descriptions.

  Args:
      tables_with_descriptions (Dict[str, Dict[str, Dict[str, str]]]): The
        current tables with descriptions.
      retrieved_descriptions (Dict[str, Dict[str, Dict[str, str]]]): The
        retrieved descriptions.

  Returns:
      Dict[str, Dict[str, Dict[str, str]]]: The updated tables with
      descriptions.
  """
  logging.info("Adding descriptions to tables")
  for table_name, column_descriptions in retrieved_descriptions.items():
    if table_name not in tables_with_descriptions:
      tables_with_descriptions[table_name] = {}
    for column_name, description in column_descriptions.items():
      if (
          column_name not in tables_with_descriptions[table_name]
          or description["score"]
          > tables_with_descriptions[table_name][column_name]["score"]
      ):
        tables_with_descriptions[table_name][column_name] = description
  return tables_with_descriptions


def _format_retrieved_descriptions(
    retrieved_columns: Dict[str, Dict[str, Dict[str, str]]],
) -> Dict[str, Dict[str, Dict[str, str]]]:
  """Formats retrieved descriptions by removing the score key.

  Args:
      retrieved_columns (Dict[str, Dict[str, Dict[str, str]]]): The retrieved
        columns with descriptions.

  Returns:
      Dict[str, Dict[str, Dict[str, str]]]: The formatted descriptions.
  """
  logging.info("Formatting retrieved descriptions")
  for column_descriptions in retrieved_columns.values():
    for column_info in column_descriptions.values():
      column_info.pop("score", None)
  return retrieved_columns
