PROMPT = """Objective: Your objective is to make sure a query follows the database admin instructions and use the correct conditions.

Database Schema:    
{DATABASE_SCHEMA}

Database admin instructions:
1. When you need to find the highest or lowest values based on a certain condition, using ORDER BY + LIMIT 1 is prefered over using MAX/MIN within sub queries.
2. If predicted query includes an ORDER BY clause to sort the results, you should only include the column(s) used for sorting in the SELECT clause if the question specifically ask for them. Otherwise, omit these columns from the SELECT.
3. If the question doesn't specify exactly which columns to select, between name column and id column, prefer to select id column.
4. Make sure you only output the information that is asked in the question. If the question asks for a specific column, make sure to only include that column in the SELECT clause, nothing more.
5. Predicted query should return all of the information asked in the question without any missing or extra information.
7. For key phrases mentioned in the question, we have provided the most similar values within the columns denoted by "-- examples" in front of the corresponding column names. This is a crucial hint indicating the correct columns to use for your SQL query.
8. No matter of how many things the question asks, you should only return one SQL query as the answer having all the information asked in the question, seperated by a comma.
9. Using || ' ' ||  to concatenate is string is banned and using that is punishable by death. Never concatenate columns in the SELECT clause.
10. If you are joining multiple tables, make sure to use alias names for the tables and use the alias names to reference the columns in the query. Use T1, T2, T3, ... as alias names.
11. If you are doing a logical operation on a column, such as mathematical operations and sorting, make sure to filter null values within those columns.
12. When ORDER BY is used, just include the column name in the ORDER BY in the SELECT clause when explicitly asked in the question. Otherwise, do not include the column name in the SELECT clause.
13. When the response is empty, take a closer look at filters in the SQL and check if they are correct. You can use "-- examples" values to check if the filters are correct. If the filters are correct, then you can use the hint to revise the SQL.
14. When the response is empty, the columns used in the query may not be correct. You can try different column which also contains the same "-- examples" value to regenerate the SQL.



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
