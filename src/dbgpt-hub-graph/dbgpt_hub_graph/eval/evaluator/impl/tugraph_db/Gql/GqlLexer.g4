lexer grammar GqlLexer;

options { caseInsensitive = true; }

AMPERSAND
   : '&'
   ;

ASTERISK
   : '*'
   ;

CIRCUMFLEX
   : '^'
   ;

COLON
   : ':'
   ;

COMMA
   : ','
   ;

DOLLAR_SIGN
   : '$'
   ;

EQUALS_OPERATOR
   : '='
   ;

EXCLAMATION_MARK
   : '!'
   ;

RIGHT_ANGLE_BRACKET
   : '>'
   ;

LEFT_BRACE
   : '{'
   ;

LEFT_BRACKET
   : '['
   ;

LEFT_PAREN
   : '('
   ;

LEFT_ANGLE_BRACKET
   : '<'
   ;

MINUS_SIGN
   : '-'
   ;

PERCENT
   : '%'
   ;

PERIOD
   : '.'
   ;

PLUS_SIGN
   : '+'
   ;

QUESTION_MARK
   : '?'
   ;

REVERSE_SOLIDUS
   : '\\'
   ;

RIGHT_BRACE
   : '}'
   ;

RIGHT_BRACKET
   : ']'
   ;

RIGHT_PAREN
   : ')'
   ;

SEMICOLON
   : ';'
   ;

SOLIDUS
   : '/'
   ;

TILDE
   : '~'
   ;

UNDERSCORE
   : '_'
   ;

VERTICAL_BAR
   : '|'
   ;

ABS
   : 'ABS'
   ;

ACOS
   : 'ACOS'
   ;

ACYCLIC
   : 'ACYCLIC'
   ;

ALL
   : 'ALL'
   ;

ALL_DIFFERENT
   : 'ALL_DIFFERENT'
   ;

ALLOW_ANONYMOUS_TABLE
   : 'ALLOW_ANONYMOUS_TABLE'
   ;

AND
   : 'AND' | '&&'
   ;

ANY
   : 'ANY'
   ;

ARRAY
   : 'ARRAY'
   ;

AS
   : 'AS'
   ;

ASC
   : 'ASC'
   ;

ASCENDING
   : 'ASCENDING'
   ;

ASIN
   : 'ASIN'
   ;

AT
   : 'AT'
   ;

ATAN
   : 'ATAN'
   ;

AVG
   : 'AVG'
   ;

BETWEEN
   : 'BETWEEN'
   ;

BIG
   : 'BIG'
   ;

BIGINT
   : 'BIGINT'
   ;

BINARY
   : 'BINARY'
   ;

BINDING
   : 'BINDING'
   ;

BINDINGS
   : 'BINDINGS'
   ;

BOOL
   : 'BOOL'
   ;

BOOLEAN
   : 'BOOLEAN'
   ;

BOTH
   : 'BOTH'
   ;

BTRIM
   : 'BTRIM'
   ;

BY
   : 'BY'
   ;

BYTE_LENGTH
   : 'BYTE_LENGTH'
   ;

BYTES
   : 'BYTES'
   ;

CALL
   : 'CALL'
   ;

CASE
   : 'CASE'
   ;

CAST
   : 'CAST'
   ;

CEIL
   : 'CEIL'
   ;

CEILING
   : 'CEILING'
   ;

CHAR_LENGTH
   : 'CHAR_LENGTH'
   ;

CHARACTER_LENGTH
   : 'CHARACTER_LENGTH'
   ;

CHARACTERISTICS
   : 'CHARACTERISTICS'
   ;

CLOSE
   : 'CLOSE'
   ;

COALESCE
   : 'COALESCE'
   ;

COLLECT
   : 'COLLECT'
   ;

COMMIT
   : 'COMMIT'
   ;

CONNECTION
   : 'CONNECTION'
   ;

CONNECTING
   : 'CONNECTING'
   ;

COPY
   : 'COPY'
   ;

COS
   : 'COS'
   ;

COSH
   : 'COSH'
   ;

COT
   : 'COT'
   ;

COUNT
   : 'COUNT'
   ;

CREATE
   : 'CREATE'
   ;

CURRENT_DATE
   : 'CURRENT_DATE'
   ;

CURRENT_GRAPH
   : 'CURRENT_GRAPH'
   ;

CURRENT_PROPERTY_GRAPH
   : 'CURRENT_PROPERTY_GRAPH'
   ;

CURRENT_SCHEMA
   : 'CURRENT_SCHEMA'
   ;

CURRENT_TIME
   : 'CURRENT_TIME'
   ;

CURRENT_TIMESTAMP
   : 'CURRENT_TIMESTAMP'
   ;

CURRENT_USER
   : 'CURRENT_USER'
   ;

DATE
   : 'DATE'
   ;

DATETIME
   : 'DATETIME'
   ;

DEC
   : 'DEC'
   ;

DECIMAL
   : 'DECIMAL'
   ;

DEGREES
   : 'DEGREES'
   ;

DELETE
   : 'DELETE'
   ;

DESC
   : 'DESC'
   ;

DESCENDING
   : 'DESCENDING'
   ;

DESTINATION
   : 'DESTINATION'
   ;

DETACH
   : 'DETACH'
   ;

DIFFERENT
   : 'DIFFERENT'
   ;

DIRECTED
   : 'DIRECTED'
   ;

DISTINCT
   : 'DISTINCT'
   ;

DOUBLE
   : 'DOUBLE'
   ;

DROP
   : 'DROP'
   ;

DURATION
   : 'DURATION'
   ;

DURATION_BETWEEN
   : 'DURATION_BETWEEN'
   ;

ELEMENT
   : 'ELEMENT'
   ;

ELEMENT_ID
   : 'ELEMENT_ID'
   ;

ELEMENTS
   : 'ELEMENTS'
   ;

ELSE
   : 'ELSE'
   ;

END
   : 'END'
   ;

EXCEPT
   : 'EXCEPT'
   ;

EXISTS
   : 'EXISTS'
   ;

EXP
   : 'EXP'
   ;

FALSE
   : 'FALSE'
   ;

FILTER
   : 'FILTER'
   ;

FINISH
   : 'FINISH'
   ;

FIRST
   : 'FIRST'
   ;

FLOAT
   : 'FLOAT'
   ;

FLOAT128
   : 'FLOAT128'
   ;

FLOAT16
   : 'FLOAT16'
   ;

FLOAT256
   : 'FLOAT256'
   ;

FLOAT32
   : 'FLOAT32'
   ;

FLOAT64
   : 'FLOAT64'
   ;

FLOOR
   : 'FLOOR'
   ;

FOR
   : 'FOR'
   ;

FROM
   : 'FROM'
   ;

GRAPH
   : 'GRAPH'
   ;

GROUP
   : 'GROUP'
   ;

GROUPS
   : 'GROUPS'
   ;

GROUP_CONCAT
   : 'GROUP_CONCAT'
   ;

HAVING
   : 'HAVING'
   ;

HOME_GRAPH
   : 'HOME_GRAPH'
   ;

HOME_PROPERTY_GRAPH
   : 'HOME_PROPERTY_GRAPH'
   ;

HOME_SCHEMA
   : 'HOME_SCHEMA'
   ;

ID
   : 'ID'
   ;

I_DONT_KNOW_1
   : 'I_DONT_KNOW_1'
   ;

I_DONT_KNOW_2
   : 'I_DONT_KNOW_2'
   ;

I_DONT_KNOW_3
   : 'I_DONT_KNOW_3'
   ;

I_DONT_KNOW_4
   : 'I_DONT_KNOW_4'
   ;

I_DONT_KNOW_5
   : 'I_DONT_KNOW_5'
   ;

IF
   : 'IF'
   ;

IN
   : 'IN'
   ;

INSERT
   : 'INSERT'
   ;

INT
   : 'INT'
   ;

INT8
   : 'INT8'
   ;

INT16
   : 'INT16'
   ;

INT32
   : 'INT32'
   ;

INT64
   : 'INT64'
   ;

INT128
   : 'INT128'
   ;

INT256
   : 'INT256'
   ;

INTEGER
   : 'INTEGER'
   ;

INTEGER8
   : 'INTEGER8'
   ;

INTEGER16
   : 'INTEGER16'
   ;

INTEGER32
   : 'INTEGER32'
   ;

INTEGER64
   : 'INTEGER64'
   ;

INTEGER128
   : 'INTEGER128'
   ;

INTEGER256
   : 'INTEGER256'
   ;

INTERSECT
   : 'INTERSECT'
   ;

IS
   : 'IS'
   ;

KEEP
   : 'KEEP'
   ;

LABEL
   : 'LABEL'
   ;

LABELED
   : 'LABELED'
   ;

LABELS
   : 'LABELS'
   ;

LAST
   : 'LAST'
   ;

KILL
   : 'KILL'
   ;

LEADING
   : 'LEADING'
   ;

LEFT
   : 'LEFT'
   ;

LENGTH
   : 'LENGTH'
   ;

LET
   : 'LET'
   ;

LIKE
   : 'LIKE'
   ;

LIMIT
   : 'LIMIT'
   ;

LIST
   : 'LIST'
   ;

LN
   : 'LN'
   ;

LOCAL
   : 'LOCAL'
   ;

LOCAL_DATETIME
   : 'LOCAL_DATETIME'
   ;

LOCAL_TIME
   : 'LOCAL_TIME'
   ;

LOCAL_TIMESTAMP
   : 'LOCAL_TIMESTAMP'
   ;

LOG
   : 'LOG'
   ;

LOG10
   : 'LOG10'
   ;

LONG
   : 'LONG'
   ;

LOWER
   : 'LOWER'
   ;

LTRIM
   : 'LTRIM'
   ;

MAP
   : 'MAP'
   ;

MATCH
   : 'MATCH'
   ;

MAX_
   : 'MAX'
   ;

MIN_
   : 'MIN'
   ;

MOD
   : 'MOD'
   ;

NEXT
   : 'NEXT'
   ;

NFC
   : 'NFC'
   ;

NFD
   : 'NFD'
   ;

NFKC
   : 'NFKC'
   ;

NFKD
   : 'NFKD'
   ;

NO
   : 'NO'
   ;

NODETACH
   : 'NODETACH'
   ;

NORMALIZE
   : 'NORMALIZE'
   ;

NORMALIZED
   : 'NORMALIZED'
   ;

NOT
   : 'NOT'
   ;

NULL_
   : 'NULL'
   ;

NULLIF
   : 'NULLIF'
   ;

NULLS
   : 'NULLS'
   ;

OCTET_LENGTH
   : 'OCTET_LENGTH'
   ;

OF
   : 'OF'
   ;

OFFSET
   : 'OFFSET'
   ;

ONLY
   : 'ONLY'
   ;

OPEN
   : 'OPEN'
   ;

OPTIONAL
   : 'OPTIONAL'
   ;

OR
   : 'OR'
   ;

ORDER
   : 'ORDER'
   ;

ORDINALITY
   : 'ORDINALITY'
   ;

OTHERWISE
   : 'OTHERWISE'
   ;

PARAMETER
   : 'PARAMETER'
   ;

PARAMETERS
   : 'PARAMETERS'
   ;

PATH
   : 'PATH'
   ;

PATH_LENGTH
   : 'PATH_LENGTH'
   ;

PATHS
   : 'PATHS'
   ;

PERCENTILE_CONT
   : 'PERCENTILE_CONT'
   ;

PERCENTILE_DISC
   : 'PERCENTILE_DISC'
   ;

PER_NODE_LIMIT
   : 'PER_NODE_LIMIT'
   ;

PER_SHARD_LIMIT
   : 'PER_SHARD_LIMIT'
   ;

POWER
   : 'POWER'
   ;

PRECISION
   : 'PRECISION'
   ;

PROCESSLIST
   : 'PROCESSLIST'
   ;

PROPERTY
   : 'PROPERTY'
   ;

PROPERTY_EXISTS
   : 'PROPERTY_EXISTS'
   ;

RADIANS
   : 'RADIANS'
   ;

READ
   : 'READ'
   ;

READ_CONSISTENCY
   : 'READ_CONSISTENCY'
   ;

REAL
   : 'REAL'
   ;

RECORD
   : 'RECORD'
   ;

REMOVE
   : 'REMOVE'
   ;

REPEATABLE
   : 'REPEATABLE'
   ;

REPLACE
   : 'REPLACE'
   ;

RESET
   : 'RESET'
   ;

RETURN
   : 'RETURN'
   ;

ROLLBACK
   : 'ROLLBACK'
   ;

RTRIM
   : 'RTRIM'
   ;

RIGHT
   : 'RIGHT'
   ;

SAME
   : 'SAME'
   ;

SCHEMA
   : 'SCHEMA'
   ;

SELECT
   : 'SELECT'
   ;

SESSION
   : 'SESSION'
   ;

SET
   : 'SET'
   ;

SHORTEST
   : 'SHORTEST'
   ;

SHOW
   : 'SHOW'
   ;

SIGNED
   : 'SIGNED'
   ;

SIMPLE
   : 'SIMPLE'
   ;

SIN
   : 'SIN'
   ;

SINH
   : 'SINH'
   ;

SKIP_
   : 'SKIP'
   ;

SMALL
   : 'SMALL'
   ;

SMALLINT
   : 'SMALLINT'
   ;

SOURCE
   : 'SOURCE'
   ;

SQRT
   : 'SQRT'
   ;

START
   : 'START'
   ;

STDDEV_POP
   : 'STDDEV_POP'
   ;

STDDEV_SAMP
   : 'STDDEV_SAMP'
   ;

STRING
   : 'STRING'
   ;

SUBSTR
   : 'SUBSTR'
   ;

SUM
   : 'SUM'
   ;

TABLE
   : 'TABLE'
   ;

TAN
   : 'TAN'
   ;

TANH
   : 'TANH'
   ;

TEMP
   : 'TEMP'
   ;

THEN
   : 'THEN'
   ;

TIME
   : 'TIME'
   ;

TIMESTAMP
   : 'TIMESTAMP'
   ;

TIMEZONE
   : 'TIMEZONE'
   ;

TO
   : 'TO'
   ;

TRAIL
   : 'TRAIL'
   ;

TRAILING
   : 'TRAILING'
   ;

TRANSACTION
   : 'TRANSACTION'
   ;

TRIM
   : 'TRIM'
   ;

TRUE
   : 'TRUE'
   ;

TYPE
   : 'TYPE'
   ;

TYPED
   : 'TYPED'
   ;

UBIGINT
   : 'UBIGINT'
   ;

UINT
   : 'UINT'
   ;

UINT128
   : 'UINT128'
   ;

UINT16
   : 'UINT16'
   ;

UINT256
   : 'UINT256'
   ;

UINT32
   : 'UINT32'
   ;

UINT64
   : 'UINT64'
   ;

UINT8
   : 'UINT8'
   ;

UNDIRECTED
   : 'UNDIRECTED'
   ;

UNION
   : 'UNION'
   ;

UNKNOWN
   : 'UNKNOWN'
   ;

UNSIGNED
   : 'UNSIGNED'
   ;

UPPER
   : 'UPPER'
   ;

USE
   : 'USE'
   ;

USMALLINT
   : 'USMALLINT'
   ;

VALUE
   : 'VALUE'
   ;

VARBINARY
   : 'VARBINARY'
   ;

VARCHAR
   : 'VARCHAR'
   ;

VARIABLE
    : 'VARIABLE'
    ;

WALK
   : 'WALK'
   ;

WHEN
   : 'WHEN'
   ;

WHERE
   : 'WHERE'
   ;

WITH
   : 'WITH'
   ;

WITHOUT
   : 'WITHOUT'
   ;

WRITE
   : 'WRITE'
   ;

XOR
   : 'XOR'
   ;

YIELD
   : 'YIELD'
   ;

ZONE
   : 'ZONE'
   ;

ZONED
   : 'ZONED'
   ;

ZONED_DATETIME
   : 'ZONED_DATETIME'
   ;

ZONED_TIME
   : 'ZONED_TIME'
   ;

INTERVAL_DAY
   : 'DAY'
   | 'DAYS'
   ;

INTERVAL_WEEK
   : 'WEEK'
   | 'WEEKS'
   ;

INTERVAL_MONTH
   : 'MONTH'
   | 'MONTHS'
   ;

INTERVAL_YEAR
   : 'YEAR'
   | 'YEARS'
   ;

//[Extend: Geaphi] start

//window function extend

PARTITION
   : 'PARTITION'
   ;

ROW_NUMBER
   : 'ROW_NUMBER'
   ;

RANK
   : 'RANK'
   ;

DENSE_RANK
   : 'DENSE_RANK'
   ;

CUME_DIST
   : 'CUME_DIST'
   ;

PERCENT_RANK
   : 'PERCENT_RANK'
   ;

OVER
   : 'OVER'
   ;

// join

JOIN
   : 'JOIN'
   ;

ON
   : 'ON'
   ;

INNER
   : 'INNER'
   ;

CROSS
   : 'CROSS'
   ;

//Contruct

CONSTRUCT
   : 'CONSTRUCT'
   ;

PROPERTIES
   : 'PROPERTIES'
   ;

PRIMARY
   : 'PRIMARY'
   ;

KEY
   : 'KEY'
   ;

// sliding windows

SLIDING
   : 'SLIDING'
   ;

UNTIL
   : 'UNTIL'
   ;

STEP
   : 'STEP'
   ;

//[Extend: Geaphi] end

EDGE_SYNONYM
   : 'EDGE'
   | 'RELATIONSHIP'
   ;

EDGES_SYNONYM
   : 'EDGES'
   | 'RELATIONSHIPS'
   ;

NODE_SYNONYM
   : 'NODE'
   | 'VERTEX'
   ;

// pre-reserved words
AGGREGATE
   : 'aggregate'
   ;

AGGREGATES
   : 'aggregates'
   ;

ALTER
   : 'alter'
   ;

CATALOG
   : 'catalog'
   ;

CLEAR
   : 'clear'
   ;

CLONE
   : 'clone'
   ;

CONSTRAINT
   : 'contraint'
   ;

CURRENT_ROLE
   : 'current_role'
   ;

DATA
   : 'data'
   ;

DIRECTORY
   : 'directory'
   ;

EXACT
   : 'exact'
   ;

EXISTING
   : 'existing'
   ;

FUNCTION
   : 'function'
   ;

GQLSTATUS
   : 'gqlstatus'
   ;

GRANT
   : 'grant'
   ;

INSTANT
   : 'instant'
   ;

NOTHING
   : 'nothing'
   ;

NUMERIC
   : 'numeric'
   ;

PROCEDURE
   : 'procedure'
   ;

PRODUCT
   : 'product'
   ;

PROJECT
   : 'project'
   ;

QUERY
   : 'query'
   ;

RECORDS
   : 'records'
   ;

REFERENCE
   : 'reference'
   ;

RENAME
   : 'rename'
   ;

REVOKE
   : 'revoke'
   ;

SUBSTRING
   : 'substring'
   ;

TEMPORAL
   : 'temporal'
   ;

UNIQUE
   : 'unique'
   ;

UNIT
   : 'unit'
   ;

VALUES
   : 'values'
   ;

MULTISET_ALTERNATION_OPERATOR
   : '|+|'
   ;

// DELIMITER_TOKEN : GQL_SPECIAL_CHARACTER|BRACKET_RIGHT_ARROW|BRACKET_TILDE_RIGHT_ARROW|CHARACTER_STRING_LITERAL|CONCATENATION_OPERATOR|DATE_STRING|DATETIME_STRING|DELIMITED_IDENTIFIER|DOUBLE_COLON|DOUBLE_MINUS_SIGN|DOUBLE_PERIOD|DURATION_STRING|GREATER_THAN_OPERATOR|GREATER_THAN_OR_EQUALS_OPERATOR|LEFT_ARROW|LEFT_ARROW_BRACKET|LEFT_ARROW_TILDE|LEFT_ARROW_TILDE_BRACKET|LEFT_MINUS_RIGHT|LEFT_MINUS_SLASH|LEFT_TILDE_SLASH|LESS_THAN_OPERATOR|LESS_THAN_OR_EQUALS_OPERATOR|MINUS_LEFT_BRACKET|MINUS_SLASH|NOT_EQUALS_OPERATOR|RIGHT_ARROW|RIGHT_BRACKET_MINUS|RIGHT_BRACKET_TILDE|SLASH_MINUS|SLASH_MINUS_RIGHT|SLASH_TILDE|SLASH_TILDE_RIGHT|TILDE_LEFT_BRACKET|TILDE_RIGHT_ARROW|TILDE_SLASH|TIME_STRING ;

//BRACKET_RIGHT_ARROW : ']->' ;

//BRACKET_TILDE_RIGHT_ARROW : ']~>' ;

CONCATENATION_OPERATOR
   : '||'
   ;

DOUBLE_COLON
   : '::'
   ;

//remove Feature GB02 support

//DOUBLE_MINUS_SIGN : '--' ;

DOUBLE_PERIOD
   : '..'
   ;

GREATER_THAN_OR_EQUALS_OPERATOR
   : '>='
   ;

HINT_BEGIN
   : '/*+'
   ;

//HINT_END : '*/' ;

//LEFT_ARROW : '<-' ;

//LEFT_ARROW_TILDE : '<~' ;

//LEFT_ARROW_BRACKET : '<-[' ;

//LEFT_ARROW_TILDE_BRACKET : '<~[' ;

LEFT_MINUS_RIGHT
   : '<->'
   ;

LEFT_MINUS_SLASH
   : '<-/'
   ;

LEFT_SHIFT
   : '<<'
   ;

LEFT_TILDE_SLASH
   : '<~/'
   ;

LESS_THAN_OR_EQUALS_OPERATOR
   : '<='
   ;

//MINUS_LEFT_BRACKET : '-[' ;

MINUS_SLASH
   : '-/'
   ;

NOT_EQUALS_OPERATOR
   : '<>'
   | '!='
   ;

RIGHT_ARROW
   : '->'
   ;

//RIGHT_BRACKET_MINUS : ']-' ;

//RIGHT_BRACKET_TILDE : ']~' ;

RIGHT_SHIFT
   : '>>'
   ;

SAFE_EXQUAL_OPERATOR
   : '<=>'
   ;

//SLASH_MINUS : '/-' ;

SLASH_MINUS_RIGHT
   : '/->'
   ;

//SLASH_TILDE : '/~' ;

SLASH_TILDE_RIGHT
   : '/~>'
   ;

//TILDE_LEFT_BRACKET : '~[' ;

TILDE_RIGHT_ARROW
   : '~>'
   ;

TILDE_SLASH
   : '~/'
   ;

DOUBLE_SOLIDUS
   : '//'
   ;

ESCAPED_CHARACTER
   : ESCAPED_REVERSE_SOLIDUS
   | ESCAPED_QUOTE
   | ESCAPED_DOUBLE_QUOTE
   | ESCAPED_GRAVE_ACCENT
   | ESCAPED_TAB
   | ESCAPED_BACKSPACE
   | ESCAPED_NEWLINE
   | ESCAPED_CARRIAGE_RETURN
   | ESCAPED_FORM_FEED
   | UNICODE_ESCAPE_VALUE
   ;

ESCAPED_REVERSE_SOLIDUS
   : REVERSE_SOLIDUS REVERSE_SOLIDUS
   ;

ESCAPED_QUOTE
   : REVERSE_SOLIDUS QUOTE
   ;

ESCAPED_DOUBLE_QUOTE
   : REVERSE_SOLIDUS DOUBLE_QUOTE
   ;

ESCAPED_GRAVE_ACCENT
   : REVERSE_SOLIDUS GRAVE_ACCENT
   ;

ESCAPED_TAB
   : REVERSE_SOLIDUS 't'
   ;

ESCAPED_BACKSPACE
   : REVERSE_SOLIDUS 'b'
   ;

ESCAPED_NEWLINE
   : REVERSE_SOLIDUS 'n'
   ;

ESCAPED_CARRIAGE_RETURN
   : REVERSE_SOLIDUS 'r'
   ;

ESCAPED_FORM_FEED
   : REVERSE_SOLIDUS 'f'
   ;

UNICODE_ESCAPE_VALUE
   : UNICODE_4_DIGIT_ESCAPE_VALUE
   | UNICODE_6_DIGIT_ESCAPE_VALUE
   ;

UNICODE_4_DIGIT_ESCAPE_VALUE
   : REVERSE_SOLIDUS 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
   ;

UNICODE_6_DIGIT_ESCAPE_VALUE
   : REVERSE_SOLIDUS 'U' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
   ;

UNSIGNED_DECIMAL_INTEGER
   : STANDARD_DIGIT ((UNDERSCORE)? STANDARD_DIGIT)*
   ;

UNSIGNED_HEXADECIMAL_INTEGER
   : '0x' ((UNDERSCORE)? HEX_DIGIT)+
   ;

UNSIGNED_OCTAL_INTEGER
   : '0o' ((UNDERSCORE)? OCTAL_DIGIT)+
   ;

UNSIGNED_BINARY_INTEGER
   : '0b' ((UNDERSCORE)? BINARY_DIGIT)+
   ;

UNSIGNED_DECIMAL_IN_SCIENTIFIC_NOTATION
   : UNSIGNED_DECIMAL_INTEGER EXPONENT_NUM_PART
   ;

UNSIGNED_DECIMAL_IN_COMMON_NOTATION
   : UNSIGNED_DECIMAL_INTEGER PERIOD UNSIGNED_DECIMAL_INTEGER?
   | PERIOD UNSIGNED_DECIMAL_INTEGER
   ;

FOUR_DIGIT
   : STANDARD_DIGIT STANDARD_DIGIT STANDARD_DIGIT STANDARD_DIGIT
   ;

DOUBLE_DIGIT
   : STANDARD_DIGIT STANDARD_DIGIT
   ;

SINGLE_QUOTED_STRING_LITERAL
   : COMMERCIAL_AT? QUOTE (ESCAPED_CHARACTER | StringLiteral_1)*? QUOTE
   ;

DOUBLE_QUOTED_STRING_LITERAL
   : COMMERCIAL_AT? DOUBLE_QUOTE (ESCAPED_CHARACTER | StringLiteral_0)*? DOUBLE_QUOTE
   ;

ACCENT_QUOTED_STRING_LITERAL
   : COMMERCIAL_AT? GRAVE_ACCENT (EscapedSymbolicName_0)* GRAVE_ACCENT
   ;

BYTE_STRING_LITERAL
   : 'X' QUOTE (SPACE)* (HEX_DIGIT (SPACE)* HEX_DIGIT (SPACE)*)* QUOTE (SEPARATOR QUOTE (SPACE)* (HEX_DIGIT (SPACE)* HEX_DIGIT (SPACE)*)* QUOTE)*
   ;

QUOTE
   : '\''
   ;

DOUBLE_QUOTE
   : '"'
   ;

GRAVE_ACCENT
   : '`'
   ;

REGULAR_IDENTIFIER
   : IDENTIFIER_START (IDENTIFIER_EXTEND)*
   ;

// EXTENDED_IDENTIFIER : ( IDENTIFIER_EXTEND )+ ;

IDENTIFIER_START
   : ID_Start
   | Pc
   | '@'
   ;

IDENTIFIER_EXTEND
   : ID_Continue
   | Sc
   | '#'
   ;

SP
   : (SEPARATOR)+ -> channel(HIDDEN)
   ;

SEPARATOR
   : (COMMENT | WHITESPACE)+
   ;

WHITESPACE
   : SPACE
   | TAB
   | LF
   | VT
   | FF
   | CR
   | FS
   | GS
   | RS
   | US
   | '\u1680'
   | '\u180e'
   | '\u2000'
   | '\u2001'
   | '\u2002'
   | '\u2003'
   | '\u2004'
   | '\u2005'
   | '\u2006'
   | '\u2008'
   | '\u2009'
   | '\u200a'
   | '\u2028'
   | '\u2029'
   | '\u205f'
   | '\u3000'
   | '\u00a0'
   | '\u2007'
   | '\u202f'
   | Comment
   ;

Comment
   : ('/*' Comment_4 (Comment_1 | ('*' Comment_2))* '*/')
   | ('//' (Comment_3)* CR? (LF | EOF))
   ;

BIDIRECTIONAL_CONTROL_CHARACTER
   : '\u202a'
   ;

COMMENT
   : SIMPLE_COMMENT
   | BRACKETED_COMMENT
   ;

SIMPLE_COMMENT
   : SIMPLE_COMMENT_INTRODUCER (SIMPLE_COMMENT_CHARACTER)* LF
   ;

SIMPLE_COMMENT_INTRODUCER
   : DOUBLE_SOLIDUS
   ; // | DOUBLE_MINUS_SIGN

SIMPLE_COMMENT_CHARACTER
   : 'I_DONT_KNOW_15'
   ;

BRACKETED_COMMENT
   : BRACKETED_COMMENT_INTRODUCER BRACKETED_COMMENT_CONTENTS BRACKETED_COMMENT_TERMINATOR
   ;

BRACKETED_COMMENT_INTRODUCER
   : '/*'
   ;

BRACKETED_COMMENT_TERMINATOR
   : '*/'
   ;

BRACKETED_COMMENT_CONTENTS
   : 'I_DONT_KNOW_16'
   ;

GQL_TERMINAL_CHARACTER
   : GQL_LANGUAGE_CHARACTER
   | OTHER_LANGUAGE_CHARACTER
   ;

GQL_LANGUAGE_CHARACTER
   : SIMPLE_LATIN_LETTER
   | STANDARD_DIGIT
   | GQL_SPECIAL_CHARACTER
   ;

SIMPLE_LATIN_LETTER
   : SIMPLE_LATIN_LOWER_CASE_LETTER
   | SIMPLE_LATIN_UPPER_CASE_LETTER
   ;

SIMPLE_LATIN_LOWER_CASE_LETTER
   : 'a'
   | 'b'
   | 'c'
   | 'd'
   | 'e'
   | 'f'
   | 'g'
   | 'h'
   | 'i'
   | 'j'
   | 'k'
   | 'l'
   | 'm'
   | 'n'
   | 'o'
   | 'p'
   | 'q'
   | 'r'
   | 's'
   | 't'
   | 'u'
   | 'v'
   | 'w'
   | 'x'
   | 'y'
   | 'z'
   ;

SIMPLE_LATIN_UPPER_CASE_LETTER
   : 'A'
   | 'B'
   | 'C'
   | 'D'
   | 'E'
   | 'F'
   | 'G'
   | 'H'
   | 'I'
   | 'J'
   | 'K'
   | 'L'
   | 'M'
   | 'N'
   | 'O'
   | 'P'
   | 'Q'
   | 'R'
   | 'S'
   | 'T'
   | 'U'
   | 'V'
   | 'W'
   | 'X'
   | 'Y'
   | 'Z'
   ;

OTHER_DIGIT
   : 'I_DONT_KNOW_18'
   ;

GQL_SPECIAL_CHARACTER
   : SPACE
   | AMPERSAND
   | ASTERISK
   | COLON
   | EQUALS_OPERATOR
   | COMMA
   ;

OTHER_LANGUAGE_CHARACTER
   : 'I_DONT_KNOW_20'
   ;

//KEYWORD:LABEL| LABELS;

fragment COMMERCIAL_AT
   : '@'
   ;

fragment HEX_DIGIT
   : [0-9A-F]
   ;

fragment BINARY_DIGIT
   : [01]
   ;

fragment OCTAL_DIGIT
   : [0-7]
   ;

fragment STANDARD_DIGIT
   : [0-9]
   ;

fragment FF
   : [\f]
   ;

fragment EscapedSymbolicName_0
   : ~ [`]
   ;

fragment RS
   : [\u001E]
   ;

fragment ID_Continue
   : [\p{ID_Continue}]
   ;

fragment Comment_1
   : ~ [*]
   ;

fragment StringLiteral_0
   : ~ ["]
   ;

fragment StringLiteral_1
   : ~ [']
   ;

fragment Comment_3
   : ~ [\n\r]
   ;

fragment Comment_2
   : ~ [/]
   ;

fragment Comment_4
   : ~ [+]
   ;

fragment GS
   : [\u001D]
   ;

fragment FS
   : [\u001C]
   ;

fragment CR
   : [\r]
   ;

fragment Sc
   : [\p{Sc}]
   ;

fragment SPACE
   : [ ]
   ;

fragment Pc
   : [\p{Pc}]
   ;

fragment TAB
   : [\t]
   ;

fragment LF
   : [\n]
   ;

fragment VT
   : [\u000B]
   ;

fragment US
   : [\u001F]
   ;

fragment ID_Start
   : [\p{ID_Start}]
   ;

fragment DEC_DIGIT
   : [0-9]
   ;

fragment EXPONENT_NUM_PART
   : 'E' [-+]? DEC_DIGIT+
   ;