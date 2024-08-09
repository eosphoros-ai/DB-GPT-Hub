import logging
from typing import Any, Dict, List

from nl2sql_eval.chess_utils.templates.column_selection import PROMPT
from nl2sql_eval.parsers import get_parser
from nl2sql_eval.utils import call_vertex_llm_with_cache


def column_selection(
    task: Any, schema, schema_string: str, model_name: str
) -> Dict[str, Any]:
  """Selects columns based on the specified mode and updates the tentative schema.

  Args:
      task (Any): The task object containing the question and evidence.
      tentative_schema (Dict[str, List[str]]): The current tentative schema.
      execution_history (List[Dict[str, Any]]): The history of executions.

  Returns:
      Dict[str, Any]: A dictionary containing the updated tentative schema and
      selected columns.
  """
  logging.info("Starting column selection")
  parser = get_parser("column_selection")

  request_kwargs = {
      "DATABASE_SCHEMA": schema_string,
      "HINT": task["hint"],
      "QUESTION": task["question"],
  }

  prompt = PROMPT.format(**request_kwargs)
  response = call_vertex_llm_with_cache(
      prompt=prompt, model=model_name, tag="column_selection"
  )

  logging.info("Parsing column selection")
  print(parser.parse(response))
  aggregated_result = aggregate_columns(parser.parse(response), schema.keys())

  column_names = aggregated_result

  result = {
      "col_selection_schema": column_names,
  }

  logging.info("Column selection completed successfully")
  return result


def aggregate_columns(
    columns_dicts: Dict[str, Any], selected_tables: List[str]
) -> Dict[str, List[str]]:
  """Aggregates columns from multiple responses and consolidates reasoning.

  Args:
      columns_dicts (List[Dict[str, Any]]): List of dictionaries containing
        column names and reasoning.
      selected_tables (List[str]): List of selected tables.

  Returns:
      Dict[str, List[str]]: Aggregated result with unique column names and
      consolidated reasoning.
  """
  logging.info("Aggregating columns from multiple responses")
  columns = {}

  for key, value in columns_dicts.items():
    if key == "chain_of_thought_reasoning":
      continue
    else:  # key is table name
      table_name = key
      if table_name.startswith("`"):
        table_name = table_name[1:-1]
      column_names = value
      if table_name.lower() in [t.lower() for t in selected_tables]:
        for column_name in column_names:
          if column_name.startswith("`"):
            column_name = column_name[1:-1]
          if table_name not in columns:
            columns[table_name] = []
          if column_name.lower() not in [
              col.lower() for col in columns[table_name]
          ]:
            columns[table_name].append(column_name)

  aggregation_result = columns

  logging.info(f"Aggregated columns: {columns}")
  return aggregation_result
