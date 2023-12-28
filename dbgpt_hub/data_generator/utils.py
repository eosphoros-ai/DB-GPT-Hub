COT_PROMPT = """
Please use the following database information, genarate different difficulty level of natural language questions with their corresponding SQL querires.
There are three different difficulty levels:
When generating natual language questions and their corresponding SQL queries, you should consider different SQL operators such as  WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, JOIN, INTERSECT, EXCEPT, UNION, NOT IN, OR, AND, EXISTS, LIKE as well as nested queries.
Moreover, please make sure that each table in the database appears in at least one query.

There are three different difficulty levels, which are defined as follows:
Easy: Queries that require basic filtering or aggregation on a single table.
Medium: Queries that encompass more complex filtering or aggregation and involve joining multiple tables.
Hard: Queries that entail advanced filtering or aggregation, multiple joins, and the use of subqueries.

Here is the basic information of database: {schema}

Based on the tables, columns, primary keys, foreign keys and different difficulty levels, generate {easy_count} Easy, {medium_count} Medium, and {hard_count} Hard natural language questions with their correlated SQL queries.
Provide your answer in JSON form. Reply with only the answer in JSON form and include no other commentary:
RESPONSE FORMAT:
{few_shots_example}

The "db_id" in the above examples means the name of used database. Do not fill out it with "_database" suffix.
"""

FEW_SHOTS_EXAMPLE = """
[
  {
    'db_id': 'music_2',
    'question': 'Who performed the song named "Le Pop"?',
    'query': 'SELECT T2.firstname, T2.lastname FROM Performance AS T1 JOIN Band AS T2 ON T1.bandmate=T2.id JOIN Songs AS T3 ON T3.SongId=T1.SongId WHERE T3.Title="Le Pop"'
  },
  {
    'db_id': 'insurance_fnol',
    'question': 'Tell me the types of the policy used by the customer named "Dayana Robel".',
    'query': 'SELECT DISTINCT t3.policy_type_code FROM customers AS t1 JOIN customers_policies AS t2 ON t1.customer_id=t2.customer_id JOIN available_policies AS t3 ON t2.policy_id=t3.policy_id WHERE t1.customer_name="Dayana Robel"'
  }
]
"""