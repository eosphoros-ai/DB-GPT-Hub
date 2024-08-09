import logging
from typing import Any, Dict, List
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from nl2sql_eval.chess_utils.templates.candidate_generation import PROMPT
from nl2sql_eval.chess_utils.templates.candidate_generation_with_examples import PROMPT as WITH_EXAMPLES_PROMPT
from nl2sql_eval.const import QUESTION_ANSWER_PROMPT
from nl2sql_eval.parsers import get_parser
from nl2sql_eval.synthetic_examples.templates.example_generation import PROMPT as SYNTHETIC_EXAMPLES_PROMPT
from nl2sql_eval.utils import call_vertex_llm_with_cache


def get_prompt_to_use(use_examples: bool) -> str:
  if use_examples:
    return WITH_EXAMPLES_PROMPT
  else:
    return PROMPT


def get_examples(schema_str: str, model_name: str) -> List[Dict[str, str]]:
  parser = get_parser("synthetic_examples")
  prompt = SYNTHETIC_EXAMPLES_PROMPT.format(schema=schema_str)
  response = call_vertex_llm_with_cache(
      prompt=prompt, model=model_name, tag="synthetic_examples"
  )
  example_list = parser.parse(response)
  examples_prompt = ""

  if example_list:
    for example in example_list:
      examples_prompt += QUESTION_ANSWER_PROMPT.format(
          question=example["question"], answer=example["sql"]
      )
  return examples_prompt


def candidate_generation(
    task: Any, schema_str: str, model_name: str, use_examples=True
) -> Dict[str, Any]:
  """Generates candidate SQL queries based on the task's question and evidence.

  Args:
      task (Any): The task object containing the question and evidence.
      tentative_schema (Dict[str, List[str]]): The current tentative schema.
      execution_history (List[Dict[str, Any]]): The history of executions.

  Returns:
      Dict[str, Any]: A dictionary containing the best SQL query result.
  """
  logging.info("Starting candidate generation")
  example_list = get_examples(schema_str, model_name)
  prompt_to_use = get_prompt_to_use(use_examples)

  parser = get_parser("candidate_generation")
  request_kwargs = {
      "DATABASE_SCHEMA": schema_str,
      "HINT": task["hint"],
      "QUESTION": task["question"],
      "EXAMPLES": example_list,
  }

  prompt = prompt_to_use.format(**request_kwargs)
  logging.info("Candidate generation prompt: %s", prompt)
  response = call_vertex_llm_with_cache(
      prompt=prompt, model=model_name, tag="candidate_generation"
  )

  response = parser.parse(response)

  result = response["SQL"]

  logging.info("Candidate generation completed successfully")
  return result


def get_example_parser():
  class SyntheticExamples(BaseModel):
    examples: List[Dict[str, str]] = Field(description="examples")

  parser = JsonOutputParser(pydantic_object=SyntheticExamples)
  return parser
