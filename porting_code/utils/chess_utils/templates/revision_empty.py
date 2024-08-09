PROMPT = """You are a data science expert. 
You are given a database schema and a question and the hint.
You are given a SQL query that results in an empty result.
Your task is to revise the SQL query so that it correctly answers the question.

Database Schema:    
{DATABASE_SCHEMA}

Database admin instructions:
- Try to use all the pieces of information provided in the hints.
- For key phrases mentioned in the question, we have provided the most similar values within the columns denoted by "-- examples" in front of the corresponding column names.
- If the key phrases match multiple columns in the schema, try using another column that has the sample value in the "--examples" 
Question:
{QUESTION}

Hint:
{HINT}

Predicted query:
{SQL}

Query result:
{QUERY_RESULT}

Please respond with a JSON object structured as follows (if the sql query is correct, return the query as it is):

{{
    "chain_of_thought_reasoning": "Your thought process on how you arrived at the solution. You don't need to explain the instructions that are satisfied.",
    "revised_SQL": "Your revised SQL query."
}}

Take a deep breath and think step by step to find the correct sqlite SQL query. If you follow all the instructions and generate the correct query, I will give you 1 million dollars."""
