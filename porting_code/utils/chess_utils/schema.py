from dataclasses import dataclass, field
import logging
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class ColumnInfo:
  """Represents metadata for a single column in a database table.

  Attributes:
      original_column_name (str): The original name of the column.
      column_name (str): The standardized name of the column.
      column_description (str): A description of the column.
      data_format (str): The format of the data in the column.
      value_description (str): A description of the values in the column.
      type (str): The data type of the column.
      examples (List[str]): Example values from the column.
      primary_key (bool): Whether the column is a primary key.
      foreign_keys (List[Tuple[str, str]]): Foreign keys referencing other
        tables and columns.
      referenced_by (List[Tuple[str, str]]): Columns in other tables that
        reference this column.
  """

  original_column_name: str = ""
  column_name: str = ""
  column_description: str = ""
  data_format: str = ""
  value_description: str = ""
  type: str = ""
  examples: List[str] = field(default_factory=list)
  primary_key: bool = False
  foreign_keys: List[Tuple[str, str]] = field(default_factory=list)
  referenced_by: List[Tuple[str, str]] = field(default_factory=list)


def set_field(column_info: ColumnInfo, field_name: str, value: Any) -> None:
  """Sets a field in the ColumnInfo dataclass.

  Args:
      column_info (ColumnInfo): The ColumnInfo instance to update.
      field_name (str): The field name to set.
      value (Any): The value to set for the field.

  Raises:
      ValueError: If the field_name is not a valid field of ColumnInfo.
  """
  if field_name in column_info.__dataclass_fields__:
    setattr(column_info, field_name, value)
  else:
    raise ValueError(f"{field_name} is not a valid field of ColumnInfo")


@dataclass
class TableSchema:
  """Represents the schema of a single table in a database.

  Attributes:
      columns (Dict[str, ColumnInfo]): A dictionary mapping column names to
        their metadata.
  """

  columns: Dict[str, ColumnInfo] = field(default_factory=dict)


def get_primary_keys(table_schema: TableSchema) -> List[str]:
  """Retrieves the primary key columns from a table schema.

  Args:
      table_schema (TableSchema): The table schema to analyze.

  Returns:
      List[str]: A list of primary key column names.
  """
  return [
      name for name, info in table_schema.columns.items() if info.primary_key
  ]


@dataclass
class DatabaseSchema:
  """Represents the schema of an entire database, consisting of multiple tables.

  Attributes:
      tables (Dict[str, TableSchema]): A dictionary mapping table names to their
        schemas.
  """

  tables: Dict[str, TableSchema] = field(default_factory=dict)

  @classmethod
  def from_table_names(cls, table_names: List[str]) -> "DatabaseSchema":
    """Creates a DatabaseSchema from a list of table names.

    Args:
        table_names (List[str]): The names of the tables to include in the
          schema.

    Returns:
        DatabaseSchema: The constructed database schema.
    """
    return cls(tables={name: TableSchema() for name in table_names})

  @classmethod
  def from_schema_dict(
      cls, schema_dict: Dict[str, List[str]]
  ) -> "DatabaseSchema":
    """Creates a DatabaseSchema from a dictionary mapping table names to lists of column names.

    Args:
        schema_dict (Dict[str, List[str]]): The schema dictionary to convert.

    Returns:
        DatabaseSchema: The constructed database schema.
    """
    return cls(
        tables={
            table_name: TableSchema(
                columns={
                    column_name: ColumnInfo() for column_name in column_names
                }
            )
            for table_name, column_names in schema_dict.items()
        }
    )

  @classmethod
  def from_schema_dict_with_examples(
      cls, schema_dict_with_info: Dict[str, Dict[str, List[str]]]
  ) -> "DatabaseSchema":
    """Creates a DatabaseSchema from a dictionary with example values for each column.

    Args:
        schema_dict_with_info (Dict[str, Dict[str, List[str]]]): The schema
          dictionary with example values.

    Returns:
        DatabaseSchema: The constructed database schema.
    """
    return cls(
        tables={
            table_name: TableSchema(
                columns={
                    column_name: ColumnInfo(examples=column_info)
                    for column_name, column_info in column_dict.items()
                }
            )
            for table_name, column_dict in schema_dict_with_info.items()
        }
    )

  @classmethod
  def from_schema_dict_with_descriptions(
      cls, schema_dict_with_info: Dict[str, Dict[str, Dict[str, Any]]]
  ) -> "DatabaseSchema":
    """Creates a DatabaseSchema from a dictionary with detailed information for each column.

    Args:
        schema_dict_with_info (Dict[str, Dict[str, Dict[str, Any]]]): The schema
          dictionary with detailed information.

    Returns:
        DatabaseSchema: The constructed database schema.
    """
    database_schema = cls.from_schema_dict(schema_dict_with_info)
    for table_name, columns_info in schema_dict_with_info.items():
      for column_name, info in columns_info.items():
        column_info = database_schema.tables[table_name].columns[column_name]
        for field_name, value in info.items():
          set_field(column_info, field_name, value)
    return database_schema

  def get_actual_table_name(self, table_name: str) -> Optional[str]:
    """Retrieves the actual table name matching the provided name, case-insensitive.

    Args:
        table_name (str): The name of the table to search for.

    Returns:
        Optional[str]: The actual table name if found, otherwise None.
    """
    table_name_lower = table_name.lower()
    return next(
        (name for name in self.tables if name.lower() == table_name_lower), None
    )

  def get_table_info(self, table_name: str) -> Optional[TableSchema]:
    """Retrieves the TableSchema object for the specified table name.

    Args:
        table_name (str): The name of the table to retrieve.

    Returns:
        Optional[TableSchema]: The TableSchema if found, otherwise None.
    """
    actual_name = self.get_actual_table_name(table_name)
    return self.tables.get(actual_name)

  def get_actual_column_name(
      self, table_name: str, column_name: str
  ) -> Optional[str]:
    """Retrieves the actual column name matching the provided name, case-insensitive.

    Args:
        table_name (str): The name of the table containing the column.
        column_name (str): The name of the column to search for.

    Returns:
        Optional[str]: The actual column name if found, otherwise None.
    """
    table_info = self.get_table_info(table_name)
    if table_info:
      column_name_lower = column_name.lower()
      return next(
          (
              name
              for name in table_info.columns
              if name.lower() == column_name_lower
          ),
          None,
      )
    return None

  def get_column_info(
      self, table_name: str, column_name: str
  ) -> Optional[ColumnInfo]:
    """Retrieves the ColumnInfo object for the specified column in a table.

    Args:
        table_name (str): The name of the table containing the column.
        column_name (str): The name of the column to retrieve.

    Returns:
        Optional[ColumnInfo]: The ColumnInfo if found, otherwise None.
    """
    actual_name = self.get_actual_column_name(table_name, column_name)
    if actual_name:
      return self.tables[table_name].columns[actual_name]
    return None

  def set_columns_info(
      self, schema_with_info: Dict[str, Dict[str, Dict[str, Any]]]
  ) -> None:
    """Sets detailed information for columns in the schema.

    Args:
        schema_with_info (Dict[str, Dict[str, Dict[str, Any]]]): The schema
          information to set.
    """
    for table_name, columns_info in schema_with_info.items():
      table_info = self.get_table_info(table_name)
      if table_info is None:
        logging.warning(f"Table {table_name} not found in the schema")
        continue
      for column_name, info in columns_info.items():
        actual_name = self.get_actual_column_name(table_name, column_name)
        if actual_name is None:
          logging.warning(
              f"Column {column_name} not found in table {table_name}"
          )
          continue
        schema_column_info = table_info.columns[actual_name]
        for field_name, value in info.items():
          set_field(schema_column_info, field_name, value)

  def subselect_schema(
      self, selected_database_schema: "DatabaseSchema"
  ) -> "DatabaseSchema":
    """Creates a new DatabaseSchema containing only the selected tables and columns.

    Args:
        selected_database_schema (DatabaseSchema): The schema to subselect from.

    Returns:
        DatabaseSchema: The new subselected database schema.
    """
    new_schema = DatabaseSchema({})
    for table_name, table_info in selected_database_schema.tables.items():
      actual_table_name = self.get_actual_table_name(table_name)
      if actual_table_name is None:
        logging.warning(f"Table {table_name} not found in the schema")
        continue
      new_table_info = TableSchema()
      for column_name, column_info in table_info.columns.items():
        actual_column_name = self.get_actual_column_name(
            table_name, column_name
        )
        if actual_column_name is None:
          logging.warning(
              f"Column {column_name} not found in table {table_name}"
          )
          continue
        new_table_info.columns[actual_column_name] = column_info
      new_schema.tables[actual_table_name] = new_table_info
    return new_schema

  def add_info_from_schema(
      self, schema: "DatabaseSchema", field_names: List[str]
  ) -> None:
    """Adds additional field information from another schema to the current schema.

    Args:
        schema (DatabaseSchema): The schema to copy information from.
        field_names (List[str]): The list of field names to copy.
    """
    for table_name, table_info in self.tables.items():
      actual_table_name = schema.get_actual_table_name(table_name)
      if actual_table_name is None:
        continue
      for column_name, column_info in table_info.columns.items():
        actual_column_name = schema.get_actual_column_name(
            table_name, column_name
        )
        if actual_column_name is None:
          continue
        new_column_info = schema.tables[actual_table_name].columns[
            actual_column_name
        ]
        for field_name in field_names:
          set_field(
              column_info, field_name, getattr(new_column_info, field_name)
          )

  def to_dict(self) -> Dict[str, List[str]]:
    """Converts the DatabaseSchema to a dictionary representation.

    Returns:
        Dict[str, List[str]]: The dictionary representation of the schema.
    """
    return {
        table_name: list(table_info.columns.keys())
        for table_name, table_info in self.tables.items()
    }
