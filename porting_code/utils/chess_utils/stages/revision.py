import logging
from typing import Any, Dict, List

from nl2sql_eval.chess_utils.templates.revision import PROMPT
from nl2sql_eval.parsers import get_parser
from nl2sql_eval.utils import call_vertex_llm_with_cache


def revision(
    task: Any, sql: str, query_result: str, schema_str: str, model_name: str
) -> Dict[str, Any]:

  parser = get_parser("revision")
  request_kwargs = {
      "DATABASE_SCHEMA": schema_str,
      "HINT": task["hint"],
      "QUESTION": task["question"],
      "QUERY_RESULT": query_result,
      "SQL": sql,
  }
  retry_prompt = PROMPT.format(**request_kwargs)
  response = call_vertex_llm_with_cache(retry_prompt, model_name)
  result = parser.parse(response)
  result = {
      "chain_of_thought_reasoning": result.get(
          "chain_of_thought_reasoning", ""
      ),
      "SQL": result["revised_SQL"],
  }
  return result
