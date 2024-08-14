parser grammar GqlParser;

options { tokenVocab = GqlLexer; }

gqlRequest
   : gqlProgram SEMICOLON? EOF
   ;

gqlProgram
   : programActivity sessionCloseCommand?
   | sessionCloseCommand
   ;

programActivity
   : sessionActivity
   | transactionActivity
   ;

sessionActivity
   : sessionActivityCommand+
   ;

sessionActivityCommand
   : sessionSetCommand
   | sessionResetCommand
   ;

transactionActivity
   : startTransactionCommand (procedureSpecification endTransactionCommand?)?
   | procedureSpecification endTransactionCommand?
   | endTransactionCommand
   ;

endTransactionCommand
   : rollbackCommand
   | commitCommand
   ;

sessionSetCommand
   : SESSION SET (sessionSetSchemaClause | sessionSetGraphClause | sessionSetTimeZoneClause | sessionSetParameterClause)
   ;

sessionSetSchemaClause
   : SCHEMA schemaReference
   ;

sessionSetGraphClause
   : PROPERTY? GRAPH graphExpression
   ;

sessionSetTimeZoneClause
   : TIME ZONE setTimeZoneValue
   ;

setTimeZoneValue
   : expressionAtom
   ;

sessionSetParameterClause
   : sessionSetGraphParameterClause
   | sessionSetBindingTableParameterClause
   | sessionSetValueParameterClause
   ;

sessionSetGraphParameterClause
   : PROPERTY? GRAPH sessionSetParameterName optTypedGraphInitializer
   ;

sessionSetBindingTableParameterClause
   : BINDING? TABLE sessionSetParameterName optTypedBindingTableInitializer
   ;

sessionSetValueParameterClause
   : VALUE sessionSetParameterName optTypedValueInitializer
   ;

sessionSetParameterName
   : (IF NOT EXISTS)? parameterName
   ;

sessionResetCommand
   : SESSION RESET sessionResetArguments?
   ;

sessionResetArguments
   : ALL? (PARAMETERS | CHARACTERISTICS)
   | SCHEMA
   | PROPERTY? GRAPH
   | TIME ZONE
   | PARAMETER? parameterName
   ;

sessionCloseCommand
   : SESSION CLOSE
   ;

startTransactionCommand
   : START TRANSACTION transactionCharacteristics?
   ;

transactionCharacteristics
   : transactionMode (COMMA transactionMode)*
   ;

transactionMode
   : transactionAccessMode
   | implementationDefinedAccessMode
   ;

transactionAccessMode
   : READ ONLY
   | READ WRITE
   ;

implementationDefinedAccessMode
   : I_DONT_KNOW_1
   ; //TODO: Need to refer to other standard definition, temporarily vacant

rollbackCommand
   : ROLLBACK
   ;

commitCommand
   : COMMIT
   ;

nestedProcedureSpecification
   : LEFT_BRACE procedureSpecification RIGHT_BRACE
   ;

procedureSpecification
   : procedureBody
   ;

catalogModifyingProcedureSpecification
   : procedureBody
   ;

nestedDataModifyingProcedureSpecification
   : LEFT_BRACE dataModifyingProcedureSpecification RIGHT_BRACE
   ;

dataModifyingProcedureSpecification
   : procedureBody
   ;

nestedQuerySpecification
   : LEFT_BRACE procedureSpecification RIGHT_BRACE
   ;

querySpecification
   : procedureBody
   ;

unsignedNumericLiteral
   : integerLiteral
   | floatLiteral
   ;

integerLiteral
   : UNSIGNED_DECIMAL_INTEGER
   | UNSIGNED_OCTAL_INTEGER
   | UNSIGNED_HEXADECIMAL_INTEGER
   | UNSIGNED_BINARY_INTEGER
   ;

floatLiteral
   : UNSIGNED_DECIMAL_IN_COMMON_NOTATION
   | UNSIGNED_DECIMAL_IN_SCIENTIFIC_NOTATION
   ;

singleQuotedCharacterSequence
   : SINGLE_QUOTED_STRING_LITERAL
   ;

doubleQuotedCharacterSequence
   : DOUBLE_QUOTED_STRING_LITERAL
   ;

accentQuotedCharacterSequence
   : ACCENT_QUOTED_STRING_LITERAL
   ;

nullLiteral
   : NULL_
   ;

temporalLiteral
   : dateLiteral
   | timeLiteral
   | datetimeLiteral
   | sqlDatetimeLiteral
   ;

sqlDatetimeLiteral
   : DATE QUOTE FOUR_DIGIT MINUS_SIGN DOUBLE_DIGIT MINUS_SIGN DOUBLE_DIGIT QUOTE
   | TIME QUOTE DOUBLE_DIGIT COLON DOUBLE_DIGIT COLON DOUBLE_DIGIT QUOTE
   | TIMESTAMP QUOTE FOUR_DIGIT MINUS_SIGN DOUBLE_DIGIT MINUS_SIGN DOUBLE_DIGIT DOUBLE_DIGIT COLON DOUBLE_DIGIT COLON DOUBLE_DIGIT QUOTE
   | DATETIME QUOTE FOUR_DIGIT MINUS_SIGN DOUBLE_DIGIT MINUS_SIGN DOUBLE_DIGIT DOUBLE_DIGIT COLON DOUBLE_DIGIT COLON DOUBLE_DIGIT QUOTE
   ;

dateLiteral
   : DATE characterStringLiteral
   ;

timeLiteral
   : TIME characterStringLiteral
   ;

datetimeLiteral
   : (DATETIME | TIMESTAMP) characterStringLiteral
   ;

durationLiteral
   : DURATION characterStringLiteral
   | sqlIntervalLiteral
   ;

sqlIntervalLiteral
   : UNSIGNED_DECIMAL_INTEGER sqlIntervalType
   ;

sqlIntervalType
   : INTERVAL_DAY
   | INTERVAL_WEEK
   | INTERVAL_MONTH
   | INTERVAL_YEAR
   ;

identifier
   : keyWord
   | REGULAR_IDENTIFIER
   | delimitedIdentifier
   ; //[Extend] keyWord tokens are supported as identifiers

keyWord
   : reservedWord
   | nonReservedWord
   ;

reservedWord
   : preReservedWord
   | ABS
   | ACOS
   | ALL
   | ALL_DIFFERENT
   | AND
   | ANY
   | ARRAY
   | AS
   | ASC
   | ASCENDING
   | ASIN
   | AT
   | ATAN
   | AVG
   | BIG
   | BIGINT
   | BINARY
   | BOOL
   | BOOLEAN
   | BOTH
   | BTRIM
   | BY
   | BYTE_LENGTH
   | BYTES
   | CALL
   | CASE
   | CAST
   | CEIL
   | CEILING
   | CHAR_LENGTH
   | CHARACTER_LENGTH
   | CHARACTERISTICS
   | CLOSE
   | COALESCE
   | COLLECT
   | COMMIT
   | COPY
   | COS
   | COSH
   | COT
   | COUNT
   | CREATE
   | CURRENT_DATE
   | CURRENT_GRAPH
   | CURRENT_PROPERTY_GRAPH
   | CURRENT_SCHEMA
   | CURRENT_TIME
   | CURRENT_TIMESTAMP
   | CURRENT_USER
   | DATE
   | DATETIME
   | DEC
   | DECIMAL
   | DEGREES
   | DELETE
   | DESC
   | DESCENDING
   | DETACH
   | DISTINCT
   | DOUBLE
   | DROP
   | DURATION
   | DURATION_BETWEEN
   | ELEMENT_ID
   | ELSE
   | END
   | EXCEPT
   | EXISTS
   | EXP
   | FALSE
   | FILTER
   | FINISH
   | FLOAT
   | FLOAT16
   | FLOAT32
   | FLOAT64
   | FLOAT128
   | FLOAT256
   | FLOOR
   | FOR
   | FROM
   | GROUP
   | HAVING
   | HOME_GRAPH
   | HOME_PROPERTY_GRAPH
   | HOME_SCHEMA
   | IF
   | IN
   | INSERT
   | INT
   | INTEGER
   | INT8
   | INTEGER8
   | INT16
   | INTEGER16
   | INT32
   | INTEGER32
   | INT64
   | INTEGER64
   | INT128
   | INTEGER128
   | INT256
   | INTEGER256
   | INTERSECT
   | INTERVAL_DAY
   | INTERVAL_WEEK
   | INTERVAL_MONTH
   | INTERVAL_YEAR
   | IS
   | LEADING
   | LET
   | LIKE
   | LIMIT
   | LIST
   | LN
   | LOCAL
   | LOCAL_DATETIME
   | LOCAL_TIME
   | LOCAL_TIMESTAMP
   | LOG
   | LOG10
   | LOWER
   | LTRIM
   | MATCH
   | MAX_
   | MIN_
   | MOD
   | NEXT
   | NODETACH
   | NORMALIZE
   | NOT
   | NULL_
   | NULLIF
   | NULLS
   | OCTET_LENGTH
   | OF
   | OFFSET
   | OPEN
   | OPTIONAL
   | OR
   | ORDER
   | OTHERWISE
   | PARAMETER
   | PARAMETERS
   | PATH
   | PATH_LENGTH
   | PATHS
   | PERCENTILE_CONT
   | PERCENTILE_DISC
   | POWER
   | PRECISION
   | PROPERTY_EXISTS
   | RADIANS
   | REAL
   | RECORD
   | REMOVE
   | REPLACE
   | RESET
   | RETURN
   | ROLLBACK
   | RTRIM
   | SAME
   | SCHEMA
   | SELECT
   | SESSION
   | SET
   | SIGNED
   | SIN
   | SINH
   | SKIP_
   | SMALL
   | SMALLINT
   | SQRT
   | START
   | STDDEV_POP
   | STDDEV_SAMP
   | STRING
   | SUM
   | TAN
   | TANH
   | THEN
   | TIME
   | TIMESTAMP
   | TRAILING
   | TRIM
   | TRUE
   | TYPED
   | UBIGINT
   | UINT
   | UINT8
   | UINT16
   | UINT32
   | UINT64
   | UINT128
   | UINT256
   | UNION
   | UNKNOWN
   | UNSIGNED
   | UPPER
   | USE
   | USMALLINT
   | VALUE
   | VARBINARY
   | VARCHAR
   | WHEN
   | WHERE
   | WITH
   | XOR
   | YIELD
   | ZONED
   | ZONED_DATETIME
   | ZONED_TIME
   ;

preReservedWord
   : AGGREGATE
   | AGGREGATES
   | ALTER
   | CATALOG
   | CLEAR
   | CLONE
   | CONSTRAINT
   | CURRENT_ROLE
   | DATA
   | DIRECTORY
   | EXACT
   | EXISTING
   | FUNCTION
   | GQLSTATUS
   | GRANT
   | INSTANT
   | LEFT
   | NOTHING
   | NUMERIC
   | ON
   | PARTITION
   | PROCEDURE
   | PRODUCT
   | PROJECT
   | QUERY
   | RECORDS
   | REFERENCE
   | RENAME
   | REVOKE
   | RIGHT
   | SUBSTRING
   | TEMPORAL
   | UNIQUE
   | UNIT
   | VALUES
   ;

nonReservedWord
   : ACYCLIC
   | BETWEEN
   | BINDING
   | BINDINGS
   | CONNECTING
   | CONSTRUCT
   | CROSS
   | CUME_DIST
   | DENSE_RANK
   | DESTINATION
   | DIFFERENT
   | DIRECTED
   | EDGE_SYNONYM
   | EDGES_SYNONYM
   | ELEMENT
   | ELEMENTS
   | FIRST
   | GRAPH
   | GROUPS
   | GROUP_CONCAT
   | ID
   | INNER
   | JOIN
   | KEEP
   | KEY
   | LABEL
   | LABELED
   | LABELS
   | LAST
   | LENGTH
   | LONG
   | MAP
   | NFC
   | NFD
   | NFKC
   | NFKD
   | NO
   | NODE_SYNONYM
   | NORMALIZED
   | ONLY
   | OVER
   | ORDINALITY
   | PERCENT_RANK
   | PER_NODE_LIMIT
   | PRIMARY
   | PROPERTY
   | PROPERTIES
   | RANK
   | READ
   | READ_CONSISTENCY
   | REPEATABLE
   | ROW_NUMBER
   | SHORTEST
   | SIMPLE
   | SLIDING
   | SOURCE
   | STEP
   | SUBSTR
   | TABLE
   | TEMP
   | TIMEZONE
   | TO
   | TRAIL
   | TRANSACTION
   | TYPE
   | UNDIRECTED
   | UNTIL
   | WALK
   | WITHOUT
   | WRITE
   | ZONE
   ;

//delimitedIdentifier
//   : doubleQuotedCharacterSequence
//   | accentQuotedCharacterSequence
//   ;

//[Extend]
delimitedIdentifier
   : accentQuotedCharacterSequence
   ;

objectName
   : identifier
   ;

objectNameOrBindingVariable
   : REGULAR_IDENTIFIER
   ;

directoryName
   : identifier
   ;

schemaName
   : identifier
   ;

graphName
   : REGULAR_IDENTIFIER
   | delimitedGraphName
   ;

delimitedGraphName
   : delimitedIdentifier
   ;

graphTypeName
   : identifier
   ;

elementTypeName
   : identifier
   ;

bindingTableName
   : REGULAR_IDENTIFIER
   | delimitedBindingTableName
   ;

delimitedBindingTableName
   : delimitedIdentifier
   ;

procedureName
   : identifier
   ;

labelName
   : identifier
   ;

functionName
   : identifier
   ;

propertyName
   : identifier
   ;

fieldName
   : identifier
   ;

// change unsignedDecimalInteger to unsignedNumericLiteral
parameterName
   : '$' (unsignedNumericLiteral | identifier)
   | PERCENT (unsignedNumericLiteral | identifier) PERCENT
   ; //[Extend:GeaPhi]：%xxx%

//variable : graphVariable|graphPatternVariable|bindingTableVariable|valueVariable|bindingVariable ;
variable
   : bindingVariable
   ;

graphVariable
   : bindingVariable
   ;

graphPatternVariable
   : elementVariable
   | pathOrSubpathVariable
   ;

pathOrSubpathVariable
   : pathVariable
   | subpathVariable
   ;

elementVariable
   : bindingVariable
   ;

pathVariable
   : bindingVariable
   ;

subpathVariable
   : identifier
   ;

bindingTableVariable
   : bindingVariable
   ;

valueVariable
   : bindingVariable
   ;

bindingVariable
   : identifier
   ;

predefinedTypeLiteral
   : booleanLiteral
   | characterStringLiteral
   | byteStringLiteral
   | temporalLiteral
   | durationLiteral
   | nullLiteral
   ;

booleanLiteral
   : TRUE
   | FALSE
   | UNKNOWN
   ;

characterStringLiteral
   : singleQuotedCharacterSequence
   | doubleQuotedCharacterSequence
   ;

byteStringLiteral
   : BYTE_STRING_LITERAL
   ;

procedureBody
   : atSchemaClause? bindingVariableDefinitionBlock? statementBlock
   ;

bindingVariableDefinitionBlock
   : bindingVariableDefinition+
   ;

bindingVariableDefinition
   : graphVariableDefinition
   | bindingTableVariableDefinition
   | valueVariableDefinition
   ;

statementBlock
   : statement nextStatement*
   ;

statement
   : linearCatalogModifyingStatement
   | linearDataModifyingStatement
   | queryStatement
   | managerStatement
   ;

nextStatement
   : (NEXT | THEN) yieldClause? statement // [EXTEND:geabase] then
   ;

graphVariableDefinition
   : PROPERTY? GRAPH graphVariable optTypedGraphInitializer
   ;

optTypedGraphInitializer
   : (typed? graphReferenceValueType)? graphInitializer
   ;

graphInitializer
   : EQUALS_OPERATOR graphExpression
   ;

bindingTableVariableDefinition
   : BINDING? TABLE bindingTableVariable optTypedBindingTableInitializer
   ;

optTypedBindingTableInitializer
   : (typed? bindingTableReferenceValueType)? bindingTableInitializer
   ;

bindingTableInitializer
   : EQUALS_OPERATOR bindingTableExpression
   ;

valueVariableDefinition
   : VALUE valueVariable optTypedValueInitializer
   ;

optTypedValueInitializer
   : (typed? valueType)? EQUALS_OPERATOR expression
   ;

graphExpression
   : nestedGraphQuerySpecification
   | objectExpressionPrimary
   | graphReference
   | objectNameOrBindingVariable
   | currentGraph
   ;

currentGraph
   : CURRENT_PROPERTY_GRAPH
   | CURRENT_GRAPH
   ;

nestedGraphQuerySpecification
   : nestedQuerySpecification
   ;

bindingTableExpression
   : nestedBindingTableQuerySpecification
   | objectExpressionPrimary
   | bindingTableReference
   | objectNameOrBindingVariable
   ;

nestedBindingTableQuerySpecification
   : nestedQuerySpecification
   ;

objectExpressionPrimary
   : VARIABLE expressionAtom
   | LEFT_PAREN expression RIGHT_PAREN
   | expressionAtom
   ;

linearCatalogModifyingStatement
   : simpleCatalogModifyingStatement+
   ;

simpleCatalogModifyingStatement
   : primitiveCatalogModifyingStatement
   | callCatalogModifyingProcedureStatement
   ;

primitiveCatalogModifyingStatement
   : createSchemaStatement
   | createGraphStatement
   | createGraphTypeStatement
   | dropSchemaStatement
   | dropGraphStatement
   | dropGraphTypeStatement
   ;

createSchemaStatement
   : CREATE SCHEMA (IF NOT EXISTS)? catalogSchemaParentAndName
   ;

dropSchemaStatement
   : DROP SCHEMA (IF EXISTS)? catalogSchemaParentAndName
   ;

createGraphStatement
   : CREATE (PROPERTY? GRAPH (IF NOT EXISTS)? | OR REPLACE PROPERTY? GRAPH) catalogGraphParentAndName (openGraphType | ofGraphType) graphSource?
   ;

openGraphType
   : typed? ANY (PROPERTY? GRAPH)?
   ;

ofGraphType
   : graphTypeLikeGraph
   | typed? graphTypeReference
   | typed? (PROPERTY? GRAPH)? nestedGraphTypeSpecification
   ;

graphTypeLikeGraph
   : LIKE graphExpression
   ;

graphSource
   : AS COPY OF graphExpression
   ;

dropGraphStatement
   : DROP PROPERTY? GRAPH (IF EXISTS)? catalogGraphParentAndName
   ;

createGraphTypeStatement
   : CREATE (PROPERTY? GRAPH TYPE (IF NOT EXISTS)? | OR REPLACE PROPERTY? GRAPH TYPE) catalogGraphTypeParentAndName graphTypeSource
   ;

graphTypeSource
   : AS? copyOfGraphType
   | graphTypeLikeGraph
   | AS? nestedGraphTypeSpecification
   ;

copyOfGraphType
   : COPY OF (graphTypeReference | externalObjectReference)
   ;

dropGraphTypeStatement
   : DROP PROPERTY? GRAPH TYPE (IF EXISTS)? catalogGraphTypeParentAndName
   ;

callCatalogModifyingProcedureStatement
   : callProcedureStatement
   ;

linearDataModifyingStatement
   : focusedLinearDataModifyingStatement
   | ambientLinearDataModifyingStatement
   ;

focusedLinearDataModifyingStatement
   : focusedLinearDataModifyingStatementBody
   | focusedNestedDataModifyingProcedureSpecification
   ;

focusedLinearDataModifyingStatementBody
   : useGraphClause simpleLinearDataAccessingStatement primitiveResultStatement?
   ;

focusedNestedDataModifyingProcedureSpecification
   : useGraphClause nestedDataModifyingProcedureSpecification
   ;

ambientLinearDataModifyingStatement
   : ambientLinearDataModifyingStatementBody
   | nestedDataModifyingProcedureSpecification
   ;

ambientLinearDataModifyingStatementBody
   : simpleLinearQueryStatement? simpleDataModifyingStatement+ primitiveResultStatement?
   ;

simpleLinearDataAccessingStatement
   : simpleDataAccessingStatement+
   ;

simpleDataAccessingStatement
   : simpleQueryStatement
   | simpleDataModifyingStatement
   ;

simpleDataModifyingStatement
   : primitiveDataModifyingStatement
   | callDataModifyingProcedureStatement
   ;

primitiveDataModifyingStatement
   : insertStatement
   | setStatement
   | removeStatement
   | deleteStatement
   | replaceStatement
   ;

insertStatement
   : INSERT insertGraphPattern
   ;

setStatement
   : SET setItemList
   ;

setItemList
   : setItem (COMMA setItem)*
   ;

setItem
   : setPropertyItem
   | setAllPropertiesItem
   | updatePropertiesItem// [EXTEND]: += Update partial attributes
   | setLabelItem
   ;

setPropertyItem
   : bindingVariableReference PERIOD propertyName EQUALS_OPERATOR expression
   ;

setAllPropertiesItem
   : bindingVariableReference EQUALS_OPERATOR LEFT_BRACE propertyKeyValuePairList? RIGHT_BRACE
   ;

updatePropertiesItem
   : bindingVariableReference PLUS_SIGN EQUALS_OPERATOR LEFT_BRACE propertyKeyValuePairList? RIGHT_BRACE
   ;

setLabelItem
   : bindingVariableReference isOrColon labelName
   ;

labelSetSpecification
   : labelName (AMPERSAND labelName)*
   ;

removeStatement
   : REMOVE removeItemList
   ;

removeItemList
   : removeItem (COMMA removeItem)*
   ;

removeItem
   : removePropertyItem
   | removeLabelItem
   ;

removePropertyItem
   : bindingVariableReference PERIOD propertyName
   ;

removeLabelItem
   : bindingVariableReference isOrColon labelName
   ;

deleteStatement
   : (DETACH | NODETACH)? DELETE deleteItemList
   ;

deleteItemList
   : deleteItem (COMMA deleteItem)*
   ;

deleteItem
   : expression
   ;

replaceStatement
   : REPLACE insertGraphPattern
   ;

callDataModifyingProcedureStatement
   : callProcedureStatement
   ;

queryStatement
   : joinQueryExpression //[EXTEND:Geaphi]: Join support
   ;

joinQueryExpression
   : compositeQueryStatement (joinRightPart primitiveResultStatement?)*
   ;

joinRightPart
    : joinType? JOIN compositeQueryStatement (ON expression)?
    ;

compositeQueryStatement
   : compositeQueryExpression
   ;

managerStatement
    : SHOW PROCESSLIST
    | KILL killMode? integerLiteral
    ;

killMode
    : CONNECTION
    | QUERY
    ;

compositeQueryExpression
   : linearQueryStatement (queryConjunction linearQueryStatement)*
   ;

queryConjunction
   : setOperator
   | OTHERWISE
   ;

setOperator
   : UNION setQuantifier?
   | EXCEPT setQuantifier?
   | INTERSECT setQuantifier?
   ;

joinType
   : INNER
   | CROSS
   | LEFT
   | RIGHT
   ;

linearQueryStatement
   : focusedLinearQueryStatement
   | ambientLinearQueryStatement
   ;

focusedLinearQueryStatement
   : focusedQueryStatement
   | focusedPrimitiveResultStatement
   | focusedNestedQuerySpecification
   | selectStatement
   ;

focusedQueryStatement
    : focusedLinearQueryStatementPart* focusedLinearQueryAndPrimitiveResultStatementPart
    ;

focusedLinearQueryStatementPart
   : useGraphClause simpleLinearQueryStatement
   ;

focusedLinearQueryAndPrimitiveResultStatementPart
   : useGraphClause simpleLinearQueryStatement primitiveResultStatement
   ;

focusedPrimitiveResultStatement
   : useGraphClause primitiveResultStatement
   ;

focusedNestedQuerySpecification
   : useGraphClause nestedQuerySpecification
   ;

ambientLinearQueryStatement
   : simpleLinearQueryStatement? primitiveResultStatement
   | nestedQuerySpecification
   ;

simpleLinearQueryStatement
   : simpleQueryStatement+
   ;

simpleQueryStatement
   : primitiveQueryStatement
   | callQueryStatement
   ;

primitiveQueryStatement
   : matchStatement
   | letStatement
   | forStatement
   | filterStatement
   | orderByAndPageStatement
   ;

matchStatement
   : simpleMatchStatement
   | optionalMatchStatement
   ;

simpleMatchStatement
   : MATCH graphPatternBindingTable
   ;

optionalMatchStatement
   : OPTIONAL optionalOperand
   ;

optionalOperand
   : simpleMatchStatement
   | LEFT_BRACE matchStatementBlock RIGHT_BRACE
   | LEFT_PAREN matchStatementBlock RIGHT_PAREN
   ;

matchStatementBlock
   : matchStatement+
   ;

callQueryStatement
   : callProcedureStatement
   ;

filterStatement
   : FILTER (whereClause | expression)
   ;

letStatement
   : LET letVariableDefinitionList
   ;

letVariableDefinitionList
   : letVariableDefinition (COMMA letVariableDefinition)*
   ;

letVariableDefinition
   : valueVariableDefinition
   | valueVariable EQUALS_OPERATOR expression
   ;

forStatement
   : FOR forItem forOrdinalityOrOffset?
   ;

forItem
   : forItemAlias expressionAtom
   ;

forItemAlias
   : identifier IN
   ;

forOrdinalityOrOffset
   : WITH (ORDINALITY | OFFSET) identifier
   ;

orderByAndPageStatement
   : orderByClause offsetClause? limitClause?
   | offsetClause limitClause?
   | limitClause
   ;

primitiveResultStatement
   : returnStatement orderByAndPageStatement?
   | constructGraphStatement //[EXTEND:geaphi]: contruct
   | FINISH
   ;

returnStatement
   : RETURN returnStatementBody
   ;

returnStatementBody
   : hintItemlist? setQuantifier? (ASTERISK | returnItemList) groupByClause?
   | NO BINDINGS
   ;

returnItemList
   : returnItem (COMMA returnItem)*
   ;

returnItem
   : expression (AS identifier)?
   ;

//[EXTEND:geabsae]: hint
hintItemlist
   : HINT_BEGIN hintItem (COMMA hintItem)* BRACKETED_COMMENT_TERMINATOR
   ;

hintItem
   : READ_CONSISTENCY LEFT_PAREN identifier RIGHT_PAREN                         #gqlReadConsistency
   | ALLOW_ANONYMOUS_TABLE LEFT_PAREN unsignedBooleanSpecification RIGHT_PAREN  #gqlAllowAnonymousTable
   ;

//[EXTEND:geaphi]: contruct
constructGraphStatement
   : CONSTRUCT constructElementList
   ;

constructElementList
   : constructElement (COMMA constructElement)*
   ;

constructElement
   : currentElement
   | newElement
   ;

currentElement
   : bindingVariable propertyList?
   ;

propertyList
   : PROPERTIES LEFT_PAREN propertyName (COMMA propertyName)* RIGHT_PAREN
   ;

newElement
   : newNode
   | newEdge
   ;

newNode
   : LEFT_PAREN constructElementPatternFiller RIGHT_PAREN
   ;

newEdge
   : LEFT_PAREN startVar RIGHT_PAREN constructEdgePattern LEFT_PAREN endVar RIGHT_PAREN
   ;

constructElementPatternFiller
   : (elementVariableDeclaration)? isLabelExpression (primaryKey)? constructElementPropertySpecification
   ;

constructEdgePattern
   : (constructEdgePointingRight | constructEdgePointingLeft | constructEdgeAnyDirection)
   ;

constructEdgePointingRight
   : MINUS_SIGN LEFT_BRACKET constructElementPatternFiller RIGHT_BRACKET RIGHT_ARROW
   ;

constructEdgePointingLeft
   : LEFT_ANGLE_BRACKET MINUS_SIGN LEFT_BRACKET constructElementPatternFiller RIGHT_BRACKET MINUS_SIGN
   ;

constructEdgeAnyDirection
   : MINUS_SIGN LEFT_BRACKET constructElementPatternFiller RIGHT_BRACKET MINUS_SIGN
   ;

primaryKey
   : PRIMARY KEY LEFT_PAREN (identifier)+ RIGHT_PAREN
   ;

constructElementPropertySpecification
   : LEFT_BRACE propertyKeyValuePairList (COMMA extendElement)? RIGHT_BRACE
   ;

extendElement
   : DOUBLE_PERIOD identifier
   ;

startVar
   : identifier
   ;

endVar
   : identifier
   ;

selectStatement
   : SELECT hintItemlist? setQuantifier? (ASTERISK | selectItemList) selectStatementBody? whereClause? groupByClause? havingClause? orderByClause? offsetClause? limitClause?
   ; // [EXTEND:Geabase]

selectItemList
   : selectItem (COMMA selectItem)*
   ;

selectItem
   : expression (AS identifier)?
   ;

havingClause
   : HAVING expression
   ;

selectStatementBody
   : FROM selectGraphMatchList
   | FROM selectQuerySpecification
   | matchStatement (COMMA matchStatement)* // [EXTEND:Geabase]
   ;

selectGraphMatchList
   : selectGraphMatch (COMMA selectGraphMatch)*
   ;

selectGraphMatch
   : graphExpression matchStatement
   ;

selectQuerySpecification
   : nestedQuerySpecification
   | graphExpression nestedQuerySpecification
   ;

callProcedureStatement
   : OPTIONAL? CALL procedureCall
   ;

procedureCall
   : inlineProcedureCall
   | namedProcedureCall
   ;

inlineProcedureCall
   : variableScopeClause? nestedProcedureSpecification
   ;

variableScopeClause
   : LEFT_PAREN bindingVariableReferenceList? RIGHT_PAREN
   ;

bindingVariableReferenceList
   : bindingVariableReference (COMMA bindingVariableReference)*
   ;

namedProcedureCall
   : procedureReference LEFT_PAREN procedureArgumentList? RIGHT_PAREN yieldClause?
   ;

procedureArgumentList
   : procedureArgument (COMMA procedureArgument)*
   ;

procedureArgument
   : expression
   ;

useGraphClause
   : (USE | FROM) graphExpression  //[Extended:Geaphi] ADD from in use graph clause
   ;

atSchemaClause
   : AT schemaReference
   ;

bindingVariableReference
   : bindingVariable
   ;

elementVariableReference
   : bindingVariableReference
   ;

pathVariableReference
   : bindingVariableReference
   ;

parameter
   : parameterName
   ;

graphPatternBindingTable
   : graphPattern graphPatternYieldClause?
   ;

graphPatternYieldClause
   : YIELD graphPatternYieldItemList
   ;

graphPatternYieldItemList
   : graphPatternYieldItem (COMMA graphPatternYieldItem)*
   | NO BINDINGS
   ;

graphPatternYieldItem
   : elementVariableReference
   | pathVariableReference
   ;

graphPattern
   : matchMode? pathPatternList keepClause? whereClause?
   ;

matchMode
   : repeatableElementsMatchMode
   | differentEdgesMatchMode
   ;

repeatableElementsMatchMode
   : REPEATABLE elementBindingsOrElements
   ;

differentEdgesMatchMode
   : DIFFERENT edgeBindingsOrEdges
   ;

elementBindingsOrElements
   : ELEMENT BINDINGS?
   | ELEMENTS
   ;

edgeBindingsOrEdges
   : EDGE_SYNONYM BINDINGS?
   | EDGES_SYNONYM
   ;

pathPatternList
   : pathPattern (COMMA pathPattern)*
   ;

pathPattern
   : pathVariableDeclaration? pathPatternPrefix? pathPatternExpression
   ;

pathVariableDeclaration
   : pathVariable EQUALS_OPERATOR
   ;

keepClause
   : KEEP pathPatternPrefix
   ;


pathPatternPrefix
   : pathModePrefix
   | pathSearchPrefix
   ;

pathModePrefix
   : pathMode pathOrPaths?
   ;

pathMode
   : WALK
   | TRAIL
   | SIMPLE
   | ACYCLIC
   ;

pathSearchPrefix
   : allPathSearch
   | anyPathSearch
   | shortestPathSearch
   ;

allPathSearch
   : ALL pathMode? pathOrPaths?
   ;

pathOrPaths
   : PATH
   | PATHS
   ;

anyPathSearch
   : ANY numberOfPaths? pathMode? pathOrPaths?
   ;

numberOfPaths
   : unsignedIntegerSpecification
   ;

shortestPathSearch
   : allShortestPathSearch
   | anyShortestPathSearch
   | countedShortestPathSearch
   | countedShortestGroupSearch
   ;

allShortestPathSearch
   : ALL SHORTEST pathMode? pathOrPaths?
   ;

anyShortestPathSearch
   : ANY SHORTEST pathMode? pathOrPaths?
   ;

countedShortestPathSearch
   : SHORTEST numberOfPaths pathMode? pathOrPaths?
   ;

countedShortestGroupSearch
   : SHORTEST numberOfGroups pathMode? pathOrPaths? (GROUP | GROUPS)
   ;

numberOfGroups
   : unsignedIntegerSpecification
   ;

pathPatternExpression
   : pathTerm
   | pathMultisetAlternation
   | pathPatternUnion
   ;

pathMultisetAlternation
   : pathTerm MULTISET_ALTERNATION_OPERATOR pathTerm (MULTISET_ALTERNATION_OPERATOR pathTerm)*
   ;

pathPatternUnion
   : pathTerm VERTICAL_BAR pathTerm (VERTICAL_BAR pathTerm)*
   ;

pathTerm
   : pathFactor+
   ;

pathFactor
   : pathPrimary
   | quantifiedPathPrimary
   | questionedPathPrimary
   ;

quantifiedPathPrimary
   : pathPrimary graphPatternQuantifier
   ;

questionedPathPrimary
   : pathPrimary QUESTION_MARK
   ;

pathPrimary
   : elementPattern
   | parenthesizedPathPatternExpression
   | simplifiedPathPatternExpression
   ;

elementPattern
   : nodePattern
   | edgePattern
   ;

nodePattern
   : LEFT_PAREN elementPatternFiller RIGHT_PAREN
   ;

elementPatternFiller
   : elementVariableDeclaration? isLabelExpression? elementPatternPredicate?
   ;

elementVariableDeclaration
   : TEMP? elementVariable
   ;

isLabelExpression
   : isOrColon labelExpression
   ;

isOrColon
   : IS
   | COLON
   ;

// [Extend: ALL] PERNODELIMIT
elementPatternPredicate
   : whereClause
   | elementPropertySpecification
   | perNodeLimitClause
   | perNodeLimitWherePredicate
   | perNodeLimitPropertyPredicate
   | perShardLimitClause
   | perShardLimitWherePredicate
   | perShardLimitPropertyPredicate
   ;

elementPropertySpecification
   : LEFT_BRACE propertyKeyValuePairList RIGHT_BRACE
   ;

propertyKeyValuePairList
   : propertyKeyValuePair (COMMA propertyKeyValuePair)*
   ;

propertyKeyValuePair
   : propertyName COLON expression
   ;

perNodeLimitClause
   : PER_NODE_LIMIT unsignedIntegerSpecification
   | PER_NODE_LIMIT LEFT_PAREN unsignedIntegerSpecification RIGHT_PAREN
   ;

perNodeLimitWherePredicate
   : perNodeLimitLeftWherePredicate
   | perNodeLimitRightWherePredicate
   | perNodeLimitBothWherePredicate
   ;

perNodeLimitLeftWherePredicate
   : lhs = perNodeLimitClause whereClause
   ;

perNodeLimitRightWherePredicate
   : whereClause rhs = perNodeLimitClause
   ;

perNodeLimitBothWherePredicate
   : lhs = perNodeLimitClause whereClause rhs = perNodeLimitClause
   ;

perNodeLimitPropertyPredicate
   : perNodeLimitLeftPropertyPredicate
   | perNodeLimitRightPropertyPredicate
   | perNodeLimitBothPropertyPredicate
   ;

perNodeLimitLeftPropertyPredicate
   : lhs = perNodeLimitClause elementPropertySpecification
   ;
perNodeLimitRightPropertyPredicate
   : elementPropertySpecification rhs = perNodeLimitClause
   ;
perNodeLimitBothPropertyPredicate
   : lhs = perNodeLimitClause elementPropertySpecification rhs = perNodeLimitClause
   ;

perShardLimitClause
   : PER_SHARD_LIMIT unsignedIntegerSpecification
   | PER_SHARD_LIMIT LEFT_PAREN unsignedIntegerSpecification RIGHT_PAREN
   ;

perShardLimitWherePredicate
   : perShardLimitLeftWherePredicate
   | perShardLimitRightWherePredicate
   | perShardLimitBothWherePredicate
   ;

perShardLimitLeftWherePredicate
   : lhs = perShardLimitClause whereClause
   ;

perShardLimitRightWherePredicate
   : whereClause rhs = perShardLimitClause
   ;

perShardLimitBothWherePredicate
   : lhs = perShardLimitClause whereClause rhs = perShardLimitClause
   ;

perShardLimitPropertyPredicate
   : perShardLimitLeftPropertyPredicate
   | perShardLimitRightPropertyPredicate
   | perShardLimitBothPropertyPredicate
   ;

perShardLimitLeftPropertyPredicate
   : lhs = perShardLimitClause elementPropertySpecification
   ;

perShardLimitRightPropertyPredicate
   : elementPropertySpecification rhs = perShardLimitClause
   ;

perShardLimitBothPropertyPredicate
   : lhs = perShardLimitClause elementPropertySpecification rhs = perShardLimitClause
   ;

edgePattern
   : fullEdgePattern
   | abbreviatedEdgePattern
   ;

fullEdgePattern
   : fullEdgePointingLeft
   | fullEdgeUndirected
   | fullEdgePointingRight
   | fullEdgeLeftOrUndirected
   | fullEdgeUndirectedOrRight
   | fullEdgeLeftOrRight
   | fullEdgeAnyDirection
   ;

fullEdgePointingLeft
   : LEFT_ANGLE_BRACKET MINUS_SIGN LEFT_BRACKET elementPatternFiller RIGHT_BRACKET MINUS_SIGN
   ; // <-[]-

fullEdgeUndirected
   : TILDE LEFT_BRACKET elementPatternFiller RIGHT_BRACKET TILDE
   ; // ~[]~

fullEdgePointingRight
   : MINUS_SIGN LEFT_BRACKET elementPatternFiller RIGHT_BRACKET RIGHT_ARROW
   ; // -[]->

fullEdgeLeftOrUndirected
   : LEFT_ANGLE_BRACKET TILDE LEFT_BRACKET elementPatternFiller RIGHT_BRACKET TILDE
   ; // <~[]~

fullEdgeUndirectedOrRight
   : TILDE LEFT_BRACKET elementPatternFiller RIGHT_BRACKET TILDE_RIGHT_ARROW
   ; // ~[]~>

fullEdgeLeftOrRight
   : LEFT_ANGLE_BRACKET MINUS_SIGN LEFT_BRACKET elementPatternFiller RIGHT_BRACKET RIGHT_ARROW
   ; // <-[]->

fullEdgeAnyDirection
   : MINUS_SIGN LEFT_BRACKET elementPatternFiller RIGHT_BRACKET MINUS_SIGN
   ; // -[]-

abbreviatedEdgePattern
   : LEFT_ANGLE_BRACKET MINUS_SIGN  #abbreviatedEdgePointingLeft
   | TILDE                          #abbreviatedEdgeUndirected
   | RIGHT_ARROW                    #abbreviatedEdgePointingRight
   | LEFT_ANGLE_BRACKET TILDE       #abbreviatedEdgeLeftOrUndirected
   | TILDE_RIGHT_ARROW              #abbreviatedEdgeUndirectedOrRight
   | LEFT_MINUS_RIGHT               #abbreviatedEdgeLeftOrRight
   | MINUS_SIGN                     #abbreviatedEdgeAnyDirection
   ;

parenthesizedPathPatternExpression
   : LEFT_PAREN parenthesizedPathPatternExpressionBody RIGHT_PAREN
   | LEFT_BRACKET parenthesizedPathPatternExpressionBody RIGHT_BRACKET
   ;

//[EXTEND:geaphi] sliding window start
parenthesizedPathPatternExpressionBody
   : subpathVariableDeclaration? pathModePrefix? pathPatternExpression slidingPart? parenthesizedPathPatternWhereClause? untilPart?
   ;

untilPart
   : UNTIL expression
   ;

slidingPart
   : SLIDING lengthPart (stepPart)? AS identifier (whereClause)?
   ;

lengthPart
   : LENGTH integerLiteral
   ;

stepPart
   : STEP integerLiteral
   ;
//[EXTEND:geaphi] sliding window end

subpathVariableDeclaration
   : subpathVariable EQUALS_OPERATOR
   ;

parenthesizedPathPatternWhereClause
   : WHERE expression
   ;

insertGraphPattern
   : insertPathPatternList
   ;

insertPathPatternList
   : insertPathPattern (COMMA insertPathPattern)*
   ;

insertPathPattern
   : insertNodePattern (insertEdgePattern insertNodePattern)*
   ;

insertNodePattern
   : LEFT_PAREN insertElementPatternFiller? RIGHT_PAREN
   ;

insertEdgePattern
   : insertEdgePointingLeft
   | insertEdgePointingRight
   | insertEdgeUndirected
   ;

insertEdgePointingLeft
   : LEFT_ANGLE_BRACKET MINUS_SIGN LEFT_BRACKET insertElementPatternFiller? RIGHT_BRACKET MINUS_SIGN
   ;

insertEdgePointingRight
   : MINUS_SIGN LEFT_BRACKET insertElementPatternFiller? RIGHT_BRACKET RIGHT_ARROW
   ;

insertEdgeUndirected
   : (TILDE | MINUS_SIGN) LEFT_BRACKET insertElementPatternFiller? RIGHT_BRACKET (TILDE | MINUS_SIGN)
   //[EXTEND]: ()-[]-()
   ;

insertElementPatternFiller
   : elementVariableDeclaration labelAndPropertySetSpecification
   | elementVariableDeclaration
   | labelAndPropertySetSpecification
   ;

labelAndPropertySetSpecification
   : isOrColon labelSetSpecification
   | isOrColon labelSetSpecification elementPropertySpecification
   | elementPropertySpecification
   ;

labelExpression
   : labelTerm (VERTICAL_BAR labelTerm)*
   ;

labelTerm
   : labelFactor (AMPERSAND labelFactor)*
   ;

labelFactor
   : (EXCLAMATION_MARK)? labelPrimary
   ;

labelPrimary
   : labelName
   | wildcardLabel
   | parenthesizedLabelExpression
   ;

wildcardLabel
   : PERCENT
   ;

parenthesizedLabelExpression
   : LEFT_PAREN labelExpression RIGHT_PAREN
   ;

graphPatternQuantifier
   : ASTERISK                                          #gqlGraphPatternAsteriskQuantifier
   | PLUS_SIGN                                         #gqlGraphPatternPlusSignQuantifier
   | fixedQuantifier                                   #gqlGraphPatternFixedQuantifier
   | generalQuantifier                                 #gqlGraphPatternGeneralQuantifier
   ;

fixedQuantifier
   : LEFT_BRACE unsignedIntegerSpecification RIGHT_BRACE // [EXTEND:Geabase] support parameterized
   ;

generalQuantifier
   : LEFT_BRACE lowerBound? COMMA upperBound? RIGHT_BRACE
   ;

lowerBound
   : unsignedIntegerSpecification// [EXTEND:Geabase] support parameterized lower bound
   ;

upperBound
   : unsignedIntegerSpecification// [EXTEND:Geabase] support parameterized lower bound
   ;

simplifiedPathPatternExpression
   : simplifiedDefaultingLeft
   | simplifiedDefaultingUndirected
   | simplifiedDefaultingRight
   | simplifiedDefaultingLeftOrUndirected
   | simplifiedDefaultingUndirectedOrRight
   | simplifiedDefaultingLeftOrRight
   | simplifiedDefaultingAnyDirection
   ;

simplifiedDefaultingLeft
   : LEFT_MINUS_SLASH simplifiedContents SOLIDUS MINUS_SIGN
   ;

simplifiedDefaultingUndirected
   : TILDE_SLASH simplifiedContents SOLIDUS TILDE
   ;

simplifiedDefaultingRight
   : MINUS_SLASH simplifiedContents SLASH_MINUS_RIGHT
   ;

simplifiedDefaultingLeftOrUndirected
   : LEFT_TILDE_SLASH simplifiedContents SOLIDUS TILDE
   ;

simplifiedDefaultingUndirectedOrRight
   : TILDE_SLASH simplifiedContents SLASH_TILDE_RIGHT
   ;

simplifiedDefaultingLeftOrRight
   : LEFT_MINUS_SLASH simplifiedContents SLASH_MINUS_RIGHT
   ;

simplifiedDefaultingAnyDirection
   : MINUS_SLASH simplifiedContents SOLIDUS MINUS_SIGN
   ;

simplifiedContents
   : simplifiedTerm
   | simplifiedPathUnion
   | simplifiedMultisetAlternation
   ;

simplifiedPathUnion
   : simplifiedTerm VERTICAL_BAR simplifiedTerm (VERTICAL_BAR simplifiedTerm)*
   ;

simplifiedMultisetAlternation
   : simplifiedTerm MULTISET_ALTERNATION_OPERATOR simplifiedTerm (MULTISET_ALTERNATION_OPERATOR simplifiedTerm)*
   ;

simplifiedTerm
   : (simplifiedFactorLow)+
   ;

simplifiedFactorLow
   : simplifiedFactorHigh (AMPERSAND simplifiedFactorHigh)*
   ;

simplifiedFactorHigh
   : simplifiedTertiary
   | simplifiedQuantified
   | simplifiedQuestioned
   ;

simplifiedQuantified
   : simplifiedTertiary graphPatternQuantifier
   ;

simplifiedQuestioned
   : simplifiedTertiary QUESTION_MARK
   ;

simplifiedTertiary
   : simplifiedDirectionOverride
   | simplifiedSecondary
   ;

simplifiedDirectionOverride
   : simplifiedOverrideLeft
   | simplifiedOverrideUndirected
   | simplifiedOverrideRight
   | simplifiedOverrideLeftOrUndirected
   | simplifiedOverrideUndirectedOrRight
   | simplifiedOverrideLeftOrRight
   | simplifiedOverrideAnyDirection
   ;

simplifiedOverrideLeft
   : LEFT_ANGLE_BRACKET simplifiedSecondary
   ;

simplifiedOverrideUndirected
   : TILDE simplifiedSecondary
   ;

simplifiedOverrideRight
   : simplifiedSecondary RIGHT_ANGLE_BRACKET
   ;

simplifiedOverrideLeftOrUndirected
   : LEFT_ANGLE_BRACKET TILDE simplifiedSecondary
   ;

simplifiedOverrideUndirectedOrRight
   : TILDE simplifiedSecondary RIGHT_ANGLE_BRACKET
   ;

simplifiedOverrideLeftOrRight
   : LEFT_ANGLE_BRACKET simplifiedSecondary RIGHT_ANGLE_BRACKET
   ;

simplifiedOverrideAnyDirection
   : MINUS_SIGN simplifiedSecondary
   ;

simplifiedSecondary
   : simplifiedPrimary
   | simplifiedNegation
   ;

simplifiedNegation
   : EXCLAMATION_MARK simplifiedPrimary
   ;

simplifiedPrimary
   : labelName
   | LEFT_PAREN simplifiedContents RIGHT_PAREN
   ;

whereClause
   : WHERE expression
   ;

yieldClause
   : YIELD yieldItemList
   ;

yieldItemList
   : yieldItem (COMMA yieldItem)*
   ;

yieldItem
   : yieldItemName yieldItemAlias?
   ;

yieldItemName
   : fieldName
   ;

yieldItemAlias
   : AS bindingVariable
   ;

groupByClause
   : GROUP BY groupingElementList
   ;

groupingElementList
   : groupingElement (COMMA groupingElement)*
   | emptyGroupingSet
   ;

groupingElement
   : expression
   ; //gebabase : bindingVariableReference ->expression

emptyGroupingSet
   : LEFT_PAREN RIGHT_PAREN
   ;

orderByClause
   : ORDER BY sortSpecificationList
   ;

// [extend:geabase]: count DISTINCT
aggregateFunction
   : COUNT LEFT_PAREN ASTERISK RIGHT_PAREN                                                                                   #gqlCountAllFunction
   | COUNT LEFT_PAREN DISTINCT expression (COMMA expression)+ RIGHT_PAREN                                                    #gqlCountDistinctFunction
   | generalSetFunctionType LEFT_PAREN setQuantifier? expression RIGHT_PAREN                                                 #gqlGeneralSetFunction
   | binarySetFunctionType LEFT_PAREN setQuantifier? lhs = expression COMMA rhs = expression RIGHT_PAREN                     #gqlBinarySetFunction
   | (generalSetFunctionType | windowFunctionType) LEFT_PAREN (setQuantifier? expression)? RIGHT_PAREN windowClause          #gqlWindowFunction
   | generalSetFunctionType LEFT_PAREN expression DISTINCT BY expression (COMMA expression)* RIGHT_PAREN                     #gqlDistinctInGeneralFunction //[EXTEND]: 解决路径膨张问题
   ;

// [Extend: geabase]: GROUP_CONCAT
generalSetFunctionType
   : AVG
   | COUNT
   | MAX_
   | MIN_
   | SUM
   | COLLECT
   | STDDEV_SAMP
   | STDDEV_POP
   | GROUP_CONCAT
   ;

setQuantifier
   : DISTINCT
   | ALL
   ;

binarySetFunctionType
   : PERCENTILE_CONT
   | PERCENTILE_DISC
   ;

//[Extend: Geaphi]: window function extend
windowFunctionType
   : ROW_NUMBER
   | RANK
   | DENSE_RANK
   | CUME_DIST
   | PERCENT_RANK
   ;

windowClause
   : OVER LEFT_PAREN PARTITION BY expressionAtom (COMMA expressionAtom)* (orderByClause)? RIGHT_PAREN
   ;

sortSpecificationList
   : sortSpecification (COMMA sortSpecification)*
   ;

sortSpecification
   : sortKey orderingSpecification? nullOrdering?
   ;

sortKey
   : expression
   ;

orderingSpecification
   : ASC
   | ASCENDING
   | DESC
   | DESCENDING
   ;

nullOrdering
   : NULLS FIRST
   | NULLS LAST
   ;

limitClause
   : LIMIT unsignedIntegerSpecification
   ;

offsetClause
   : offsetSynonym unsignedIntegerSpecification
   ;

offsetSynonym
   : OFFSET
   | SKIP_
   ;

nestedGraphTypeSpecification
   : LEFT_BRACE graphTypeSpecificationBody RIGHT_BRACE
   ;

graphTypeSpecificationBody
   : elementTypeDefinitionList
   ;

elementTypeDefinitionList
   : elementTypeDefinition (COMMA elementTypeDefinition)*
   ;

elementTypeDefinition
   : nodeTypeDefinition
   | edgeTypeDefinition
   ;

nodeTypeDefinition
   : nodeTypePattern
   | NODE_SYNONYM nodeTypePhrase
   ;

nodeTypePattern
   : LEFT_PAREN nodeTypeName? nodeTypeFiller? RIGHT_PAREN
   ;

nodeTypePhrase
   : TYPE? nodeTypeName nodeTypeFiller?
   | nodeTypeFiller
   ;

nodeTypeName
   : elementTypeName
   ;

nodeTypeFiller
   : nodeTypeLabelSetDefinition
   | nodeTypePropertyTypeSetDefinition
   | nodeTypeLabelSetDefinition nodeTypePropertyTypeSetDefinition
   ;

nodeTypeLabelSetDefinition
   : labelSetDefinition
   ;

nodeTypePropertyTypeSetDefinition
   : propertyTypeSetDefinition
   ;

edgeTypeDefinition
   : edgeTypePattern
   | edgeKind? EDGE_SYNONYM edgeTypePhrase
   ;

edgeTypePattern
   : fullEdgeTypePattern
   | abbreviatedEdgeTypePattern
   ;

edgeTypePhrase
   : TYPE? edgeTypeName (edgeTypeFiller endpointDefinition)?
   | edgeTypeFiller endpointDefinition
   ;

edgeTypeName
   : elementTypeName
   ;

edgeTypeFiller
   : edgeTypeLabelSetDefinition
   | edgeTypePropertyTypeSetDefinition
   | edgeTypeLabelSetDefinition edgeTypePropertyTypeSetDefinition
   ;

edgeTypeLabelSetDefinition
   : labelSetDefinition
   ;

edgeTypePropertyTypeSetDefinition
   : propertyTypeSetDefinition
   ;

fullEdgeTypePattern
   : fullEdgeTypePatternPointingRight
   | fullEdgeTypePatternPointingLeft
   | fullEdgeTypePatternUndirected
   ;

fullEdgeTypePatternPointingRight
   : sourceNodeTypeReference arcTypePointingRight destinationNodeTypeReference
   ;

fullEdgeTypePatternPointingLeft
   : destinationNodeTypeReference arcTypePointingLeft sourceNodeTypeReference
   ;

fullEdgeTypePatternUndirected
   : sourceNodeTypeReference arcTypeUndirected destinationNodeTypeReference
   ;

arcTypePointingRight
   : MINUS_SIGN LEFT_BRACKET arcTypeFiller RIGHT_BRACKET RIGHT_ARROW
   ;

arcTypePointingLeft
   : LEFT_ANGLE_BRACKET MINUS_SIGN LEFT_BRACKET arcTypeFiller RIGHT_BRACKET MINUS_SIGN
   ;

arcTypeUndirected
   : TILDE LEFT_BRACKET arcTypeFiller RIGHT_BRACKET TILDE
   ;

arcTypeFiller
   : edgeTypeName? edgeTypeFiller?
   ;

abbreviatedEdgeTypePattern
   : abbreviatedEdgeTypePatternPointingRight
   | abbreviatedEdgeTypePatternPointingLeft
   | abbreviatedEdgeTypePatternUndirected
   ;

abbreviatedEdgeTypePatternPointingRight
   : sourceNodeTypeReference RIGHT_ARROW destinationNodeTypeReference
   ;

abbreviatedEdgeTypePatternPointingLeft
   : destinationNodeTypeReference LEFT_ANGLE_BRACKET MINUS_SIGN sourceNodeTypeReference
   ;

abbreviatedEdgeTypePatternUndirected
   : sourceNodeTypeReference TILDE destinationNodeTypeReference
   ;

nodeTypeReference
   : sourceNodeTypeReference
   | destinationNodeTypeReference
   ;

sourceNodeTypeReference
   : LEFT_PAREN sourceNodeTypeName RIGHT_PAREN
   | LEFT_PAREN nodeTypeFiller? RIGHT_PAREN
   ;

destinationNodeTypeReference
   : LEFT_PAREN destinationNodeTypeName RIGHT_PAREN
   | LEFT_PAREN nodeTypeFiller? RIGHT_PAREN
   ;

edgeKind
   : DIRECTED
   | UNDIRECTED
   ;

endpointDefinition
   : CONNECTING endpointPairDefinition
   ;

endpointPairDefinition
   : endpointPairDefinitionPointingRight
   | endpointPairDefinitionPointingLeft
   | endpointPairDefinitionUndirected
   | abbreviatedEdgeTypePattern
   ;

endpointPairDefinitionPointingRight
   : LEFT_PAREN sourceNodeTypeName connectorPointingRight destinationNodeTypeName RIGHT_PAREN
   ;

endpointPairDefinitionPointingLeft
   : LEFT_PAREN destinationNodeTypeName LEFT_ANGLE_BRACKET MINUS_SIGN sourceNodeTypeName RIGHT_PAREN
   ;

endpointPairDefinitionUndirected
   : LEFT_PAREN sourceNodeTypeName connectorUndirected destinationNodeTypeName RIGHT_PAREN
   ;

connectorPointingRight
   : TO
   | RIGHT_ARROW
   ;

connectorUndirected
   : TO
   | TILDE
   ;

sourceNodeTypeName
   : elementTypeName
   ;

destinationNodeTypeName
   : elementTypeName
   ;

labelSetDefinition
   : LABEL labelName
   | LABELS labelSetSpecification
   | isOrColon labelSetSpecification
   ;

propertyTypeSetDefinition
   : LEFT_BRACE propertyTypeDefinitionList? RIGHT_BRACE
   ;

propertyTypeDefinitionList
   : propertyTypeDefinition (COMMA propertyTypeDefinition)*
   ;

propertyTypeDefinition
   : propertyName typed? propertyValueType
   ;

propertyValueType
   : valueType
   ;

bindingTableType
   : BINDING? TABLE fieldTypesSpecification
   ;

valueType
   : predefinedType                                                                                                      #predefType
   | pathValueType                                                                                                       #pathType
   | listValueTypeName LEFT_ANGLE_BRACKET valueType RIGHT_ANGLE_BRACKET (LEFT_BRACKET maxLength RIGHT_BRACKET)? notNull? #listType1
   | valueType listValueTypeName (LEFT_BRACKET maxLength RIGHT_BRACKET)? notNull?                                        #listType2
   | ANY? RECORD notNull?                                                                                               #recordType1
   | RECORD? fieldTypesSpecification notNull?                                                                            #recordType2
   | ANY VALUE? notNull?                                                                                             #openDynamicUnionType
   | ANY? PROPERTY VALUE notNull?                                                                                      #dynamicPropertyValueType
   | ANY VALUE? LEFT_ANGLE_BRACKET valueType (VERTICAL_BAR valueType)* RIGHT_ANGLE_BRACKET                                      #closedDynamicUnionType1
   | valueType (VERTICAL_BAR valueType)+                                                                                 #closedDynamicUnionType2
   ;

typed
   : DOUBLE_COLON
   | TYPED
   ;

predefinedType
   : booleanType
   | characterStringType
   | byteStringType
   | numericType
   | temporalType
   | referenceValueType
   ;

booleanType
   : (BOOL | BOOLEAN) notNull?
   ;

characterStringType
   : (STRING | VARCHAR) (LEFT_PAREN maxLength RIGHT_PAREN)? notNull?
   ;

byteStringType
   : BYTES (LEFT_PAREN (minLength COMMA)? maxLength RIGHT_PAREN)? notNull?
   | BINARY (LEFT_PAREN fixedLength RIGHT_PAREN)? notNull?
   | VARBINARY (LEFT_PAREN maxLength RIGHT_PAREN)? notNull?
   ;

minLength
   : UNSIGNED_DECIMAL_INTEGER
   ;

maxLength
   : UNSIGNED_DECIMAL_INTEGER
   ;

fixedLength
   : UNSIGNED_DECIMAL_INTEGER
   ;

numericType
   : exactNumericType
   | approximateNumericType
   ;

exactNumericType
   : binaryExactNumericType
   | decimalExactNumericType
   ;

binaryExactNumericType
   : signedBinaryExactNumericType
   | unsignedBinaryExactNumericType
   ;

signedBinaryExactNumericType
   : INT8 notNull?
   | INT16 notNull?
   | INT32 notNull?
   | INT64 notNull?
   | INT128 notNull?
   | INT256 notNull?
   | SMALLINT notNull?
   | INT (LEFT_PAREN precision RIGHT_PAREN)? notNull?
   | BIGINT
   | SIGNED? verboseBinaryExactNumericType notNull?
   | LONG notNull? // [Extend: geabase]
   ;

unsignedBinaryExactNumericType
   : UINT8 notNull?
   | UINT16 notNull?
   | UINT32 notNull?
   | UINT64 notNull?
   | UINT128 notNull?
   | UINT256 notNull?
   | USMALLINT notNull?
   | UINT (LEFT_PAREN precision RIGHT_PAREN)? notNull?
   | UBIGINT notNull?
   | UNSIGNED verboseBinaryExactNumericType notNull?
   ;

verboseBinaryExactNumericType
   : INTEGER8 notNull?
   | INTEGER16 notNull?
   | INTEGER32 notNull?
   | INTEGER64 notNull?
   | INTEGER128 notNull?
   | INTEGER256 notNull?
   | SMALL INTEGER notNull?
   | INTEGER (LEFT_PAREN precision RIGHT_PAREN)? notNull?
   | BIG INTEGER notNull?
   ;

decimalExactNumericType
   : (DECIMAL | DEC) (LEFT_PAREN precision (COMMA scale)? RIGHT_PAREN notNull?)?
   ;

precision
   : UNSIGNED_DECIMAL_INTEGER
   ;

scale
   : UNSIGNED_DECIMAL_INTEGER
   ;

approximateNumericType
   : FLOAT16 notNull?
   | FLOAT32 notNull?
   | FLOAT64 notNull?
   | FLOAT128 notNull?
   | FLOAT256 notNull?
   | FLOAT (LEFT_PAREN precision (COMMA scale)? RIGHT_PAREN)? notNull?
   | REAL notNull?
   | DOUBLE PRECISION? notNull?
   ;

temporalType
   : temporalInstantType
   | temporalDurationType
   ;

temporalInstantType
   : datetimeType
   | localdatetimeType
   | dateType
   | timeType
   | localtimeType
   ;

temporalDurationType
   : durationType
   ;

datetimeType
   : ZONED DATETIME notNull?
   | TIMESTAMP WITH TIMEZONE notNull?
   | DATETIME notNull? // [Extend: geabase]: cast (x AS Datetime)
   ;

localdatetimeType
   : LOCAL DATETIME notNull?
   | TIMESTAMP (WITHOUT TIMEZONE)? notNull?
   ;

dateType
   : DATE notNull?
   ;

timeType
   : ZONED TIME notNull?
   | TIME WITH TIMEZONE notNull?
   ;

localtimeType
   : LOCAL TIME notNull?
   | TIME WITHOUT TIMEZONE notNull?
   ;

durationType
   : DURATION notNull?
   ;

referenceValueType
   : graphReferenceValueType
   | bindingTableReferenceValueType
   | nodeReferenceValueType
   | edgeReferenceValueType
   ;

graphReferenceValueType
   : openGraphReferenceValueType
   | closedGraphReferenceValueType
   ;

closedGraphReferenceValueType
   : PROPERTY? GRAPH nestedGraphTypeSpecification notNull?
   ;

openGraphReferenceValueType
   : ANY PROPERTY? GRAPH notNull?
   ;

bindingTableReferenceValueType
   : bindingTableType notNull?
   ;

nodeReferenceValueType
   : openNodeReferenceValueType
   | closedNodeReferenceValueType
   ;

closedNodeReferenceValueType
   : nodeTypeDefinition notNull?
   ;

openNodeReferenceValueType
   : ANY? NODE_SYNONYM notNull?
   ;

edgeReferenceValueType
   : openEdgeReferenceValueType
   | closedEdgeReferenceValueType
   ;

closedEdgeReferenceValueType
   : edgeTypeDefinition notNull?
   ;

openEdgeReferenceValueType
   : ANY? EDGE_SYNONYM notNull?
   ;

listValueTypeName
   : GROUP? listValueTypeNameSynonym
   ;

listValueTypeNameSynonym
   : LIST
   | ARRAY
   ;

fieldTypesSpecification
   : LEFT_BRACE fieldTypeList? RIGHT_BRACE
   ;

fieldTypeList
   : fieldType (COMMA fieldType)*
   ;

pathValueType
   : PATH notNull?
   ;

notNull
   : NOT NULL_
   ;

fieldType
   : fieldName typed? valueType
   ;

schemaReference
   : absoluteCatalogSchemaReference
   | relativeCatalogSchemaReference
   | referenceParameter
   ;

absoluteCatalogSchemaReference
   : SOLIDUS
   | absoluteDirectoryPath schemaName
   ;

catalogSchemaParentAndName
   : absoluteDirectoryPath schemaName
   ;

relativeCatalogSchemaReference
   : predefinedSchemaReference
   | relativeDirectoryPath schemaName
   ;

predefinedSchemaReference
   : HOME_SCHEMA
   | CURRENT_SCHEMA
   | PERIOD
   ;

absoluteDirectoryPath
   : SOLIDUS simpleDirectoryPath?
   ;

relativeDirectoryPath
   : DOUBLE_PERIOD ((SOLIDUS DOUBLE_PERIOD)* SOLIDUS simpleDirectoryPath?)?
   ;

simpleDirectoryPath
   : (directoryName SOLIDUS)+
   ;

graphReference
   : catalogObjectParentReference graphName
   | delimitedGraphName
   | homeGraph
   | referenceParameter
   ;

catalogGraphParentAndName
   : catalogObjectParentReference? graphName
   ;

homeGraph
   : HOME_PROPERTY_GRAPH
   | HOME_GRAPH
   ;

graphTypeReference
   : catalogGraphTypeParentAndName
   | referenceParameter
   ;

catalogGraphTypeParentAndName
   : catalogObjectParentReference? graphTypeName
   ;

bindingTableReference
   : catalogObjectParentReference bindingTableName
   | delimitedBindingTableName
   | referenceParameter
   ;

catalogBindingTableParentAndName
   : catalogObjectParentReference? bindingTableName
   ;

procedureReference
   : catalogProcedureParentAndName
   | referenceParameter
   ;

catalogProcedureParentAndName
   : catalogObjectParentReference? procedureName
   ;

catalogObjectParentReference
   : schemaReference SOLIDUS? (objectName PERIOD)*
   | (objectName PERIOD)+
   ;

referenceParameter
   : parameter
   ;

// TODO: EOR shall be a URI with a mandatory scheme as specified by RFC 3986
//       or alternatively shall be an absolute-URL-with-fragment character string as specified by WHATWG URL.
externalObjectReference
   : I_DONT_KNOW_3
   ;

comparisonPredicateCond
   : compOp expression
   ;

compOp
   : EQUALS_OPERATOR
   | NOT_EQUALS_OPERATOR
   | LEFT_ANGLE_BRACKET
   | RIGHT_ANGLE_BRACKET
   | LESS_THAN_OR_EQUALS_OPERATOR
   | GREATER_THAN_OR_EQUALS_OPERATOR
   | SAFE_EXQUAL_OPERATOR
   ;

nullPredicateCond
   : IS NOT? NULL_
   ;

normalizedPredicateCond
   : IS NOT? normalForm? NORMALIZED
   ;

directedPredicateCond
   : IS NOT? DIRECTED
   ;

labeledPredicateCond
   : (IS NOT? LABELED | COLON) labelExpression
   ;

sourceDestinationPredicateCond
   : IS NOT? (SOURCE | DESTINATION) OF elementVariableReference
   ;

expression
   : NOT expression                                                         #gqlNotExpression
   | lhs = expression AND rhs = expression                                  #gqlLogicalAndExpression
   | lhs = expression XOR rhs = expression                                  #gqlLogicalXorExpression
   | lhs = expression (OR | CONCATENATION_OPERATOR) rhs = expression        #gqlLogicalOrExpression  //geabase 拓展了or，可以用||代替
   | expressionPredicate                                                    #gqlPredicateExpression
   ;

expressionPredicate
   : expressionPredicate NOT? IN listValueTypeName? listValue                                           #gqlInExpression
   | expressionPredicate (IS NOT? | EQUALS_OPERATOR | NOT_EQUALS_OPERATOR) truthValue                   #gqlBooleanTestExpression
   | self = expressionPredicate NOT? LIKE regex = expressionPredicate                                   #gqlLikeExpression
   | lhs = expressionPredicate compOp rhs = expressionPredicate                                         #gqlComparisonExpression
   | val = expressionPredicate NOT? BETWEEN low = expressionPredicate AND high = expressionPredicate    #gqlBetweenExpression
   | EXISTS ( LEFT_BRACE graphPattern RIGHT_BRACE
            | LEFT_PAREN graphPattern RIGHT_PAREN
            | LEFT_BRACE matchStatementBlock RIGHT_BRACE
            | LEFT_PAREN matchStatementBlock RIGHT_PAREN
            | nestedQuerySpecification)                                                                 #gqlExistsExpression
   | expressionPredicate nullPredicateCond                                                              #gqlNullExpression
   | expressionPredicate normalizedPredicateCond                                                             #gqlNormalizedExpression
   | elementVariableReference directedPredicateCond                                                     #gqlDirectedExpression
   | elementVariableReference labeledPredicateCond                                                      #gqlLabeledExpression
   | elementVariableReference sourceDestinationPredicateCond                                            #gqlSourceDestinationExpression
   | ALL_DIFFERENT LEFT_PAREN elementVariableReference (COMMA elementVariableReference)+ RIGHT_PAREN    #gqlAllDifferentExpression
   | SAME LEFT_PAREN elementVariableReference (COMMA elementVariableReference)+ RIGHT_PAREN             #gqlSameExpression
   | PROPERTY_EXISTS LEFT_PAREN elementVariableReference COMMA propertyName RIGHT_PAREN                 #gqlPropertyExistExpression
   | PROPERTY? GRAPH graphExpression                                                                    #gqlGraphRefValueExpression
   | BINDING? TABLE bindingTableExpression                                                              #gqlBindingTableValueExpression
   | LET letVariableDefinitionList IN expression END                                                    #gqlLetExpression
   | expressionAtom                                                                                     #gqlAtomExpression
   ;

expressionAtom
   : LEFT_PAREN expression RIGHT_PAREN                                                      #gqlParenthesizedExpression
   | expressionAtom LEFT_BRACKET unsignedNumericLiteral RIGHT_BRACKET                       #gqlSubscriptExpression //[EXTEND: GeaPhi]
   | expressionAtom PERIOD propertyName                                                     #gqlPropertyReference
//   | expressionAtom CONCATENATION_OPERATOR expressionAtom                                   #gqlConcatenationExpression
   | unsignedLiteral                                                                        #gqlLiteralExpression
   | unaryOperator expressionAtom                                                           #gqlUnaryExpression
   | functionCall                                                                           #gqlFunctionExpression
   | collectionValueConstructor                                                             #gqlCollectionExpression
   | VALUE nestedQuerySpecification                                                         #gqlValueQueryExpression
   | lhs = expressionAtom CIRCUMFLEX rhs = expressionAtom                                   #gqlBitXorExpression // [Extend: geabase]
   | lhs = expressionAtom op = (ASTERISK | SOLIDUS | PERCENT | MOD) rhs = expressionAtom    #gqlHighArithmeticExpression // [Extend: geabase]: PERCENT MOD
   | lhs = expressionAtom op = (PLUS_SIGN | MINUS_SIGN) rhs = expressionAtom                #gqlLowArithmeticExpression
   | lhs = expressionAtom (LEFT_SHIFT | RIGHT_SHIFT) rhs = expressionAtom                   #gqlBitShiftExpression // [Extend: geabase]
   | lhs = expressionAtom AMPERSAND rhs = expressionAtom                                    #gqlBitAndExpression // [Extend: geabase]
   | lhs = expressionAtom VERTICAL_BAR rhs = expressionAtom                                 #gqlBitOrExpression // [Extend: geabase]
   | parameterValueSpecification                                                            #gqlParameterExpression
   | variable                                                                               #gqlVariableExpression
   ;

truthValue
   : TRUE
   | FALSE
   | UNKNOWN
   ;

unaryOperator
   : EXCLAMATION_MARK
   | PLUS_SIGN
   | MINUS_SIGN
   | TILDE // [Extend: geabase]: TILDE
   ;

// functions yielding a value of expression,including numeric value function ,string value function and so on.
functionCall
   : numericFunction
   | aggregateFunction
   | caseFunction
   | castFunction
   | elementFunction
   | datetimeValueFunction
   | durationFunction
   | listFunction
   | stringFunction
   | generalFunction
   ;

numericFunction
   : oneArgNumericFunctionName LEFT_PAREN functionParameter RIGHT_PAREN                             #gqlOneArgScalarFunction
   | twoArgNumericFunctionName LEFT_PAREN functionParameter COMMA functionParameter RIGHT_PAREN     #gqlTwoArgScalarFunction
   | IF LEFT_PAREN functionParameter COMMA functionParameter COMMA functionParameter RIGHT_PAREN    #gqlIfFunction
   ;

// may exist ambiguities
functionParameter
   : unsignedLiteral
   | propertyReference
   | functionCall
   | variable
   | expression
   ;

propertyReference
   : variable PERIOD propertyName
   ;

oneArgNumericFunctionName
   : CHAR_LENGTH
   | CHARACTER_LENGTH
   | BYTE_LENGTH
   | OCTET_LENGTH
   | PATH_LENGTH
   | ABS
   | SIN
   | COS
   | TAN
   | COT
   | SINH
   | COSH
   | TANH
   | ASIN
   | ACOS
   | ATAN
   | DEGREES
   | RADIANS
   | LOG10
   | LN
   | EXP
   | SQRT
   | FLOOR
   | CEIL
   | CEILING
   | LOG // [Extend: geabase] :log(a)
   | LAST // [Extend: geabase]: last(list)函数
   | LABELS // [Extend: geabase]
   | LABEL // [Extend: geabase]
   | LENGTH // [Extend: geabase]
   ;

twoArgNumericFunctionName
   : MOD
   | LOG
   | POWER
   ;

stringFunction
   : SUBSTR LEFT_PAREN str = expressionAtom COMMA startPos = expressionAtom (COMMA len = expressionAtom)? RIGHT_PAREN   #gqlSubstringFunction
   | LEFT LEFT_PAREN expressionAtom COMMA expressionAtom RIGHT_PAREN                                                    #gqlLeftStringFunction
   | RIGHT LEFT_PAREN expressionAtom COMMA expressionAtom RIGHT_PAREN                                                   #gqlRightStringFunction
   | dir = (UPPER | LOWER) LEFT_PAREN expressionAtom RIGHT_PAREN                                                        #gqlFoldStringFunction
   | TRIM LEFT_PAREN (trimSpecification? expressionAtom? FROM)? trimSrc = expressionAtom RIGHT_PAREN                    #gqlSingleTrimStringFunction
   | dir = (BTRIM | LTRIM | RTRIM) LEFT_PAREN trimSrc = expressionAtom (COMMA delChar = expressionAtom)? RIGHT_PAREN    #gqlMultiTrimStringFunction
   | NORMALIZE LEFT_PAREN expressionAtom (COMMA normalForm)? RIGHT_PAREN                                                #gqlNormStringFunction
   ;

listFunction
   : TRIM LEFT_PAREN list = expressionAtom COMMA trim = expressionAtom RIGHT_PAREN      #gqlListTrimFunction
   | ELEMENTS LEFT_PAREN expressionAtom RIGHT_PAREN                                     #gqlElementsOfPathFunction
   ;

// [Extend: geabase] : at least one parameter is required in coalesce
caseFunction
   : NULLIF LEFT_PAREN lhs = expression COMMA rhs = expression RIGHT_PAREN  #gqlNullIfCaseFunction
   | COALESCE LEFT_PAREN expression (COMMA expression)* RIGHT_PAREN         #gqlCoalesceCaseFunction
   | CASE expressionAtom simpleWhenClause+ elseClause? END                  #gqlSimpleCaseFunction
   | CASE searchedWhenClause+ elseClause? END                               #gqlSearchedCaseFunction
   ;

simpleWhenClause
   : WHEN whenOperand (COMMA whenOperand)* THEN expression
   ;

searchedWhenClause
   : WHEN expression THEN expression
   ;

elseClause
   : ELSE expression
   ;

whenOperand
   : expressionAtom
   | comparisonPredicateCond
   | nullPredicateCond
   | directedPredicateCond
   | labeledPredicateCond
   | sourceDestinationPredicateCond
   ;

// cast specification
castFunction
   : CAST LEFT_PAREN expression AS valueType RIGHT_PAREN
   ;

elementFunction
   : elementFunctionName LEFT_PAREN variable RIGHT_PAREN
   ;

elementFunctionName
   : ELEMENT_ID
   | ID // [EXTEND:geabase]
   | TIMESTAMP
   ;

datetimeValueFunction
   : dateFunction
   | timeFunction
   | datetimeFunction
   | localTimeFunction
   | localDatetimeFunction
   ;

dateFunction
   : CURRENT_DATE
   | DATE LEFT_PAREN dateFunctionParameters? RIGHT_PAREN
   ;

timeFunction
   : CURRENT_TIME
   | ZONED_TIME LEFT_PAREN timeFunctionParameters? RIGHT_PAREN
   ;

localTimeFunction
   : LOCAL_TIME (LEFT_PAREN timeFunctionParameters? RIGHT_PAREN)?
   ;

datetimeFunction
   : CURRENT_TIMESTAMP
   | ZONED_DATETIME LEFT_PAREN datetimeFunctionParameters? RIGHT_PAREN
   ;

localDatetimeFunction
   : LOCAL_TIMESTAMP
   | LOCAL_DATETIME LEFT_PAREN datetimeFunctionParameters? RIGHT_PAREN
   ;

durationFunction
   : DURATION_BETWEEN LEFT_PAREN expressionAtom COMMA expressionAtom RIGHT_PAREN    #gqlDatetimeSubtractionFunction
   | DURATION LEFT_PAREN durationFunctionParameters RIGHT_PAREN                     #gqlDurationFunction
   ;

dateFunctionParameters
   : dateString
   | recordValueConstructor
   ;

timeFunctionParameters
   : timeString
   | recordValueConstructor
   ;

datetimeFunctionParameters
   : datetimeString
   | recordValueConstructor
   ;

dateString
   : characterStringLiteral
   ;

timeString
   : characterStringLiteral
   ;

datetimeString
   : characterStringLiteral
   ;

durationFunctionParameters
   : durationString
   | recordValueConstructor
   ;

durationString
   : characterStringLiteral
   ;

generalFunction
   : functionName LEFT_PAREN (functionParameter (COMMA functionParameter)*)? RIGHT_PAREN
   ;

collectionValueConstructor
   : listValueConstructor
   | recordValueConstructor
   | pathValueConstructor
   | mapValueConstructor // [Extend: geabase]
   ;

trimSpecification
   : LEADING
   | TRAILING
   | BOTH
   ;

normalForm
   : NFC
   | NFD
   | NFKC
   | NFKD
   ;

listValueConstructor
   : listValueTypeName? LEFT_BRACKET (expression (COMMA expression)*)? RIGHT_BRACKET
   ;

listValue
   : LEFT_BRACKET expression (COMMA expression)* RIGHT_BRACKET
   | LEFT_PAREN expression (COMMA expression)* RIGHT_PAREN
   ;

recordValueConstructor
   : RECORD? LEFT_BRACE (field (COMMA field)*)? RIGHT_BRACE
   ;

field
   : key = fieldName COLON value = expression
   ;

pathValueConstructor
   : PATH LEFT_BRACKET expressionAtom (COMMA expressionAtom COMMA expressionAtom)* RIGHT_BRACKET
   ;

// [Extend: geabase]
mapValueConstructor
   : MAP LEFT_BRACE mapElement (COMMA mapElement)* RIGHT_BRACE
   ;

mapElement
   : key = expression COLON value = expression
   ;

unsignedValueSpecification
   : unsignedLiteral
   | parameterValueSpecification
   ;

unsignedIntegerSpecification
   : integerLiteral
   | parameter
   ;

unsignedBooleanSpecification
   : booleanLiteral
   | parameter
   ;

parameterValueSpecification
   : parameter
   | predefinedParameter
   ;

predefinedParameter
   : CURRENT_USER
   ;

unsignedLiteral
   : unsignedNumericLiteral
   | generalLiteral
   ;

generalLiteral
   : predefinedTypeLiteral
   | listLiteral
   | mapLiteral //[Extend:geabase]
   | recordLiteral
   ;

listLiteral
   : listValueTypeName? LEFT_BRACKET (generalLiteral (COMMA generalLiteral)*)? RIGHT_BRACKET
   ;

mapLiteral
   : MAP LEFT_BRACE mapElementLiteral (COMMA mapElementLiteral)* RIGHT_BRACE
   ;

mapElementLiteral
   : key = generalLiteral COLON value = generalLiteral
   ;

recordLiteral
   : RECORD? LEFT_BRACE (recordFieldLiteral (COMMA recordFieldLiteral)*)? RIGHT_BRACE
   ;

recordFieldLiteral
   : key = variable COLON value = generalLiteral
   ;