import os

### path config
ROOT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ROOT_PATH = "/root/autodl-tmp"
# MODELS_PARENT_PATH = "/home/model_files/codellama/"
# DEFAULT_FT_MODEL_NAME = "CodeLlama-7b-Instruct-hf"
MODELS_PARENT_PATH = "/home/model/"
DEFAULT_FT_MODEL_NAME = "Baichuan2-13B-Chat"
MODEL_PATH = os.path.join(MODELS_PARENT_PATH, DEFAULT_FT_MODEL_NAME)

# MODEL_PATH = os.path.join(ROOT_PATH, "model")
ADAPTER_PATH = os.path.join(ROOT_PATH, "dbgpt_hub/output/adapter")
MERGED_MODELS = os.path.join(ROOT_PATH, "dbgpt_hub/output/merged_models")

# DATA_PATH = "/root/autodl-tmp/data/spider/pre_processed_data"
# OUT_DIR= "/root/autodl-tmp/codellama"

DATA_PATH = os.path.join(ROOT_PATH, "dbgpt_hub/data")
PREDICTED_DATA_PATH = os.path.join(ROOT_PATH,
                                   "dbgpt_hub/data/eval_data/dev_sql.json")
PREDICTED_OUT_FILENAME = "pred_sql.sql"
# OUT_DIR = os.path.join(DATA_PATH, "out_pred")
OUT_DIR = os.path.join(ROOT_PATH, "dbgpt_hub/output/")

## model constants
IGNORE_INDEX = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "<s>"
DEFAULT_UNK_TOKEN = "<unk>"

LOG_FILE_NAME = "trainer_log.jsonl"

# head_state_dict,model save name
VALUE_HEAD_FILE_NAME = "value_head.bin"

# output ,finetuning_args save_to_json name
FINETUNING_ARGS_NAME = "finetuning_args.json"

#  when prepare_model_for_training ,layer_norm_names
LAYERNORM_NAMES = ["norm", "ln_f", "ln_attn", "ln_mlp"]
EXT2TYPE = {"csv": "csv", "json": "json", "jsonl": "json", "txt": "text"}

# text2sql dataset information for processing sql data
# TODO: BIRD \ WiKiSQL \ ...
SQL_DATA_INFO = [
    # {
    #     "data_source": "spider",
    #     "train_file": ["train_spider.json", "train_others.json"],
    #     "dev_file": ["test_data/dev.json"],
    #     "train_tables_file": "tables.json",
    #     "dev_tables_file": "test_data/tables.json",
    #     "db_id_name": "db_id",
    #     "output_name": "query",
    #     "is_multiple_turn": False,
    #     "train_tab_emb_file": "train_tab_emb.pickle",
    # "dev_tab_emb_file": "dev_tab_emb.pickle",
    # "train_col_emb_file": "train_col_emb.pickle",
    # "dev_col_emb_file": "dev_col_emb.pickle",
    # }
    {
        "data_source": "bird",
        "train_file": ["train/train.json"],
        "dev_file": ["dev/dev.json"],
        "train_tables_file": "train/train_tables.json",
        "dev_tables_file": "dev/dev_tables.json",
        "db_id_name": "db_id",
        "output_name": "SQL",
        "is_multiple_turn": False,
        "train_tab_emb_file": "train_tab_emb.pickle",
        "dev_tab_emb_file": "dev_tab_emb.pickle",
        "train_col_emb_file": "train_col_emb.pickle",
        "dev_col_emb_file": "dev_col_emb.pickle",
        "example_store_file": "example_store.pickle",
        "document_store_file": "doc_store.pickle",
    }
    # ,
    # {
    #     "data_source": "chase",
    #     "train_file": ["Chase/chase_train.json"],
    #     "dev_file": ["Chase/chase_dev.json"],
    #     "tables_file": "Chase/chase_tables.json",
    #     "db_id_name": "database_id",
    #     "is_multiple_turn": True,
    # }
    # ,
    # {
    #     "data_source": "cosql_dataset",
    #     "train_file": ["sql_state_tracking/cosql_train.json"],
    #     "dev_file": ["sql_state_tracking/cosql_dev.json"],
    #     "tables_file": "tables.json",
    #     "db_id_name": "database_id",
    #     "is_multiple_turn": True,
    # }
    # ,
    # {
    # {
    #     "data_source": "sparc",
    #     "train_file": ["train.json"],
    #     "train_tables_file": "tables.json",
    #     "dev_tables_file": "tables.json",
    #     "dev_file": ["dev.json"],
    #     "db_id_name": "database_id",
    #     "is_multiple_turn": True,
    #     "output_name": "query",
    # }
]

#### ICL Experimentation ####
BASIC_INSTRUCTION_PROMPT = """\
You are a SQLite SQL expert.
You need to generate SQLite SQL query given a question in natural language.
The database ("{db_name}") structure is defined by the following table schemas (comments after '--' provide additional column descriptions).

Given the "Table creation statements" and the "Question", you need understand the database and columns.

Consider the natural language question to SQL query "Examples".

Also consider the "Rules" and some useful "Hints" if provided.

***************************
###Rules###
- Try to use all the pieces of information provided in the hints.
- Column values/literals: Make sure that column values and literals are correct. Consider the column example values and hints provided.
- Table Aliases: Use aliases to avoid duplicate table name conflicts.
- Column References: Verify column names and use table_name.column_name format.
- Functions: Use correct SQLite functions for the intended data types.
- HAVING Clause: Employ boolean expressions (comparisons, AND, OR, NOT). Consider subqueries for top values.
- Table Joins: Ensure table names are correct and use appropriate joins.
- Arithmetic: Use basic operators (+, -, *, /) if dedicated functions are missing.
- Put double quotations around column names and table names, especially when there is a space in between words.
- Use double quotations for string literals.
- A single quote within the string can be encoded by putting two single quotes in a row (''): "Men's basketball" should be "Men''s basketball"
- When comparing string/text type in filter criteria, use LIKE operator and surround the text with wildcards %.
- When you need to find the highest or lowest values based on a certain condition, using ORDER BY with LIMIT 1 is prefered over using MAX/MIN within sub queries.
- If the question doesn't specify exactly which columns to select, between name column and id column, prefer to select id column.
***************************
###Table creation statements###
{schema}
***************************
###Examples###
{examples}
***************************
###Documentation###
{documentation}
***************************
###Question###
{question}

(Hints: {hints})
***************************
Now generate SQLite SQL query to answer the given "Question".

Output the SQL query string ONLY.
"""

NOT_NULL_TEMPLATE = """You are a SQLite SQL exeprt.

You have written a SQL query, "SQL", to answer a user question, "Question".

***************************
###SQL###
{sql}
***************************
###Question###
{question}
***************************

Your job is to verify and fix the SQL query if needed.

Your verification should be based on the following rules:
- If you are doing a logical operation on a column, such as mathematical operations and sorting, make sure to filter null values within those columns
- When ORDER BY is used, just include the column name in the ORDER BY in the SELECT clause when explicitly asked in the question. Otherwise, do not include the column name in the SELECT clause.

See if you should modify the SQL to satify the verification rules above. Return the updated SQL query. Make sure that the SQL query is in SQLite dialect.
If the SQL already satisfies the rules or the rules are not applicable, then just return the original SQL.

Just return the SQL query string.
"""

COT_INSTRUCTION_PROMPT = """\
You are a SQLite SQL expert.
You need to generate SQLite SQL query given a question in natural language.
The database ("{db_name}") structure is defined by the following table schemas (comments after '--' provide additional column descriptions).

Given the "Table creation statements" and the "Question", you need understand the database and columns.

Always output the steps to decompose the question into subquestions for text-to-SQL generation.
Start the answer with ###Answer### followed by the line "Decompose the question into sub questions, considering the【Rules】, and generate the SQL after thinking step by step:"

When you are OK with the generated query, output the postgres query string ONLY inside the xml delimiter <FINAL_ANSWER></FINAL_ANSWER>.
===========
Example 1
**************************
###Table creation statements###
CREATE TABLE account (
    account_id INT PRIMARY KEY,
    district_id INT REFERENCES district(district_id),
    frequency VARCHAR(255) NOT NULL,
    date DATE NOT NULL
);
CREATE TABLE client (
    client_id INT PRIMARY KEY,
    gender CHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    district_id INT REFERENCES district(district_id)
);
CREATE TABLE district (
    district_id INT PRIMARY KEY,
    a4 VARCHAR(255) NOT NULL, -- Assuming A4 and A11 are strings due to examples
    a11 VARCHAR(255) NOT NULL
);
**************************
###Question###
What is the gender of the youngest client who opened account in the lowest average salary branch? Given that Later birthdate refers to younger age; A11 refers to average salary

###Answer###
Decompose the question into sub questions, considering the【Rules】, and generate the SQL after thinking step by step:
Sub question 1: What is the district_id of the branch with the lowest average salary?
SQL
```sql
SELECT "district"."district_id"
  FROM "district"
  ORDER BY "A11" ASC NULLS LAST
  LIMIT 1
```

Sub question 2: What is the youngest client who opened account in the lowest average salary branch?
SQL
```sql
SELECT "T1"."client_id"
  FROM "client" AS "T1"
  INNER JOIN "district" AS "T2"
  ON "T1"."district_id" = "T2"."district_id"
  ORDER BY "T2"."A11" ASC, "T1"."birth_date" DESC NULLS LAST
  LIMIT 1
```

Sub question 3: What is the gender of the youngest client who opened account in the lowest average salary branch?
SQL
```sql
SELECT "T1"."gender"
  FROM "client" AS "T1"
  INNER JOIN "district" AS "T2"
  ON "T1"."district_id" = "T2"."district_id"
  ORDER BY "T2"."A11" ASC, "T1"."birth_date" DESC NULLS LAST
  LIMIT 1
```
Question Solved.

<FINAL_ANSWER>
SELECT "T1"."gender"
  FROM "client" AS "T1"
  INNER JOIN "district" AS "T2"
  ON "T1"."district_id" = "T2"."district_id"
  ORDER BY "T2"."A11" ASC, "T1"."birth_date" DESC NULLS LAST
  LIMIT 1
</FINAL_ANSWER>

===========
Example 2
**************************
###Table creation statements###
CREATE TABLE frpm (
    2013-14 CALPADS Fall 1 Certification Status bigint, -- 2013-14 CALPADS Fall 1 Certification Status
    Academic Year text, -- Academic Year
    CDSCode bigint, -- CDSCode
    Charter Funding Type text, -- Charter Funding Type
    Charter School (Y/N) double precision, -- Charter School (Y/N)
    County Code bigint, -- County Code
    County Name text, -- County Code
    District Code bigint, -- District Code Type
    Educational Option Type text, -- Educational Option Type
    Enrollment (Ages 5-17) double precision, -- Enrollment (Ages 5-17)
    Enrollment (K-12) double precision, -- Enrollment (K-12)
    Percent (%) Eligible Free (Ages 5-17) double precision,
    Percent (%) Eligible Free (K-12) double precision,
    School Name text, -- School Name
    School Type text,
);
**************************
###Question###
What is the highest eligible free rate for K-12 students in the schools in Alameda County? Eligible free rate for K-12 = "Free Meal Count (K-12)" / "Enrollment (K-12)"

###Answer###
Decompose the question into sub questions, considering the【Rules】, and generate the SQL after thinking step by step:
Sub question 1: What is the highest eligible free rate for K-12 students in the schools in Alameda County?
SQL
```sql
SELECT MAX("Percent (%) Eligible Free (K-12)")
  AS "Highest Eligible Free Rate for K-12 Students"
  FROM "frpm" WHERE "County Name" = 'Alameda' and "Percent (%) Eligible Free (K-12)" IS NOT NULL;
```
Question Solved.

<FINAL_ANSWER>
SELECT MAX("Percent (%) Eligible Free (K-12)")
  AS "Highest Eligible Free Rate for K-12 Students"
  FROM "frpm" WHERE "County Name" = 'Alameda' and "Percent (%) Eligible Free (K-12)" IS NOT NULL;
</FINAL_ANSWER>

===========
Example 3 (When it's not clear which column should be used for a string matching, use a loosen condition such as string LIKE and OR condition to cover multiple possible columns.)
**************************
###Table creation statements###
CREATE TABLE "student_programs" (
    "Program Type" text, -- Program Type Example values: ['Summer School', 'After School Program', 'Special Education']
    "Participants (Ages 10-15)" double precision, -- Participants (Ages 10-15) Example values: ['1250.0', '500.0', '75.0']
    "Total Enrollment (Ages 10-15)" double precision, -- Total Enrollment (Ages 10-15) Example values: ['500.0', '1800.0', '1000.0']
    "School Category" text, --  Example values: ['Charter Schools', 'Private Schools', 'Magnet Schools']
);
**************************
###Question###
Please list the lowest three participation rates for students aged 10-15 in online programs. Participation rate for students aged 10-15 = "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)"
###Answer###
Decompose the question into sub questions, considering the【Rules】, and generate the SQL after thinking step by step:

Sub question 1: List all the online programs. The given table has "School Category" and "Program Type" columns.
It's not clear which column contains information about online programs. We can do a wildcard matching on both columns.
SQL
```sql
SELECT * from "student_programs" WHERE LOWER("School Category") LIKE '%online%' OR LOWER("Program Type") LIKE '%online%';
```

Sub question 2:

Please list the lowest three participation rates for students aged 10-15 in all programs, given that participation rate for students aged 10-15 = "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)"
SQL
```sql
SELECT "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" FROM "student_programs"
  WHERE "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" IS NOT NULL
  ORDER BY "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" ASC NULLS LAST LIMIT 3;
```

Sub question 3: Please list the lowest three participation rates for students aged 10-15 in online programs. Participation rate for students aged 10-15 = "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)"
SQL
```sql
SELECT "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" FROM "student_programs"
  WHERE LOWER("School Category") LIKE '%online%' OR LOWER("Program Type") LIKE '%online%'
  AND "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" IS NOT NULL
  ORDER BY "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" ASC NULLS LAST LIMIT 3;
```
Question Solved.

<FINAL_ANSWER>
SELECT "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" FROM "student_programs"
  WHERE LOWER("School Category") LIKE '%online%' OR LOWER("Program Type") LIKE '%online%'
  AND "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" IS NOT NULL
  ORDER BY "Participants (Ages 10-15)" / "Total Enrollment (Ages 10-15)" ASC NULLS LAST LIMIT 3;
</FINAL_ANSWER>

=============

Now here is the real table creation statement and the question. Remember to generate the most concise SQL query.

Also consider the "Rules" and some useful "Hints" if provided.

***************************
###Rules###
- Verify column names and use table_name.column_name format.
- Functions: use correct SQLite SQL functions for the intended data types.
- HAVING Clause: Employ boolean expressions (comparisons, AND, OR, NOT). Consider subqueries for top values.
- Table Joins: Ensure table names are correct and use appropriate joins.
- Arithmetic: Use basic operators (+, -, *, /) if dedicated functions are missing.
***************************
###Hints###
{hints}
***************************
###Table creation statements###
{schema}
***************************
###Question###
{question}
"""

MAJORITY_VOTING = """You are a SQLite SQL expert.

You need to the most likely or correct SQLite SQL from a set of candidates that answers a question in natural language.

The database structure is defined by the following table schemas (comments after '--' provide additional column descriptions).

Given the "Table creation statements" and the "Question", you need understand the database and columns.

Consider the natural language question to SQL query "Examples".

Also consider the "Rules" and some useful "Hints" if provided.

***************************
{input}
***************************
Now consider the following SQL candidates and pick a single SQL query that most likely and correctly
answers the given "Question":
{candidates}

Only return a single SQL query from the candidates and the SQL only as a string.
"""

SYNTAX_FIXER_TEMPLATE = """You are a SQLite SQL expert.
You need to check the syntax of a given SQL query. Check if the query follows the rules. If not, fix it.
- Put double quotations around column names and table names, especially when there is a space in between words.
- Use double quotations for string literals.
- Use "IS NOT NULL" in WHERE clause unless the question is asking for NULL values.
- SQLite is case-insensitive by default for identifiers.
- Be mindful of implicit conversions and potential type mismatches.

If there was no problem with the query, just output the original query.
Use Chain of Thought to generate the output. Think step by step. Analyze the given queries against the rules.
Output the final query string ONLY inside the xml delimiter <FINAL_ANSWER></FINAL_ANSWER>.

===== Example 1 =====
###Question###
Please list the lowest three eligible free rates for students aged 5-17 in continuation schools. Eligible free rates for students aged 5-17 = "Free Meal Count (Ages 5-17)" / "Enrollment (Ages 5-17)"

###SQL Query to check###
SELECT `Free Meal Count (Ages 5-17)` / `Enrollment (Ages 5-17)`
  FROM frpm WHERE `Educational Option Type` = 'Continuation School'
  ORDER BY `Free Meal Count (Ages 5-17)` / `Enrollment (Ages 5-17)` ASC LIMIT 3;

###Answer###
In the query, the table name "frpm" is not quoted. It should be quoted.
The WHERE clause should exclude NULL values.

The fixed query should be:
SELECT "Free Meal Count (Ages 5-17)" / "Enrollment (Ages 5-17)"
  FROM "frpm" WHERE "Educational Option Type" = "Continuation School"
  AND "Free Meal Count (Ages 5-17)" / "Enrollment (Ages 5-17)" IS NOT NULL
  ORDER BY "Free Meal Count (Ages 5-17)" / "Enrollment (Ages 5-17)" ASC LIMIT 3;

<FINAL_ANSWER>
SELECT "Free Meal Count (Ages 5-17)" / "Enrollment (Ages 5-17)"
  FROM "frpm" WHERE "Educational Option Type" = "Continuation School"
  AND "Free Meal Count (Ages 5-17)" / "Enrollment (Ages 5-17)" IS NOT NULL
  ORDER BY "Free Meal Count (Ages 5-17)" / "Enrollment (Ages 5-17)" ASC LIMIT 3;
</FINAL_ANSWER>

**************************
Now here is the real question.
###Question###
{}

###SQL Query to check###
{}

###Answer###
"""

EXAMPLE_GENERATOR = """You are a SQLite SQL expert.
Your job is to create a set of examples, where each example consists of a question and a SQL query to fetch the data for it.

You should generate examples that examine and showcase different aspects and relationships of the following table schemas.
Understand the database tables and their relationships. Understand the columns and their types and meanings to construct intresting examples.

I will also show you multiple examples generated for the other database and its table schemas, so you can see what
kind of examples can be generated for a given database.

**************************
###Examples from other database###
The following is the table schemas and column examples for other database:

The database (\"world_development_indicators\") structure is defined by the following table schemas (comments after '--' provide additional column descriptions).

CREATE TABLE `Country` (\n  `CountryCode` text, -- Country Code Example values: ['ABW', 'ADO', 'AFG', 'AGO', 'ALB', 'ARB', 'ARE', 'ARG', 'ARM', 'ASM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CEB', 'CHE', 'CHI', 'CHL', 'CHN', 'CIV', 'CMR', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CSS', 'CUB', 'CUW', 'CYM'] \n  `ShortName` text, -- Short Name Example values: ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Arab World', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Caribbean small states', 'Cayman Islands', 'Central African Republic', 'Central Europe and the Baltics', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', \"Côte d'Ivoire\", 'Croatia', 'Cuba'] \n  `TableName` text, -- Table Name Example values: ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Arab World', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Caribbean small states', 'Cayman Islands', 'Central African Republic', 'Central Europe and the Baltics', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Rep.', 'Costa Rica', \"Côte d'Ivoire\", 'Croatia', 'Cuba'] \n  `LongName` text, -- Long Name Example values: ['Islamic State of Afghanistan', 'Republic of Albania', \"People's Democratic Republic of Algeria\", 'American Samoa', 'Principality of Andorra', \"People's Republic of Angola\", 'Antigua and Barbuda', 'Arab World', 'Argentine Republic', 'Republic of Armenia', 'Aruba', 'Commonwealth of Australia', 'Republic of Austria', 'Republic of Azerbaijan', 'Kingdom of Bahrain', \"People's Republic of Bangladesh\", 'Barbados', 'Republic of Belarus', 'Kingdom of Belgium', 'Belize', 'Republic of Benin', 'The Bermudas', 'Kingdom of Bhutan', 'Plurinational State of Bolivia', 'Bosnia and Herzegovina', 'Republic of Botswana', 'Federative Republic of Brazil', 'Brunei Darussalam', 'Republic of Bulgaria', 'Burkina Faso', 'Republic of Burundi', 'Republic of Cabo Verde', 'Kingdom of Cambodia', 'Republic of Cameroon', 'Canada', 'Caribbean small states', 'Cayman Islands', 'Central African Republic', 'Central Europe and the Baltics', 'Republic of Chad', 'Channel Islands', 'Republic of Chile', \"People's Republic of China\", 'Republic of Colombia', 'Union of the Comoros', 'Republic of Congo', 'Republic of Costa Rica', \"Republic of Côte d'Ivoire\", 'Republic of Croatia', 'Republic of Cuba'] \n  `Alpha2Code` text, -- Alpha to Code Example values: ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AG', '1A', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BR', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'S3', 'KY', 'CF', 'B8', 'TD', '', 'CL', 'CN', 'CO', 'KM', 'CG', 'CR', 'CI', 'HR', 'CU'] \n  `CurrencyUnit` text, -- Currency Unit Example values: ['Afghan afghani', 'Albanian lek', 'Algerian dinar', 'U.S. dollar', 'Euro', 'Angolan kwanza', 'East Caribbean dollar', '', 'Argentine peso', 'Armenian dram', 'Aruban florin', 'Australian dollar', 'New Azeri manat', 'Bahraini dinar', 'Bangladeshi taka', 'Barbados dollar', 'Belarusian rubel', 'Belize dollar', 'West African CFA franc', 'Bermuda dollar', 'Bhutanese ngultrum', 'Bolivian Boliviano', 'Bosnia and Herzegovina convertible mark', 'Botswana pula', 'Brazilian real', 'Brunei dollar', 'Bulgarian lev', 'Burundi franc', 'Cabo Verde escudo', 'Cambodian riel', 'Central African CFA franc', 'Canadian dollar', 'Cayman Islands dollar', 'Pound sterling', 'Chilean peso', 'Chinese yuan', 'Colombian peso', 'Comorian franc', 'Costa Rican colon', 'Croatian kuna', 'Cuban peso', 'Netherlands Antillean guilder', 'Czech koruna', \"Democratic People's Republic of Korean won\", 'Congolese franc', 'Danish krone', 'Djibouti franc', 'Dominican peso', 'Egyptian pound', 'Eritrean nakfa'] \n  `SpecialNotes` text, -- Special Notes Example values: ['Fiscal year end: March 20; reporting period for national accounts data: FY (from 2013 are CY). Natio...[141 truncated]', '', 'April 2013 database update: Based on IMF data, national accounts data were revised for 2000 onward; ...[30 truncated]', 'April 2012 database update: Based on official government statistics, national accounts data were rev...[52 truncated]', 'Arab World aggregate. Arab World is composed of members of the League of Arab States.', 'The base year has changed to 2004.', 'SNA data for 2000-2011 are updated from official government statistics; 1994-1999 from UN databases....[41 truncated]', 'Fiscal year end: June 30; reporting period for national accounts data: FY. Value added current serie...[114 truncated]', 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', 'April 2012 database update: National accounts historical expenditure series in constant prices were ...[89 truncated]', 'Based on official government statistics; the new base year is 2010.', 'Fiscal year end: June 30; reporting period for national accounts data: FY. The new base year is 2005...[4 truncated]', 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', 'April 2013 database update: Data were updated using the government of Bhutan macroeconomic framework...[1 truncated]', 'Based on official government statistics for chain linked series; the new reference year is 2010.', 'Fiscal year end: March 31; reporting period for national accounts data: CY. Based on official govern...[155 truncated]', 'The new reference year for chain linked series is 2010. April 2011 database update: The National Sta...[139 truncated]', 'Cabo Verde is the new name for the country previously listed as Cape Verde. Based on official govern...[115 truncated]', 'Fiscal year end: March 31; reporting period for national accounts data: CY.', 'Caribbean small states aggregate. Includes Antigua and Barbuda, The Bahamas, Barbados, Belize, Guyan...[129 truncated]', 'Central Europe and the Baltics aggregate.', 'Based on IMF data, national accounts data have been revised for 2005 onward; the new base year is 20...[3 truncated]', 'On 1 July 1997 China resumed its exercise of sovereignty over Hong Kong; and on 20 December 1999 Chi...[155 truncated]', 'April 2013 database update: Based on IMF data, national accounts data were revised for 1990 onward; ...[30 truncated]', 'The new base year is 2009.', 'The new reference year for chain linked series is 2010. April 2013 database update: Based on officia...[81 truncated]', 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', 'Based on official government statistics; the new base year 2005.', 'East Asia and Pacific regional aggregate (including high-income economies).', 'East Asia and Pacific regional aggregate (does not include high-income economies).', 'National accounts have been revised from 1965 onward based on official government data; the new base...[98 truncated]', 'Fiscal year end: June 30; reporting period for national accounts data: FY. The new base year is 2001...[4 truncated]', 'National accounts have been revised from 1980 onward based on IMF data and official government stati...[33 truncated]', 'April 2013 database update: Based on IMF data, national accounts data were revised for 2000 onward; ...[30 truncated]', 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', 'Fiscal year end: July 7; reporting period for national accounts data: FY. Based on IMF data, nationa...[80 truncated]', 'Euro area aggregate.', 'Europe and Central Asia regional aggregate (including high-income economies).', 'Europe and Central Asia regional aggregate (does not include high-income economies).', 'European Union aggregate.', 'Based on data from the Bureau of Statistics, national accounts data on the expenditure side have bee...[54 truncated]', 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', 'Fragile situations aggregate. Note:  Countries with fragile situations are primarily International D...[155 truncated]', 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', 'Based on IMF data and official government statistics; the new base year is 2001.', 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', \"In 2010, the Ghana Statistical Service revised the base year for Ghana's national accounts series fr...[143 truncated]\", 'A simple multiplier is used to convert the national currencies of EMU members to euros. The followin...[155 truncated]', 'In 2010, national accounts data for 2003-09 were revised. The new data had broader coverage of all s...[100 truncated]', 'In 2010, the Bureau of Statistics introduced a new series of GDP rebased to year 2006. Current price...[56 truncated]'] \n  `Region` text, -- Region Example values: ['South Asia', 'Europe & Central Asia', 'Middle East & North Africa', 'East Asia & Pacific', 'Sub-Saharan Africa', 'Latin America & Caribbean', '', 'North America'] \n  `IncomeGroup` text, -- Income Group Example values: ['Low income', 'Upper middle income', 'High income: nonOECD', '', 'Lower middle income', 'High income: OECD'] \n  `Wb2Code` text, -- world bank to code Example values: ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AG', '1A', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BR', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'S3', 'KY', 'CF', 'B8', 'TD', 'JG', 'CL', 'CN', 'CO', 'KM', 'CG', 'CR', 'CI', 'HR', 'CU'] \n  `NationalAccountsBaseYear` text, -- National Accounts Base Year Example values: ['2002/03', 'Original chained constant price data are rescaled.', '1980', '', '2000', '2002', '2006', '2004', '2010', '2005/06', '1974', '2007', '1990', '1995', '1999', '2005', '2003', '2008', '1991', '2009', '1997', '2001/02', '2010/11', '2001', '1986/87', '2011/12', '2004/05', '1994', '2012', '1984', '1987', '2003/04', '2000/01', '1998', '1953/54', '2013', '2011', '2008/09', '1985', '1981/82. Reporting period switch from fiscal year to calendar year from 1996. Pre-1996 data converte...[19 truncated]', '2009/10', '1982'] \n  `NationalAccountsReferenceYear` text, -- National Accounts Reference Year Example values: ['', '1996', '2013/14', '2010', '2000', '2007', '2005', '2013', '1995', '2003', '1997'] \n  `SnaPriceValuation` text, -- SNA Price Valuation Example values: ['Value added at basic prices (VAB)', '', 'Value added at producer prices (VAP)'] \n  `LendingCategory` text, -- Lending Category Example values: ['IDA', 'IBRD', '', 'Blend'] \n  `OtherGroups` text, -- Other groups Example values: ['HIPC', '', 'Euro area'] \n  `SystemOfNationalAccounts` text, -- System Of National Accounts Example values: ['Country uses the 1993 System of National Accounts methodology.', 'Country uses the 1968 System of National Accounts methodology.', '', 'Country uses the 2008 System of National Accounts methodology.'] \n  `AlternativeConversionFactor` text, -- Alternative Conversion Factor Example values: ['', '1991\\x9696', '1971\\x9684', '1990\\x9695', '1992\\x9695', '1992', '1960\\x9685', '1978\\x9689, 1991\\x9692', '1992\\x9693', '1978\\x9693', '1992\\x9694', '1993', '1999\\x962001', '1965\\x9684', '1987\\x9695', '1973\\x9687', '1991', '1988\\x9689', '1980\\x962002', '1997, 2004', '1986', '1965\\x9695', '1971\\x9698', '1989', '1985\\x9690', '1987\\x9689, 1992', '1994', '1977\\x9690', '1970\\x962010', '1987\\x9695, 1997\\x962007', '1990\\x9696', '1990\\x9692', '1991, 1998'] \n  `PppSurveyYear` text, -- purchasing power parity survey year Example values: ['', 'Rolling', '2011', '2011 (household consumption only).'] \n  `BalanceOfPaymentsManualInUse` text, -- Balance Of Payments Manual In Use Example values: ['', 'IMF Balance of Payments Manual, 6th edition.'] \n  `ExternalDebtReportingStatus` text, -- External Debt Reporting Status Example values: ['Actual', '', 'Preliminary', 'Estimate'] \n  `SystemOfTrade` text, -- System Of Trade Example values: ['General trade system', 'Special trade system', ''] \n  `GovernmentAccountingConcept` text, -- Government Accounting Concept Example values: ['Consolidated central government', 'Budgetary central government', ''] \n  `ImfDataDisseminationStandard` text, -- International Monetory Fund Data Dissemination Standard Example values: ['General Data Dissemination System (GDDS)', '', 'Special Data Dissemination Standard (SDDS)'] \n  `LatestPopulationCensus` text, -- Latest Population Census Example values: ['1979', '2011', '2008', '2010', '2011. Population data compiled from administrative registers.', '2014', '', '2009', '2013', '2005', '2012', '2006', '2003', 'Guernsey: 2009; Jersey: 2011.', '2007', '1984', '2002', '2006. Rolling census based on continuous sample survey.', '1997', '2004', '1943', '1993', '1998', '1987', '2001', '1989'] \n  `LatestHouseholdSurvey` text, -- Latest Household Survey Example values: ['Multiple Indicator Cluster Survey (MICS), 2010/11', 'Demographic and Health Survey (DHS), 2008/09', 'Multiple Indicator Cluster Survey (MICS), 2012', '', 'Malaria Indicator Survey (MIS), 2011', 'Multiple Indicator Cluster Survey (MICS), 2011/12', 'Demographic and Health Survey (DHS), 2010', 'Demographic and Health Survey (DHS), 2006', 'Demographic and Health Survey (DHS), 2014; HIV/Maternal and Child Health (HIV/MCH) Service Provision...[24 truncated]', 'Multiple Indicator Cluster Survey (MICS), 2011', 'Multiple Indicator Cluster Survey (MICS), 2014', 'Multiple Indicator Cluster Survey (MICS), 2010', 'Demographic and Health Survey (DHS), 2008', 'Multiple Indicator Cluster Survey (MICS), 2000', 'World Health Survey (WHS), 2003', 'Living Standards Measurement Study Survey (LSMS), 2007', 'Malaria Indicator Survey (MIS), 2014', 'Malaria Indicator Survey (MIS), 2012', 'Demographic and Health Survey (DHS), 2005', 'Demographic and Health Survey (DHS), 2014', 'National Sample Survey on Population Change (NSS), 2013', 'Demographic and Health Survey (DHS), 2012', 'Demographic and Health Survey (DHS), 2011/12', 'Multiple Indicator Cluster Survey (MICS), 2009', 'Demographic and Health Survey (DHS), 2013/14', 'Multiple Indicator Cluster Survey (MICS), 2006', 'Reproductive Health Survey (RHS), 2004', 'Demographic and Health Survey (DHS), 2011', 'Demographic and Health Survey (DHS), 2002', 'HIV/Maternal and Child Health (HIV/MCH) Service Provision Assessments (SPA), 2014', 'Multiple Indicator Cluster Survey (MICS), 2005; Reproductive Health Survey (RHS), 2005', 'Reproductive Health Survey (RHS), 1985', 'Reproductive Health Survey (RHS), 2008/09', 'HIV/Maternal and Child Health (HIV/MCH) Service Provision Assessments (SPA), 2013', 'Demographic and Health Survey (DHS), 2005/06', \"Iran's Multiple Indicator Demographic and Health Survey (IrMIDHS), 2010\", 'Kiribati Demographic and Health Survey (KDHS), 2009', 'Multiple Indicator Cluster Survey (MICS), 2013/14', 'Family Health Survey (FHS), 1996', 'Family Health Survey (FHS), 2004', 'Demographic and Health Survey (DHS), 2013', 'Family Health Survey (FHS), 2007', 'Malaria Indicator Survey (MIS), 2013', 'Demographic and Health Survey (DHS), 2009', 'Demographic and Health Survey (DHS), 2012/13', 'Republic of the Marshall Islands Demographic and Health Survey (RMIDHS), 2007', 'National Survey of Demographic Dynamics (ENADID), 2009', 'Multiple Indicator Cluster Survey (MICS), 2013', 'Multiple Indicator Cluster Survey (MICS)/Pan Arab Project for Family Health (PAPFAM), 2006', 'Multiple Indicator Cluster Survey (MICS), 2009/10'] \n  `SourceOfMostRecentIncomeAndExpenditureData` text, -- Source Of Most Recent Income And Expenditure Data Example values: ['Integrated household survey (IHS), 2008', 'Living Standards Measurement Study Survey (LSMS), 2011/12', 'Integrated household survey (IHS), 1995', '', 'Integrated household survey (IHS), 2008/09', 'Integrated household survey (IHS), 2012', 'Expenditure survey/budget survey (ES/BS), 2003', 'Integrated household survey (IHS), 2004', 'Integrated household survey (IHS), 2010', 'Integrated household survey (IHS), 2013', 'Integrated household survey (IHS), 2000', 'Labor force survey (LFS), 1999', 'Core Welfare Indicator Questionnaire Survey (CWIQ), 2011/12', 'Living Standards Measurement Study Survey (LSMS), 2007', 'Expenditure survey/budget survey (ES/BS), 2009/10', 'Expenditure survey/budget survey (ES/BS), 2012', 'Core Welfare Indicator Questionnaire Survey (CWIQ), 2009', 'Core Welfare Indicator Questionnaire Survey (CWIQ), 2006', 'Core Welfare Indicator Questionnaire Survey (CWIQ), 2007', 'Integrated household survey (IHS), 2011', 'Priority survey (PS), 2007', 'Labor force survey (LFS), 2010', 'Priority survey (PS), 2008', 'Priority survey (PS), 2011', 'Core Welfare Indicator Questionnaire Survey (CWIQ)/Priority survey (PS), 2011', '1-2-3 survey (1-2-3), 2005/06', 'Income tax registers (ITR), 2010', 'Priority survey (PS), 2002', 'Expenditure survey/budget survey (ES/BS), 2011', 'Priority survey (PS), 2006', 'Priority survey (PS), 1993', 'Expenditure survey/budget survey (ES/BS), 2010/11', 'Expenditure survey/budget survey (ES/BS), 2008/09', 'Expenditure survey/budget survey (ES/BS), 2005', 'Core Welfare Indicator Questionnaire Survey (CWIQ)/Integrated household survey (IHS), 2005', 'Living Standards Measurement Study Survey (LSMS), 2012', 'Living Standards Measurement Study Survey (LSMS), 2011', 'Core Welfare Indicator Questionnaire Survey (CWIQ), 2012', 'Core Welfare Indicator Questionnaire Survey (CWIQ), 2010', 'Integrated household survey (IHS), 1998', 'Integrated household survey (IHS), 2011/12', 'Expenditure survey/budget survey (ES/BS), 2010', 'Income survey (IS), 2010', 'Living Standards Measurement Study Survey (LSMS), 2010', 'Expenditure survey/budget survey (ES/BS), 2013', 'Integrated household survey (IHS), 2005/06', 'Expenditure survey/budget survey (ES/BS), 1998', 'Priority survey (PS), 2010', 'Integrated household survey (IHS), 2010/11', 'Income survey (IS), 2012'] \n  `VitalRegistrationComplete` text, -- Vital Registration Complete Example values: ['', 'Yes', 'Yes. Vital registration for Guernsey and Jersey.'] \n  `LatestAgriculturalCensus` text, -- Latest Agricultural Census Example values: ['2013/14', '2012', '', '2007', '2015', '2013', '2011', '2010', '2008', '2010. Population and Housing Census.', '2011/12', '2009', '2011. Population and Housing Census.', '2006', '2014', '2010/ 2011', '2012/13', '2013/15', '2009/2010', '2007/2008', '2013/ 2014', '2008/ 2009', '2011/2012', '2009. Population and Housing Census.', '2010/11', '2008. Population and Housing Census.', '2013/2014', '2006/ 2007', '2009/ 2010', '2011/ 2012', '2004-2008', '2012/ 2013', '2007. Population and Housing Census.', '2007/08', '2014/ 2015', '2012 /2013'] \n  `LatestIndustrialData` integer, -- Latest Industrial Data Example values: ['2011', '2010', '2002', '2008', '2007'] \n  `LatestTradeData` integer, -- Latest Trade Data Example values: ['2013', '2006', '2012', '2011', '2007'] \n  `LatestWaterWithdrawalData` integer, -- Latest Water Withdrawal Data Example values: ['2000', '2006', '2001', '2005', '2011'] \n);\nCREATE TABLE `Series` (\n  `SeriesCode` text, -- Series Code Example values: ['AG.AGR.TRAC.NO', 'AG.CON.FERT.PT.ZS', 'AG.CON.FERT.ZS', 'AG.LND.AGRI.K2', 'AG.LND.AGRI.ZS', 'AG.LND.ARBL.HA', 'AG.LND.ARBL.HA.PC', 'AG.LND.ARBL.ZS', 'AG.LND.CREL.HA', 'AG.LND.CROP.ZS', 'AG.LND.EL5M.ZS', 'AG.LND.FRST.K2', 'AG.LND.FRST.ZS', 'AG.LND.IRIG.AG.ZS', 'AG.LND.PRCP.MM', 'AG.LND.TOTL.K2', 'AG.LND.TRAC.ZS', 'AG.PRD.CREL.MT', 'AG.PRD.CROP.XD', 'AG.PRD.FOOD.XD', 'AG.PRD.LVSK.XD', 'AG.SRF.TOTL.K2', 'AG.YLD.CREL.KG', 'BG.GSR.NFSV.GD.ZS', 'BM.GSR.CMCP.ZS', 'BM.GSR.FCTY.CD', 'BM.GSR.GNFS.CD', 'BM.GSR.INSF.ZS', 'BM.GSR.MRCH.CD', 'BM.GSR.NFSV.CD', 'BM.GSR.ROYL.CD', 'BM.GSR.TOTL.CD', 'BM.GSR.TRAN.ZS', 'BM.GSR.TRVL.ZS', 'BM.KLT.DINV.GD.ZS', 'BM.TRF.PRVT.CD', 'BM.TRF.PWKR.CD.DT', 'BN.CAB.XOKA.CD', 'BN.CAB.XOKA.GD.ZS', 'BN.FIN.TOTL.CD', 'BN.GSR.FCTY.CD', 'BN.GSR.GNFS.CD', 'BN.GSR.MRCH.CD', 'BN.KAC.EOMS.CD', 'BN.KLT.DINV.CD', 'BN.KLT.PTXL.CD', 'BN.RES.INCL.CD', 'BN.TRF.CURR.CD', 'BN.TRF.KOGT.CD', 'BX.GRT.EXTA.CD.WD'] \n  `Topic` text, -- Topic Example values: ['Economic Policy & Debt: Balance of payments: Capital & financial account', 'Economic Policy & Debt: Balance of payments: Current account: Balances', 'Economic Policy & Debt: Balance of payments: Current account: Goods, services & income', 'Economic Policy & Debt: Balance of payments: Current account: Transfers', 'Economic Policy & Debt: Balance of payments: Reserves & other items', 'Economic Policy & Debt: External debt: Amortization', 'Economic Policy & Debt: External debt: Arrears, reschedulings, etc.', 'Economic Policy & Debt: External debt: Commitments', 'Economic Policy & Debt: External debt: Currency composition', 'Economic Policy & Debt: External debt: Debt outstanding', 'Economic Policy & Debt: External debt: Debt ratios & other items', 'Economic Policy & Debt: External debt: Debt service', 'Economic Policy & Debt: External debt: Disbursements', 'Economic Policy & Debt: External debt: Interest', 'Economic Policy & Debt: External debt: Net flows', 'Economic Policy & Debt: External debt: Net transfers', 'Economic Policy & Debt: External debt: Terms', 'Economic Policy & Debt: External debt: Undisbursed debt', 'Economic Policy & Debt: National accounts: Adjusted savings & income', 'Economic Policy & Debt: National accounts: Atlas GNI & GNI per capita', 'Economic Policy & Debt: National accounts: Growth rates', 'Economic Policy & Debt: National accounts: Growth rates:', 'Economic Policy & Debt: National accounts: Local currency at constant prices: Aggregate indicators', 'Economic Policy & Debt: National accounts: Local currency at constant prices: Expenditure on GDP', 'Economic Policy & Debt: National accounts: Local currency at constant prices: Other items', 'Economic Policy & Debt: National accounts: Local currency at constant prices: Value added', 'Economic Policy & Debt: National accounts: Local currency at current prices: Aggregate indicators', 'Economic Policy & Debt: National accounts: Local currency at current prices: Expenditure on GDP', 'Economic Policy & Debt: National accounts: Local currency at current prices: Value added', 'Economic Policy & Debt: National accounts: Shares of GDP & other', 'Economic Policy & Debt: National accounts: US$ at constant 2005 prices: Aggregate indicators', 'Economic Policy & Debt: National accounts: US$ at constant 2005 prices: Expenditure on GDP', 'Economic Policy & Debt: National accounts: US$ at constant 2005 prices: Value added', 'Economic Policy & Debt: National accounts: US$ at current prices: Aggregate indicators', 'Economic Policy & Debt: National accounts: US$ at current prices: Expenditure on GDP', 'Economic Policy & Debt: National accounts: US$ at current prices: Other items', 'Economic Policy & Debt: National accounts: US$ at current prices: Value added', 'Economic Policy & Debt: Official development assistance', 'Economic Policy & Debt: Purchasing power parity', 'Education: Efficiency', 'Education: Inputs', 'Education: Outcomes', 'Education: Participation', 'Environment: Agricultural production', 'Environment: Biodiversity & protected areas', 'Environment: Density & urbanization', 'Environment: Emissions', 'Environment: Energy production & use', 'Environment: Freshwater', 'Environment: Land use'] \n  `IndicatorName` text, -- Indicator Name Example values: ['Foreign direct investment, net (BoP, current US$)', 'Foreign direct investment, net inflows (% of GDP)', 'Foreign direct investment, net inflows (BoP, current US$)', 'Foreign direct investment, net outflows (% of GDP)', 'Net capital account (BoP, current US$)', 'Net errors and omissions (BoP, current US$)', 'Net financial account (BoP, current US$)', 'Portfolio equity, net inflows (BoP, current US$)', 'Portfolio Investment, net (BoP, current US$)', 'Primary income on FDI, payments (current US$)', 'Reserves and related items (BoP, current US$)', 'Current account balance (% of GDP)', 'Current account balance (BoP, current US$)', 'Net trade in goods (BoP, current US$)', 'Net trade in goods and services (BoP, current US$)', 'Charges for the use of intellectual property, payments (BoP, current US$)', 'Charges for the use of intellectual property, receipts (BoP, current US$)', 'Communications, computer, etc. (% of service exports, BoP)', 'Communications, computer, etc. (% of service imports, BoP)', 'Exports of goods and services (BoP, current US$)', 'Exports of goods, services and primary income (BoP, current US$)', 'Goods exports (BoP, current US$)', 'Goods imports (BoP, current US$)', 'Imports of goods and services (BoP, current US$)', 'Imports of goods, services and primary income (BoP, current US$)', 'Insurance and financial services (% of service exports, BoP)', 'Insurance and financial services (% of service imports, BoP)', 'Net primary income (BoP, current US$)', 'Primary income payments (BoP, current US$)', 'Primary income receipts (BoP, current US$)', 'Service exports (BoP, current US$)', 'Service imports (BoP, current US$)', 'Trade in services (% of GDP)', 'Transport services (% of service exports, BoP)', 'Transport services (% of service imports, BoP)', 'Travel services (% of service exports, BoP)', 'Travel services (% of service imports, BoP)', 'Net secondary income (BoP, current US$)', 'Personal remittances, paid (current US$)', 'Personal remittances, received (% of GDP)', 'Personal remittances, received (current US$)', 'Personal transfers, receipts (BoP, current US$)', 'Secondary income receipts (BoP, current US$)', 'Secondary income, other sectors, payments (BoP, current US$)', 'Grants, excluding technical cooperation (BoP, current US$)', 'Technical cooperation grants (BoP, current US$)', 'Total reserves (% of total external debt)', 'Total reserves (includes gold, current US$)', 'Total reserves in months of imports', 'Total reserves minus gold (current US$)'] \n  `ShortDefinition` text, -- Short Definition Example values: ['', 'Total external debt is debt owed to nonresidents repayable in foreign currency, goods, or services. ...[155 truncated]', 'Debt service is the sum of principle repayments and interest actually paid in foreign currency, good...[155 truncated]', 'Total external debt stocks to gross national income.', 'Multilateral debt service is the repayment of principal and interest to the World Bank, regional dev...[48 truncated]', 'Net official development assistance is disbursement flows (net of repayment of principal) that meet ...[102 truncated]', 'Net official development assistance per capita is disbursement flows (net of repayment of principal)...[155 truncated]', 'Net official development assistance is disbursement flows (net of repayment of principal) that meet ...[155 truncated]', 'Net official development assistance is disbursement flows (net of repayment of principal) that meet ...[142 truncated]', 'Net official development assistance is disbursement flows (net of repayment of principal) that meet ...[136 truncated]', 'Net official flows from UN agencies are the net disbursements of total official flows from the UN ag...[155 truncated]', 'Cereal yield, measured as kilograms per hectare of harvested land, includes wheat, rice, maize, barl...[155 truncated]', 'Life expectancy at birth indicates the average number of years a newborn infant would live.', 'Crude birth rate indicates the number of live births per 1,000 midyear population.', 'Crude death rate indicates the number of deaths per 1,000 midyear population.', 'Annual population growth rate. Population is based on the de facto definition of population, which c...[155 truncated]', 'Population ages 15 to 64 is the percentage of the total population that is in the age group 15 to 64...[63 truncated]', 'Population ages 65 and above as a percentage of the total population. Population is based on the de ...[31 truncated]', 'Female population is the percentage of the population that is female. Population is based on the de ...[31 truncated]', 'Maternal deaths is the number of women who die during pregnancy and childbirth.', 'Patent applications are worldwide patent applications filed through the Patent Cooperation Treaty pr...[41 truncated]', 'Trademark applications filed are applications to register a trademark with a national or regional In...[155 truncated]', 'Trademark applications filed are applications to register a trademark with a national or regional In...[150 truncated]', 'Trademark applications filed are applications to register a trademark with a national or regional In...[32 truncated]', \"Burden of Customs Procedure measures business executives' perceptions of their country's efficiency ...[104 truncated]\", 'Liner Shipping Connectivity Index score indicates how well countries are connected to global shippin...[100 truncated]', \"Quality of Port Infrastructure measures business executives' perceptions of their country's port fac...[113 truncated]\", 'Poverty gap at $1.90 a day (2011 PPP) is the mean shortfall in income or consumption from the povert...[155 truncated]', 'Poverty gap at $3.10 a day (2011 PPP) is the mean shortfall in income or consumption from the povert...[155 truncated]', 'Poverty headcount ratio at $1.90 a day is the percentage of the population living on less than $1.90...[155 truncated]', 'Poverty headcount ratio at $3.10 a day is the percentage of the population living on less than $3.10...[155 truncated]', 'The growth rate in the welfare aggregate of bottom 40% is computed as the annualized average growth ...[155 truncated]', 'The growth rate in the welfare aggregate of total population is computed as annualized average growt...[155 truncated]', 'Cost measures the fees levied on a 20-foot container in U.S. dollars. All the fees associated with c...[155 truncated]', 'Merchandise exports by the reporting economy are the total merchandise exports by the reporting econ...[117 truncated]', 'Merchandise exports to developing economies in East Asia and Pacific are the sum of merchandise expo...[155 truncated]', 'Merchandise exports to developing economies in Europe and Central Asia are the sum of merchandise ex...[155 truncated]', 'Merchandise exports to developing economies in Latin America and the Caribbean are the sum of mercha...[155 truncated]', 'Merchandise exports to developing economies in Middle East and North Africa are the sum of merchandi...[155 truncated]', 'Merchandise exports to developing economies in South Asia are the sum of merchandise exports from th...[155 truncated]', 'Merchandise exports to developing economies in Sub-Saharan Africa are the sum of merchandise exports...[155 truncated]', 'Merchandise exports to developing economies outside region are the sum of merchandise exports from t...[155 truncated]', 'Merchandise exports to developing economies within region are the sum of merchandise exports from th...[140 truncated]', 'Merchandise exports to high-income economies are the sum of merchandise exports from the reporting e...[155 truncated]', 'Merchandise imports from developing economies in East Asia and Pacific are the sum of merchandise im...[155 truncated]', 'Merchandise imports from developing economies in Europe and Central Asia are the sum of merchandise ...[155 truncated]', 'Merchandise imports from developing economies in Latin America and the Caribbean are the sum of merc...[155 truncated]', 'Merchandise imports from developing economies in Middle East and North Africa are the sum of merchan...[155 truncated]', 'Merchandise imports from developing economies in South Asia are the sum of merchandise imports by th...[155 truncated]', 'Merchandise imports from developing economies in Sub-Saharan Africa are the sum of merchandise impor...[155 truncated]'] \n  `LongDefinition` text, -- Long Definition Example values: ['Foreign direct investment are the net inflows of investment to acquire a lasting management interest...[155 truncated]', 'Foreign direct investment refers to direct investment equity flows in the reporting economy. It is t...[155 truncated]', 'Net capital account records acquisitions and disposals of nonproduced nonfinancial assets, such as l...[155 truncated]', 'Net errors and omissions constitute a residual category needed to ensure that accounts in the balanc...[155 truncated]', 'The net financial account shows net acquisition and disposal of financial assets and liabilities. It...[155 truncated]', 'Portfolio equity includes net inflows from equity securities other than those recorded as direct inv...[155 truncated]', 'Portfolio investment covers transactions in equity securities and debt securities. Data are in curre...[16 truncated]', 'Primary income on foreign direct investment covers payments of direct investment income (debit side)...[155 truncated]', \"Reserves and related items is the net change in a country's holdings of international reserves resul...[155 truncated]\", 'Current account balance is the sum of net exports of goods and services, net primary income, and net...[18 truncated]', 'Current account balance is the sum of net exports of goods and services, net primary income, and net...[52 truncated]', 'Net trade in goods is the difference between exports and imports of goods. Trade in services is not ...[43 truncated]', 'Net trade in goods and services is derived by offsetting imports of goods and services against expor...[155 truncated]', 'Charges for the use of intellectual property are payments and receipts between residents and nonresi...[155 truncated]', 'Communications, computer, information, and other services cover international telecommunications; co...[155 truncated]', 'Exports of goods and services comprise all transactions between residents of a country and the rest ...[155 truncated]', 'Exports of goods, services and primary income is the sum of goods exports, service exports and prima...[53 truncated]', 'Goods exports refer to all movable goods (including nonmonetary gold and net exports of goods under ...[112 truncated]', 'Goods imports refer to all movable goods (including nonmonetary gold) involved in a change of owners...[69 truncated]', 'Imports of goods and services comprise all transactions between residents of a country and the rest ...[155 truncated]', 'Imports of goods, services and primary income is the sum of goods imports, service imports and prima...[53 truncated]', 'Insurance and financial services cover various types of insurance provided to nonresidents by reside...[155 truncated]', 'Net primary income refers to receipts and payments of employee compensation paid to nonresident work...[155 truncated]', 'Primary income payments refer to employee compensation paid to nonresident workers and investment in...[112 truncated]', 'Primary income receipts refer to employee compensation paid to resident workers working abroad and i...[155 truncated]', 'Services refer to economic output of intangible commodities that may be produced, transferred, and c...[59 truncated]', 'Trade in services is the sum of service exports and imports divided by the value of GDP, all in curr...[17 truncated]', 'Transport covers all transport services (sea, air, land, internal waterway, pipeline, space and elec...[155 truncated]', 'Travel covers goods and services acquired from an economy by travelers for their own use during visi...[155 truncated]', 'Secondary income refers to transfers recorded in the balance of payments whenever an economy provide...[155 truncated]', 'Personal remittances comprise personal transfers and compensation of employees. Personal transfers c...[155 truncated]', 'Personal transfers consist of all current transfers in cash or in kind made or received by resident ...[155 truncated]', 'Grants are defined as legally binding commitments that obligate a specific value of funds available ...[95 truncated]', 'Technical cooperation grants include free-standing technical cooperation grants, which are intended ...[155 truncated]', 'International reserves to total external debt stocks.', 'Total reserves comprise holdings of monetary gold, special drawing rights, reserves of IMF members h...[155 truncated]', 'Total reserves minus gold comprise special drawing rights, reserves of IMF members held by the IMF, ...[137 truncated]', 'IMF repurchases are total repayments of outstanding drawings from the General Resources Account duri...[105 truncated]', 'Nonguaranteed long-term debt from bonds that are privately placed. Principal repayments are actual a...[144 truncated]', 'Nonguaranteed long-term commercial bank loans from private banks and other private financial institu...[155 truncated]', 'Bilateral debt includes loans from governments and their agencies (including central banks), loans f...[155 truncated]', 'Bilateral debt includes loans from governments and their agencies (including central banks), loans f...[155 truncated]', 'Public and publicly guaranteed debt from bonds that are either publicly issued or privately placed. ...[155 truncated]', 'Public and publicly guaranteed commercial bank loans from private banks and other private financial ...[155 truncated]', 'Public and publicly guaranteed debt outstanding from the International Bank for Reconstruction and D...[155 truncated]', 'Public and publicly guaranteed debt outstanding from the International Development Association (IDA)...[155 truncated]', 'Public and publicly guaranteed multilateral loans include loans and credits from the World Bank, reg...[155 truncated]', 'Public and publicly guaranteed debt from official creditors includes loans from international organi...[155 truncated]', 'Public and publicly guaranteed other private credits from manufacturers, exporters, and other suppli...[155 truncated]', 'Public and publicly guaranteed debt from private creditors include bonds that are either publicly is...[155 truncated]'] \n  `UnitOfMeasure` text, -- Unit Of Measure Example values: ['', '`', '%', '2005 PPP $', '2011 PPP $'] \n  `Periodicity` text, -- Periodicity Example values: ['Annual'] \n  `BasePeriod` text, -- Base Period Example values: ['', '2005', 'varies by country', '2011', '2004-06', '2010', '2000', '1990'] \n  `OtherNotes` integer, -- Other Notes \n  `AggregationMethod` text, -- Aggregation Method Example values: ['', 'Weighted average', 'Sum', 'Gap-filled total', 'Median', 'Linear mixed-effect model estimates', 'Unweighted average'] \n  `LimitationsAndExceptions` text, -- Limitations And Exceptions Example values: ['', 'FDI data do not give a complete picture of international investment in an economy. Balance of paymen...[155 truncated]', 'Portfolio investors typically have less of a role in the decision making of the enterprise with pote...[155 truncated]', 'Discrepancies may arise in the balance of payments because there is no single source for balance of ...[155 truncated]', 'Remittance transactions have grown in importance over the past decade. In a number of developing eco...[155 truncated]', 'Data on ODA is for aid-receiving countries. The data cover loans and grants from DAC member countrie...[155 truncated]', 'The DRS encourages debtor countries to voluntarily provide information on their short-term external ...[155 truncated]', 'The present value of external debt provides a measure of future debt service obligations. It is calc...[155 truncated]', \"The IMF's loan instruments have changed over time to address the specific circumstances of its membe...[3 truncated]\", \"Data on external debt are gathered through the World Bank's Debtor Reporting System (DRS). Long term...[155 truncated]\", 'Although some outstanding IBRD loans have a low enough interest rate to be classified as concessiona...[155 truncated]', 'In exceptional circumstances IDA extends temporary eligibility to countries above the IDA cutoff tha...[155 truncated]', 'Adjusted net national income differs from the adjustments made in the calculation of adjusted net sa...[155 truncated]', 'The exercise treats public education expenditures as an addition to savings. However, because of the...[155 truncated]', 'Public education expenditures are considered an addition to savings. However, because of the wide va...[155 truncated]', 'Because gross savings is calculated as a residual it includes errors, which may not be offsetting, i...[17 truncated]', 'Net forest depletion is not the monetary value of deforestation. Roundwood and fuelwood production a...[155 truncated]', 'A positive net depletion figure for forest resources implies that the harvest rate exceeds the rate ...[155 truncated]', 'Labor productivity losses, as calculated within the framework of adjusted net savings, represent onl...[96 truncated]', 'Among the difficulties faced by compilers of national accounts is the extent of unreported economic ...[155 truncated]', \"Each industry's contribution to growth in the economy's output is measured by growth in the industry...[155 truncated]\", 'Ideally, industrial output should be measured through regular censuses and surveys of firms. But in ...[155 truncated]', 'In the services industries, including most of government, value added in constant prices is often im...[155 truncated]', 'In establishing classifications systems compilers must define both the types of activities to be des...[155 truncated]', 'Because policymakers have tended to focus on fostering the growth of output, and because data on pro...[155 truncated]', 'In the services industry the many self-employed workers and one-person businesses are sometimes diff...[155 truncated]', 'Gross domestic product (GDP), though widely tracked, may not always be the most relevant summary of ...[155 truncated]', 'Data exclude DAC members\\x92 multilateral aid (contributions to the regular budgets of the multilateral...[155 truncated]', 'Official or market exchange rates are often used to convert economic statistics in local currencies ...[155 truncated]', 'The quality of data is affected when new entrants and repeaters are not correctly distinguished in t...[155 truncated]', 'The estimates have limitations in capturing real trend in that an observed rate will be applied to t...[155 truncated]', 'The quality of data on the transition rate is affected when new entrants and repeaters are not corre...[123 truncated]', 'Country policies on repetition and promotion differ. In some cases the number of repeaters is contro...[155 truncated]', 'Data disaggregated by level of education are estimates in some instances. It is often difficult to s...[86 truncated]', 'Data may refer to spending by the ministry of education only (excluding spending on educational acti...[28 truncated]', 'Data on government expenditure on education may refer to spending by the ministry of education only ...[155 truncated]', 'The theoretical entrance age to a given programme or level is typically, but not always, the most co...[18 truncated]', 'The comparability of pupil-teacher ratios across countries is affected by the definition of teachers...[155 truncated]', \"This indicator does not take into account differences in teachers' experiences and status, teaching ...[155 truncated]\", 'In practice, literacy is difficult to measure. Estimating literacy rates requires census or survey m...[155 truncated]', 'Data limitations preclude adjusting for students who drop out during the final year of lower seconda...[155 truncated]', 'Data limitations preclude adjusting for students who drop out during the final year of primary educa...[155 truncated]', 'Enrollment indicators are based on annual school surveys, but do not necessarily reflect actual atte...[155 truncated]', 'Due to different data sources for enrollment and population data, the number may not capture the act...[55 truncated]', \"The percentage of female enrollment is limited in assessing gender parity, because it's affected by ...[137 truncated]\", \"Religious or private schools, which are not registered with the government or don't follow the commo...[43 truncated]\", 'The data are collected by the Food and Agriculture Organization of the United Nations (FAO) through ...[155 truncated]', 'Agricultural data are collected by the Food and Agriculture Organization of the United Nations (FAO)...[155 truncated]', 'Data on cereal production may be affected by a variety of reporting and timing differences. Millet a...[155 truncated]', 'Cereals production data relate to crops harvested for dry grain only. Cereal crops harvested for hay...[155 truncated]'] \n  `NotesFromOriginalSource` text, -- Notes From Original Source Example values: ['', 'Estimates are presented with uncertainty intervals (see footnote). When ranges are presented, the lo...[155 truncated]', 'In some cases, the sum of public and private expenditures on health may not add up to 100% because o...[155 truncated]', 'All the indicators refer to expenditures by financing agent except external resources which is a fin...[155 truncated]', 'PPP series resulting from the 2005 International comparison project (ICP) estimated by the World Ban...[155 truncated]', 'Depending on the source and means of monitoring, data may not be exactly comparable across countries...[49 truncated]', 'Estimates of maternal mortality are presented along with upper and lower  limits of intervals (see f...[155 truncated]', 'All surveys were administered using the Enterprise Surveys methodology as outlined in the Methodolog...[57 truncated]', 'Most surveys were administered using the Enterprise Surveys methodology as outlined in the Methodolo...[155 truncated]', 'SIPRI statistical data on arms transfers relates to actual deliveries of major conventional weapons....[155 truncated]', 'The 2007-2011 refugee population category also includes people in a refugee-like situation, most of ...[155 truncated]'] \n  `GeneralComments` text, -- General Comments Example values: [\"Note: Data are based on the sixth edition of the IMF's Balance of Payments Manual (BPM6) and are onl...[155 truncated]\", \"Note: Data starting from 2005 are based on the sixth edition of the IMF's Balance of Payments Manual...[8 truncated]\", \"Note: Data are based on the sixth edition of the IMF's Balance of Payments Manual (BPM6) and are onl...[30 truncated]\", '', \"Note: Data are based on the sixth edition of the IMF's Balance of Payments Manual (BPM6) and are onl...[82 truncated]\", \"Note: Data are based on the sixth edition of the IMF's Balance of Payments Manual (BPM6) and are onl...[155 truncated]\", 'Note: Data for OECD countries are based on ISIC, revision 4.', 'Data for net official flows from UNECE at present  are reported at the regional level only. A more d...[71 truncated]', 'Data for net official flows from WHO at present  are reported at the regional level only. A more det...[69 truncated]', 'Restricted use: Please contact the International Energy Agency for third-party use of these data.', 'Electricity production shares may not sum to 100 percent because other sources of generated electric...[154 truncated]', 'Country-specific metadata can be found on the IMF\\x92s FAS website at \\xa0http://fas.imf.org.', 'Stock market data were previously sourced from Standard & Poor\\'s until they discontinued their \"Glob...[155 truncated]', 'In the WDI database, the DEC alternative conversion factor is used to convert data in local currency...[31 truncated]', 'The derivation of this indicator was simplified in September 2012 to be current-year broad money div...[35 truncated]', 'The derivation of this indicator was simplified in September 2012 to be current-year M2 divided by c...[26 truncated]', 'Relevance to gender indicator: Infant mortality rates are higher for boys than for girls in countrie...[57 truncated]', 'Relevance to gender: Given that data on the incidence and prevalence of diseases are frequently unav...[155 truncated]', 'Children under age 5 and pregnant women have the highest risk for anemia. Data on anemia are compile...[155 truncated]', 'Relevance to gender indicator: this indicator implies the dependency burden that the working-age pop...[155 truncated]', 'The composition of a household plays a role in the determining other characteristics of a household,...[84 truncated]', 'Relevance to gender indicator: disaggregating the population composition by gender will help a count...[66 truncated]', 'Relevance to gender indicator: Women who are assisted by trained professionals is important to decre...[155 truncated]', \"Relevance to gender indicator: it is an indicator of women's empowerment and are related to several ...[84 truncated]\", 'Relevance to gender indicator: it can indicate the status of women within households and a woman\\x92s d...[49 truncated]', 'Relevance to gender indicator: this indicator represents the risk associated with each pregnancy and...[80 truncated]', 'Relevance to gender indicator: Good prenatal and postnatal care improve maternal health and reduce m...[29 truncated]', 'Relevance to gender indicator: Unmet need for contraception measures the capacity women have in achi...[155 truncated]', 'Relevance to gender:  In many developing countries most new infections occur in young adults, with y...[33 truncated]', 'Please cite the International Telecommunication Union for third-party use of these data.', 'This series only includes estimates that to the best of our knowledge are reasonably comparable over...[137 truncated]', 'The comparability of welfare aggregates (consumption or income) for the chosen years T0 and T1 is as...[155 truncated]', 'The choice of consumption or income for a country is made according to which welfare aggregate is us...[155 truncated]', 'Data are presented for the survey year instead of publication year.', 'Data are presented for the survey year instead of publication year. Data before 2013 are not compara...[61 truncated]', 'Relevance to gender indicator: Women are vastly underrepresented in decision making positions at the...[89 truncated]', 'For cross-country comparability, only limited liability corporations that operate in the formal sect...[16 truncated]', 'Merchandise export shares may not sum to 100 percent because of unclassified trade.', 'Merchandise import shares may not sum to 100 percent because of unclassified trade.', 'Data for some countries are based on partial or uncertain data or rough estimates.', 'General cut off date is end-December. Relevance to gender indicator: Women are vastly underrepresent...[155 truncated]', 'The time series may not be comparable across countries and over time due to differences in survey in...[93 truncated]', 'Relevance to gender indicator: this indicator monitors the participation of women in work and the la...[89 truncated]', 'Relevance to gender indicator: Men still make up the majority of people employed in all three sector...[155 truncated]', \"The employment to population ratios presented here are the ILO estimates from the ILO's Key Indicato...[155 truncated]\", 'Data are based on national surveys or censuses and may differ from the ILO estimates (SL.EMP.TOTL.SP...[8 truncated]', 'Data are based on national surveys or censuses and may differ from the ILO estimates (SL.EMP.TOTL.SP...[8 truncated]', 'Data are based on national surveys or censuses and may differ from the ILO estimates (SL.EMP.TOTL.SP...[5 truncated]', 'Data are based on national surveys or censuses and may differ from the ILO estimates (SL.EMP.1524.SP...[8 truncated]', 'Data are based on national surveys or censuses and may differ from the ILO estimates (SL.EMP.1524.SP...[8 truncated]'] \n  `Source` text, -- Source Example values: ['International Monetary Fund, Balance of Payments Statistics Yearbook and data files.', 'International Monetary Fund, International Financial Statistics and Balance of Payments databases, W...[80 truncated]', 'International Monetary Fund, Balance of Payments database, supplemented by data from the United Nati...[70 truncated]', 'International Monetary Fund, Balance of Payments database, and World Bank, International Debt Statis...[5 truncated]', 'World Bank, International Debt Statistics.', 'International Monetary Fund, Balance of Payments Statistics Yearbook and data files, and World Bank ...[23 truncated]', 'World Bank staff estimates based on IMF balance of payments data.', 'World Bank staff estimates based on IMF balance of payments data, and World Bank and OECD GDP estima...[4 truncated]', 'World Bank, International Debt Statistics, and OECD.', 'International Monetary Fund, International Financial Statistics and data files.', 'World Bank.', 'World Bank staff estimates based on sources and methods in World Bank\\'s \"The Changing Wealth of Nati...[69 truncated]', 'World Bank staff estimates based on Samuel Fankhauser\\'s \"Valuing Climate Change: The Economics of th...[21 truncated]', \"World Bank staff estimates using data from the United Nations Statistics Division's National Account...[13 truncated]\", \"World Bank staff estimates using data from the United Nations Statistics Division's Statistical Year...[62 truncated]\", 'World Bank national accounts data files.', 'Data on health impacts from exposure to ambient PM2.5 pollution and household air pollution are from...[143 truncated]', 'World Bank national accounts data, and OECD National Accounts data files.', 'United Nations Industrial Development Organization, International Yearbook of Industrial Statistics.', 'Development Assistance Committee of the Organisation for Economic Co-operation and Development.', 'Development Assistance Committee of the Organisation for Economic Co-operation and Development, Geog...[155 truncated]', 'World Bank, International Comparison Program database.', 'United Nations Educational, Scientific, and Cultural Organization (UNESCO) Institute for Statistics.', 'United Nations Educational, Scientific, and Cultural Organization (UNESCO), special data collection ...[37 truncated]', 'Food and Agriculture Organization, electronic files and web site.', 'Derived from World Bank national accounts files and Food and Agriculture Organization, Production Ye...[22 truncated]', 'United Nations Environmental Program and the World Conservation Monitoring Centre, and International...[66 truncated]', 'Froese, R. and Pauly, D. (eds). 2008. FishBase database, www.fishbase.org.', 'Kiran Dev Pandey, Piet Buys, Ken Chomitz, and David Wheeler\\'s, \"Biodiversity Conservation Indicators...[76 truncated]', 'United Nations Environmental Program and the World Conservation Monitoring Centre, as compiled by th...[120 truncated]', 'Food and Agriculture Organization and World Bank population estimates.', 'United Nations, World Urbanization Prospects.', 'The data on urban population shares used to estimate rural population come from the United Nations, ...[80 truncated]', 'World Bank Staff estimates based on United Nations, World Urbanization Prospects.', 'European Commission, Joint Research Centre (JRC)/Netherlands Environmental Assessment Agency (PBL). ...[89 truncated]', 'Carbon Dioxide Information Analysis Center, Environmental Sciences Division, Oak Ridge National Labo...[33 truncated]', 'IEA Statistics © OECD/IEA 2014 (http://www.iea.org/stats/index.asp), subject to https://www.iea.org/...[23 truncated]', 'United Nations Framework Convention on Climate Change.', 'Brauer, M. et al. 2015. \"Ambient Air Pollution Exposure Estimation for the Global Burden of Disease ...[119 truncated]', 'World Bank, Sustainable Energy for All (SE4ALL) database from World Bank, Global Electrification dat...[6 truncated]', 'World Bank, Sustainable Energy for all (SE4ALL) database from WHO Global Household Energy database.', '© OECD/IEA and World Bank, based on IEA data in IEA World Energy Balances © OECD/IEA 2013 edition, s...[53 truncated]', 'Food and Agriculture Organization, AQUASTAT data.', 'Food and Agriculture Organization, AQUASTAT data, and World Bank and OECD GDP estimates.', '(UNISDR, 2009-2011 Progress Reports, http://www.preventionweb.net/english/hyogo).', 'EM-DAT: The OFDA/CRED International Disaster Database: www.emdat.be, Université Catholique de Louvai...[34 truncated]', 'Center for International Earth Science Information Network (CIESIN), Place II dataset.', 'Estimates based on sources and methods described in \"The Changing Wealth of Nations: Measuring Susta...[61 truncated]', 'International Monetary Fund, Financial Access Survey.', 'Consultative Group to Assist the Poor and the World Bank Group\\x92s \"Financial Access 2010.\"'] \n  `StatisticalConceptAndMethodology` text, -- Statistical Concept And Methodology Example values: ['', 'Data on equity flows are based on balance of payments data reported by the International Monetary Fu...[155 truncated]', 'Data on equity flows are based on balance of payments data reported by the International Monetary Fu...[155 truncated]', 'The balance of payments (BoP) is a double-entry accounting system that shows all flows of goods and ...[155 truncated]', 'The two main components of personal remittances, \"personal transfers\" and \"compensation of employees...[155 truncated]', 'The two main components of personal remittances, \"personal transfers\" and \"compensation of employees...[155 truncated]', 'Grants are transfers made in cash, goods or services for which no repayment is required. Data exclud...[155 truncated]', 'Technical cooperation contributions take the form mainly of the supply of human resources from donor...[155 truncated]', \"Data on external debt are gathered through the World Bank's Debtor Reporting System (DRS). Long term...[155 truncated]\", \"Data related to the operations of the IMF come from the IMF Treasurer's Department and are converted...[155 truncated]\", 'Commercial banks include all commercial banks, whether or not publicly owned, that provide loans and...[155 truncated]', 'Data show concessional and nonconcessional financial flows from official bilateral sources. The Orga...[155 truncated]', \"The World Bank's International Bank for Reconstruction and Development (IBRD) lends to creditworthy ...[155 truncated]\", 'World Bank concessional lending is done by the International Development Association (IDA) based on ...[94 truncated]', 'The International Monetary Fund (IMF) makes concessional funds available through its Extended Credit...[155 truncated]', 'Nonconcessional lending from the IMF is provided mainly through Stand-by Arrangements, the Flexible ...[44 truncated]', 'Data show concessional and nonconcessional financial flows from international financial institutions...[155 truncated]', 'Regional development banks also maintain concessional windows. Their loans are recorded according to...[155 truncated]', 'Bonds are debt instruments issued by public and publicly guaranteed or private debtors with duration...[155 truncated]', 'Adjusted net national income complements gross national income (GNI) in assessing economic progress ...[155 truncated]', 'Adjusted net savings are derived from standard national accounting measures of gross savings by maki...[155 truncated]', 'Pollution damage from emissions of carbon dioxide is calculated as the marginal social cost per unit...[155 truncated]', 'Gross savings are calculated as a residual from the national accounts by taking the difference betwe...[130 truncated]', 'Natural resources depletion is the sum of net forest depletion, energy depletion, and mineral deplet...[155 truncated]', 'Within the national accounting framework, air pollution damages are estimated following a human capi...[155 truncated]', 'The World Bank uses Atlas method GNI per capita in U.S. dollars to classify countries for analytical...[155 truncated]', 'In calculating GNI and GNI per capita in U.S. dollars for certain operational purposes, the World Ba...[155 truncated]', 'Gross domestic product (GDP) represents the sum of value added by all its producers. Value added is ...[155 truncated]', 'For more information, see the metadata for constant U.S. dollar GDP (NY.GDP.MKTP.KD) and total popul...[20 truncated]', 'The data on the distribution of manufacturing value added by industry are provided by the United Nat...[155 truncated]', 'Gross domestic product (GDP) from the expenditure side is made up of household final consumption exp...[155 truncated]', 'Gross savings represent the difference between disposable income and consumption and replace gross d...[155 truncated]', 'For more information, see the metadata for current U.S. dollar GDP (NY.GDP.MKTP.CD) and total popula...[19 truncated]', \"The data on manufacturing value added in U.S. dollars are from the World Bank's national accounts fi...[155 truncated]\", 'The Development Assistance Committee (DAC) of the Organisation for Economic Co-operation and Develop...[155 truncated]', 'Net official development assistance (ODA) per capita consists of disbursements of loans made on conc...[155 truncated]', 'The ODA excludes nonconcessional flows from official creditors, which are classified as \"other offic...[155 truncated]', 'Net official aid refers to aid flows (net of repayments) from official donors to countries and terri...[155 truncated]', 'The flows of official and private financial resources from the members of the Development Assistance...[155 truncated]', 'PPP rates provide a standard measure allowing comparison of real levels of expenditure between count...[155 truncated]', 'For more information, see the metadata for PPP GDP in current international dollars (NY.GDP.MKTP.PP....[39 truncated]', 'Because exchange rates do not always reflect differences in price levels between countries, GDP and ...[155 truncated]', 'For more information, see the metadata for PPP GNI in current international dollars (NY.GNP.MKTP.PP....[39 truncated]', 'Because exchange rates do not always reflect differences in price levels between countries, GNI and ...[155 truncated]', 'The ratio of the PPP conversion factor to the market exchange rate - the national price level or com...[155 truncated]', 'Gross intake ratio in the first grade of primary education is calculated by dividing the number of n...[155 truncated]', 'Net intake rate in the first grade of primary education is calculated by dividing the number of chil...[155 truncated]', 'Cohort survival rate is calculated by dividing the total number of children belonging to a cohort wh...[155 truncated]', 'Effective transition rate is calculated by dividing the number of new entrants in the first grade of...[155 truncated]', 'Share of repeaters in primary school is calculated by dividing the sum of repeaters in all grades of...[155 truncated]'] \n  `DevelopmentRelevance` text, -- Development Relevance Example values: ['', 'Private financial flows - equity and debt - account for the bulk of development finance. Equity flow...[155 truncated]', 'The balance of payments records an economy\\x92s transactions with the rest of the world. Balance of pay...[155 truncated]', 'Movement of people, most often through migration, is a significant part of global integration. Migra...[155 truncated]', 'DAC exists to help its members coordinate their development assistance and to encourage the expansio...[155 truncated]', \"External indebtedness affects a country's creditworthiness and investor perceptions. Nonreporting co...[155 truncated]\", 'External debt is that part of the total debt in a country that is owed to creditors outside the coun...[155 truncated]', 'Adjusted net national income is particularly useful in monitoring low-income, resource-rich economie...[155 truncated]', 'Adjusted net savings measure the change in value of a specified set of assets, excluding capital gai...[155 truncated]', 'Gross savings is used as a starting point for calculating adjusted net savings. Adjusted net saving ...[52 truncated]', 'Natural resources depletion is a critical component in the calculation of adjusted net national inco...[155 truncated]', 'Air pollution places a major burden on world health. In many places, including cities but also nearb...[155 truncated]', 'Because development encompasses many factors - economic, environmental, cultural, educational, and i...[155 truncated]', \"An economy's growth is measured by the change in the volume of its output or in the real incomes of ...[155 truncated]\", 'Firms typically use multiple processes to produce a product. For example, an automobile manufacturer...[155 truncated]', \"Ratio of aid to central government expense provides measures of recipient country's dependency on ai...[155 truncated]\", \"The ratio of aid to GNI provides a measure of recipient country's dependency on aid. Ratios of aid a...[155 truncated]\", \"The ratio of aid to gross capital formation provides a measure of recipient country's dependency on ...[155 truncated]\", \"The ratio of aid to imports of goods and services provides a measure of recipient country's dependen...[155 truncated]\", \"The ratio of aid per capita provides a measure of recipient country's dependency on aid. DAC exists ...[155 truncated]\", 'In a market-based economy, household, producer, and government choices about resource allocation are...[155 truncated]', 'The gross intake ratio in the first grade of primary education indicates the level of access to prim...[155 truncated]', 'The net intake rate in the first grade of primary education indicates the level of access to primary...[155 truncated]', \"The cohort survival rate measures an education system's holding power and internal efficiency. Rates...[72 truncated]\", 'The effective transition rate from primary to secondary education conveys the degree of access or tr...[155 truncated]', \"Data on repeaters are often used to indicate an education system's internal efficiency. Repeaters no...[114 truncated]\", 'The share of government expenditure for a specific education level allows an assessment of the prior...[155 truncated]', 'The percentage of government expenditure on education to GDP is useful to compare education expendit...[155 truncated]', 'The share of government expenditure devoted to education allows an assessment of the priority a gove...[155 truncated]', 'Women teachers are important as they serve as role models to girls and help to attract and retain gi...[14 truncated]', 'The share of female teachers shows the level of gender representation in the teaching force. A value...[155 truncated]', 'The pupil-teacher ratio is often used to compare the quality of schooling across countries, but it i...[68 truncated]', 'Trained teachers refer to teaching force with the necessary pedagogical skills to teach and use teac...[155 truncated]', 'Literacy rate is an outcome indicator to evaluate educational attainment. This data can predict the ...[155 truncated]', 'The World Bank and the UNESCO Institute for Statistics jointly developed the primary completion rate...[155 truncated]', 'Relevance to gender indicator: Women teachers are important as they serve as role models to girls an...[45 truncated]', 'Gross enrollment ratios indicate the capacity of each level of the education system, but a high rati...[155 truncated]', 'Large numbers of children out of school create pressure to enroll children and provide classrooms, t...[155 truncated]', 'The share of girls allows an assessment on gender composition in school enrollment. A value greater ...[93 truncated]', 'The Gender Parity Index (GPI) indicates parity between girls and boys. A GPI of less than 1 suggests...[155 truncated]', 'The share of enrollment in private institutions indicates the scale and capacity of private educatio...[155 truncated]', \"Agricultural land covers more than one-third of the world's land area. In many industrialized countr...[155 truncated]\", 'Until 2000, agriculture was the mainstay of employment around the world. Since then, the services se...[155 truncated]', 'The Food and Agriculture Organization (FAO) estimates that cereals supply 51 percent of Calories and...[155 truncated]', 'In developed countries, cereal crops are universally machine-harvested, typically using a combine ha...[155 truncated]', 'The commodities covered in the computation of indices of agricultural production are all crops and l...[155 truncated]', 'Factors such as the green revolution, has led to impressive progress in increasing crop yields over ...[155 truncated]', 'The cultivation of cereals varies widely in different countries and depends partly upon the developm...[155 truncated]', 'As threats to biodiversity mount, the international community is increasingly focusing on conserving...[155 truncated]', 'Biodiversity is defined as \"the variability among living organisms from all sources including, inter...[155 truncated]'] \n  `RelatedSourceLinks` text, -- Related Source Links Example values: ['', 'World Bank, PovcalNet: an online poverty analysis tool, http://iresearch.worldbank.org/PovcalNet/ind...[6 truncated]'] \n  `OtherWebLinks` integer, -- Other Web Links \n  `RelatedIndicators` integer, -- Related Indicators \n  `LicenseType` text, -- License Type Example values: ['Open', 'Restricted'] \n);\nCREATE TABLE `CountryNotes` (\n  `Countrycode` text\n    foreign key (Countrycode) references Country (CountryCode), -- Country code Example values: ['ABW', 'ADO', 'AFG', 'AGO', 'ALB', 'ARE', 'ARG', 'ARM', 'ASM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CHE', 'CHI', 'CHL', 'CHN', 'CIV', 'CMR', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CYM', 'CYP', 'CZE', 'DEU'] \n  `Seriescode` text\n    foreign key (Seriescode) references Series (SeriesCode), -- Series code Example values: ['EG.EGY.PRIM.PP.KD', 'EG.ELC.RNEW.ZS', 'EG.FEC.RNEW.ZS', 'SM.POP.NETM', 'SM.POP.TOTL', 'SP.DYN.AMRT.FE', 'SP.DYN.AMRT.MA', 'SP.DYN.CBRT.IN', 'SP.DYN.CDRT.IN', 'SP.DYN.LE00.FE.IN', 'SP.DYN.LE00.IN', 'SP.DYN.LE00.MA.IN', 'SP.DYN.TFRT.IN', 'SP.POP.GROW', 'SP.POP.TOTL', 'DT.DOD.DECT.CD', 'NE.CON.PRVT.PP.CD', 'NE.CON.PRVT.PP.KD', 'NY.GDP.MKTP.PP.CD', 'NY.GDP.MKTP.PP.KD', 'NY.GDP.PCAP.PP.CD', 'NY.GDP.PCAP.PP.KD', 'NY.GNP.MKTP.PP.CD', 'NY.GNP.MKTP.PP.KD', 'NY.GNP.PCAP.PP.CD', 'NY.GNP.PCAP.PP.KD', 'PA.NUS.PPP', 'PA.NUS.PPPC.RF', 'PA.NUS.PRVT.PP', 'SH.XPD.EXTR.ZS', 'SH.XPD.OOPC.TO.ZS', 'SH.XPD.OOPC.ZS', 'SH.XPD.PCAP', 'SH.XPD.PCAP.PP.KD', 'SH.XPD.PRIV.ZS', 'SH.XPD.PUBL', 'SH.XPD.PUBL.GX.ZS', 'SH.XPD.PUBL.ZS', 'SH.XPD.TOTL.ZS', 'FB.AST.NPER.ZS', 'FB.BNK.CAPA.ZS', 'CM.MKT.TRNR', 'EG.GDP.PUSE.KO.PP', 'EG.GDP.PUSE.KO.PP.KD', 'EG.USE.COMM.GD.PP.KD', 'EN.ATM.CO2E.PP.GD', 'EN.ATM.CO2E.PP.GD.KD', 'FP.CPI.TOTL', 'FP.CPI.TOTL.ZG', 'FP.WPI.TOTL'] \n  `Description` text, -- Description Example values: ['Sources: Estimated based on UN Energy Statistics (2014); World Development Indicators, WDI (2014)', 'Sources: UN Energy Statistics (2014)', 'Data sources : United Nations World Population Prospects', 'Estimates are derived from data on foreign-born population.', 'Data source : United Nations World Population Prospects', 'Derived using male and female life expectancy', 'Data sources: United Nations World Population Prospects', 'Estimates are derived from data on foreign population. Foreign population is people who are citizens...[53 truncated]', 'Data sources : Eurostat', 'Long-term public and publicly guaranteed debt data for 2014 are based on reports provided by the cou...[155 truncated]', 'Estimates are based on regression.', 'Non-profit institutions (such as NGOs) serving households are accounted for in \\x93external assistance\\x94...[43 truncated]', 'Long-term public and publicly guaranteed debt data for 2014 are based on reports provided by the cou...[142 truncated]', 'Sources: World Energy Statistics and Balances, IEA (2014); World Development Indicators, WDI (2014)', 'Sources: World Energy Statistics and Balances, IEA (2014)', 'Some estimates should be viewed with caution as these are derived from scarce data.', 'Estimates are derived from data on foreign-born population. Number of refugees reported by the UN Re...[62 truncated]', 'Long-term public and publicly guaranteed debt data for 2014 are based on reports provided by the cou...[155 truncated]', 'Non FSI Reporter: Data for this indicator collected from IMF Area Department and may not follow the ...[22 truncated]', 'Changes for per capita values are due to fluctuations in the US$ exchange rates.', 'Data sources : Institute of Statistics, Eurostat', 'Method of calculation: Total domestic value of share trading of Abu Dhabi Serurities Market and Duba...[88 truncated]', 'Estimates are derived from data on foreign population. Foreign population is people who are citizens...[155 truncated]', 'Data series will be calculated once ongoing revisions to official statistics reported by the Nationa...[69 truncated]', 'Data are officially reported statistics by the National Statistics and Censuses Institute of Argenti...[155 truncated]', 'Based on data officially reported by the National Statistics and Censuses Institute of Argentina. On...[155 truncated]', 'The decrease in the refugee population in 1998 is mainly due to a verification of records.', 'Long-term public and publicly guaranteed debt data for 2014 are based on reports provided by the cou...[155 truncated]', 'Estimates are derived from data on foreign-born population. The estimates for American Samoa reflect...[65 truncated]', 'Data sources : United Nations Population and Vital Statistics Report', 'About 30% of the expenditure in residential facilities for care of the aged has a health purpose, bu...[155 truncated]', 'Data since 2007 are UNHCR estimates based on the arrival of refugees and asylum-seeker recognition o...[155 truncated]', 'Estimates are derived from data on foreign-born population. For purposes of estimation, Australia, t...[105 truncated]', 'Including Christmas Island, Cocos (Keeling) Islands and Norfolk Island.', 'Data source : Human Mortality Database by University of California, Berkeley, and Max Planck Institu...[28 truncated]', 'Data sources : Australian Bureau of Statistics', 'Including Other Territories comprising Jervis Bay Territory, Christmas Island and the Cocos (Keeling...[11 truncated]', 'Data sources: Australian Bureau of Statistics', 'Data are reported in Austrian schillings.', 'UNHCR estimates based on the arrival of refugees and asylum-seeker recognition over a 10-year period...[32 truncated]', 'Data sources : Eurostat, Statistik Austria', 'European Union (EU) member countries apply a common tariff schedule. Historical data for EU member c...[155 truncated]', 'Long-term public and publicly guaranteed debt data for 2014 are based on reports provided by the cou...[155 truncated]', 'Adjustments for currency change (from old to new manat) were made for the entire Azerbaijan series s...[42 truncated]', 'The decrease in the refugee population in 2000 is due to the naturalization of some 188,000 ethnic-A...[105 truncated]', 'Including Nagorno-Karabakh.', 'Data source : United Nations World Population Prospects. Including Nagorno-Karabakh.', 'Data sources : State Statistical Committee, United Nations World Population Prospects', 'Data sources : State Statistical Committee, Eurostat, United Nations World Population Prospects', 'Data sources: Eurostat, State Statistical Committee, United Nations World Population Prospects'] \n);\nCREATE TABLE `Footnotes` (\n  `Countrycode` text\n    foreign key (Countrycode) references Country (CountryCode), -- Country code Example values: ['ABW', 'ADO', 'AFG', 'AGO', 'ALB', 'ARB', 'ARE', 'ARG', 'ARM', 'ASM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CEB', 'CHE', 'CHI', 'CHL', 'CHN', 'CIV', 'CMR', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CSS', 'CUB', 'CUW', 'CYM'] \n  `Seriescode` text\n    foreign key (Seriescode) references Series (SeriesCode), -- Series code Example values: ['AG.LND.FRST.K2', 'BX.KLT.DINV.CD.WD', 'DC.DAC.AUSL.CD', 'DC.DAC.AUTL.CD', 'DC.DAC.BELL.CD', 'DC.DAC.CANL.CD', 'DC.DAC.CECL.CD', 'DC.DAC.CHEL.CD', 'DC.DAC.DEUL.CD', 'DC.DAC.DNKL.CD', 'DC.DAC.ESPL.CD', 'DC.DAC.FINL.CD', 'DC.DAC.FRAL.CD', 'DC.DAC.GBRL.CD', 'DC.DAC.GRCL.CD', 'DC.DAC.IRLL.CD', 'DC.DAC.ITAL.CD', 'DC.DAC.JPNL.CD', 'DC.DAC.LUXL.CD', 'DC.DAC.NLDL.CD', 'DC.DAC.NORL.CD', 'DC.DAC.NZLL.CD', 'DC.DAC.PRTL.CD', 'DC.DAC.SWEL.CD', 'DC.DAC.TOTL.CD', 'DC.DAC.USAL.CD', 'DT.NFL.IFAD.CD', 'DT.NFL.UNCF.CD', 'DT.NFL.UNCR.CD', 'DT.NFL.UNDP.CD', 'DT.NFL.UNFP.CD', 'DT.NFL.UNRW.CD', 'DT.NFL.UNTA.CD', 'DT.NFL.WFPG.CD', 'DT.ODA.ALLD.CD', 'DT.ODA.ALLD.KD', 'EG.ELC.ACCS.RU.ZS', 'EG.ELC.ACCS.UR.ZS', 'EG.ELC.ACCS.ZS', 'IS.SHP.GOOD.TU', 'IT.NET.SECR', 'SE.PRM.NINT.FE.ZS', 'SE.PRM.NINT.MA.ZS', 'SE.PRM.NINT.ZS', 'SE.PRM.TENR', 'SE.PRM.TENR.FE', 'SE.PRM.TENR.MA', 'SE.PRM.UNER', 'SE.PRM.UNER.FE', 'SE.PRM.UNER.MA'] \n  `Year` text, -- Year Example values: ['YR1990', 'YR2000', 'YR2005', 'YR1987', 'YR1988', 'YR1989', 'YR2013', 'YR2001', 'YR2002', 'YR2003', 'YR2004', 'YR2010', 'YR2012', 'YR2007', 'YR2008', 'YR2009', 'YR2006', 'YR2011', 'YR1994', 'YR1997', 'YR2014', 'YR1991', 'YR1992', 'YR1993', 'YR1995', 'YR1996', 'YR1998', 'YR1999', 'YR1986', 'YR2015', 'YR1970', 'YR1971', 'YR1972', 'YR1973', 'YR1976', 'YR1977', 'YR1979', 'YR1980', 'YR1981', 'YR1982', 'yr2002', 'yr2004', 'YR1961', 'YR1962', 'YR1963', 'YR1964', 'YR1965', 'YR1966', 'YR1967', 'YR1968'] \n  `Description` text, -- Description Example values: ['Not specified', 'Source: United Nations Conference on Trade and Development, Foreign Direct Investment Online databas...[2 truncated]', 'Data are classified as official aid.', 'Source: Estimate', 'Source:Estimate', 'Data are from the UNCTAD secretariat, derived from information contained in Containerisation Interna...[155 truncated]', 'Oct-06', 'Dec-07', 'December, 2008', 'December, 2009', 'December, 2010', 'December, 2011', 'December, 2012', 'UNESCO Institute for Statistics (UIS) estimate', 'Source: Labour force survey. Coverage: Total. Coverage (employment): Total employment. Age: 15+. Ref...[23 truncated]', 'Source: Population census. Coverage: Total. Coverage (employment): Total employment. Age: 15+. Refer...[38 truncated]', 'Source: Labour force survey. Coverage: Total. Coverage (employment): Total employment. Age: 15+. Ref...[40 truncated]', 'Source: Labour force survey. Coverage: Total. Coverage (employment): Total employment. Age: 15+. Bre...[13 truncated]', 'Health situation in the americas. Basic  indicators 2006. PAHO', 'Uncertainty bound is 41 - 53', 'Uncertainty bound is 55 - 72', 'Uncertainty bound is 200 - 260', 'Uncertainty bound is 81 - 110', 'Uncertainty bound is 16 - 20', 'Uncertainty bound is 11 - 14', 'Uncertainty bound is 10 - 14', 'Uncertainty bound is 10 - 13', 'Uncertainty bound is 9.6 - 12', 'Source: Household or labour force survey. Coverage: Total. Age: 15+.', 'Source: Population census. Coverage: Total. Age: 15+. Reference period: October. Break in series.', 'Source: Household or labour force survey. Coverage: Total. Age: 15+. Reference period: October. Brea...[12 truncated]', 'Source: Population census. Coverage: Total. Age: 14+. Reference period: September. Break in series.', 'Source: Labour force survey. Coverage: Total. Age: 15+. Break in series.', 'Source: Population census. Coverage: Civilian. Coverage (employment): Civilian employment. Age: 14-2...[86 truncated]', 'Source: Population census. Age: 14+. Coverage: Total. Reference period: October.', 'Source: Household or labour force survey. Age: 15+. Coverage: Total. Break in series.', 'Source: Population census. Age: 15+. Coverage: Total. Reference period: October. Break in series.', 'Source: Household or labour force survey. Age: 15+. Coverage: Total. Reference period: October. Brea...[12 truncated]', 'Source: Population census. Age: 14+. Coverage: Total. Reference period: September. Break in series.', 'Source: Household or labour force survey. Age: 15+. Coverage: Total.', 'Source: Population census. Coverage: Total. Coverage (employment): Total employment. Age: 14+. Refer...[21 truncated]', 'Source: Household or labour force survey. Coverage: Total. Coverage (employment): Total employment. ...[53 truncated]', 'Source: Population census. Coverage: Civilian. Coverage (employment): Civilian employment. Age: 14+....[84 truncated]', 'Source: Labour force survey. Coverage: Total. Coverage (employment): Total employment. Age: 15+. Not...[102 truncated]', 'Source: Population census. Age: 15-24. Coverage: Total. Reference period: October.', 'Source: Labour force survey. Age: 15-24. Coverage: Total.', 'Source: Population census. Age: 14-24. Coverage: Civilian. Reference period: September. Coverage lim...[93 truncated]', 'Source: Population census. Age: 15+. Coverage: Total. Reference period: October.', 'Source: Labour force survey. Age: 15+. Coverage: Total.', 'Source: Population census. Age: 14+. Coverage: Civilian. Reference period: September. Coverage limit...[91 truncated]'] \n);\nCREATE TABLE `Indicators` (\n  `CountryName` text, -- Country code Example values: ['Arab World', 'Caribbean small states', 'Central Europe and the Baltics', 'East Asia & Pacific (all income levels)', 'East Asia & Pacific (developing only)', 'Euro area', 'Europe & Central Asia (all income levels)', 'Europe & Central Asia (developing only)', 'European Union', 'Fragile and conflict affected situations', 'Heavily indebted poor countries (HIPC)', 'High income', 'High income: nonOECD', 'High income: OECD', 'Latin America & Caribbean (all income levels)', 'Latin America & Caribbean (developing only)', 'Least developed countries: UN classification', 'Low & middle income', 'Low income', 'Lower middle income', 'Middle East & North Africa (all income levels)', 'Middle East & North Africa (developing only)', 'Middle income', 'North America', 'OECD members', 'Other small states', 'Pacific island small states', 'Small states', 'South Asia', 'Sub-Saharan Africa (all income levels)', 'Sub-Saharan Africa (developing only)', 'Upper middle income', 'World', 'Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados'] \n  `CountryCode` text\n    foreign key (CountryCode) references Country (CountryCode), -- Series code Example values: ['ABW', 'ADO', 'AFG', 'AGO', 'ALB', 'ARB', 'ARE', 'ARG', 'ARM', 'ASM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CEB', 'CHE', 'CHI', 'CHL', 'CHN', 'CIV', 'CMR', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CSS', 'CUB', 'CUW', 'CYM'] \n  `IndicatorName` text, -- Indicator Name Example values: ['Adolescent fertility rate (births per 1,000 women ages 15-19)', 'Age dependency ratio (% of working-age population)', 'Age dependency ratio, old (% of working-age population)', 'Age dependency ratio, young (% of working-age population)', 'Arms exports (SIPRI trend indicator values)', 'Arms imports (SIPRI trend indicator values)', 'Birth rate, crude (per 1,000 people)', 'CO2 emissions (kt)', 'CO2 emissions (metric tons per capita)', 'CO2 emissions from gaseous fuel consumption (% of total)', 'CO2 emissions from liquid fuel consumption (% of total)', 'CO2 emissions from liquid fuel consumption (kt)', 'CO2 emissions from solid fuel consumption (% of total)', 'Death rate, crude (per 1,000 people)', 'Fertility rate, total (births per woman)', 'Fixed telephone subscriptions', 'Fixed telephone subscriptions (per 100 people)', 'Hospital beds (per 1,000 people)', 'International migrant stock (% of population)', 'International migrant stock, total', 'Life expectancy at birth, female (years)', 'Life expectancy at birth, male (years)', 'Life expectancy at birth, total (years)', 'Merchandise exports (current US$)', 'Merchandise exports by the reporting economy (current US$)', 'Merchandise exports by the reporting economy, residual (% of total merchandise exports)', 'Merchandise exports to developing economies in East Asia & Pacific (% of total merchandise exports)', 'Merchandise exports to developing economies in Latin America & the Caribbean (% of total merchandise...[9 truncated]', 'Merchandise exports to developing economies in Middle East & North Africa (% of total merchandise ex...[6 truncated]', 'Merchandise exports to developing economies in South Asia (% of total merchandise exports)', 'Merchandise exports to developing economies in Sub-Saharan Africa (% of total merchandise exports)', 'Merchandise exports to developing economies outside region (% of total merchandise exports)', 'Merchandise exports to developing economies within region (% of total merchandise exports)', 'Merchandise exports to economies in the Arab World (% of total merchandise exports)', 'Merchandise exports to high-income economies (% of total merchandise exports)', 'Merchandise imports (current US$)', 'Merchandise imports by the reporting economy (current US$)', 'Merchandise imports by the reporting economy, residual (% of total merchandise imports)', 'Merchandise imports from developing economies in East Asia & Pacific (% of total merchandise imports...[1 truncated]', 'Merchandise imports from developing economies in Latin America & the Caribbean (% of total merchandi...[11 truncated]', 'Merchandise imports from developing economies in Middle East & North Africa (% of total merchandise ...[8 truncated]', 'Merchandise imports from developing economies in South Asia (% of total merchandise imports)', 'Merchandise imports from developing economies in Sub-Saharan Africa (% of total merchandise imports)', 'Merchandise imports from developing economies outside region (% of total merchandise imports)', 'Merchandise imports from developing economies within region (% of total merchandise imports)', 'Merchandise imports from economies in the Arab World (% of total merchandise imports)', 'Merchandise imports from high-income economies (% of total merchandise imports)', 'Merchandise trade (% of GDP)', 'Mobile cellular subscriptions', 'Mobile cellular subscriptions (per 100 people)'] \n  `IndicatorCode` text, -- Indicator Code Example values: ['AG.LND.AGRI.K2', 'AG.LND.AGRI.ZS', 'AG.LND.ARBL.HA', 'AG.LND.ARBL.HA.PC', 'AG.LND.ARBL.ZS', 'AG.LND.EL5M.ZS', 'AG.LND.FRST.K2', 'AG.LND.FRST.ZS', 'AG.LND.TOTL.K2', 'AG.SRF.TOTL.K2', 'BG.GSR.NFSV.GD.ZS', 'BM.GSR.CMCP.ZS', 'BM.GSR.FCTY.CD', 'BM.GSR.GNFS.CD', 'BM.GSR.INSF.ZS', 'BM.GSR.MRCH.CD', 'BM.GSR.NFSV.CD', 'BM.GSR.ROYL.CD', 'BM.GSR.TOTL.CD', 'BM.GSR.TRAN.ZS', 'BM.GSR.TRVL.ZS', 'BM.KLT.DINV.GD.ZS', 'BM.TRF.PRVT.CD', 'BM.TRF.PWKR.CD.DT', 'BN.CAB.XOKA.CD', 'BN.CAB.XOKA.GD.ZS', 'BN.FIN.TOTL.CD', 'BN.GSR.FCTY.CD', 'BN.GSR.GNFS.CD', 'BN.GSR.MRCH.CD', 'BN.KAC.EOMS.CD', 'BN.KLT.DINV.CD', 'BN.KLT.PTXL.CD', 'BN.RES.INCL.CD', 'BN.TRF.CURR.CD', 'BN.TRF.KOGT.CD', 'BX.GRT.EXTA.CD.WD', 'BX.GRT.TECH.CD.WD', 'BX.GSR.CCIS.CD', 'BX.GSR.CCIS.ZS', 'BX.GSR.CMCP.ZS', 'BX.GSR.FCTY.CD', 'BX.GSR.GNFS.CD', 'BX.GSR.INSF.ZS', 'BX.GSR.MRCH.CD', 'BX.GSR.NFSV.CD', 'BX.GSR.ROYL.CD', 'BX.GSR.TOTL.CD', 'BX.GSR.TRAN.ZS', 'BX.GSR.TRVL.ZS'] \n  `Year` integer, -- Year Example values: ['1961', '1962', '1963', '1964', '1965'] \n  `Value` integer, -- Value Example values: ['133', '87', '6', '81', '3000000'] \n);\nCREATE TABLE `SeriesNotes` (\n  `Seriescode` text\n    primary key, -- Series code Example values: ['DT.DOD.PVLX.CD', 'IC.CUS.DURS.EX', 'IC.FRM.BNKS.ZS', 'IC.FRM.CORR.ZS', 'IC.FRM.CRIM.ZS', 'IC.FRM.DURS', 'IC.FRM.FEMO.ZS', 'IC.FRM.FREG.ZS', 'IC.FRM.ISOC.ZS', 'IC.FRM.OUTG.ZS', 'IC.FRM.TRNG.ZS', 'IC.GOV.DURS.ZS', 'IC.TAX.METG', 'IQ.WEF.CUST.XQ', 'IQ.WEF.PORT.XQ', 'NY.ADJ.SVNG.GN.ZS', 'SM.POP.NETM', 'SM.POP.REFG', 'SM.POP.REFG.OR', 'SN.ITK.VITA.ZS', 'SP.ADO.TFRT', 'SP.DYN.AMRT.FE', 'SP.DYN.AMRT.MA', 'SP.DYN.TO65.FE.ZS', 'SP.DYN.TO65.MA.ZS'] \n  `Year` text\n    primary key, -- Year Example values: ['YR2014', 'YR2002', 'YR2003', 'YR2004', 'YR2005', 'YR2006', 'YR2007', 'YR2008', 'YR2009', 'YR2011', 'YR2012', 'YR2013', 'YR1962', 'YR1967', 'YR1972', 'YR1977', 'YR1982', 'YR1987', 'YR1992', 'YR1997', 'YR1960', 'YR1961', 'YR1963', 'YR1964', 'YR1965', 'YR1966', 'YR1968', 'YR1969', 'YR1970', 'YR1971', 'YR1973', 'YR1974', 'YR1975', 'YR1976', 'YR1978', 'YR1979', 'YR1980', 'YR1981', 'YR1983', 'YR1984', 'YR1985', 'YR1986', 'YR1988', 'YR1989', 'YR1990', 'YR1991', 'YR1993', 'YR1994', 'YR1995', 'YR1996'] \n  `Description` text, -- Description Example values: ['Interpolated using data for 1957 and 1962.', 'Interpolated using data for 1957 and 1962, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1960-1965.', 'The data refer to 1960-1965, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1960 to 30 June, 1965.', 'Interpolated using data for 1962 and 1967.', 'Interpolated using data for 1962 and 1967, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1965-1970.', 'The data refer to 1965-1970, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1965 to 30 June, 1970.', 'Interpolated using data for 1967 and 1972.', 'Interpolated using data for 1967 and 1972, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1970-1975.', 'The data refer to 1970-1975, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1970 to 30 June, 1975.', 'Interpolated using data for 1972 and 1977.', 'Interpolated using data for 1972 and 1977, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1975-1980.', 'The data refer to 1975-1980, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1975 to 30 June, 1980.', 'Interpolated using data for 1977 and 1982.', 'Interpolated using data for 1977 and 1982, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1980-1985.', 'The data refer to 1980-1985, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1980 to 30 June, 1985.', 'Interpolated using data for 1982 and 1987.', 'Interpolated using data for 1982 and 1987, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1985-1990.', 'The data refer to 1985-1990, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1985 to 30 June, 1990.', 'Interpolated using data for 1987 and 1992.', 'Interpolated using data for 1987 and 1992, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1990-1995.', 'The data refer to 1990-1995, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1990 to 30 June, 1995.', 'Interpolated using data for 1992 and 1997.', 'Interpolated using data for 1992 and 1997, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 1995-2000.', 'The data refer to 1995-2000, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 1995 to 30 June,2000.', 'Interpolated using data for 1997 and 2002.', 'Interpolated using data for 1997 and 2002, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 2000-2005.', 'The data refer to 2000-2005, if the data source is United Nations World Population Prospects.', 'The data refer to five-year periods running from 1 July, 2000 to 30 June, 2005.', 'The sample was drawn from the manufacturing sector only.', 'Interpolated using data for 2002 and 2007.', 'Interpolated using data for 2002 and 2007, if the data source is United Nations World Population Pro...[7 truncated]', 'The data refer to 2005-2010.', 'The data refer to 2005-2010, if the data source is United Nations World Population Prospects.'] \n);

--------------------------
The folloiwing are the examples generated for the above database schemas:

Example 1)
"input": "Among the countries in the group of Heavily Indebted Poor Countries, how many of them are under the lending category of the International Development Associations?\n\n(Hints: group of Heavily Indebted Poor Countries is OtherGroups = 'HIPC'; International Development Associations refers to lendingcategory = 'IDA')"

"output": "SELECT COUNT(CountryCode) FROM Country WHERE LendingCategory = 'IDA' AND OtherGroups = 'HIPC'"

Example 2)
"input": "Please list the countries under the lending category of the International Development Associations and have a external debt reporting finished by estimation.\n\n(Hints: countries refer to the ShortName; International Development Associations refers to lendingcategory = 'IDA'; have a external debt reporting finished by estimation refers to ExternalDebtReportingStatus = 'Estimate')"

"output": "SELECT ShortName, ExternalDebtReportingStatus FROM Country WHERE LendingCategory = 'IDA'"

Example 3)
"input": "What's the description of the series code SM.POP.TOTL for Aruba?\n\n(Hints: Aruba is the name of the country where ShortName = 'Aruba')"

"output": "SELECT T2.Description FROM Country AS T1 INNER JOIN CountryNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T1.ShortName = 'Aruba' AND T2.Seriescode = 'SM.POP.TOTL'"

Example 4)
"input": "Please list the countries in Latin America & Caribbean with a note on the series code SM.POP.TOTL.\n\n(Hints: Countries refer to the ShortName; Latin America & Caribbean is the name of the region)"

"output": "SELECT T1.SHORTNAME, T2.Description FROM Country AS T1 INNER JOIN CountryNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T1.Region = 'Latin America & Caribbean' AND T2.Seriescode = 'SM.POP.TOTL'"

Example 5)
"input": "Among the countries with note on the series code SM.POP.TOTL, how many of them are in the low-income group?\n\n(Hints: countries refer to Countrycode; low-income group refers to incomegroup = 'Low income'; with notes refers to description IS NOT NULL; series code SM.POP.TOTL refers to Seriescode = 'SM.POP.TOTL')"

"output": "SELECT COUNT(T1.Countrycode) FROM Country AS T1 INNER JOIN CountryNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T2.Seriescode = 'SM.POP.TOTL' AND T1.IncomeGroup = 'Low income'"

Example 6)
"input": "Please list the descriptions of the series code SM.POP.TOTL for all the countries that are under the lending category of the International Development Associations.\n\n(Hints: Countries are the Countrycode; International Development Associations refers to lendingcategory = 'IDA'"

"output": "SELECT T2.Description FROM Country AS T1 INNER JOIN CountryNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T1.LendingCategory = 'IDA' AND T2.Seriescode = 'SM.POP.TOTL'"

Example 7)
"input": "How many low-income countries under the lending category of the International Development Associations have a note on the series code SM.POP.TOTL?\n\n(Hints: low-income countries are where the incomegroup = Low income)"

"output": "SELECT COUNT(T1.Countrycode) FROM Country AS T1 INNER JOIN CountryNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T1.LendingCategory = 'IDA' AND T2.Seriescode = 'SM.POP.TOTL' AND IncomeGroup = 'Low income'"

Example 8)
"input": "Among the countries in the High income: OECD group whose currency unit is Euro, how many of them have a note on the series code SP.DYN.AMRT.FE?\n\n(Hints: countries refer to Countrycode; in the high income refers to incomegroup = 'High'; with notes refers to description IS NOT NULL; series code SP.DYN.AMRT.FE refers to Seriescode = 'SP.DYN.AMRT.FE')"

"output": "SELECT COUNT(T1.Countrycode) FROM Country AS T1 INNER JOIN CountryNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T1.IncomeGroup = 'High income: OECD' AND T1.CurrencyUnit = 'Euro' AND T2.Seriescode = 'SP.DYN.AMRT.FE'"

Example 9)
"input": "What is the long name of the country with the description \"Estimates are derived from data on foreign-born population.\" on the series code SM.POP.TOTL?\n\n(Hints: )"

"output": "SELECT T1.LongName FROM Country AS T1 INNER JOIN CountryNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T2.Description = 'Estimates are derived FROM data on foreign-born population.' AND T2.Seriescode = 'SM.POP.TOTL'"

Example 10)
"input": "What is the description of the footnote on the series code AG.LND.FRST.K2 in 1990 for Aruba?\n\n(Hints: Year = 1990; Aruba is the name of country where ShortName = 'Aruba')"

"output": "SELECT T2.Description FROM Country AS T1 INNER JOIN FootNotes AS T2 ON T1.CountryCode = T2.Countrycode WHERE T1.ShortName = 'Aruba' AND T2.Seriescode = 'AG.LND.FRST.K2' AND T2.Year = 'YR1990'"

**************************

Now similarly, generate examples (question input and SQL output pairs) for the table schemas defined below, in "Table creation statements".
**************************
###Table creation statements###
{}

**************************

Only outputs the examples (question input and SQL output pairs), and each eaxmple can be separated by a new line.

"""

LITERAL_ERROR_TEMPLATE = """You are a SQLite SQL expert.
Someone had a question and they tried to run a SQL query to fetch the data for it.
It is possible there were some literal errors in the query.
Or you used a wrong table(s) and column(s) in the query.

The provided "Hints" should also give you the right column names and the literal values.

Now you need to fix the query based on the question and the table schemas with example column values.

The database structure is defined by the following table schemas (comments after '--' provide additional column descriptions and example values).

This time, I will provide additional table column example values in a separate section, "Table column example values" in the following format:
* `table_name`.`column_name`: [val1, val2, val3, ...]
* `table_name`.`column_name`: [val1, val2, val3, ...]

Use this list to correct for any typos in your literals, also they are case sensitive.
If the literal you are looking for do not appear in the table column value list, then also check if similar literals appear in the column or even in other columns.
If it belongs to another column, consider rewriting your query with that and verify your query.
Correct your SQL query based on this.


**************************
###Table creation statements###
{}
**************************
###Table column example values###
{}
**************************
The original question is:
{}
**************************
The SQL query executed was:
{}

**************************
Based on the question, table schemas, the example column values and the executed query, analyze what the query was trying to achieve and fix the query.

DONT FORGET Additional rules to generate correct SQLite SQL dialect:
- Try to use all the pieces of information provided in the hints.
- Column values/literals: Make sure that column values and literals are correct. Consider the column example values and hints provided.
- Table Aliases: Use aliases to avoid duplicate table name conflicts.
- Column References: Verify column names and use table_name.column_name format.
- Functions: Use correct SQLite functions for the intended data types.
- HAVING Clause: Employ boolean expressions (comparisons, AND, OR, NOT). Consider subqueries for top values.
- Table Joins: Ensure table names are correct and use appropriate joins.
- Arithmetic: Use basic operators (+, -, *, /) if dedicated functions are missing.
- Put double quotations around column names and table names, especially when there is a space in between words.
- Use double quotations for string literals.
- A single quote within the string can be encoded by putting two single quotes in a row (''): "Men's basketball" should be "Men''s basketball"
- When comparing string/text type in filter criteria, use LIKE operator and surround the text with wildcards %.
- When you need to find the highest or lowest values based on a certain condition, using ORDER BY and LIMIT 1 is prefered over using MAX/MIN within sub queries.
- If the question doesn't specify exactly which columns to select between name column and id column, prefer to select id column.


If there is no error you can find or fix, just output the original SQL query.
Output the sqlite query string ONLY. It should be the query in plain text.
"""

CHECKER_TEMPLATE = """You are a SQLite SQL expert.
Someone had a question and they tried to run a SQL query to fetch the data for it.
However, the query execution failed for some error.
Now you need to fix the query based on the previous execution error.

The database structure is defined by the following table schemas (comments after '--' provide additional column descriptions).
**************************
###Table creation statements###
{}
**************************
The original question is:
{}

The SQL query executed was:
{}

The execution failed with error:
{}

**************************
Based on the question, table schemas and the errored query, analyze what the query was trying to achieve and fix the error.

If the error cannot be fixed by fixing the query, for example, connection error or permission error, just output the original query.
Otherwise, think step by step about generating correct SQLite SQL result!

Analyze the error and how to fix.

DONT FORGET Additional rules to generate correct SQLite SQL dialect:
- Try to use all the pieces of information provided in the hints.
- Column values/literals: Make sure that column values and literals are correct. Consider the column example values and hints provided.
- Table Aliases: Use aliases to avoid duplicate table name conflicts.
- Column References: Verify column names and use table_name.column_name format.
- Functions: Use correct SQLite functions for the intended data types.
- HAVING Clause: Employ boolean expressions (comparisons, AND, OR, NOT). Consider subqueries for top values.
- Table Joins: Ensure table names are correct and use appropriate joins.
- Arithmetic: Use basic operators (+, -, *, /) if dedicated functions are missing.
- Put double quotations around column names and table names, especially when there is a space in between words.
- Use double quotations for string literals.
- A single quote within the string can be encoded by putting two single quotes in a row (''): "Men's basketball" should be "Men''s basketball"
- When comparing string/text type in filter criteria, use LIKE operator and surround the text with wildcards %.
- When you need to find the highest or lowest values based on a certain condition, using ORDER BY and LIMIT 1 is prefered over using MAX/MIN within sub queries.
- If the question doesn't specify exactly which columns to select between name column and id column, prefer to select id column.


When you are OK with the fixed query, output the sqlite query string ONLY. It should be the query in plain text.
"""

removed_rules = """
- Respect the upper and lower case in the question, make sure they are the same in the query.
"""

VERIFICATION_TEMPLATE = """You are a SQLite SQL expert.
Someone had a question and they tried to run a SQL query to fetch the data for it.
Now you need to verify if the query is correctly addressing the question,
given the table schemas, column definitions and example values, and hints.

The database structure is defined by the following table schemas (comments after '--' provide additional column descriptions).
**************************
###Table creation statements###
{}
**************************
The original question is:
{}

The SQL query executed was:
{}

**************************
Based on the question, table schemas, analyze what the query was trying to achieve and verify against the question.

Your response should be one of the following:

- Return "correct" if SQL is correctly answering the question.
- Return "incorrect" if SQL is not correctly answering the question.
"""

#### SPIDER ####
INSTRUCTION_PROMPT = """\
I want you to act as a SQL expert, who writes a SQL query (in sqlite dialect) per user request. \
You only need to return the sql command to me. Below is some helpful context information, \
including a database's tables and their column names, some examples and hints. \
Note that the table names and column names are case sensitive and put inside quotations including the spaces; \
do not remove the spaces in the column names, \
and make sure to associate the columns to the correct corresponding tables. The context should be clear \
which table contains which columns. \
Write a response that appropriately completes the request. \n"
### Context:\n{}\n"""
INPUT_PROMPT = "###Input:\n{}\n\n###Response:"

INSTRUCTION_N_SHOT_PROMPT = """\
I want you to act as a SQL expert, who writes a SQL (in sqlite dialect) query per user request. \
You only need to return the sql command to me. Below is some helpful context information, \
including a database's tables and their column names, some examples and hints. \
Note that the table names and column names are case sensitive and put inside quotations including the spaces; \
do not remove the spaces in the column names, \
and make sure to associate the columns to the correct corresponding tables. The context should be clear \
which table contains which columns. \
Write a response that appropriately completes the request. \n"
### Context:\n{}\n"""

INSTRUCTION_ONE_SHOT_PROMPT = """\
I want you to act as a SQL expert, who writes a SQL (in sqlite dialect) query per user request. \
You only need to return the sql command to me. Below is some helpful context information, \
including a database's tables and their column names, some examples and hints. \
Note that the table names and column names are case sensitive and put inside quotations including the spaces; \
do not remove the spaces in the column names, \
and make sure to associate the columns to the correct corresponding tables. The context should be clear \
which table contains which columns. \
Write a response that appropriately completes the request. \n"
\n### Example1 Context:
The database contains tables such as employee, salary, and position. \
Table employee has columns such as employee_id, name, age, and position_id. employee_id is the primary key. \
Table salary has columns such as employee_id, amount, and date. employee_id is the primary key. \
Table position has columns such as position_id, title, and department. position_id is the primary key. \
The employee_id of salary is the foreign key of employee_id of employee. \
The position_id of employee is the foreign key of position_id of position.\
\n### Example1 Input:\nList the names and ages of employees in the 'Engineering' department. \
\n### Example1 Response:\nSELECT employee.name, employee.age FROM employee JOIN position ON employee.position_id = position.position_id WHERE position.department = 'Engineering' \
\n\n### Context:\n{}\n"""

INSTRUCTION_THREE_SHOT_PROMPT = """\
I want you to act as a SQL expert, who writes a SQL (in sqlite dialect) query per user request. \
You only need to return the sql command to me. Below is some helpful context information, \
including a database's tables and their column names, some examples and hints. \
Note that the table names and column names are case sensitive and put inside quotations including the spaces; \
do not remove the spaces in the column names, \
and make sure to associate the columns to the correct corresponding tables. The context should be clear \
which table contains which columns. \
Write a response that appropriately completes the request. \n"
\n### Example1 Context: \
The database contains tables such as state, callcenterlogs, client, district, events, reviews. \
Table state has columns such as StateCode, State, Region. StateCode is the primary key.\nTable callcenterlogs \
has columns such as Date received, Complaint ID, rand client, phonefinal, vru+line, call_id, priority, type, outcome, server, ser_start, ser_exit, ser_time. \
Complaint ID is the primary key.\nTable client has columns such as client_id, sex, day, month, year, age, social, first, middle, last, phone, email, address_1, address_2, city, state, zipcode, district_id. client_id is the primary key. \
\nTable district has columns such as district_id, city, state_abbrev, division. district_id is the primary key.\nTable events has columns such as Date received, Product, Sub-product, Issue, Sub-issue, Consumer complaint narrative, \
Tags, Consumer consent provided?, Submitted via, Date sent to company, Company response to consumer, Timely response?, Consumer disputed?, Complaint ID, Client_ID. The combination of (Complaint ID, Client_ID) are the primary key. \
\nTable reviews has columns such as Date, Stars, Reviews, Product, district_id. Date is the primary key.\nThe rand client of callcenterlogs is the foreign key of client_id of client. The district_id of client is the foreign key of \
district_id of district. The state_abbrev of district is the foreign key of StateCode of state. The Client_ID of events is the foreign key of client_id of client. The Complaint ID of events is the foreign key of Complaint ID of callcenterlogs. \
The district_id of reviews is the foreign key of district_id of district. \nHere is some useful hints to generate the output: percentage = MULTIPLY(DIVIDE(SUM(\"Consumer disputed?\" = 'Yes' AND city = 'Houston'), COUNT(client_id)), 1.0); Houston refers to city = 'Houston';. \
\n### Example1 Input:\nWhat percentage of consumers from Houston disputed complaints? \
\n### Example1 Response:\nSELECT CAST(SUM(CASE WHEN T2.`Consumer disputed?` = 'Yes' AND T1.city = 'Houston' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.client_id) FROM client AS T1 INNER JOIN events AS T2 ON T1.client_id = T2.Client_ID \
\n\n### Example2 Context: \
The database  contains tables such as film_text, actor, address, category, city, country, customer, \
film, film_actor, film_category, inventory, language, payment, rental, staff, store. Table film_text \
has columns such as film_id, title, description. film_id is the primary key.\nTable actor has columns \
such as actor_id, first_name, last_name, last_update. actor_id is the primary key.\nTable address has \
columns such as address_id, address, address2, district, city_id, postal_code, phone, last_update. address_id \
is the primary key.\nTable category has columns such as category_id, name, last_update. category_id is the primary key. \
\nTable city has columns such as city_id, city, country_id, last_update. city_id is the primary key.\nTable country \
has columns such as country_id, country, last_update. country_id is the primary key.\nTable customer has columns such as \
customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update. customer_id is the primary \
key.\nTable film has columns such as film_id, title, description, release_year, language_id, original_language_id, rental_duration, \
rental_rate, length, replacement_cost, rating, special_features, last_update. film_id is the primary key.\nTable film_actor has columns \
such as actor_id, film_id, last_update. The combination of (actor_id, film_id) are the primary key.\nTable film_category has columns such as \
film_id, category_id, last_update. The combination of (film_id, category_id) are the primary key.\nTable inventory has columns such as inventory_id, \
film_id, store_id, last_update. inventory_id is the primary key.\nTable language has columns such as language_id, name, last_update. language_id is \
the primary key.\nTable payment has columns such as payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update. payment_id is the \
primary key.\nTable rental has columns such as rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update. rental_id is the \
primary key.\nTable staff has columns such as staff_id, first_name, last_name, address_id, picture, email, store_id, active, username, password, \
last_update. staff_id is the primary key.\nTable store has columns such as store_id, manager_staff_id, address_id, last_update. store_id is the primary \
key.\n\nHere is some useful hints to generate the output: over 4.99 refers to amount > 4.99. \
\n### Example2 Input:\nAmong the payments made by Mary Smith, how many of them are over 4.99? \
\n### Example2 Response:\nSELECT COUNT(T1.amount) FROM payment AS T1 INNER JOIN customer AS T2 ON T1.customer_id = T2.customer_id WHERE T2.first_name = 'MARY' AND T2.last_name = 'SMITH' AND T1.amount > 4.99 \
\n\n### Example3 Context: \
The database contains tables such as film_text, actor, address, category, city, country, customer, film, film_actor, \
film_category, inventory, language, payment, rental, staff, store. Table film_text has columns such as film_id, \
title, description. film_id is the primary key.\nTable actor has columns such as actor_id, first_name, last_name, \
last_update. actor_id is the primary key.\nTable address has columns such as address_id, address, address2, district, \
city_id, postal_code, phone, last_update. address_id is the primary key.\nTable category has columns such as category_id, \
name, last_update. category_id is the primary key.\nTable city has columns such as city_id, city, country_id, last_update. \
city_id is the primary key.\nTable country has columns such as country_id, country, last_update. country_id is the primary key.\n \
Table customer has columns such as customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update. \
customer_id is the primary key.\nTable film has columns such as film_id, title, description, release_year, language_id, original_language_id, \
rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update. film_id is the primary key.\nTable film_actor has columns such as actor_id, \
film_id, last_update. The combination of (actor_id, film_id) are the primary key.\nTable film_category has columns such as film_id, category_id, last_update. \
The combination of (film_id, category_id) are the primary key.\nTable inventory has columns such as inventory_id, film_id, store_id, last_update. \
inventory_id is the primary key.\nTable language has columns such as language_id, name, last_update. language_id is the primary key.\nTable payment \
has columns such as payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update. payment_id is the primary key.\nTable rental has columns such \
as rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update. rental_id is the primary key.\nTable staff has columns such as staff_id, \
first_name, last_name, address_id, picture, email, store_id, active, username, password, last_update. staff_id is the primary key.\nTable store has columns such as store_id, \
manager_staff_id, address_id, last_update. store_id is the primary key.\n\nHere is some useful hints to generate the output: Italy refers to country = 'Italy'; \
average amount = divide(sum(amount), count(customer_id)) where country = 'Italy'. \
\n### Example3 Input:\nWhat is the average amount of money spent by a customer in Italy on a single film rental? \
\n### Example3 Response:\SELECT AVG(T5.amount) FROM address AS T1 INNER JOIN city AS T2 ON T1.city_id = T2.city_id INNER JOIN country AS T3 ON T2.country_id = T3.country_id INNER JOIN customer AS T4 ON T1.address_id = T4.address_id INNER JOIN payment AS T5 ON T4.customer_id = T5.customer_id WHERE T3.country = 'Italy' \
\n\n### Context:\n{}\n"""

# EXAMPLES =[EXAMPLE1, EXAMPLE1]

# EXAMPLE1 = "\n### Example1 Input:\nList the names and ages of employees in the 'Engineering' department.\n\
# \n### Example1 Response:\nSELECT employee.name, employee.age FROM employee JOIN position ON employee.position_id = position.position_id WHERE position.department = 'Engineering';\
# \n###New Instruction:\n{}\n"

### test--------------------

# METHODS = ["full", "freeze", "lora"]

# STAGES = ["SFT", "Reward Modeling", "PPO", "DPO", "Pre-Training"]

# DATASET_STAGE_MAP = {
#     "SFT": "sft",
#     "Pre-Training": "pt",
#     "Reward Modeling": "rm",
#     "PPO": "sft",
#     "DPO": "rm",
# }

# SUPPORTED_MODELS = {
#     "LLaMA-7B": "huggyllama/llama-7b",
#     "LLaMA-13B": "huggyllama/llama-13b",
#     "LLaMA-30B": "huggyllama/llama-30b",
#     "LLaMA-65B": "huggyllama/llama-65b",
#     "LLaMA2-7B": "meta-llama/Llama-2-7b-hf",
#     "LLaMA2-13B": "meta-llama/Llama-2-13b-hf",
#     "LLaMA2-70B": "meta-llama/Llama-2-70b-hf",
#     "LLaMA2-7B-Chat": "meta-llama/Llama-2-7b-chat-hf",
#     "LLaMA2-13B-Chat": "meta-llama/Llama-2-13b-chat-hf",
#     "LLaMA2-70B-Chat": "meta-llama/Llama-2-70b-chat-hf",
#     "ChineseLLaMA2-7B": "ziqingyang/chinese-llama-2-7b",
#     "ChineseLLaMA2-13B": "ziqingyang/chinese-llama-2-13b",
#     "ChineseLLaMA2-7B-Chat": "ziqingyang/chinese-alpaca-2-7b",
#     "ChineseLLaMA2-13B-Chat": "ziqingyang/chinese-alpaca-2-13b",
#     "BLOOM-560M": "bigscience/bloom-560m",
#     "BLOOM-3B": "bigscience/bloom-3b",
#     "BLOOM-7B1": "bigscience/bloom-7b1",
#     "BLOOMZ-560M": "bigscience/bloomz-560m",
#     "BLOOMZ-3B": "bigscience/bloomz-3b",
#     "BLOOMZ-7B1-mt": "bigscience/bloomz-7b1-mt",
#     "Falcon-7B": "tiiuae/falcon-7b",
#     "Falcon-7B-Chat": "tiiuae/falcon-7b-instruct",
#     "Falcon-40B": "tiiuae/falcon-40b",
#     "Falcon-40B-Chat": "tiiuae/falcon-40b-instruct",
#     "Baichuan-7B": "baichuan-inc/Baichuan-7B",
#     "Baichuan-13B": "baichuan-inc/Baichuan-13B-Base",
#     "Baichuan-13B-Chat": "baichuan-inc/Baichuan-13B-Chat",
#     "Baichuan2-7B": "baichuan-inc/Baichuan2-7B-Base",
#     "Baichuan2-13B": "baichuan-inc/Baichuan2-13B-Base",
#     "Baichuan2-7B-Chat": "baichuan-inc/Baichuan2-7B-Chat",
#     "Baichuan2-13B-Chat": "baichuan-inc/Baichuan2-13B-Chat",
#     "InternLM-7B": "internlm/internlm-7b",
#     "InternLM-7B-Chat": "internlm/internlm-chat-7b",
#     "Qwen-7B": "Qwen/Qwen-7B",
#     "Qwen-7B-Chat": "Qwen/Qwen-7B-Chat",
#     "XVERSE-13B": "xverse/XVERSE-13B",
#     "ChatGLM2-6B-Chat": "THUDM/chatglm2-6b",
#     "ChatGLM3-6B-Base": "THUDM/chatglm3-6b-base",
#     "ChatGLM3-6B-Chat": "THUDM/chatglm3-6b"
# }

# DEFAULT_MODULE = {
#     "LLaMA": "q_proj,v_proj",
#     "LLaMA2": "q_proj,v_proj",
#     "ChineseLLaMA2": "q_proj,v_proj",
#     "BLOOM": "query_key_value",
#     "BLOOMZ": "query_key_value",
#     "Falcon": "query_key_value",
#     "Baichuan": "W_pack",
#     "Baichuan2": "W_pack",
#     "InternLM": "q_proj,v_proj",
#     "Qwen": "c_attn",
#     "XVERSE": "q_proj,v_proj",
#     "ChatGLM2": "query_key_value",
#     "ChatGLM3": "query_key_value",

# }

# DEFAULT_TEMPLATE = {
#     "LLaMA2": "llama2",
#     "ChineseLLaMA2": "llama2_zh",
#     "Baichuan": "baichuan",
#     "Baichuan2": "baichuan2",
#     "InternLM": "intern",
#     "Qwen": "chatml",
#     "ChatGLM2": "chatglm2",
#     "ChatGLM3": "chatglm3",

# }
