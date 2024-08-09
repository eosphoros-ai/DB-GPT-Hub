import logging
from typing import Any, Dict
from nl2sql_eval.chess_utils.templates.keyword_extraction import PROMPT
from nl2sql_eval.parsers import get_parser
from nl2sql_eval.utils import call_vertex_llm_with_cache


def keyword_extraction(
    task: Dict,
    model_name: str = "gemini-1.5-flash-preview-0514",
) -> Dict[str, Any]:
  """Extracts keywords from the task using an LLM chain call.

  Args:
      task (Any): The task object containing the evidence and question.

  Returns:
      Dict[str, Any]: A dictionary containing the extracted keywords.
  """
  request_kwargs = {
      "HINT": task["hint"],
      "QUESTION": task["question"],
  }

  prompt = PROMPT.format(**request_kwargs)
  parser = get_parser("keyword_extraction")
  logging.info("Initiating LLM call for keyword extraction")
  response = call_vertex_llm_with_cache(
      prompt=prompt, model=model_name, tag="keyword_extraction"
  )

  if response is not None:
    keywords = parser.parse(response)
    result = {"keywords": keywords}
    logging.info(f"Keywords extracted: {keywords}")
  else:
    result = {"keywords": []}

  return result
