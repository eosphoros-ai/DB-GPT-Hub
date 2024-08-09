import concurrent.futures
import difflib
import logging
from typing import Any, Dict, List, Optional, Tuple

from datasketch import MinHash, MinHashLSH
from langchain_openai import OpenAIEmbeddings
from nl2sql_eval.chess_utils.db_values.search import query_lsh
import numpy as np

EMBEDDING_FUNCTION = OpenAIEmbeddings(model="text-embedding-3-small")


def entity_retrieval(
    task: Dict[str, str], keywords: List[str], schema, lsh, minihashes
) -> Dict[str, Any]:
  """Retrieves entities and columns similar to given keywords from the task.

  Args:
      task (Any): The task object containing the evidence and question.

  Returns:
      Dict[str, Any]: A dictionary containing similar columns and values.
  """
  logging.info("Starting entity retrieval")

  similar_columns = get_similar_columns(
      keywords=keywords,
      question=task["question"],
      hint=task["hint"],
      schema=schema,
  )
  result = {"similar_columns": similar_columns}

  similar_values = get_similar_entities(
      keywords=keywords, lsh=lsh, minihashes=minihashes
  )
  result["similar_values"] = similar_values

  logging.info("Entity retrieval completed successfully")
  return result


### Column name similarity ###


def get_similar_columns(
    keywords: List[str], question: str, hint: str, schema: List[str]
) -> Dict[str, List[str]]:
  """Finds columns similar to given keywords based on question and hint.

  Args:
      keywords (List[str]): The list of keywords.
      question (str): The question string.
      hint (str): The hint string.

  Returns:
      Dict[str, List[str]]: A dictionary mapping table names to lists of similar
      column names.
  """
  logging.info("Retrieving similar columns")
  selected_columns = {}
  for keyword in keywords:
    similar_columns = _get_similar_column_names(
        keyword=keyword, question=question, hint=hint, schema=schema
    )
    for table_name, column_name in similar_columns:
      selected_columns.setdefault(table_name, []).append(column_name)
  return selected_columns


def _column_value(string: str) -> Tuple[Optional[str], Optional[str]]:
  """Splits a string into column and value parts if it contains '='.

  Args:
      string (str): The string to split.

  Returns:
      Tuple[Optional[str], Optional[str]]: The column and value parts.
  """
  if "=" in string:
    left_equal = string.find("=")
    first_part = string[:left_equal].strip()
    second_part = (
        string[left_equal + 1 :].strip()
        if len(string) > left_equal + 1
        else None
    )
    return first_part, second_part
  return None, None


def _extract_paranthesis(string: str) -> List[str]:
  """Extracts strings within parentheses from a given string.

  Args:
      string (str): The string to extract from.

  Returns:
      List[str]: A list of strings within parentheses.
  """
  paranthesis_matches = []
  open_paranthesis = []
  for i, char in enumerate(string):
    if char == "(":
      open_paranthesis.append(i)
    elif char == ")" and open_paranthesis:
      start = open_paranthesis.pop()
      found_string = string[start : i + 1]
      if found_string:
        paranthesis_matches.append(found_string)
  return paranthesis_matches


def _does_keyword_match_column(
    keyword: str, column_name: str, threshold: float = 0.9
) -> bool:
  """Checks if a keyword matches a column name based on similarity.

  Args:
      keyword (str): The keyword to match.
      column_name (str): The column name to match against.
      threshold (float, optional): The similarity threshold. Defaults to 0.9.

  Returns:
      bool: True if the keyword matches the column name, False otherwise.
  """
  keyword = keyword.lower().replace(" ", "").replace("_", "").rstrip("s")
  column_name = (
      column_name.lower().replace(" ", "").replace("_", "").rstrip("s")
  )
  similarity = difflib.SequenceMatcher(None, column_name, keyword).ratio()
  return similarity >= threshold


def _get_similar_column_names(
    keyword: str, question: str, hint: str, schema: List[str]
) -> List[Tuple[str, str]]:
  """Finds column names similar to a keyword.

  Args:
      keyword (str): The keyword to find similar columns for.
      question (str): The question string.
      hint (str): The hint string.

  Returns:
      List[Tuple[str, str]]: A list of tuples containing table and column names.
  """
  keyword = keyword.strip()
  potential_column_names = [keyword]

  column, value = _column_value(keyword)
  if column:
    potential_column_names.append(column)

  potential_column_names.extend(_extract_paranthesis(keyword))

  if " " in keyword:
    potential_column_names.extend(part.strip() for part in keyword.split())

  similar_column_names = []
  for table, column, _ in schema:
    for potential_column_name in potential_column_names:
      if _does_keyword_match_column(potential_column_name, column):
        similarity_score = _get_semantic_similarity_with_openai(
            f"`{table}`.`{column}`", [f"{question} {hint}"]
        )[0]
        similar_column_names.append((table, column, similarity_score))

  similar_column_names.sort(key=lambda x: x[2], reverse=True)
  return [(table, column) for table, column, _ in similar_column_names[:1]]


### Entity similarity ###


def get_similar_entities(
    keywords: List[str],
    lsh: MinHashLSH,
    minihashes: Dict[str, Tuple[MinHash, str, str, str]],
) -> Dict[str, Dict[str, List[str]]]:
  """Retrieves similar entities from the database based on keywords.

  Args:
      keywords (List[str]): The list of keywords.

  Returns:
      Dict[str, Dict[str, List[str]]]: A dictionary mapping table and column
      names to similar entities.
  """
  logging.info("Retrieving similar entities")
  selected_values = {}

  def get_similar_values_target_string(target_string: str):
    unique_similar_values = query_lsh(
        lsh, minihashes, keyword=target_string, signature_size=100, top_n=10
    )
    return target_string, _get_similar_entities_to_keyword(
        target_string, unique_similar_values
    )

  for keyword in keywords:
    keyword = keyword.strip()
    to_search_values = [keyword]
    if (" " in keyword) and ("=" not in keyword):
      for i in range(len(keyword)):
        if keyword[i] == " ":
          first_part = keyword[:i]
          second_part = keyword[i + 1 :]
          if first_part not in to_search_values:
            to_search_values.append(first_part)
          if second_part not in to_search_values:
            to_search_values.append(second_part)

    to_search_values.sort(key=len, reverse=True)
    hint_column, hint_value = _column_value(keyword)
    if hint_value:
      to_search_values = [hint_value, *to_search_values]

    with concurrent.futures.ThreadPoolExecutor() as executor:
      futures = {
          executor.submit(get_similar_values_target_string, ts): ts
          for ts in to_search_values
      }
      for future in concurrent.futures.as_completed(futures):
        target_string, similar_values = future.result()
        for table_name, column_values in similar_values.items():
          for column_name, entities in column_values.items():
            if entities:
              selected_values.setdefault(table_name, {}).setdefault(
                  column_name, []
              ).extend([
                  (ts, value, edit_distance, embedding)
                  for ts, value, edit_distance, embedding in entities
              ])

  for table_name, column_values in selected_values.items():
    for column_name, values in column_values.items():
      max_edit_distance = max(values, key=lambda x: x[2])[2]
      selected_values[table_name][column_name] = list(
          set(
              value
              for _, value, edit_distance, _ in values
              if edit_distance == max_edit_distance
          )
      )
  return selected_values


def _get_similar_entities_to_keyword(
    keyword: str, unique_values: Dict[str, Dict[str, List[str]]]
) -> Dict[str, Dict[str, List[Tuple[str, str, float, float]]]]:
  """Finds entities similar to a keyword in the database.

  Args:
      keyword (str): The keyword to find similar entities for.
      unique_values (Dict[str, Dict[str, List[str]]]): The dictionary of unique
        values from the database.

  Returns:
      Dict[str, Dict[str, List[Tuple[str, str, float, float]]]]: A dictionary
      mapping table and column names to similar entities.
  """
  return {
      table_name: {
          column_name: _get_similar_values(keyword, values)
          for column_name, values in column_values.items()
      }
      for table_name, column_values in unique_values.items()
  }


def _get_similar_values(
    target_string: str, values: List[str]
) -> List[Tuple[str, str, float, float]]:
  """Finds values similar to the target string based on edit distance and embedding similarity.

  Args:
      target_string (str): The target string to compare against.
      values (List[str]): The list of values to compare.

  Returns:
      List[Tuple[str, str, float, float]]: A list of tuples containing the
      target string, value, edit distance, and embedding similarity.
  """
  edit_distance_threshold = 0.3
  top_k_edit_distance = 5
  embedding_similarity_threshold = 0.6
  top_k_embedding = 1

  edit_distance_similar_values = [
      (
          value,
          difflib.SequenceMatcher(
              None, value.lower(), target_string.lower()
          ).ratio(),
      )
      for value in values
      if difflib.SequenceMatcher(
          None, value.lower(), target_string.lower()
      ).ratio()
      >= edit_distance_threshold
  ]
  edit_distance_similar_values.sort(key=lambda x: x[1], reverse=True)
  edit_distance_similar_values = edit_distance_similar_values[
      :top_k_edit_distance
  ]
  similarities = _get_semantic_similarity_with_openai(
      target_string, [value for value, _ in edit_distance_similar_values]
  )
  embedding_similar_values = [
      (
          target_string,
          edit_distance_similar_values[i][0],
          edit_distance_similar_values[i][1],
          similarities[i],
      )
      for i in range(len(edit_distance_similar_values))
      if similarities[i] >= embedding_similarity_threshold
  ]

  embedding_similar_values.sort(key=lambda x: x[2], reverse=True)
  return embedding_similar_values[:top_k_embedding]


def _get_semantic_similarity_with_openai(
    target_string: str, list_of_similar_words: List[str]
) -> List[float]:
  """Computes semantic similarity between a target string and a list of similar words using OpenAI embeddings.

  Args:
      target_string (str): The target string to compare.
      list_of_similar_words (List[str]): The list of similar words to compare
        against.

  Returns:
      List[float]: A list of similarity scores.
  """
  target_string_embedding = EMBEDDING_FUNCTION.embed_query(target_string)
  all_embeddings = EMBEDDING_FUNCTION.embed_documents(list_of_similar_words)
  similarities = [
      np.dot(target_string_embedding, embedding) for embedding in all_embeddings
  ]
  return similarities
