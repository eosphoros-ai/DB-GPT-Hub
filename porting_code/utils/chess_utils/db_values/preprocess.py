import logging
from pathlib import Path
import pickle
from typing import Any, Dict, List, Tuple
from datasketch import MinHash, MinHashLSH
from nl2sql_eval.query_executor import SQLQueryExecutor
from nl2sql_eval.utils import create_sqlite_engine
from tqdm import tqdm


def _get_unique_values(db_path: str) -> Dict[str, Dict[str, List[str]]]:
  """Retrieves unique text values from the database excluding primary keys.

  Args:
      db_path (str): The path to the SQLite database file.

  Returns:
      Dict[str, Dict[str, List[str]]]: A dictionary containing unique values for
      each table and column.
  """
  engine = create_sqlite_engine(db_path)
  table_names = [
      table[0]
      for table in SQLQueryExecutor(engine).execute(
          "SELECT name FROM sqlite_master WHERE type='table';"
      )[0]
  ]
  primary_keys = []

  for table_name in table_names:
    columns = SQLQueryExecutor(engine).execute(
        f"PRAGMA table_info('{table_name}')"
    )[0]
    for column in columns:
      if column[5] > 0:  # Check if it's a primary key
        column_name = column[1]
        if column_name.lower() not in [c.lower() for c in primary_keys]:
          primary_keys.append(column_name)

  unique_values: Dict[str, Dict[str, List[str]]] = {}
  for table_name in table_names:
    if table_name == "sqlite_sequence":
      continue
    logging.info(f"Processing {table_name}")
    columns = [
        col[1]
        for col in SQLQueryExecutor(engine).execute(
            f"PRAGMA table_info('{table_name}')"
        )[0]
        if (
            "TEXT" in col[2]
            and col[1].lower() not in [c.lower() for c in primary_keys]
        )
    ]
    table_values: Dict[str, List[str]] = {}

    for column in columns:
      if any(
          keyword in column.lower()
          for keyword in [
              "_id",
              " id",
              "url",
              "email",
              "web",
              "time",
              "phone",
              "date",
              "address",
          ]
      ) or column.endswith("Id"):
        continue

      result = SQLQueryExecutor(engine).execute(f"""
                SELECT SUM(LENGTH(unique_values)), COUNT(unique_values)
                FROM (
                    SELECT DISTINCT `{column}` AS unique_values
                    FROM `{table_name}`
                    WHERE `{column}` IS NOT NULL
                ) AS subquery
            """)[0][0]

      sum_of_lengths, count_distinct = result
      if sum_of_lengths is None or count_distinct == 0:
        continue

      average_length = sum_of_lengths / count_distinct
      logging.info(
          f"Column: {column}, sum_of_lengths: {sum_of_lengths}, count_distinct:"
          f" {count_distinct}, average_length: {average_length}"
      )

      if ("name" in column.lower() and sum_of_lengths < 5000000) or (
          sum_of_lengths < 2000000 and average_length < 25
      ):
        logging.info(f"Fetching distinct values for {column}")
        values = [
            str(value[0])
            for value in SQLQueryExecutor(engine).execute(
                f"SELECT DISTINCT `{column}` FROM `{table_name}` WHERE"
                f" `{column}` IS NOT NULL",
            )[0]
        ]
        logging.info(f"Number of different values: {len(values)}")
        table_values[column] = values

    unique_values[table_name] = table_values

  return unique_values


def _create_minhash(signature_size: int, string: str, n_gram: int) -> MinHash:
  """Creates a MinHash object for a given string.

  Args:
      signature_size (int): The size of the MinHash signature.
      string (str): The input string to create the MinHash for.
      n_gram (int): The n-gram size for the MinHash.

  Returns:
      MinHash: The MinHash object for the input string.
  """
  m = MinHash(num_perm=signature_size)
  for d in [string[i : i + n_gram] for i in range(len(string) - n_gram + 1)]:
    m.update(d.encode("utf8"))
  return m


def skip_column(column_name: str, column_values: List[str]) -> bool:
  """Determines whether to skip processing a column based on its values.

  Args:
      column_name (str): The name of the column.
      column_values (List[str]): The list of values in the column.

  Returns:
      bool: True if the column should be skipped, False otherwise.
  """
  if "name" in column_name.lower():
    return False
  sum_of_lengths = sum(len(value) for value in column_values)
  average_length = sum_of_lengths / len(column_values)
  return (sum_of_lengths > 50000) and (average_length > 20)


def make_lsh(
    unique_values: Dict[str, Dict[str, List[str]]],
    signature_size: int,
    n_gram: int,
    threshold: float,
    verbose: bool = True,
) -> Tuple[MinHashLSH, Dict[str, Tuple[MinHash, str, str, str]]]:
  """Creates a MinHash LSH from unique values.

  Args:
      unique_values (Dict[str, Dict[str, List[str]]]): The dictionary of unique
        values.
      signature_size (int): The size of the MinHash signature.
      n_gram (int): The n-gram size for the MinHash.
      threshold (float): The threshold for the MinHash LSH.
      verbose (bool): Whether to display progress information.

  Returns:
      Tuple[MinHashLSH, Dict[str, Tuple[MinHash, str, str, str]]]: The MinHash
      LSH object and the dictionary of MinHashes.
  """
  lsh = MinHashLSH(threshold=threshold, num_perm=signature_size)
  minhashes: Dict[str, Tuple[MinHash, str, str, str]] = {}
  try:
    total_unique_values = sum(
        len(column_values)
        for table_values in unique_values.values()
        for column_values in table_values.values()
    )
    logging.info(f"Total unique values: {total_unique_values}")

    progress_bar = (
        tqdm(total=total_unique_values, desc="Creating LSH")
        if verbose
        else None
    )

    for table_name, table_values in unique_values.items():
      for column_name, column_values in table_values.items():
        logging.info(
            f"Processing {table_name} - {column_name} - {len(column_values)}"
        )

        for id, value in enumerate(column_values):
          minhash = _create_minhash(signature_size, value, n_gram)
          minhash_key = f"{table_name}_{column_name}_{id}"
          minhashes[minhash_key] = (minhash, table_name, column_name, value)
          lsh.insert(minhash_key, minhash)

          if verbose:
            progress_bar.update(1)

    if verbose:
      progress_bar.close()
  except Exception as e:
    logging.error(f"Error creating LSH: {e}")

  return lsh, minhashes


def make_db_lsh(db_directory_path: str, **kwargs: Any) -> None:
  """Creates a MinHash LSH for the database and saves the results.

  Args:
      db_directory_path (str): The path to the database directory.
      **kwargs (Any): Additional arguments for the LSH creation.
  """
  db_id = Path(db_directory_path).name
  preprocessed_path = Path(db_directory_path) / "preprocessed"
  preprocessed_path.mkdir(exist_ok=True)

  unique_values = _get_unique_values(
      str(Path(db_directory_path) / f"{db_id}.sqlite")
  )
  logging.info("Unique values obtained")

  with open(preprocessed_path / f"{db_id}_unique_values.pkl", "wb") as file:
    pickle.dump(unique_values, file)
  logging.info("Saved unique values")

  lsh, minhashes = make_lsh(unique_values, **kwargs)

  with open(preprocessed_path / f"{db_id}_lsh.pkl", "wb") as file:
    pickle.dump(lsh, file)
  with open(preprocessed_path / f"{db_id}_minhashes.pkl", "wb") as file:
    pickle.dump(minhashes, file)
