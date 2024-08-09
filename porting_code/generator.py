class GeminiGeneratorSRG(QueryGenerator):

  def __init__(
      self,
      location: str = DEFAULT_GCP_PROJECT_LOCATION,
      project_id: str = DEFAULT_GCP_PROJECT_ID,
      query_executor: QueryExecutor = None,
      generation_config=None,
      logger=None,
      schema=None,
      foreign_key_relations=None,
      stages: Dict = {
          "keyword_extraction": {"model": MODEL_GEMINI_1_5_FLASH},
          "column_selection": {"model": MODEL_GEMINI_1_5_PRO},
          "candidate_generation": {"model": MODEL_GEMINI_1_5_PRO},
          "query_checker": {"model": MODEL_GEMINI_1_5_PRO},
      },
      db_dir: str = "",
      db_id: str = "",
      vector_db: Chroma = None,
      cache_path: str = "",
      execution_history_path: str = "",
      examples_path: str = "",
  ):
    super().__init__()
    self.name = "gemini-generator-with-checker-srg"
    if generation_config:
      assert isinstance(generation_config, GenerationConfig)
    vertexai.init(project=project_id, location=location)
    self.generation_config = (
        generation_config
        if generation_config is not None
        else GenerationConfig(**DEFAULT_MODEL_CONFIG)
    )
    self.query_executor = query_executor
    self.logger = logger if logger is not None else logging.getLogger()
    self.stages = stages
    self.db_dir = Path(db_dir)
    self.db_id = db_id
    self.schema = schema
    self.foreign_key_relations = foreign_key_relations
    self.vector_db = vector_db
    self.cache_path = cache_path
    self.full_schema = get_db_schema(
        db_path=str(self.db_dir / self.db_id / f"{self.db_id}.sqlite"),
    )
    self.lsh = None
    self.minihashes = None
    with (self.db_dir / f"{db_id}" / "preprocessed" / f"{db_id}_lsh.pkl").open(
        "rb"
    ) as f:
      self.lsh = pickle.load(f)
    with (
        self.db_dir / f"{db_id}" / "preprocessed" / f"{db_id}_minhashes.pkl"
    ).open("rb") as f:
      self.minihashes = pickle.load(f)

    self.execution_history_path = execution_history_path
    self.examples_path = examples_path

  def get_database_schema_string(
      self,
      tentative_schema: Dict[str, List[str]],
      schema_with_examples: Dict[str, List[str]],
      schema_with_descriptions: Dict[str, Dict[str, Dict[str, Any]]],
      include_value_description: bool,
  ) -> str:
    """Generates a schema string for the database.

    Args:
        tentative_schema (Dict[str, List[str]]): The tentative schema.
        schema_with_examples (Dict[str, List[str]]): Schema with example values.
        schema_with_descriptions (Dict[str, Dict[str, Dict[str, Any]]]): Schema
          with descriptions.
        include_value_description (bool): Whether to include value descriptions.

    Returns:
        str: The generated schema string.
    """
    schema_generator = DatabaseSchemaGenerator(
        tentative_schema=DatabaseSchema.from_schema_dict(tentative_schema),
        schema_with_examples=DatabaseSchema.from_schema_dict_with_examples(
            schema_with_examples
        )
        if schema_with_examples
        else None,
        schema_with_descriptions=DatabaseSchema.from_schema_dict_with_descriptions(
            schema_with_descriptions
        )
        if schema_with_descriptions
        else None,
        db_id=self.db_id,
        db_path=str(self.db_dir / self.db_id / f"{self.db_id}.sqlite"),
    )
    schema_string = schema_generator.generate_schema_string(
        include_value_description=include_value_description
    )
    schema_with_connections = schema_generator.get_schema_with_connections()
    return schema_string, schema_with_connections

  def add_columns_to_tentative_schema(
      self,
      tentative_schema: Dict[str, List[str]],
      selected_columns: Dict[str, List[str]],
  ) -> None:
    """Adds columns to the tentative schema based on selected columns.

    Args:
        tentative_schema (Dict[str, List[str]]): The tentative schema.
        selected_columns (Dict[str, List[str]]): The selected columns to add.
    """
    for table_name, columns in selected_columns.items():
      target_table_name = next(
          (
              t
              for t in tentative_schema.keys()
              if t.lower() == table_name.lower()
          ),
          None,
      )
      if target_table_name:
        for column in columns:
          if column.lower() not in [
              c.lower() for c in tentative_schema[target_table_name]
          ]:
            tentative_schema[target_table_name].append(column)
      else:
        tentative_schema[table_name] = columns

  def _dump_execution_history(self, key, value):
    with diskcache.Cache(self.execution_history_path) as cache_db:
      cache_db[key] = value

  def try_cache(self, call_func, cache_key):
    if self.cache_path:
      with diskcache.Cache(self.cache_path) as cache_db:
        if cache_key in cache_db:
          result = cache_db[cache_key]
        else:
          result = call_func()
          cache_db[cache_key] = result
    else:
      result = call_func()
    return result

  def check_query(
      self,
      selected_schema_str: str,
      full_schema_str: str,
      task,
      query: str,
      remaining_check_times: int = 3,
  ):
    if remaining_check_times > 1:
      schema_to_use = selected_schema_str
    else:
      schema_to_use = full_schema_str
    # first retry with selected schema
    if remaining_check_times == 0:
      self.logger.warning(
          "number of remaining checks ran out. Returning the query"
      )
      return query
    try:
      res = self.query_executor.execute(query=query)[0]
      if not res:
        self.logger.warning(f"check_query {query} failed with empty result")
        revision_result = revision(
            task=task,
            sql=query,
            query_result="query returned empty result",
            schema_str=schema_to_use,
            model_name=self.stages["query_checker"]["model"],
        )
        self.logger.info(f"revision_result: {revision_result}")
        return self.check_query(
            selected_schema_str,
            full_schema_str,
            task,
            revision_result["SQL"],
            remaining_check_times - 1,
        )

    except Exception as e:
      if "statement timeout" not in str(e):
        self.logger.warning(
            f"check_query {query} failed with non-timeout error: {e}"
        )
        revision_result = revision(
            task=task,
            sql=query,
            query_result=str(e),
            schema_str=schema_to_use,
            model_name=self.stages["query_checker"]["model"],
        )
        self.logger.info(f"revision_result: {revision_result}")
        return self.check_query(
            selected_schema_str,
            full_schema_str,
            task,
            revision_result["SQL"],
            remaining_check_times - 1,
        )

    self.logger.info(f"check_query succeeded: {query}")
    return query

  def generate(
      self,
      human_language_question: str,
      hint: str = "",
      db_id: str = "",
      eval_item_id: str = "",
      golden_sql: str = "",
  ):
    task = {"question": human_language_question, "hint": hint}
    self.logger.info(f"Question: {human_language_question}")
    self.logger.info(f"Hint: {hint}")

    # do keyword extraction
    keyword_extraction_model = self.stages["keyword_extraction"]["model"]
    keyword_extraction_result = keyword_extraction(
        task,
        model_name=keyword_extraction_model,
    )
    self.logger.info(keyword_extraction_result)
    # entity retrieval

    call_func = lambda: entity_retrieval(
        task,
        keyword_extraction_result["keywords"],
        self.schema,
        self.lsh,
        self.minihashes,
    )
    cache_key = (
        "entity_retrieval: "
        f"keywords: {keyword_extraction_result['keywords']} "
        f"question: {human_language_question} hint: {hint}"
    )
    entity_retrieval_result = self.try_cache(call_func, cache_key)
    self.logger.info(entity_retrieval_result)

    # context retrieval
    call_func = lambda: context_retrieval(
        task,
        keyword_extraction_result["keywords"],
        self.vector_db,
    )
    cache_key = (
        "context_retrieval: "
        f"keywords: {keyword_extraction_result['keywords']} "
        f"question: {human_language_question} hint: {hint}"
    )
    context_retrieval_result = self.try_cache(call_func, cache_key)
    # self.logger.info(context_retrieval_result)

    # correct_schema_str, _ = self.get_database_schema_string(
    #     get_sql_columns_dict(
    #         db_path=str(self.db_dir / self.db_id / f"{self.db_id}.sqlite"),
    #         sql=golden_sql,
    #     ),
    #     entity_retrieval_result["similar_values"],
    #     context_retrieval_result["schema_with_descriptions"],
    #     True,
    # )

    # create schema based on context retrieval and entity retrieval

    schema_str, _ = self.get_database_schema_string(
        self.full_schema,
        entity_retrieval_result["similar_values"],
        context_retrieval_result["schema_with_descriptions"],
        True,
    )
    self.logger.info(f"column selection schema: {schema_str}")
    # column selection
    column_selection_result = column_selection(
        task,
        self.full_schema,
        schema_str,
        self.stages["column_selection"]["model"],
    )
    selected_schema = column_selection_result["col_selection_schema"]
    self.logger.info(column_selection_result)

    # candidate generation
    # append similar columns to the selected schema
    self.add_columns_to_tentative_schema(
        selected_schema, entity_retrieval_result["similar_columns"]
    )

    # determine how good is the selected schema
    schema_status = missings_status(
        sql=golden_sql,
        tentative_schema=selected_schema,
        db_path=str(self.db_dir / self.db_id / f"{self.db_id}.sqlite"),
    )

    selected_schema_str, selected_schema_with_connections = (
        self.get_database_schema_string(
            selected_schema,
            entity_retrieval_result["similar_values"],
            context_retrieval_result["schema_with_descriptions"],
            True,
        )
    )

    schema_status["selected_schema_with_connections"] = (
        selected_schema_with_connections
    )

    self._dump_execution_history(
        f"selected_schema: {eval_item_id}", selected_schema_str
    )

    correct_schema_str, _ = self.get_database_schema_string(
        schema_status["correct_columns"],
        entity_retrieval_result["similar_values"],
        context_retrieval_result["schema_with_descriptions"],
        True,
    )

    selected_schema_with_connections_str, selected_schema_with_connections = (
        self.get_database_schema_string(
            selected_schema_with_connections,
            entity_retrieval_result["similar_values"],
            context_retrieval_result["schema_with_descriptions"],
            True,
        )
    )

    self.logger.info(f"candidate generation: {selected_schema_str}")

    revised_query = ""
    if False:
      examples = ""
      if self.examples_path:
        examples = pd.read_csv(self.examples_path)[
            lambda df: df["input_eval_item_id"] == eval_item_id
        ]["synthetic_examples"].to_numpy()[0]
      candidate_generation_result = candidate_generation(
          task,
          selected_schema_str,
          self.stages["candidate_generation"]["model"],
          examples,
      )
      self.logger.info(candidate_generation_result)

      # check query
      full_schema_str = self.get_database_schema_string(
          self.full_schema,
          entity_retrieval_result["similar_values"],
          context_retrieval_result["schema_with_descriptions"],
          include_value_description=True,
      )
      revised_query = self.check_query(
          selected_schema_str,
          full_schema_str,
          task,
          candidate_generation_result,
          remaining_check_times=3,
      )
    return (
        revised_query,
        0.0,
        {
            "schema_status": schema_status,
            "schema_strs": {
                "selected_schema": selected_schema_str,
                "selected_schema_with_connections": (
                    selected_schema_with_connections_str
                ),
                "correct_schema": correct_schema_str,
            },
        },
    )
