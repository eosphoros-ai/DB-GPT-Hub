import logging
import random
import sqlite3
from typing import Any, Dict, List, Union
from func_timeout import FunctionTimedOut, func_timeout


def _clean_sql(sql: str) -> str:
  """Cleans the SQL query by removing unwanted characters and whitespace.

  Args:
      sql (str): The SQL query string.

  Returns:
      str: The cleaned SQL query string.
  """
  return sql.replace("\n", " ").replace('"', "'").strip("`.")


def execute_sql(db_path: str, sql: str, fetch: Union[str, int] = "all") -> Any:
  """Executes an SQL query on a database and fetches results.

  Args:
      db_path (str): The path to the database file.
      sql (str): The SQL query to execute.
      fetch (Union[str, int]): How to fetch the results. Options are "all",
        "one", "random", or an integer.

  Returns:
      Any: The fetched results based on the fetch argument.

  Raises:
      Exception: If an error occurs during SQL execution.
  """
  try:
    with sqlite3.connect(db_path) as conn:
      cursor = conn.cursor()
      cursor.execute(sql)
      if fetch == "all":
        return cursor.fetchall()
      elif fetch == "one":
        return cursor.fetchone()
      elif fetch == "random":
        samples = cursor.fetchmany(10)
        return random.choice(samples) if samples else []
      elif isinstance(fetch, int):
        return cursor.fetchmany(fetch)
      else:
        raise ValueError(
            "Invalid fetch argument. Must be 'all', 'one', 'random', or an"
            " integer."
        )
  except Exception as e:
    logging.error(f"Error in execute_sql: {e}\nSQL: {sql}")
    raise e


def _compare_sqls_outcomes(
    db_path: str, predicted_sql: str, ground_truth_sql: str
) -> int:
  """Compares the outcomes of two SQL queries to check for equivalence.

  Args:
      db_path (str): The path to the database file.
      predicted_sql (str): The predicted SQL query.
      ground_truth_sql (str): The ground truth SQL query.

  Returns:
      int: 1 if the outcomes are equivalent, 0 otherwise.

  Raises:
      Exception: If an error occurs during SQL execution.
  """
  try:
    predicted_res = execute_sql(db_path, predicted_sql)
    ground_truth_res = execute_sql(db_path, ground_truth_sql)
    return int(set(predicted_res) == set(ground_truth_res))
  except Exception as e:
    logging.critical(f"Error comparing SQL outcomes: {e}")
    raise e


def compare_sqls(
    db_path: str,
    predicted_sql: str,
    ground_truth_sql: str,
    meta_time_out: int = 30,
) -> Dict[str, Union[int, str]]:
  """Compares predicted SQL with ground truth SQL within a timeout.

  Args:
      db_path (str): The path to the database file.
      predicted_sql (str): The predicted SQL query.
      ground_truth_sql (str): The ground truth SQL query.
      meta_time_out (int): The timeout for the comparison.

  Returns:
      dict: A dictionary with the comparison result and any error message.
  """
  # predicted_sql = _clean_sql(predicted_sql)
  try:
    res = func_timeout(
        meta_time_out,
        _compare_sqls_outcomes,
        args=(db_path, predicted_sql, ground_truth_sql),
    )
    error = "incorrect answer" if res == 0 else "--"
  except FunctionTimedOut:
    logging.warning("Comparison timed out.")
    error = "timeout"
    res = 0
  except Exception as e:
    logging.error(f"Error in compare_sqls: {e}")
    error = str(e)
    res = 0
  return {"exec_res": res, "exec_err": error}


def validate_sql_query(
    db_path: str, sql: str, max_returned_rows: int = 30
) -> Dict[str, Union[str, Any]]:
  """Validates an SQL query by executing it and returning the result.

  Args:
      db_path (str): The path to the database file.
      sql (str): The SQL query to validate.
      max_returned_rows (int): The maximum number of rows to return.

  Returns:
      dict: A dictionary with the SQL query, result, and status.
  """
  try:
    result = execute_sql(db_path, sql, fetch=max_returned_rows)
    return {"SQL": sql, "RESULT": result, "STATUS": "OK"}
  except Exception as e:
    logging.error(f"Error in validate_sql_query: {e}")
    return {"SQL": sql, "RESULT": str(e), "STATUS": "ERROR"}


def aggregate_sqls(db_path: str, sqls: List[str]) -> str:
  """Aggregates multiple SQL queries by validating them and clustering based on result sets.

  Args:
      db_path (str): The path to the database file.
      sqls (List[str]): A list of SQL queries to aggregate.

  Returns:
      str: The shortest SQL query from the largest cluster of equivalent
      queries.
  """
  results = [validate_sql_query(db_path, sql) for sql in sqls]
  clusters = {}

  # Group queries by unique result sets
  for result in results:
    if result["STATUS"] == "OK":
      # Using a frozenset as the key to handle unhashable types like lists
      key = frozenset(tuple(row) for row in result["RESULT"])
      if key in clusters:
        clusters[key].append(result["SQL"])
      else:
        clusters[key] = [result["SQL"]]

  if clusters:
    # Find the largest cluster
    largest_cluster = max(clusters.values(), key=len, default=[])
    # Select the shortest SQL query from the largest cluster
    if largest_cluster:
      return min(largest_cluster, key=len)

  logging.warning("No valid SQL clusters found. Returning the first SQL query.")
  return sqls[0]
