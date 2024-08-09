import logging
from typing import Any, Dict, List, Optional

from sqlglot import exp, parse_one
from sqlglot.optimizer.qualify import qualify

from .db_info import get_db_all_tables, get_table_all_columns
from .execution import execute_sql


def get_sql_tables(db_path: str, sql: str) -> List[str]:
  """Retrieves table names involved in an SQL query.

  Args:
      db_path (str): Path to the database file.
      sql (str): The SQL query string.

  Returns:
      List[str]: List of table names involved in the SQL query.
  """
  db_tables = get_db_all_tables(db_path)
  try:
    parsed_tables = list(parse_one(sql, read="sqlite").find_all(exp.Table))
    correct_tables = [
        str(table.name).strip().replace('"', "").replace("`", "")
        for table in parsed_tables
        if str(table.name).strip().lower()
        in [db_table.lower() for db_table in db_tables]
    ]
    return correct_tables
  except Exception as e:
    logging.critical(f"Error in get_sql_tables: {e}\nSQL: {sql}")
    raise e


def _get_main_parent(expression: exp.Expression) -> Optional[exp.Expression]:
  """Retrieves the main parent expression for a given SQL expression.

  Args:
      expression (exp.Expression): The SQL expression.

  Returns:
      Optional[exp.Expression]: The main parent expression or None if not found.
  """
  parent = expression.parent
  while parent and not isinstance(parent, exp.Subquery):
    parent = parent.parent
  return parent


def _get_table_with_alias(
    parsed_sql: exp.Expression, alias: str
) -> Optional[exp.Table]:
  """Retrieves the table associated with a given alias.

  Args:
      parsed_sql (exp.Expression): The parsed SQL expression.
      alias (str): The table alias.

  Returns:
      Optional[exp.Table]: The table associated with the alias or None if not
      found.
  """
  return next(
      (
          table
          for table in parsed_sql.find_all(exp.Table)
          if table.alias == alias
      ),
      None,
  )


def get_sql_columns_dict(db_path: str, sql: str) -> Dict[str, List[str]]:
  """Retrieves a dictionary of tables and their respective columns involved in an SQL query.

  Args:
      db_path (str): Path to the database file.
      sql (str): The SQL query string.

  Returns:
      Dict[str, List[str]]: Dictionary of tables and their columns.
  """
  sql = (
      qualify(
          parse_one(sql, read="sqlite"),
          qualify_columns=True,
          validate_qualify_columns=False,
      )
      if isinstance(sql, str)
      else sql
  )
  columns_dict = {}

  sub_queries = [subq for subq in sql.find_all(exp.Subquery) if subq != sql]
  for sub_query in sub_queries:
    subq_columns_dict = get_sql_columns_dict(db_path, sub_query)
    for table, columns in subq_columns_dict.items():
      if table not in columns_dict:
        columns_dict[table] = columns
      else:
        columns_dict[table].extend([
            col
            for col in columns
            if col.lower() not in [c.lower() for c in columns_dict[table]]
        ])

  for column in sql.find_all(exp.Column):
    column_name = column.name
    table_alias = column.table
    table = _get_table_with_alias(sql, table_alias) if table_alias else None
    table_name = table.name if table else None

    if not table_name:
      candidate_tables = [
          t
          for t in sql.find_all(exp.Table)
          if _get_main_parent(t) == _get_main_parent(column)
      ]
      for candidate_table in candidate_tables:
        table_columns = get_table_all_columns(db_path, candidate_table.name)
        if column_name.lower() in [col.lower() for col in table_columns]:
          table_name = candidate_table.name
          break

    if table_name:
      if table_name not in columns_dict:
        columns_dict[table_name] = []
      if column_name.lower() not in [
          c.lower() for c in columns_dict[table_name]
      ]:
        columns_dict[table_name].append(column_name)

  return columns_dict


def get_sql_condition_literals(
    db_path: str, sql: str
) -> Dict[str, Dict[str, List[str]]]:
  """Retrieves literals used in SQL query conditions.

  Args:
      db_path (str): Path to the database file.
      sql (str): The SQL query string.

  Returns:
      Dict[str, Dict[str, List[str]]]: Dictionary of tables and their columns
      with condition literals.
  """
  try:
    columns_dict = get_sql_columns_dict(db_path, sql)
    used_entities = {}
    for where_exp in parse_one(sql, read="sqlite").find_all(exp.Where):
      for literal in where_exp.find_all(exp.Literal):
        if literal == literal.parent.expression:
          for column_exp in literal.parent.find_all(exp.Column):
            column_name = column_exp.name
            table_name = next(
                (
                    table
                    for table, columns in columns_dict.items()
                    if column_name.lower() in [c.lower() for c in columns]
                ),
                None,
            )
            if table_name:
              if table_name not in used_entities:
                used_entities[table_name] = {}
              if column_name not in used_entities[table_name]:
                used_entities[table_name][column_name] = []
              if literal.this not in used_entities[table_name][column_name]:
                used_entities[table_name][column_name].append(literal.this)
    return used_entities
  except Exception as e:
    logging.critical(f"Error in get_sql_condition_literals: {e}\nSQL: {sql}")
    raise e


def _check_value_exists(
    db_path: str, table_name: str, column_name: str, value: str
) -> Optional[str]:
  """Checks if a value exists in a column of a table in the database.

  Args:
      db_path (str): Path to the database file.
      table_name (str): The name of the table.
      column_name (str): The name of the column.
      value (str): The value to check.

  Returns:
      Optional[str]: The value if it exists, otherwise None.
  """
  query = (
      f"SELECT {column_name} FROM {table_name} WHERE {column_name} LIKE"
      f" '%{value}%' LIMIT 1"
  )
  result = execute_sql(db_path, query, "one")
  return result[0] if result else None


def get_sql_condition_literals(
    db_path: str, sql: str
) -> Dict[str, Dict[str, List[str]]]:
  """Retrieves literals used in SQL query conditions and checks their existence in the database.

  Args:
      db_path (str): Path to the database file.
      sql (str): The SQL query string.

  Returns:
      Dict[str, Dict[str, List[str]]]: Dictionary of tables and their columns
      with condition literals.
  """
  try:
    columns_dict = get_sql_columns_dict(db_path=db_path, sql=sql)
    used_entities = {}
    for sql_exp in parse_one(sql, read="sqlite").flatten():
      for literal in sql_exp.find_all(exp.Literal):
        if literal == literal.parent.expression:
          for column_exp in literal.parent.find_all(exp.Column):
            column_name = column_exp.name
            for table_name, column_names in columns_dict.items():
              if column_name.lower() in [col.lower() for col in column_names]:
                example_exist = False
                example = literal.this
                if "(" in str(literal.parent):
                  value_check = _check_value_exists(
                      db_path, table_name, column_name, literal.this
                  )
                  if value_check:
                    example_exist = True
                    example = value_check
                if "LIKE" in str(literal.parent):
                  example_to_search = literal.this.replace("%", "")
                  value_check = _check_value_exists(
                      db_path, table_name, column_name, example_to_search
                  )
                  if value_check:
                    example_exist = True
                    example = example_to_search
                else:
                  example_exist = True
                if example_exist:
                  if table_name not in used_entities:
                    used_entities[table_name] = {}
                  if column_name not in used_entities[table_name]:
                    used_entities[table_name][column_name] = []
                  if example not in used_entities[table_name][column_name]:
                    used_entities[table_name][column_name].append(example)
    return used_entities
  except Exception as e:
    logging.critical(f"Error in get_sql_condition_literals: {e}\nSQL {sql}\n")
    raise e


def missings_status(
    sql: str, tentative_schema: Dict[str, List[str]], db_path: str
) -> Dict[str, Any]:
  """Checks for missing tables and columns in the tentative schema.

  Args:
      tentative_schema (Dict[str, List[str]]): The tentative schema.

  Returns:
      Dict[str, Any]: A dictionary with the status of missing tables and
      columns.
  """
  correct_columns = get_sql_columns_dict(db_path=db_path, sql=sql)
  missing_tables = []
  missing_columns = []

  for table_name, cols in correct_columns.items():
    for col in cols:
      selected_table = [
          table
          for table in tentative_schema.keys()
          if table.lower() == table_name.lower()
      ]
      if not selected_table:

        if table_name not in missing_tables:
          missing_tables.append(table_name)
      else:
        selected_table = selected_table[0]
        if col.lower() not in [
            selected_col.lower()
            for selected_col in tentative_schema[selected_table]
        ]:

          missing_columns.append(f"'{table_name}'.'{col}'")

  status = {
      "missing_tables": missing_tables,
      "missing_columns": missing_columns,
      "correct_columns": correct_columns,
      "selected_schema": tentative_schema,
  }
  return status
