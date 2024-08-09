import logging
from typing import Dict
from langchain_chroma import Chroma


def query_vector_db(
    vector_db: Chroma, query: str, top_k: int
) -> Dict[str, Dict[str, dict]]:
  """Queries the vector database for the most relevant documents based on the query.

  Args:
      vector_db (Chroma): The vector database to query.
      query (str): The query string to search for.
      top_k (int): The number of top results to return.

  Returns:
      Dict[str, Dict[str, dict]]: A dictionary containing table descriptions
      with their column details and scores.
  """
  table_description = {}

  try:
    relevant_docs_score = vector_db.similarity_search_with_score(query, k=top_k)
    logging.info(f"Query executed successfully: {query}")
  except Exception as e:
    logging.error(f"Error executing query: {query}, Error: {e}")
    raise e

  for doc, score in relevant_docs_score:
    metadata = doc.metadata
    table_name = metadata["table_name"]
    original_column_name = metadata["original_column_name"].strip()
    column_name = metadata["column_name"].strip()
    column_description = metadata["column_description"].strip()
    value_description = metadata["value_description"].strip()

    if table_name not in table_description:
      table_description[table_name] = {}

    if original_column_name not in table_description[table_name]:
      table_description[table_name][original_column_name] = {
          "column_name": column_name,
          "column_description": column_description,
          "value_description": value_description,
          "score": score,
      }

  logging.info(f"Query results processed for query: {query}")
  return table_description
