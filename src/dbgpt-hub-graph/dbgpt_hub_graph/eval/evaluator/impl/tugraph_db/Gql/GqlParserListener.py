# Generated from GqlParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GqlParser import GqlParser
else:
    from GqlParser import GqlParser

# This class defines a complete listener for a parse tree produced by GqlParser.
class GqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by GqlParser#gqlRequest.
    def enterGqlRequest(self, ctx:GqlParser.GqlRequestContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlRequest.
    def exitGqlRequest(self, ctx:GqlParser.GqlRequestContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlProgram.
    def enterGqlProgram(self, ctx:GqlParser.GqlProgramContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlProgram.
    def exitGqlProgram(self, ctx:GqlParser.GqlProgramContext):
        pass


    # Enter a parse tree produced by GqlParser#programActivity.
    def enterProgramActivity(self, ctx:GqlParser.ProgramActivityContext):
        pass

    # Exit a parse tree produced by GqlParser#programActivity.
    def exitProgramActivity(self, ctx:GqlParser.ProgramActivityContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionActivity.
    def enterSessionActivity(self, ctx:GqlParser.SessionActivityContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionActivity.
    def exitSessionActivity(self, ctx:GqlParser.SessionActivityContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionActivityCommand.
    def enterSessionActivityCommand(self, ctx:GqlParser.SessionActivityCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionActivityCommand.
    def exitSessionActivityCommand(self, ctx:GqlParser.SessionActivityCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#transactionActivity.
    def enterTransactionActivity(self, ctx:GqlParser.TransactionActivityContext):
        pass

    # Exit a parse tree produced by GqlParser#transactionActivity.
    def exitTransactionActivity(self, ctx:GqlParser.TransactionActivityContext):
        pass


    # Enter a parse tree produced by GqlParser#endTransactionCommand.
    def enterEndTransactionCommand(self, ctx:GqlParser.EndTransactionCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#endTransactionCommand.
    def exitEndTransactionCommand(self, ctx:GqlParser.EndTransactionCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetCommand.
    def enterSessionSetCommand(self, ctx:GqlParser.SessionSetCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetCommand.
    def exitSessionSetCommand(self, ctx:GqlParser.SessionSetCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetSchemaClause.
    def enterSessionSetSchemaClause(self, ctx:GqlParser.SessionSetSchemaClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetSchemaClause.
    def exitSessionSetSchemaClause(self, ctx:GqlParser.SessionSetSchemaClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetGraphClause.
    def enterSessionSetGraphClause(self, ctx:GqlParser.SessionSetGraphClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetGraphClause.
    def exitSessionSetGraphClause(self, ctx:GqlParser.SessionSetGraphClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetTimeZoneClause.
    def enterSessionSetTimeZoneClause(self, ctx:GqlParser.SessionSetTimeZoneClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetTimeZoneClause.
    def exitSessionSetTimeZoneClause(self, ctx:GqlParser.SessionSetTimeZoneClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#setTimeZoneValue.
    def enterSetTimeZoneValue(self, ctx:GqlParser.SetTimeZoneValueContext):
        pass

    # Exit a parse tree produced by GqlParser#setTimeZoneValue.
    def exitSetTimeZoneValue(self, ctx:GqlParser.SetTimeZoneValueContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetParameterClause.
    def enterSessionSetParameterClause(self, ctx:GqlParser.SessionSetParameterClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetParameterClause.
    def exitSessionSetParameterClause(self, ctx:GqlParser.SessionSetParameterClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetGraphParameterClause.
    def enterSessionSetGraphParameterClause(self, ctx:GqlParser.SessionSetGraphParameterClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetGraphParameterClause.
    def exitSessionSetGraphParameterClause(self, ctx:GqlParser.SessionSetGraphParameterClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetBindingTableParameterClause.
    def enterSessionSetBindingTableParameterClause(self, ctx:GqlParser.SessionSetBindingTableParameterClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetBindingTableParameterClause.
    def exitSessionSetBindingTableParameterClause(self, ctx:GqlParser.SessionSetBindingTableParameterClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetValueParameterClause.
    def enterSessionSetValueParameterClause(self, ctx:GqlParser.SessionSetValueParameterClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetValueParameterClause.
    def exitSessionSetValueParameterClause(self, ctx:GqlParser.SessionSetValueParameterClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionSetParameterName.
    def enterSessionSetParameterName(self, ctx:GqlParser.SessionSetParameterNameContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionSetParameterName.
    def exitSessionSetParameterName(self, ctx:GqlParser.SessionSetParameterNameContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionResetCommand.
    def enterSessionResetCommand(self, ctx:GqlParser.SessionResetCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionResetCommand.
    def exitSessionResetCommand(self, ctx:GqlParser.SessionResetCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionResetArguments.
    def enterSessionResetArguments(self, ctx:GqlParser.SessionResetArgumentsContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionResetArguments.
    def exitSessionResetArguments(self, ctx:GqlParser.SessionResetArgumentsContext):
        pass


    # Enter a parse tree produced by GqlParser#sessionCloseCommand.
    def enterSessionCloseCommand(self, ctx:GqlParser.SessionCloseCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#sessionCloseCommand.
    def exitSessionCloseCommand(self, ctx:GqlParser.SessionCloseCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#startTransactionCommand.
    def enterStartTransactionCommand(self, ctx:GqlParser.StartTransactionCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#startTransactionCommand.
    def exitStartTransactionCommand(self, ctx:GqlParser.StartTransactionCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#transactionCharacteristics.
    def enterTransactionCharacteristics(self, ctx:GqlParser.TransactionCharacteristicsContext):
        pass

    # Exit a parse tree produced by GqlParser#transactionCharacteristics.
    def exitTransactionCharacteristics(self, ctx:GqlParser.TransactionCharacteristicsContext):
        pass


    # Enter a parse tree produced by GqlParser#transactionMode.
    def enterTransactionMode(self, ctx:GqlParser.TransactionModeContext):
        pass

    # Exit a parse tree produced by GqlParser#transactionMode.
    def exitTransactionMode(self, ctx:GqlParser.TransactionModeContext):
        pass


    # Enter a parse tree produced by GqlParser#transactionAccessMode.
    def enterTransactionAccessMode(self, ctx:GqlParser.TransactionAccessModeContext):
        pass

    # Exit a parse tree produced by GqlParser#transactionAccessMode.
    def exitTransactionAccessMode(self, ctx:GqlParser.TransactionAccessModeContext):
        pass


    # Enter a parse tree produced by GqlParser#implementationDefinedAccessMode.
    def enterImplementationDefinedAccessMode(self, ctx:GqlParser.ImplementationDefinedAccessModeContext):
        pass

    # Exit a parse tree produced by GqlParser#implementationDefinedAccessMode.
    def exitImplementationDefinedAccessMode(self, ctx:GqlParser.ImplementationDefinedAccessModeContext):
        pass


    # Enter a parse tree produced by GqlParser#rollbackCommand.
    def enterRollbackCommand(self, ctx:GqlParser.RollbackCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#rollbackCommand.
    def exitRollbackCommand(self, ctx:GqlParser.RollbackCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#commitCommand.
    def enterCommitCommand(self, ctx:GqlParser.CommitCommandContext):
        pass

    # Exit a parse tree produced by GqlParser#commitCommand.
    def exitCommitCommand(self, ctx:GqlParser.CommitCommandContext):
        pass


    # Enter a parse tree produced by GqlParser#nestedProcedureSpecification.
    def enterNestedProcedureSpecification(self, ctx:GqlParser.NestedProcedureSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#nestedProcedureSpecification.
    def exitNestedProcedureSpecification(self, ctx:GqlParser.NestedProcedureSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#procedureSpecification.
    def enterProcedureSpecification(self, ctx:GqlParser.ProcedureSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#procedureSpecification.
    def exitProcedureSpecification(self, ctx:GqlParser.ProcedureSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#catalogModifyingProcedureSpecification.
    def enterCatalogModifyingProcedureSpecification(self, ctx:GqlParser.CatalogModifyingProcedureSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#catalogModifyingProcedureSpecification.
    def exitCatalogModifyingProcedureSpecification(self, ctx:GqlParser.CatalogModifyingProcedureSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#nestedDataModifyingProcedureSpecification.
    def enterNestedDataModifyingProcedureSpecification(self, ctx:GqlParser.NestedDataModifyingProcedureSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#nestedDataModifyingProcedureSpecification.
    def exitNestedDataModifyingProcedureSpecification(self, ctx:GqlParser.NestedDataModifyingProcedureSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#dataModifyingProcedureSpecification.
    def enterDataModifyingProcedureSpecification(self, ctx:GqlParser.DataModifyingProcedureSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#dataModifyingProcedureSpecification.
    def exitDataModifyingProcedureSpecification(self, ctx:GqlParser.DataModifyingProcedureSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#nestedQuerySpecification.
    def enterNestedQuerySpecification(self, ctx:GqlParser.NestedQuerySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#nestedQuerySpecification.
    def exitNestedQuerySpecification(self, ctx:GqlParser.NestedQuerySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#querySpecification.
    def enterQuerySpecification(self, ctx:GqlParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#querySpecification.
    def exitQuerySpecification(self, ctx:GqlParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#unsignedNumericLiteral.
    def enterUnsignedNumericLiteral(self, ctx:GqlParser.UnsignedNumericLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#unsignedNumericLiteral.
    def exitUnsignedNumericLiteral(self, ctx:GqlParser.UnsignedNumericLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:GqlParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:GqlParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#floatLiteral.
    def enterFloatLiteral(self, ctx:GqlParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#floatLiteral.
    def exitFloatLiteral(self, ctx:GqlParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#singleQuotedCharacterSequence.
    def enterSingleQuotedCharacterSequence(self, ctx:GqlParser.SingleQuotedCharacterSequenceContext):
        pass

    # Exit a parse tree produced by GqlParser#singleQuotedCharacterSequence.
    def exitSingleQuotedCharacterSequence(self, ctx:GqlParser.SingleQuotedCharacterSequenceContext):
        pass


    # Enter a parse tree produced by GqlParser#doubleQuotedCharacterSequence.
    def enterDoubleQuotedCharacterSequence(self, ctx:GqlParser.DoubleQuotedCharacterSequenceContext):
        pass

    # Exit a parse tree produced by GqlParser#doubleQuotedCharacterSequence.
    def exitDoubleQuotedCharacterSequence(self, ctx:GqlParser.DoubleQuotedCharacterSequenceContext):
        pass


    # Enter a parse tree produced by GqlParser#accentQuotedCharacterSequence.
    def enterAccentQuotedCharacterSequence(self, ctx:GqlParser.AccentQuotedCharacterSequenceContext):
        pass

    # Exit a parse tree produced by GqlParser#accentQuotedCharacterSequence.
    def exitAccentQuotedCharacterSequence(self, ctx:GqlParser.AccentQuotedCharacterSequenceContext):
        pass


    # Enter a parse tree produced by GqlParser#nullLiteral.
    def enterNullLiteral(self, ctx:GqlParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#nullLiteral.
    def exitNullLiteral(self, ctx:GqlParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#temporalLiteral.
    def enterTemporalLiteral(self, ctx:GqlParser.TemporalLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#temporalLiteral.
    def exitTemporalLiteral(self, ctx:GqlParser.TemporalLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#sqlDatetimeLiteral.
    def enterSqlDatetimeLiteral(self, ctx:GqlParser.SqlDatetimeLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#sqlDatetimeLiteral.
    def exitSqlDatetimeLiteral(self, ctx:GqlParser.SqlDatetimeLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#dateLiteral.
    def enterDateLiteral(self, ctx:GqlParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#dateLiteral.
    def exitDateLiteral(self, ctx:GqlParser.DateLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#timeLiteral.
    def enterTimeLiteral(self, ctx:GqlParser.TimeLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#timeLiteral.
    def exitTimeLiteral(self, ctx:GqlParser.TimeLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#datetimeLiteral.
    def enterDatetimeLiteral(self, ctx:GqlParser.DatetimeLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#datetimeLiteral.
    def exitDatetimeLiteral(self, ctx:GqlParser.DatetimeLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#durationLiteral.
    def enterDurationLiteral(self, ctx:GqlParser.DurationLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#durationLiteral.
    def exitDurationLiteral(self, ctx:GqlParser.DurationLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#sqlIntervalLiteral.
    def enterSqlIntervalLiteral(self, ctx:GqlParser.SqlIntervalLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#sqlIntervalLiteral.
    def exitSqlIntervalLiteral(self, ctx:GqlParser.SqlIntervalLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#sqlIntervalType.
    def enterSqlIntervalType(self, ctx:GqlParser.SqlIntervalTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#sqlIntervalType.
    def exitSqlIntervalType(self, ctx:GqlParser.SqlIntervalTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#identifier.
    def enterIdentifier(self, ctx:GqlParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GqlParser#identifier.
    def exitIdentifier(self, ctx:GqlParser.IdentifierContext):
        pass


    # Enter a parse tree produced by GqlParser#keyWord.
    def enterKeyWord(self, ctx:GqlParser.KeyWordContext):
        pass

    # Exit a parse tree produced by GqlParser#keyWord.
    def exitKeyWord(self, ctx:GqlParser.KeyWordContext):
        pass


    # Enter a parse tree produced by GqlParser#reservedWord.
    def enterReservedWord(self, ctx:GqlParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by GqlParser#reservedWord.
    def exitReservedWord(self, ctx:GqlParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by GqlParser#preReservedWord.
    def enterPreReservedWord(self, ctx:GqlParser.PreReservedWordContext):
        pass

    # Exit a parse tree produced by GqlParser#preReservedWord.
    def exitPreReservedWord(self, ctx:GqlParser.PreReservedWordContext):
        pass


    # Enter a parse tree produced by GqlParser#nonReservedWord.
    def enterNonReservedWord(self, ctx:GqlParser.NonReservedWordContext):
        pass

    # Exit a parse tree produced by GqlParser#nonReservedWord.
    def exitNonReservedWord(self, ctx:GqlParser.NonReservedWordContext):
        pass


    # Enter a parse tree produced by GqlParser#delimitedIdentifier.
    def enterDelimitedIdentifier(self, ctx:GqlParser.DelimitedIdentifierContext):
        pass

    # Exit a parse tree produced by GqlParser#delimitedIdentifier.
    def exitDelimitedIdentifier(self, ctx:GqlParser.DelimitedIdentifierContext):
        pass


    # Enter a parse tree produced by GqlParser#objectName.
    def enterObjectName(self, ctx:GqlParser.ObjectNameContext):
        pass

    # Exit a parse tree produced by GqlParser#objectName.
    def exitObjectName(self, ctx:GqlParser.ObjectNameContext):
        pass


    # Enter a parse tree produced by GqlParser#objectNameOrBindingVariable.
    def enterObjectNameOrBindingVariable(self, ctx:GqlParser.ObjectNameOrBindingVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#objectNameOrBindingVariable.
    def exitObjectNameOrBindingVariable(self, ctx:GqlParser.ObjectNameOrBindingVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#directoryName.
    def enterDirectoryName(self, ctx:GqlParser.DirectoryNameContext):
        pass

    # Exit a parse tree produced by GqlParser#directoryName.
    def exitDirectoryName(self, ctx:GqlParser.DirectoryNameContext):
        pass


    # Enter a parse tree produced by GqlParser#schemaName.
    def enterSchemaName(self, ctx:GqlParser.SchemaNameContext):
        pass

    # Exit a parse tree produced by GqlParser#schemaName.
    def exitSchemaName(self, ctx:GqlParser.SchemaNameContext):
        pass


    # Enter a parse tree produced by GqlParser#graphName.
    def enterGraphName(self, ctx:GqlParser.GraphNameContext):
        pass

    # Exit a parse tree produced by GqlParser#graphName.
    def exitGraphName(self, ctx:GqlParser.GraphNameContext):
        pass


    # Enter a parse tree produced by GqlParser#delimitedGraphName.
    def enterDelimitedGraphName(self, ctx:GqlParser.DelimitedGraphNameContext):
        pass

    # Exit a parse tree produced by GqlParser#delimitedGraphName.
    def exitDelimitedGraphName(self, ctx:GqlParser.DelimitedGraphNameContext):
        pass


    # Enter a parse tree produced by GqlParser#graphTypeName.
    def enterGraphTypeName(self, ctx:GqlParser.GraphTypeNameContext):
        pass

    # Exit a parse tree produced by GqlParser#graphTypeName.
    def exitGraphTypeName(self, ctx:GqlParser.GraphTypeNameContext):
        pass


    # Enter a parse tree produced by GqlParser#elementTypeName.
    def enterElementTypeName(self, ctx:GqlParser.ElementTypeNameContext):
        pass

    # Exit a parse tree produced by GqlParser#elementTypeName.
    def exitElementTypeName(self, ctx:GqlParser.ElementTypeNameContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableName.
    def enterBindingTableName(self, ctx:GqlParser.BindingTableNameContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableName.
    def exitBindingTableName(self, ctx:GqlParser.BindingTableNameContext):
        pass


    # Enter a parse tree produced by GqlParser#delimitedBindingTableName.
    def enterDelimitedBindingTableName(self, ctx:GqlParser.DelimitedBindingTableNameContext):
        pass

    # Exit a parse tree produced by GqlParser#delimitedBindingTableName.
    def exitDelimitedBindingTableName(self, ctx:GqlParser.DelimitedBindingTableNameContext):
        pass


    # Enter a parse tree produced by GqlParser#procedureName.
    def enterProcedureName(self, ctx:GqlParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by GqlParser#procedureName.
    def exitProcedureName(self, ctx:GqlParser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by GqlParser#labelName.
    def enterLabelName(self, ctx:GqlParser.LabelNameContext):
        pass

    # Exit a parse tree produced by GqlParser#labelName.
    def exitLabelName(self, ctx:GqlParser.LabelNameContext):
        pass


    # Enter a parse tree produced by GqlParser#functionName.
    def enterFunctionName(self, ctx:GqlParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by GqlParser#functionName.
    def exitFunctionName(self, ctx:GqlParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyName.
    def enterPropertyName(self, ctx:GqlParser.PropertyNameContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyName.
    def exitPropertyName(self, ctx:GqlParser.PropertyNameContext):
        pass


    # Enter a parse tree produced by GqlParser#fieldName.
    def enterFieldName(self, ctx:GqlParser.FieldNameContext):
        pass

    # Exit a parse tree produced by GqlParser#fieldName.
    def exitFieldName(self, ctx:GqlParser.FieldNameContext):
        pass


    # Enter a parse tree produced by GqlParser#parameterName.
    def enterParameterName(self, ctx:GqlParser.ParameterNameContext):
        pass

    # Exit a parse tree produced by GqlParser#parameterName.
    def exitParameterName(self, ctx:GqlParser.ParameterNameContext):
        pass


    # Enter a parse tree produced by GqlParser#variable.
    def enterVariable(self, ctx:GqlParser.VariableContext):
        pass

    # Exit a parse tree produced by GqlParser#variable.
    def exitVariable(self, ctx:GqlParser.VariableContext):
        pass


    # Enter a parse tree produced by GqlParser#graphVariable.
    def enterGraphVariable(self, ctx:GqlParser.GraphVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#graphVariable.
    def exitGraphVariable(self, ctx:GqlParser.GraphVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#graphPatternVariable.
    def enterGraphPatternVariable(self, ctx:GqlParser.GraphPatternVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#graphPatternVariable.
    def exitGraphPatternVariable(self, ctx:GqlParser.GraphPatternVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#pathOrSubpathVariable.
    def enterPathOrSubpathVariable(self, ctx:GqlParser.PathOrSubpathVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#pathOrSubpathVariable.
    def exitPathOrSubpathVariable(self, ctx:GqlParser.PathOrSubpathVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#elementVariable.
    def enterElementVariable(self, ctx:GqlParser.ElementVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#elementVariable.
    def exitElementVariable(self, ctx:GqlParser.ElementVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#pathVariable.
    def enterPathVariable(self, ctx:GqlParser.PathVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#pathVariable.
    def exitPathVariable(self, ctx:GqlParser.PathVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#subpathVariable.
    def enterSubpathVariable(self, ctx:GqlParser.SubpathVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#subpathVariable.
    def exitSubpathVariable(self, ctx:GqlParser.SubpathVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableVariable.
    def enterBindingTableVariable(self, ctx:GqlParser.BindingTableVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableVariable.
    def exitBindingTableVariable(self, ctx:GqlParser.BindingTableVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#valueVariable.
    def enterValueVariable(self, ctx:GqlParser.ValueVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#valueVariable.
    def exitValueVariable(self, ctx:GqlParser.ValueVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingVariable.
    def enterBindingVariable(self, ctx:GqlParser.BindingVariableContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingVariable.
    def exitBindingVariable(self, ctx:GqlParser.BindingVariableContext):
        pass


    # Enter a parse tree produced by GqlParser#predefinedTypeLiteral.
    def enterPredefinedTypeLiteral(self, ctx:GqlParser.PredefinedTypeLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#predefinedTypeLiteral.
    def exitPredefinedTypeLiteral(self, ctx:GqlParser.PredefinedTypeLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:GqlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:GqlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#characterStringLiteral.
    def enterCharacterStringLiteral(self, ctx:GqlParser.CharacterStringLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#characterStringLiteral.
    def exitCharacterStringLiteral(self, ctx:GqlParser.CharacterStringLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#byteStringLiteral.
    def enterByteStringLiteral(self, ctx:GqlParser.ByteStringLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#byteStringLiteral.
    def exitByteStringLiteral(self, ctx:GqlParser.ByteStringLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#procedureBody.
    def enterProcedureBody(self, ctx:GqlParser.ProcedureBodyContext):
        pass

    # Exit a parse tree produced by GqlParser#procedureBody.
    def exitProcedureBody(self, ctx:GqlParser.ProcedureBodyContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingVariableDefinitionBlock.
    def enterBindingVariableDefinitionBlock(self, ctx:GqlParser.BindingVariableDefinitionBlockContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingVariableDefinitionBlock.
    def exitBindingVariableDefinitionBlock(self, ctx:GqlParser.BindingVariableDefinitionBlockContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingVariableDefinition.
    def enterBindingVariableDefinition(self, ctx:GqlParser.BindingVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingVariableDefinition.
    def exitBindingVariableDefinition(self, ctx:GqlParser.BindingVariableDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#statementBlock.
    def enterStatementBlock(self, ctx:GqlParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by GqlParser#statementBlock.
    def exitStatementBlock(self, ctx:GqlParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by GqlParser#statement.
    def enterStatement(self, ctx:GqlParser.StatementContext):
        pass

    # Exit a parse tree produced by GqlParser#statement.
    def exitStatement(self, ctx:GqlParser.StatementContext):
        pass


    # Enter a parse tree produced by GqlParser#nextStatement.
    def enterNextStatement(self, ctx:GqlParser.NextStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#nextStatement.
    def exitNextStatement(self, ctx:GqlParser.NextStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#graphVariableDefinition.
    def enterGraphVariableDefinition(self, ctx:GqlParser.GraphVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#graphVariableDefinition.
    def exitGraphVariableDefinition(self, ctx:GqlParser.GraphVariableDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#optTypedGraphInitializer.
    def enterOptTypedGraphInitializer(self, ctx:GqlParser.OptTypedGraphInitializerContext):
        pass

    # Exit a parse tree produced by GqlParser#optTypedGraphInitializer.
    def exitOptTypedGraphInitializer(self, ctx:GqlParser.OptTypedGraphInitializerContext):
        pass


    # Enter a parse tree produced by GqlParser#graphInitializer.
    def enterGraphInitializer(self, ctx:GqlParser.GraphInitializerContext):
        pass

    # Exit a parse tree produced by GqlParser#graphInitializer.
    def exitGraphInitializer(self, ctx:GqlParser.GraphInitializerContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableVariableDefinition.
    def enterBindingTableVariableDefinition(self, ctx:GqlParser.BindingTableVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableVariableDefinition.
    def exitBindingTableVariableDefinition(self, ctx:GqlParser.BindingTableVariableDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#optTypedBindingTableInitializer.
    def enterOptTypedBindingTableInitializer(self, ctx:GqlParser.OptTypedBindingTableInitializerContext):
        pass

    # Exit a parse tree produced by GqlParser#optTypedBindingTableInitializer.
    def exitOptTypedBindingTableInitializer(self, ctx:GqlParser.OptTypedBindingTableInitializerContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableInitializer.
    def enterBindingTableInitializer(self, ctx:GqlParser.BindingTableInitializerContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableInitializer.
    def exitBindingTableInitializer(self, ctx:GqlParser.BindingTableInitializerContext):
        pass


    # Enter a parse tree produced by GqlParser#valueVariableDefinition.
    def enterValueVariableDefinition(self, ctx:GqlParser.ValueVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#valueVariableDefinition.
    def exitValueVariableDefinition(self, ctx:GqlParser.ValueVariableDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#optTypedValueInitializer.
    def enterOptTypedValueInitializer(self, ctx:GqlParser.OptTypedValueInitializerContext):
        pass

    # Exit a parse tree produced by GqlParser#optTypedValueInitializer.
    def exitOptTypedValueInitializer(self, ctx:GqlParser.OptTypedValueInitializerContext):
        pass


    # Enter a parse tree produced by GqlParser#graphExpression.
    def enterGraphExpression(self, ctx:GqlParser.GraphExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#graphExpression.
    def exitGraphExpression(self, ctx:GqlParser.GraphExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#currentGraph.
    def enterCurrentGraph(self, ctx:GqlParser.CurrentGraphContext):
        pass

    # Exit a parse tree produced by GqlParser#currentGraph.
    def exitCurrentGraph(self, ctx:GqlParser.CurrentGraphContext):
        pass


    # Enter a parse tree produced by GqlParser#nestedGraphQuerySpecification.
    def enterNestedGraphQuerySpecification(self, ctx:GqlParser.NestedGraphQuerySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#nestedGraphQuerySpecification.
    def exitNestedGraphQuerySpecification(self, ctx:GqlParser.NestedGraphQuerySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableExpression.
    def enterBindingTableExpression(self, ctx:GqlParser.BindingTableExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableExpression.
    def exitBindingTableExpression(self, ctx:GqlParser.BindingTableExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#nestedBindingTableQuerySpecification.
    def enterNestedBindingTableQuerySpecification(self, ctx:GqlParser.NestedBindingTableQuerySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#nestedBindingTableQuerySpecification.
    def exitNestedBindingTableQuerySpecification(self, ctx:GqlParser.NestedBindingTableQuerySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#objectExpressionPrimary.
    def enterObjectExpressionPrimary(self, ctx:GqlParser.ObjectExpressionPrimaryContext):
        pass

    # Exit a parse tree produced by GqlParser#objectExpressionPrimary.
    def exitObjectExpressionPrimary(self, ctx:GqlParser.ObjectExpressionPrimaryContext):
        pass


    # Enter a parse tree produced by GqlParser#linearCatalogModifyingStatement.
    def enterLinearCatalogModifyingStatement(self, ctx:GqlParser.LinearCatalogModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#linearCatalogModifyingStatement.
    def exitLinearCatalogModifyingStatement(self, ctx:GqlParser.LinearCatalogModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleCatalogModifyingStatement.
    def enterSimpleCatalogModifyingStatement(self, ctx:GqlParser.SimpleCatalogModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleCatalogModifyingStatement.
    def exitSimpleCatalogModifyingStatement(self, ctx:GqlParser.SimpleCatalogModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#primitiveCatalogModifyingStatement.
    def enterPrimitiveCatalogModifyingStatement(self, ctx:GqlParser.PrimitiveCatalogModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#primitiveCatalogModifyingStatement.
    def exitPrimitiveCatalogModifyingStatement(self, ctx:GqlParser.PrimitiveCatalogModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#createSchemaStatement.
    def enterCreateSchemaStatement(self, ctx:GqlParser.CreateSchemaStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#createSchemaStatement.
    def exitCreateSchemaStatement(self, ctx:GqlParser.CreateSchemaStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#dropSchemaStatement.
    def enterDropSchemaStatement(self, ctx:GqlParser.DropSchemaStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#dropSchemaStatement.
    def exitDropSchemaStatement(self, ctx:GqlParser.DropSchemaStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#createGraphStatement.
    def enterCreateGraphStatement(self, ctx:GqlParser.CreateGraphStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#createGraphStatement.
    def exitCreateGraphStatement(self, ctx:GqlParser.CreateGraphStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#openGraphType.
    def enterOpenGraphType(self, ctx:GqlParser.OpenGraphTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#openGraphType.
    def exitOpenGraphType(self, ctx:GqlParser.OpenGraphTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#ofGraphType.
    def enterOfGraphType(self, ctx:GqlParser.OfGraphTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#ofGraphType.
    def exitOfGraphType(self, ctx:GqlParser.OfGraphTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#graphTypeLikeGraph.
    def enterGraphTypeLikeGraph(self, ctx:GqlParser.GraphTypeLikeGraphContext):
        pass

    # Exit a parse tree produced by GqlParser#graphTypeLikeGraph.
    def exitGraphTypeLikeGraph(self, ctx:GqlParser.GraphTypeLikeGraphContext):
        pass


    # Enter a parse tree produced by GqlParser#graphSource.
    def enterGraphSource(self, ctx:GqlParser.GraphSourceContext):
        pass

    # Exit a parse tree produced by GqlParser#graphSource.
    def exitGraphSource(self, ctx:GqlParser.GraphSourceContext):
        pass


    # Enter a parse tree produced by GqlParser#dropGraphStatement.
    def enterDropGraphStatement(self, ctx:GqlParser.DropGraphStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#dropGraphStatement.
    def exitDropGraphStatement(self, ctx:GqlParser.DropGraphStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#createGraphTypeStatement.
    def enterCreateGraphTypeStatement(self, ctx:GqlParser.CreateGraphTypeStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#createGraphTypeStatement.
    def exitCreateGraphTypeStatement(self, ctx:GqlParser.CreateGraphTypeStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#graphTypeSource.
    def enterGraphTypeSource(self, ctx:GqlParser.GraphTypeSourceContext):
        pass

    # Exit a parse tree produced by GqlParser#graphTypeSource.
    def exitGraphTypeSource(self, ctx:GqlParser.GraphTypeSourceContext):
        pass


    # Enter a parse tree produced by GqlParser#copyOfGraphType.
    def enterCopyOfGraphType(self, ctx:GqlParser.CopyOfGraphTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#copyOfGraphType.
    def exitCopyOfGraphType(self, ctx:GqlParser.CopyOfGraphTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#dropGraphTypeStatement.
    def enterDropGraphTypeStatement(self, ctx:GqlParser.DropGraphTypeStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#dropGraphTypeStatement.
    def exitDropGraphTypeStatement(self, ctx:GqlParser.DropGraphTypeStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#callCatalogModifyingProcedureStatement.
    def enterCallCatalogModifyingProcedureStatement(self, ctx:GqlParser.CallCatalogModifyingProcedureStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#callCatalogModifyingProcedureStatement.
    def exitCallCatalogModifyingProcedureStatement(self, ctx:GqlParser.CallCatalogModifyingProcedureStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#linearDataModifyingStatement.
    def enterLinearDataModifyingStatement(self, ctx:GqlParser.LinearDataModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#linearDataModifyingStatement.
    def exitLinearDataModifyingStatement(self, ctx:GqlParser.LinearDataModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedLinearDataModifyingStatement.
    def enterFocusedLinearDataModifyingStatement(self, ctx:GqlParser.FocusedLinearDataModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedLinearDataModifyingStatement.
    def exitFocusedLinearDataModifyingStatement(self, ctx:GqlParser.FocusedLinearDataModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedLinearDataModifyingStatementBody.
    def enterFocusedLinearDataModifyingStatementBody(self, ctx:GqlParser.FocusedLinearDataModifyingStatementBodyContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedLinearDataModifyingStatementBody.
    def exitFocusedLinearDataModifyingStatementBody(self, ctx:GqlParser.FocusedLinearDataModifyingStatementBodyContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedNestedDataModifyingProcedureSpecification.
    def enterFocusedNestedDataModifyingProcedureSpecification(self, ctx:GqlParser.FocusedNestedDataModifyingProcedureSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedNestedDataModifyingProcedureSpecification.
    def exitFocusedNestedDataModifyingProcedureSpecification(self, ctx:GqlParser.FocusedNestedDataModifyingProcedureSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#ambientLinearDataModifyingStatement.
    def enterAmbientLinearDataModifyingStatement(self, ctx:GqlParser.AmbientLinearDataModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#ambientLinearDataModifyingStatement.
    def exitAmbientLinearDataModifyingStatement(self, ctx:GqlParser.AmbientLinearDataModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#ambientLinearDataModifyingStatementBody.
    def enterAmbientLinearDataModifyingStatementBody(self, ctx:GqlParser.AmbientLinearDataModifyingStatementBodyContext):
        pass

    # Exit a parse tree produced by GqlParser#ambientLinearDataModifyingStatementBody.
    def exitAmbientLinearDataModifyingStatementBody(self, ctx:GqlParser.AmbientLinearDataModifyingStatementBodyContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleLinearDataAccessingStatement.
    def enterSimpleLinearDataAccessingStatement(self, ctx:GqlParser.SimpleLinearDataAccessingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleLinearDataAccessingStatement.
    def exitSimpleLinearDataAccessingStatement(self, ctx:GqlParser.SimpleLinearDataAccessingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleDataAccessingStatement.
    def enterSimpleDataAccessingStatement(self, ctx:GqlParser.SimpleDataAccessingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleDataAccessingStatement.
    def exitSimpleDataAccessingStatement(self, ctx:GqlParser.SimpleDataAccessingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleDataModifyingStatement.
    def enterSimpleDataModifyingStatement(self, ctx:GqlParser.SimpleDataModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleDataModifyingStatement.
    def exitSimpleDataModifyingStatement(self, ctx:GqlParser.SimpleDataModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#primitiveDataModifyingStatement.
    def enterPrimitiveDataModifyingStatement(self, ctx:GqlParser.PrimitiveDataModifyingStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#primitiveDataModifyingStatement.
    def exitPrimitiveDataModifyingStatement(self, ctx:GqlParser.PrimitiveDataModifyingStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#insertStatement.
    def enterInsertStatement(self, ctx:GqlParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#insertStatement.
    def exitInsertStatement(self, ctx:GqlParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#setStatement.
    def enterSetStatement(self, ctx:GqlParser.SetStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#setStatement.
    def exitSetStatement(self, ctx:GqlParser.SetStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#setItemList.
    def enterSetItemList(self, ctx:GqlParser.SetItemListContext):
        pass

    # Exit a parse tree produced by GqlParser#setItemList.
    def exitSetItemList(self, ctx:GqlParser.SetItemListContext):
        pass


    # Enter a parse tree produced by GqlParser#setItem.
    def enterSetItem(self, ctx:GqlParser.SetItemContext):
        pass

    # Exit a parse tree produced by GqlParser#setItem.
    def exitSetItem(self, ctx:GqlParser.SetItemContext):
        pass


    # Enter a parse tree produced by GqlParser#setPropertyItem.
    def enterSetPropertyItem(self, ctx:GqlParser.SetPropertyItemContext):
        pass

    # Exit a parse tree produced by GqlParser#setPropertyItem.
    def exitSetPropertyItem(self, ctx:GqlParser.SetPropertyItemContext):
        pass


    # Enter a parse tree produced by GqlParser#setAllPropertiesItem.
    def enterSetAllPropertiesItem(self, ctx:GqlParser.SetAllPropertiesItemContext):
        pass

    # Exit a parse tree produced by GqlParser#setAllPropertiesItem.
    def exitSetAllPropertiesItem(self, ctx:GqlParser.SetAllPropertiesItemContext):
        pass


    # Enter a parse tree produced by GqlParser#updatePropertiesItem.
    def enterUpdatePropertiesItem(self, ctx:GqlParser.UpdatePropertiesItemContext):
        pass

    # Exit a parse tree produced by GqlParser#updatePropertiesItem.
    def exitUpdatePropertiesItem(self, ctx:GqlParser.UpdatePropertiesItemContext):
        pass


    # Enter a parse tree produced by GqlParser#setLabelItem.
    def enterSetLabelItem(self, ctx:GqlParser.SetLabelItemContext):
        pass

    # Exit a parse tree produced by GqlParser#setLabelItem.
    def exitSetLabelItem(self, ctx:GqlParser.SetLabelItemContext):
        pass


    # Enter a parse tree produced by GqlParser#labelSetSpecification.
    def enterLabelSetSpecification(self, ctx:GqlParser.LabelSetSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#labelSetSpecification.
    def exitLabelSetSpecification(self, ctx:GqlParser.LabelSetSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#removeStatement.
    def enterRemoveStatement(self, ctx:GqlParser.RemoveStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#removeStatement.
    def exitRemoveStatement(self, ctx:GqlParser.RemoveStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#removeItemList.
    def enterRemoveItemList(self, ctx:GqlParser.RemoveItemListContext):
        pass

    # Exit a parse tree produced by GqlParser#removeItemList.
    def exitRemoveItemList(self, ctx:GqlParser.RemoveItemListContext):
        pass


    # Enter a parse tree produced by GqlParser#removeItem.
    def enterRemoveItem(self, ctx:GqlParser.RemoveItemContext):
        pass

    # Exit a parse tree produced by GqlParser#removeItem.
    def exitRemoveItem(self, ctx:GqlParser.RemoveItemContext):
        pass


    # Enter a parse tree produced by GqlParser#removePropertyItem.
    def enterRemovePropertyItem(self, ctx:GqlParser.RemovePropertyItemContext):
        pass

    # Exit a parse tree produced by GqlParser#removePropertyItem.
    def exitRemovePropertyItem(self, ctx:GqlParser.RemovePropertyItemContext):
        pass


    # Enter a parse tree produced by GqlParser#removeLabelItem.
    def enterRemoveLabelItem(self, ctx:GqlParser.RemoveLabelItemContext):
        pass

    # Exit a parse tree produced by GqlParser#removeLabelItem.
    def exitRemoveLabelItem(self, ctx:GqlParser.RemoveLabelItemContext):
        pass


    # Enter a parse tree produced by GqlParser#deleteStatement.
    def enterDeleteStatement(self, ctx:GqlParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#deleteStatement.
    def exitDeleteStatement(self, ctx:GqlParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#deleteItemList.
    def enterDeleteItemList(self, ctx:GqlParser.DeleteItemListContext):
        pass

    # Exit a parse tree produced by GqlParser#deleteItemList.
    def exitDeleteItemList(self, ctx:GqlParser.DeleteItemListContext):
        pass


    # Enter a parse tree produced by GqlParser#deleteItem.
    def enterDeleteItem(self, ctx:GqlParser.DeleteItemContext):
        pass

    # Exit a parse tree produced by GqlParser#deleteItem.
    def exitDeleteItem(self, ctx:GqlParser.DeleteItemContext):
        pass


    # Enter a parse tree produced by GqlParser#replaceStatement.
    def enterReplaceStatement(self, ctx:GqlParser.ReplaceStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#replaceStatement.
    def exitReplaceStatement(self, ctx:GqlParser.ReplaceStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#callDataModifyingProcedureStatement.
    def enterCallDataModifyingProcedureStatement(self, ctx:GqlParser.CallDataModifyingProcedureStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#callDataModifyingProcedureStatement.
    def exitCallDataModifyingProcedureStatement(self, ctx:GqlParser.CallDataModifyingProcedureStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#queryStatement.
    def enterQueryStatement(self, ctx:GqlParser.QueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#queryStatement.
    def exitQueryStatement(self, ctx:GqlParser.QueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#joinQueryExpression.
    def enterJoinQueryExpression(self, ctx:GqlParser.JoinQueryExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#joinQueryExpression.
    def exitJoinQueryExpression(self, ctx:GqlParser.JoinQueryExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#joinRightPart.
    def enterJoinRightPart(self, ctx:GqlParser.JoinRightPartContext):
        pass

    # Exit a parse tree produced by GqlParser#joinRightPart.
    def exitJoinRightPart(self, ctx:GqlParser.JoinRightPartContext):
        pass


    # Enter a parse tree produced by GqlParser#compositeQueryStatement.
    def enterCompositeQueryStatement(self, ctx:GqlParser.CompositeQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#compositeQueryStatement.
    def exitCompositeQueryStatement(self, ctx:GqlParser.CompositeQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#managerStatement.
    def enterManagerStatement(self, ctx:GqlParser.ManagerStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#managerStatement.
    def exitManagerStatement(self, ctx:GqlParser.ManagerStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#killMode.
    def enterKillMode(self, ctx:GqlParser.KillModeContext):
        pass

    # Exit a parse tree produced by GqlParser#killMode.
    def exitKillMode(self, ctx:GqlParser.KillModeContext):
        pass


    # Enter a parse tree produced by GqlParser#compositeQueryExpression.
    def enterCompositeQueryExpression(self, ctx:GqlParser.CompositeQueryExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#compositeQueryExpression.
    def exitCompositeQueryExpression(self, ctx:GqlParser.CompositeQueryExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#queryConjunction.
    def enterQueryConjunction(self, ctx:GqlParser.QueryConjunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#queryConjunction.
    def exitQueryConjunction(self, ctx:GqlParser.QueryConjunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#setOperator.
    def enterSetOperator(self, ctx:GqlParser.SetOperatorContext):
        pass

    # Exit a parse tree produced by GqlParser#setOperator.
    def exitSetOperator(self, ctx:GqlParser.SetOperatorContext):
        pass


    # Enter a parse tree produced by GqlParser#joinType.
    def enterJoinType(self, ctx:GqlParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#joinType.
    def exitJoinType(self, ctx:GqlParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#linearQueryStatement.
    def enterLinearQueryStatement(self, ctx:GqlParser.LinearQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#linearQueryStatement.
    def exitLinearQueryStatement(self, ctx:GqlParser.LinearQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedLinearQueryStatement.
    def enterFocusedLinearQueryStatement(self, ctx:GqlParser.FocusedLinearQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedLinearQueryStatement.
    def exitFocusedLinearQueryStatement(self, ctx:GqlParser.FocusedLinearQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedQueryStatement.
    def enterFocusedQueryStatement(self, ctx:GqlParser.FocusedQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedQueryStatement.
    def exitFocusedQueryStatement(self, ctx:GqlParser.FocusedQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedLinearQueryStatementPart.
    def enterFocusedLinearQueryStatementPart(self, ctx:GqlParser.FocusedLinearQueryStatementPartContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedLinearQueryStatementPart.
    def exitFocusedLinearQueryStatementPart(self, ctx:GqlParser.FocusedLinearQueryStatementPartContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedLinearQueryAndPrimitiveResultStatementPart.
    def enterFocusedLinearQueryAndPrimitiveResultStatementPart(self, ctx:GqlParser.FocusedLinearQueryAndPrimitiveResultStatementPartContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedLinearQueryAndPrimitiveResultStatementPart.
    def exitFocusedLinearQueryAndPrimitiveResultStatementPart(self, ctx:GqlParser.FocusedLinearQueryAndPrimitiveResultStatementPartContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedPrimitiveResultStatement.
    def enterFocusedPrimitiveResultStatement(self, ctx:GqlParser.FocusedPrimitiveResultStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedPrimitiveResultStatement.
    def exitFocusedPrimitiveResultStatement(self, ctx:GqlParser.FocusedPrimitiveResultStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#focusedNestedQuerySpecification.
    def enterFocusedNestedQuerySpecification(self, ctx:GqlParser.FocusedNestedQuerySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#focusedNestedQuerySpecification.
    def exitFocusedNestedQuerySpecification(self, ctx:GqlParser.FocusedNestedQuerySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#ambientLinearQueryStatement.
    def enterAmbientLinearQueryStatement(self, ctx:GqlParser.AmbientLinearQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#ambientLinearQueryStatement.
    def exitAmbientLinearQueryStatement(self, ctx:GqlParser.AmbientLinearQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleLinearQueryStatement.
    def enterSimpleLinearQueryStatement(self, ctx:GqlParser.SimpleLinearQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleLinearQueryStatement.
    def exitSimpleLinearQueryStatement(self, ctx:GqlParser.SimpleLinearQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleQueryStatement.
    def enterSimpleQueryStatement(self, ctx:GqlParser.SimpleQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleQueryStatement.
    def exitSimpleQueryStatement(self, ctx:GqlParser.SimpleQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#primitiveQueryStatement.
    def enterPrimitiveQueryStatement(self, ctx:GqlParser.PrimitiveQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#primitiveQueryStatement.
    def exitPrimitiveQueryStatement(self, ctx:GqlParser.PrimitiveQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#matchStatement.
    def enterMatchStatement(self, ctx:GqlParser.MatchStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#matchStatement.
    def exitMatchStatement(self, ctx:GqlParser.MatchStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleMatchStatement.
    def enterSimpleMatchStatement(self, ctx:GqlParser.SimpleMatchStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleMatchStatement.
    def exitSimpleMatchStatement(self, ctx:GqlParser.SimpleMatchStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#optionalMatchStatement.
    def enterOptionalMatchStatement(self, ctx:GqlParser.OptionalMatchStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#optionalMatchStatement.
    def exitOptionalMatchStatement(self, ctx:GqlParser.OptionalMatchStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#optionalOperand.
    def enterOptionalOperand(self, ctx:GqlParser.OptionalOperandContext):
        pass

    # Exit a parse tree produced by GqlParser#optionalOperand.
    def exitOptionalOperand(self, ctx:GqlParser.OptionalOperandContext):
        pass


    # Enter a parse tree produced by GqlParser#matchStatementBlock.
    def enterMatchStatementBlock(self, ctx:GqlParser.MatchStatementBlockContext):
        pass

    # Exit a parse tree produced by GqlParser#matchStatementBlock.
    def exitMatchStatementBlock(self, ctx:GqlParser.MatchStatementBlockContext):
        pass


    # Enter a parse tree produced by GqlParser#callQueryStatement.
    def enterCallQueryStatement(self, ctx:GqlParser.CallQueryStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#callQueryStatement.
    def exitCallQueryStatement(self, ctx:GqlParser.CallQueryStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#filterStatement.
    def enterFilterStatement(self, ctx:GqlParser.FilterStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#filterStatement.
    def exitFilterStatement(self, ctx:GqlParser.FilterStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#letStatement.
    def enterLetStatement(self, ctx:GqlParser.LetStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#letStatement.
    def exitLetStatement(self, ctx:GqlParser.LetStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#letVariableDefinitionList.
    def enterLetVariableDefinitionList(self, ctx:GqlParser.LetVariableDefinitionListContext):
        pass

    # Exit a parse tree produced by GqlParser#letVariableDefinitionList.
    def exitLetVariableDefinitionList(self, ctx:GqlParser.LetVariableDefinitionListContext):
        pass


    # Enter a parse tree produced by GqlParser#letVariableDefinition.
    def enterLetVariableDefinition(self, ctx:GqlParser.LetVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#letVariableDefinition.
    def exitLetVariableDefinition(self, ctx:GqlParser.LetVariableDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#forStatement.
    def enterForStatement(self, ctx:GqlParser.ForStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#forStatement.
    def exitForStatement(self, ctx:GqlParser.ForStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#forItem.
    def enterForItem(self, ctx:GqlParser.ForItemContext):
        pass

    # Exit a parse tree produced by GqlParser#forItem.
    def exitForItem(self, ctx:GqlParser.ForItemContext):
        pass


    # Enter a parse tree produced by GqlParser#forItemAlias.
    def enterForItemAlias(self, ctx:GqlParser.ForItemAliasContext):
        pass

    # Exit a parse tree produced by GqlParser#forItemAlias.
    def exitForItemAlias(self, ctx:GqlParser.ForItemAliasContext):
        pass


    # Enter a parse tree produced by GqlParser#forOrdinalityOrOffset.
    def enterForOrdinalityOrOffset(self, ctx:GqlParser.ForOrdinalityOrOffsetContext):
        pass

    # Exit a parse tree produced by GqlParser#forOrdinalityOrOffset.
    def exitForOrdinalityOrOffset(self, ctx:GqlParser.ForOrdinalityOrOffsetContext):
        pass


    # Enter a parse tree produced by GqlParser#orderByAndPageStatement.
    def enterOrderByAndPageStatement(self, ctx:GqlParser.OrderByAndPageStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#orderByAndPageStatement.
    def exitOrderByAndPageStatement(self, ctx:GqlParser.OrderByAndPageStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#primitiveResultStatement.
    def enterPrimitiveResultStatement(self, ctx:GqlParser.PrimitiveResultStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#primitiveResultStatement.
    def exitPrimitiveResultStatement(self, ctx:GqlParser.PrimitiveResultStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#returnStatement.
    def enterReturnStatement(self, ctx:GqlParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#returnStatement.
    def exitReturnStatement(self, ctx:GqlParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#returnStatementBody.
    def enterReturnStatementBody(self, ctx:GqlParser.ReturnStatementBodyContext):
        pass

    # Exit a parse tree produced by GqlParser#returnStatementBody.
    def exitReturnStatementBody(self, ctx:GqlParser.ReturnStatementBodyContext):
        pass


    # Enter a parse tree produced by GqlParser#returnItemList.
    def enterReturnItemList(self, ctx:GqlParser.ReturnItemListContext):
        pass

    # Exit a parse tree produced by GqlParser#returnItemList.
    def exitReturnItemList(self, ctx:GqlParser.ReturnItemListContext):
        pass


    # Enter a parse tree produced by GqlParser#returnItem.
    def enterReturnItem(self, ctx:GqlParser.ReturnItemContext):
        pass

    # Exit a parse tree produced by GqlParser#returnItem.
    def exitReturnItem(self, ctx:GqlParser.ReturnItemContext):
        pass


    # Enter a parse tree produced by GqlParser#hintItemlist.
    def enterHintItemlist(self, ctx:GqlParser.HintItemlistContext):
        pass

    # Exit a parse tree produced by GqlParser#hintItemlist.
    def exitHintItemlist(self, ctx:GqlParser.HintItemlistContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlReadConsistency.
    def enterGqlReadConsistency(self, ctx:GqlParser.GqlReadConsistencyContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlReadConsistency.
    def exitGqlReadConsistency(self, ctx:GqlParser.GqlReadConsistencyContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlAllowAnonymousTable.
    def enterGqlAllowAnonymousTable(self, ctx:GqlParser.GqlAllowAnonymousTableContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlAllowAnonymousTable.
    def exitGqlAllowAnonymousTable(self, ctx:GqlParser.GqlAllowAnonymousTableContext):
        pass


    # Enter a parse tree produced by GqlParser#constructGraphStatement.
    def enterConstructGraphStatement(self, ctx:GqlParser.ConstructGraphStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#constructGraphStatement.
    def exitConstructGraphStatement(self, ctx:GqlParser.ConstructGraphStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#constructElementList.
    def enterConstructElementList(self, ctx:GqlParser.ConstructElementListContext):
        pass

    # Exit a parse tree produced by GqlParser#constructElementList.
    def exitConstructElementList(self, ctx:GqlParser.ConstructElementListContext):
        pass


    # Enter a parse tree produced by GqlParser#constructElement.
    def enterConstructElement(self, ctx:GqlParser.ConstructElementContext):
        pass

    # Exit a parse tree produced by GqlParser#constructElement.
    def exitConstructElement(self, ctx:GqlParser.ConstructElementContext):
        pass


    # Enter a parse tree produced by GqlParser#currentElement.
    def enterCurrentElement(self, ctx:GqlParser.CurrentElementContext):
        pass

    # Exit a parse tree produced by GqlParser#currentElement.
    def exitCurrentElement(self, ctx:GqlParser.CurrentElementContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyList.
    def enterPropertyList(self, ctx:GqlParser.PropertyListContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyList.
    def exitPropertyList(self, ctx:GqlParser.PropertyListContext):
        pass


    # Enter a parse tree produced by GqlParser#newElement.
    def enterNewElement(self, ctx:GqlParser.NewElementContext):
        pass

    # Exit a parse tree produced by GqlParser#newElement.
    def exitNewElement(self, ctx:GqlParser.NewElementContext):
        pass


    # Enter a parse tree produced by GqlParser#newNode.
    def enterNewNode(self, ctx:GqlParser.NewNodeContext):
        pass

    # Exit a parse tree produced by GqlParser#newNode.
    def exitNewNode(self, ctx:GqlParser.NewNodeContext):
        pass


    # Enter a parse tree produced by GqlParser#newEdge.
    def enterNewEdge(self, ctx:GqlParser.NewEdgeContext):
        pass

    # Exit a parse tree produced by GqlParser#newEdge.
    def exitNewEdge(self, ctx:GqlParser.NewEdgeContext):
        pass


    # Enter a parse tree produced by GqlParser#constructElementPatternFiller.
    def enterConstructElementPatternFiller(self, ctx:GqlParser.ConstructElementPatternFillerContext):
        pass

    # Exit a parse tree produced by GqlParser#constructElementPatternFiller.
    def exitConstructElementPatternFiller(self, ctx:GqlParser.ConstructElementPatternFillerContext):
        pass


    # Enter a parse tree produced by GqlParser#constructEdgePattern.
    def enterConstructEdgePattern(self, ctx:GqlParser.ConstructEdgePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#constructEdgePattern.
    def exitConstructEdgePattern(self, ctx:GqlParser.ConstructEdgePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#constructEdgePointingRight.
    def enterConstructEdgePointingRight(self, ctx:GqlParser.ConstructEdgePointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#constructEdgePointingRight.
    def exitConstructEdgePointingRight(self, ctx:GqlParser.ConstructEdgePointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#constructEdgePointingLeft.
    def enterConstructEdgePointingLeft(self, ctx:GqlParser.ConstructEdgePointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#constructEdgePointingLeft.
    def exitConstructEdgePointingLeft(self, ctx:GqlParser.ConstructEdgePointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#constructEdgeAnyDirection.
    def enterConstructEdgeAnyDirection(self, ctx:GqlParser.ConstructEdgeAnyDirectionContext):
        pass

    # Exit a parse tree produced by GqlParser#constructEdgeAnyDirection.
    def exitConstructEdgeAnyDirection(self, ctx:GqlParser.ConstructEdgeAnyDirectionContext):
        pass


    # Enter a parse tree produced by GqlParser#primaryKey.
    def enterPrimaryKey(self, ctx:GqlParser.PrimaryKeyContext):
        pass

    # Exit a parse tree produced by GqlParser#primaryKey.
    def exitPrimaryKey(self, ctx:GqlParser.PrimaryKeyContext):
        pass


    # Enter a parse tree produced by GqlParser#constructElementPropertySpecification.
    def enterConstructElementPropertySpecification(self, ctx:GqlParser.ConstructElementPropertySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#constructElementPropertySpecification.
    def exitConstructElementPropertySpecification(self, ctx:GqlParser.ConstructElementPropertySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#extendElement.
    def enterExtendElement(self, ctx:GqlParser.ExtendElementContext):
        pass

    # Exit a parse tree produced by GqlParser#extendElement.
    def exitExtendElement(self, ctx:GqlParser.ExtendElementContext):
        pass


    # Enter a parse tree produced by GqlParser#startVar.
    def enterStartVar(self, ctx:GqlParser.StartVarContext):
        pass

    # Exit a parse tree produced by GqlParser#startVar.
    def exitStartVar(self, ctx:GqlParser.StartVarContext):
        pass


    # Enter a parse tree produced by GqlParser#endVar.
    def enterEndVar(self, ctx:GqlParser.EndVarContext):
        pass

    # Exit a parse tree produced by GqlParser#endVar.
    def exitEndVar(self, ctx:GqlParser.EndVarContext):
        pass


    # Enter a parse tree produced by GqlParser#selectStatement.
    def enterSelectStatement(self, ctx:GqlParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#selectStatement.
    def exitSelectStatement(self, ctx:GqlParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#selectItemList.
    def enterSelectItemList(self, ctx:GqlParser.SelectItemListContext):
        pass

    # Exit a parse tree produced by GqlParser#selectItemList.
    def exitSelectItemList(self, ctx:GqlParser.SelectItemListContext):
        pass


    # Enter a parse tree produced by GqlParser#selectItem.
    def enterSelectItem(self, ctx:GqlParser.SelectItemContext):
        pass

    # Exit a parse tree produced by GqlParser#selectItem.
    def exitSelectItem(self, ctx:GqlParser.SelectItemContext):
        pass


    # Enter a parse tree produced by GqlParser#havingClause.
    def enterHavingClause(self, ctx:GqlParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#havingClause.
    def exitHavingClause(self, ctx:GqlParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#selectStatementBody.
    def enterSelectStatementBody(self, ctx:GqlParser.SelectStatementBodyContext):
        pass

    # Exit a parse tree produced by GqlParser#selectStatementBody.
    def exitSelectStatementBody(self, ctx:GqlParser.SelectStatementBodyContext):
        pass


    # Enter a parse tree produced by GqlParser#selectGraphMatchList.
    def enterSelectGraphMatchList(self, ctx:GqlParser.SelectGraphMatchListContext):
        pass

    # Exit a parse tree produced by GqlParser#selectGraphMatchList.
    def exitSelectGraphMatchList(self, ctx:GqlParser.SelectGraphMatchListContext):
        pass


    # Enter a parse tree produced by GqlParser#selectGraphMatch.
    def enterSelectGraphMatch(self, ctx:GqlParser.SelectGraphMatchContext):
        pass

    # Exit a parse tree produced by GqlParser#selectGraphMatch.
    def exitSelectGraphMatch(self, ctx:GqlParser.SelectGraphMatchContext):
        pass


    # Enter a parse tree produced by GqlParser#selectQuerySpecification.
    def enterSelectQuerySpecification(self, ctx:GqlParser.SelectQuerySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#selectQuerySpecification.
    def exitSelectQuerySpecification(self, ctx:GqlParser.SelectQuerySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#callProcedureStatement.
    def enterCallProcedureStatement(self, ctx:GqlParser.CallProcedureStatementContext):
        pass

    # Exit a parse tree produced by GqlParser#callProcedureStatement.
    def exitCallProcedureStatement(self, ctx:GqlParser.CallProcedureStatementContext):
        pass


    # Enter a parse tree produced by GqlParser#procedureCall.
    def enterProcedureCall(self, ctx:GqlParser.ProcedureCallContext):
        pass

    # Exit a parse tree produced by GqlParser#procedureCall.
    def exitProcedureCall(self, ctx:GqlParser.ProcedureCallContext):
        pass


    # Enter a parse tree produced by GqlParser#inlineProcedureCall.
    def enterInlineProcedureCall(self, ctx:GqlParser.InlineProcedureCallContext):
        pass

    # Exit a parse tree produced by GqlParser#inlineProcedureCall.
    def exitInlineProcedureCall(self, ctx:GqlParser.InlineProcedureCallContext):
        pass


    # Enter a parse tree produced by GqlParser#variableScopeClause.
    def enterVariableScopeClause(self, ctx:GqlParser.VariableScopeClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#variableScopeClause.
    def exitVariableScopeClause(self, ctx:GqlParser.VariableScopeClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingVariableReferenceList.
    def enterBindingVariableReferenceList(self, ctx:GqlParser.BindingVariableReferenceListContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingVariableReferenceList.
    def exitBindingVariableReferenceList(self, ctx:GqlParser.BindingVariableReferenceListContext):
        pass


    # Enter a parse tree produced by GqlParser#namedProcedureCall.
    def enterNamedProcedureCall(self, ctx:GqlParser.NamedProcedureCallContext):
        pass

    # Exit a parse tree produced by GqlParser#namedProcedureCall.
    def exitNamedProcedureCall(self, ctx:GqlParser.NamedProcedureCallContext):
        pass


    # Enter a parse tree produced by GqlParser#procedureArgumentList.
    def enterProcedureArgumentList(self, ctx:GqlParser.ProcedureArgumentListContext):
        pass

    # Exit a parse tree produced by GqlParser#procedureArgumentList.
    def exitProcedureArgumentList(self, ctx:GqlParser.ProcedureArgumentListContext):
        pass


    # Enter a parse tree produced by GqlParser#procedureArgument.
    def enterProcedureArgument(self, ctx:GqlParser.ProcedureArgumentContext):
        pass

    # Exit a parse tree produced by GqlParser#procedureArgument.
    def exitProcedureArgument(self, ctx:GqlParser.ProcedureArgumentContext):
        pass


    # Enter a parse tree produced by GqlParser#useGraphClause.
    def enterUseGraphClause(self, ctx:GqlParser.UseGraphClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#useGraphClause.
    def exitUseGraphClause(self, ctx:GqlParser.UseGraphClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#atSchemaClause.
    def enterAtSchemaClause(self, ctx:GqlParser.AtSchemaClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#atSchemaClause.
    def exitAtSchemaClause(self, ctx:GqlParser.AtSchemaClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingVariableReference.
    def enterBindingVariableReference(self, ctx:GqlParser.BindingVariableReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingVariableReference.
    def exitBindingVariableReference(self, ctx:GqlParser.BindingVariableReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#elementVariableReference.
    def enterElementVariableReference(self, ctx:GqlParser.ElementVariableReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#elementVariableReference.
    def exitElementVariableReference(self, ctx:GqlParser.ElementVariableReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#pathVariableReference.
    def enterPathVariableReference(self, ctx:GqlParser.PathVariableReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#pathVariableReference.
    def exitPathVariableReference(self, ctx:GqlParser.PathVariableReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#parameter.
    def enterParameter(self, ctx:GqlParser.ParameterContext):
        pass

    # Exit a parse tree produced by GqlParser#parameter.
    def exitParameter(self, ctx:GqlParser.ParameterContext):
        pass


    # Enter a parse tree produced by GqlParser#graphPatternBindingTable.
    def enterGraphPatternBindingTable(self, ctx:GqlParser.GraphPatternBindingTableContext):
        pass

    # Exit a parse tree produced by GqlParser#graphPatternBindingTable.
    def exitGraphPatternBindingTable(self, ctx:GqlParser.GraphPatternBindingTableContext):
        pass


    # Enter a parse tree produced by GqlParser#graphPatternYieldClause.
    def enterGraphPatternYieldClause(self, ctx:GqlParser.GraphPatternYieldClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#graphPatternYieldClause.
    def exitGraphPatternYieldClause(self, ctx:GqlParser.GraphPatternYieldClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#graphPatternYieldItemList.
    def enterGraphPatternYieldItemList(self, ctx:GqlParser.GraphPatternYieldItemListContext):
        pass

    # Exit a parse tree produced by GqlParser#graphPatternYieldItemList.
    def exitGraphPatternYieldItemList(self, ctx:GqlParser.GraphPatternYieldItemListContext):
        pass


    # Enter a parse tree produced by GqlParser#graphPatternYieldItem.
    def enterGraphPatternYieldItem(self, ctx:GqlParser.GraphPatternYieldItemContext):
        pass

    # Exit a parse tree produced by GqlParser#graphPatternYieldItem.
    def exitGraphPatternYieldItem(self, ctx:GqlParser.GraphPatternYieldItemContext):
        pass


    # Enter a parse tree produced by GqlParser#graphPattern.
    def enterGraphPattern(self, ctx:GqlParser.GraphPatternContext):
        pass

    # Exit a parse tree produced by GqlParser#graphPattern.
    def exitGraphPattern(self, ctx:GqlParser.GraphPatternContext):
        pass


    # Enter a parse tree produced by GqlParser#matchMode.
    def enterMatchMode(self, ctx:GqlParser.MatchModeContext):
        pass

    # Exit a parse tree produced by GqlParser#matchMode.
    def exitMatchMode(self, ctx:GqlParser.MatchModeContext):
        pass


    # Enter a parse tree produced by GqlParser#repeatableElementsMatchMode.
    def enterRepeatableElementsMatchMode(self, ctx:GqlParser.RepeatableElementsMatchModeContext):
        pass

    # Exit a parse tree produced by GqlParser#repeatableElementsMatchMode.
    def exitRepeatableElementsMatchMode(self, ctx:GqlParser.RepeatableElementsMatchModeContext):
        pass


    # Enter a parse tree produced by GqlParser#differentEdgesMatchMode.
    def enterDifferentEdgesMatchMode(self, ctx:GqlParser.DifferentEdgesMatchModeContext):
        pass

    # Exit a parse tree produced by GqlParser#differentEdgesMatchMode.
    def exitDifferentEdgesMatchMode(self, ctx:GqlParser.DifferentEdgesMatchModeContext):
        pass


    # Enter a parse tree produced by GqlParser#elementBindingsOrElements.
    def enterElementBindingsOrElements(self, ctx:GqlParser.ElementBindingsOrElementsContext):
        pass

    # Exit a parse tree produced by GqlParser#elementBindingsOrElements.
    def exitElementBindingsOrElements(self, ctx:GqlParser.ElementBindingsOrElementsContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeBindingsOrEdges.
    def enterEdgeBindingsOrEdges(self, ctx:GqlParser.EdgeBindingsOrEdgesContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeBindingsOrEdges.
    def exitEdgeBindingsOrEdges(self, ctx:GqlParser.EdgeBindingsOrEdgesContext):
        pass


    # Enter a parse tree produced by GqlParser#pathPatternList.
    def enterPathPatternList(self, ctx:GqlParser.PathPatternListContext):
        pass

    # Exit a parse tree produced by GqlParser#pathPatternList.
    def exitPathPatternList(self, ctx:GqlParser.PathPatternListContext):
        pass


    # Enter a parse tree produced by GqlParser#pathPattern.
    def enterPathPattern(self, ctx:GqlParser.PathPatternContext):
        pass

    # Exit a parse tree produced by GqlParser#pathPattern.
    def exitPathPattern(self, ctx:GqlParser.PathPatternContext):
        pass


    # Enter a parse tree produced by GqlParser#pathVariableDeclaration.
    def enterPathVariableDeclaration(self, ctx:GqlParser.PathVariableDeclarationContext):
        pass

    # Exit a parse tree produced by GqlParser#pathVariableDeclaration.
    def exitPathVariableDeclaration(self, ctx:GqlParser.PathVariableDeclarationContext):
        pass


    # Enter a parse tree produced by GqlParser#keepClause.
    def enterKeepClause(self, ctx:GqlParser.KeepClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#keepClause.
    def exitKeepClause(self, ctx:GqlParser.KeepClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#pathPatternPrefix.
    def enterPathPatternPrefix(self, ctx:GqlParser.PathPatternPrefixContext):
        pass

    # Exit a parse tree produced by GqlParser#pathPatternPrefix.
    def exitPathPatternPrefix(self, ctx:GqlParser.PathPatternPrefixContext):
        pass


    # Enter a parse tree produced by GqlParser#pathModePrefix.
    def enterPathModePrefix(self, ctx:GqlParser.PathModePrefixContext):
        pass

    # Exit a parse tree produced by GqlParser#pathModePrefix.
    def exitPathModePrefix(self, ctx:GqlParser.PathModePrefixContext):
        pass


    # Enter a parse tree produced by GqlParser#pathMode.
    def enterPathMode(self, ctx:GqlParser.PathModeContext):
        pass

    # Exit a parse tree produced by GqlParser#pathMode.
    def exitPathMode(self, ctx:GqlParser.PathModeContext):
        pass


    # Enter a parse tree produced by GqlParser#pathSearchPrefix.
    def enterPathSearchPrefix(self, ctx:GqlParser.PathSearchPrefixContext):
        pass

    # Exit a parse tree produced by GqlParser#pathSearchPrefix.
    def exitPathSearchPrefix(self, ctx:GqlParser.PathSearchPrefixContext):
        pass


    # Enter a parse tree produced by GqlParser#allPathSearch.
    def enterAllPathSearch(self, ctx:GqlParser.AllPathSearchContext):
        pass

    # Exit a parse tree produced by GqlParser#allPathSearch.
    def exitAllPathSearch(self, ctx:GqlParser.AllPathSearchContext):
        pass


    # Enter a parse tree produced by GqlParser#pathOrPaths.
    def enterPathOrPaths(self, ctx:GqlParser.PathOrPathsContext):
        pass

    # Exit a parse tree produced by GqlParser#pathOrPaths.
    def exitPathOrPaths(self, ctx:GqlParser.PathOrPathsContext):
        pass


    # Enter a parse tree produced by GqlParser#anyPathSearch.
    def enterAnyPathSearch(self, ctx:GqlParser.AnyPathSearchContext):
        pass

    # Exit a parse tree produced by GqlParser#anyPathSearch.
    def exitAnyPathSearch(self, ctx:GqlParser.AnyPathSearchContext):
        pass


    # Enter a parse tree produced by GqlParser#numberOfPaths.
    def enterNumberOfPaths(self, ctx:GqlParser.NumberOfPathsContext):
        pass

    # Exit a parse tree produced by GqlParser#numberOfPaths.
    def exitNumberOfPaths(self, ctx:GqlParser.NumberOfPathsContext):
        pass


    # Enter a parse tree produced by GqlParser#shortestPathSearch.
    def enterShortestPathSearch(self, ctx:GqlParser.ShortestPathSearchContext):
        pass

    # Exit a parse tree produced by GqlParser#shortestPathSearch.
    def exitShortestPathSearch(self, ctx:GqlParser.ShortestPathSearchContext):
        pass


    # Enter a parse tree produced by GqlParser#allShortestPathSearch.
    def enterAllShortestPathSearch(self, ctx:GqlParser.AllShortestPathSearchContext):
        pass

    # Exit a parse tree produced by GqlParser#allShortestPathSearch.
    def exitAllShortestPathSearch(self, ctx:GqlParser.AllShortestPathSearchContext):
        pass


    # Enter a parse tree produced by GqlParser#anyShortestPathSearch.
    def enterAnyShortestPathSearch(self, ctx:GqlParser.AnyShortestPathSearchContext):
        pass

    # Exit a parse tree produced by GqlParser#anyShortestPathSearch.
    def exitAnyShortestPathSearch(self, ctx:GqlParser.AnyShortestPathSearchContext):
        pass


    # Enter a parse tree produced by GqlParser#countedShortestPathSearch.
    def enterCountedShortestPathSearch(self, ctx:GqlParser.CountedShortestPathSearchContext):
        pass

    # Exit a parse tree produced by GqlParser#countedShortestPathSearch.
    def exitCountedShortestPathSearch(self, ctx:GqlParser.CountedShortestPathSearchContext):
        pass


    # Enter a parse tree produced by GqlParser#countedShortestGroupSearch.
    def enterCountedShortestGroupSearch(self, ctx:GqlParser.CountedShortestGroupSearchContext):
        pass

    # Exit a parse tree produced by GqlParser#countedShortestGroupSearch.
    def exitCountedShortestGroupSearch(self, ctx:GqlParser.CountedShortestGroupSearchContext):
        pass


    # Enter a parse tree produced by GqlParser#numberOfGroups.
    def enterNumberOfGroups(self, ctx:GqlParser.NumberOfGroupsContext):
        pass

    # Exit a parse tree produced by GqlParser#numberOfGroups.
    def exitNumberOfGroups(self, ctx:GqlParser.NumberOfGroupsContext):
        pass


    # Enter a parse tree produced by GqlParser#pathPatternExpression.
    def enterPathPatternExpression(self, ctx:GqlParser.PathPatternExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#pathPatternExpression.
    def exitPathPatternExpression(self, ctx:GqlParser.PathPatternExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#pathMultisetAlternation.
    def enterPathMultisetAlternation(self, ctx:GqlParser.PathMultisetAlternationContext):
        pass

    # Exit a parse tree produced by GqlParser#pathMultisetAlternation.
    def exitPathMultisetAlternation(self, ctx:GqlParser.PathMultisetAlternationContext):
        pass


    # Enter a parse tree produced by GqlParser#pathPatternUnion.
    def enterPathPatternUnion(self, ctx:GqlParser.PathPatternUnionContext):
        pass

    # Exit a parse tree produced by GqlParser#pathPatternUnion.
    def exitPathPatternUnion(self, ctx:GqlParser.PathPatternUnionContext):
        pass


    # Enter a parse tree produced by GqlParser#pathTerm.
    def enterPathTerm(self, ctx:GqlParser.PathTermContext):
        pass

    # Exit a parse tree produced by GqlParser#pathTerm.
    def exitPathTerm(self, ctx:GqlParser.PathTermContext):
        pass


    # Enter a parse tree produced by GqlParser#pathFactor.
    def enterPathFactor(self, ctx:GqlParser.PathFactorContext):
        pass

    # Exit a parse tree produced by GqlParser#pathFactor.
    def exitPathFactor(self, ctx:GqlParser.PathFactorContext):
        pass


    # Enter a parse tree produced by GqlParser#quantifiedPathPrimary.
    def enterQuantifiedPathPrimary(self, ctx:GqlParser.QuantifiedPathPrimaryContext):
        pass

    # Exit a parse tree produced by GqlParser#quantifiedPathPrimary.
    def exitQuantifiedPathPrimary(self, ctx:GqlParser.QuantifiedPathPrimaryContext):
        pass


    # Enter a parse tree produced by GqlParser#questionedPathPrimary.
    def enterQuestionedPathPrimary(self, ctx:GqlParser.QuestionedPathPrimaryContext):
        pass

    # Exit a parse tree produced by GqlParser#questionedPathPrimary.
    def exitQuestionedPathPrimary(self, ctx:GqlParser.QuestionedPathPrimaryContext):
        pass


    # Enter a parse tree produced by GqlParser#pathPrimary.
    def enterPathPrimary(self, ctx:GqlParser.PathPrimaryContext):
        pass

    # Exit a parse tree produced by GqlParser#pathPrimary.
    def exitPathPrimary(self, ctx:GqlParser.PathPrimaryContext):
        pass


    # Enter a parse tree produced by GqlParser#elementPattern.
    def enterElementPattern(self, ctx:GqlParser.ElementPatternContext):
        pass

    # Exit a parse tree produced by GqlParser#elementPattern.
    def exitElementPattern(self, ctx:GqlParser.ElementPatternContext):
        pass


    # Enter a parse tree produced by GqlParser#nodePattern.
    def enterNodePattern(self, ctx:GqlParser.NodePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#nodePattern.
    def exitNodePattern(self, ctx:GqlParser.NodePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#elementPatternFiller.
    def enterElementPatternFiller(self, ctx:GqlParser.ElementPatternFillerContext):
        pass

    # Exit a parse tree produced by GqlParser#elementPatternFiller.
    def exitElementPatternFiller(self, ctx:GqlParser.ElementPatternFillerContext):
        pass


    # Enter a parse tree produced by GqlParser#elementVariableDeclaration.
    def enterElementVariableDeclaration(self, ctx:GqlParser.ElementVariableDeclarationContext):
        pass

    # Exit a parse tree produced by GqlParser#elementVariableDeclaration.
    def exitElementVariableDeclaration(self, ctx:GqlParser.ElementVariableDeclarationContext):
        pass


    # Enter a parse tree produced by GqlParser#isLabelExpression.
    def enterIsLabelExpression(self, ctx:GqlParser.IsLabelExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#isLabelExpression.
    def exitIsLabelExpression(self, ctx:GqlParser.IsLabelExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#isOrColon.
    def enterIsOrColon(self, ctx:GqlParser.IsOrColonContext):
        pass

    # Exit a parse tree produced by GqlParser#isOrColon.
    def exitIsOrColon(self, ctx:GqlParser.IsOrColonContext):
        pass


    # Enter a parse tree produced by GqlParser#elementPatternPredicate.
    def enterElementPatternPredicate(self, ctx:GqlParser.ElementPatternPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#elementPatternPredicate.
    def exitElementPatternPredicate(self, ctx:GqlParser.ElementPatternPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#elementPropertySpecification.
    def enterElementPropertySpecification(self, ctx:GqlParser.ElementPropertySpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#elementPropertySpecification.
    def exitElementPropertySpecification(self, ctx:GqlParser.ElementPropertySpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyKeyValuePairList.
    def enterPropertyKeyValuePairList(self, ctx:GqlParser.PropertyKeyValuePairListContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyKeyValuePairList.
    def exitPropertyKeyValuePairList(self, ctx:GqlParser.PropertyKeyValuePairListContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyKeyValuePair.
    def enterPropertyKeyValuePair(self, ctx:GqlParser.PropertyKeyValuePairContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyKeyValuePair.
    def exitPropertyKeyValuePair(self, ctx:GqlParser.PropertyKeyValuePairContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitClause.
    def enterPerNodeLimitClause(self, ctx:GqlParser.PerNodeLimitClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitClause.
    def exitPerNodeLimitClause(self, ctx:GqlParser.PerNodeLimitClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitWherePredicate.
    def enterPerNodeLimitWherePredicate(self, ctx:GqlParser.PerNodeLimitWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitWherePredicate.
    def exitPerNodeLimitWherePredicate(self, ctx:GqlParser.PerNodeLimitWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitLeftWherePredicate.
    def enterPerNodeLimitLeftWherePredicate(self, ctx:GqlParser.PerNodeLimitLeftWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitLeftWherePredicate.
    def exitPerNodeLimitLeftWherePredicate(self, ctx:GqlParser.PerNodeLimitLeftWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitRightWherePredicate.
    def enterPerNodeLimitRightWherePredicate(self, ctx:GqlParser.PerNodeLimitRightWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitRightWherePredicate.
    def exitPerNodeLimitRightWherePredicate(self, ctx:GqlParser.PerNodeLimitRightWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitBothWherePredicate.
    def enterPerNodeLimitBothWherePredicate(self, ctx:GqlParser.PerNodeLimitBothWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitBothWherePredicate.
    def exitPerNodeLimitBothWherePredicate(self, ctx:GqlParser.PerNodeLimitBothWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitPropertyPredicate.
    def enterPerNodeLimitPropertyPredicate(self, ctx:GqlParser.PerNodeLimitPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitPropertyPredicate.
    def exitPerNodeLimitPropertyPredicate(self, ctx:GqlParser.PerNodeLimitPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitLeftPropertyPredicate.
    def enterPerNodeLimitLeftPropertyPredicate(self, ctx:GqlParser.PerNodeLimitLeftPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitLeftPropertyPredicate.
    def exitPerNodeLimitLeftPropertyPredicate(self, ctx:GqlParser.PerNodeLimitLeftPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitRightPropertyPredicate.
    def enterPerNodeLimitRightPropertyPredicate(self, ctx:GqlParser.PerNodeLimitRightPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitRightPropertyPredicate.
    def exitPerNodeLimitRightPropertyPredicate(self, ctx:GqlParser.PerNodeLimitRightPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perNodeLimitBothPropertyPredicate.
    def enterPerNodeLimitBothPropertyPredicate(self, ctx:GqlParser.PerNodeLimitBothPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perNodeLimitBothPropertyPredicate.
    def exitPerNodeLimitBothPropertyPredicate(self, ctx:GqlParser.PerNodeLimitBothPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitClause.
    def enterPerShardLimitClause(self, ctx:GqlParser.PerShardLimitClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitClause.
    def exitPerShardLimitClause(self, ctx:GqlParser.PerShardLimitClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitWherePredicate.
    def enterPerShardLimitWherePredicate(self, ctx:GqlParser.PerShardLimitWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitWherePredicate.
    def exitPerShardLimitWherePredicate(self, ctx:GqlParser.PerShardLimitWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitLeftWherePredicate.
    def enterPerShardLimitLeftWherePredicate(self, ctx:GqlParser.PerShardLimitLeftWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitLeftWherePredicate.
    def exitPerShardLimitLeftWherePredicate(self, ctx:GqlParser.PerShardLimitLeftWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitRightWherePredicate.
    def enterPerShardLimitRightWherePredicate(self, ctx:GqlParser.PerShardLimitRightWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitRightWherePredicate.
    def exitPerShardLimitRightWherePredicate(self, ctx:GqlParser.PerShardLimitRightWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitBothWherePredicate.
    def enterPerShardLimitBothWherePredicate(self, ctx:GqlParser.PerShardLimitBothWherePredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitBothWherePredicate.
    def exitPerShardLimitBothWherePredicate(self, ctx:GqlParser.PerShardLimitBothWherePredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitPropertyPredicate.
    def enterPerShardLimitPropertyPredicate(self, ctx:GqlParser.PerShardLimitPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitPropertyPredicate.
    def exitPerShardLimitPropertyPredicate(self, ctx:GqlParser.PerShardLimitPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitLeftPropertyPredicate.
    def enterPerShardLimitLeftPropertyPredicate(self, ctx:GqlParser.PerShardLimitLeftPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitLeftPropertyPredicate.
    def exitPerShardLimitLeftPropertyPredicate(self, ctx:GqlParser.PerShardLimitLeftPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitRightPropertyPredicate.
    def enterPerShardLimitRightPropertyPredicate(self, ctx:GqlParser.PerShardLimitRightPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitRightPropertyPredicate.
    def exitPerShardLimitRightPropertyPredicate(self, ctx:GqlParser.PerShardLimitRightPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#perShardLimitBothPropertyPredicate.
    def enterPerShardLimitBothPropertyPredicate(self, ctx:GqlParser.PerShardLimitBothPropertyPredicateContext):
        pass

    # Exit a parse tree produced by GqlParser#perShardLimitBothPropertyPredicate.
    def exitPerShardLimitBothPropertyPredicate(self, ctx:GqlParser.PerShardLimitBothPropertyPredicateContext):
        pass


    # Enter a parse tree produced by GqlParser#edgePattern.
    def enterEdgePattern(self, ctx:GqlParser.EdgePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#edgePattern.
    def exitEdgePattern(self, ctx:GqlParser.EdgePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgePattern.
    def enterFullEdgePattern(self, ctx:GqlParser.FullEdgePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgePattern.
    def exitFullEdgePattern(self, ctx:GqlParser.FullEdgePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgePointingLeft.
    def enterFullEdgePointingLeft(self, ctx:GqlParser.FullEdgePointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgePointingLeft.
    def exitFullEdgePointingLeft(self, ctx:GqlParser.FullEdgePointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeUndirected.
    def enterFullEdgeUndirected(self, ctx:GqlParser.FullEdgeUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeUndirected.
    def exitFullEdgeUndirected(self, ctx:GqlParser.FullEdgeUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgePointingRight.
    def enterFullEdgePointingRight(self, ctx:GqlParser.FullEdgePointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgePointingRight.
    def exitFullEdgePointingRight(self, ctx:GqlParser.FullEdgePointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeLeftOrUndirected.
    def enterFullEdgeLeftOrUndirected(self, ctx:GqlParser.FullEdgeLeftOrUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeLeftOrUndirected.
    def exitFullEdgeLeftOrUndirected(self, ctx:GqlParser.FullEdgeLeftOrUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeUndirectedOrRight.
    def enterFullEdgeUndirectedOrRight(self, ctx:GqlParser.FullEdgeUndirectedOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeUndirectedOrRight.
    def exitFullEdgeUndirectedOrRight(self, ctx:GqlParser.FullEdgeUndirectedOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeLeftOrRight.
    def enterFullEdgeLeftOrRight(self, ctx:GqlParser.FullEdgeLeftOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeLeftOrRight.
    def exitFullEdgeLeftOrRight(self, ctx:GqlParser.FullEdgeLeftOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeAnyDirection.
    def enterFullEdgeAnyDirection(self, ctx:GqlParser.FullEdgeAnyDirectionContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeAnyDirection.
    def exitFullEdgeAnyDirection(self, ctx:GqlParser.FullEdgeAnyDirectionContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgePointingLeft.
    def enterAbbreviatedEdgePointingLeft(self, ctx:GqlParser.AbbreviatedEdgePointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgePointingLeft.
    def exitAbbreviatedEdgePointingLeft(self, ctx:GqlParser.AbbreviatedEdgePointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeUndirected.
    def enterAbbreviatedEdgeUndirected(self, ctx:GqlParser.AbbreviatedEdgeUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeUndirected.
    def exitAbbreviatedEdgeUndirected(self, ctx:GqlParser.AbbreviatedEdgeUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgePointingRight.
    def enterAbbreviatedEdgePointingRight(self, ctx:GqlParser.AbbreviatedEdgePointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgePointingRight.
    def exitAbbreviatedEdgePointingRight(self, ctx:GqlParser.AbbreviatedEdgePointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeLeftOrUndirected.
    def enterAbbreviatedEdgeLeftOrUndirected(self, ctx:GqlParser.AbbreviatedEdgeLeftOrUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeLeftOrUndirected.
    def exitAbbreviatedEdgeLeftOrUndirected(self, ctx:GqlParser.AbbreviatedEdgeLeftOrUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeUndirectedOrRight.
    def enterAbbreviatedEdgeUndirectedOrRight(self, ctx:GqlParser.AbbreviatedEdgeUndirectedOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeUndirectedOrRight.
    def exitAbbreviatedEdgeUndirectedOrRight(self, ctx:GqlParser.AbbreviatedEdgeUndirectedOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeLeftOrRight.
    def enterAbbreviatedEdgeLeftOrRight(self, ctx:GqlParser.AbbreviatedEdgeLeftOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeLeftOrRight.
    def exitAbbreviatedEdgeLeftOrRight(self, ctx:GqlParser.AbbreviatedEdgeLeftOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeAnyDirection.
    def enterAbbreviatedEdgeAnyDirection(self, ctx:GqlParser.AbbreviatedEdgeAnyDirectionContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeAnyDirection.
    def exitAbbreviatedEdgeAnyDirection(self, ctx:GqlParser.AbbreviatedEdgeAnyDirectionContext):
        pass


    # Enter a parse tree produced by GqlParser#parenthesizedPathPatternExpression.
    def enterParenthesizedPathPatternExpression(self, ctx:GqlParser.ParenthesizedPathPatternExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#parenthesizedPathPatternExpression.
    def exitParenthesizedPathPatternExpression(self, ctx:GqlParser.ParenthesizedPathPatternExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#parenthesizedPathPatternExpressionBody.
    def enterParenthesizedPathPatternExpressionBody(self, ctx:GqlParser.ParenthesizedPathPatternExpressionBodyContext):
        pass

    # Exit a parse tree produced by GqlParser#parenthesizedPathPatternExpressionBody.
    def exitParenthesizedPathPatternExpressionBody(self, ctx:GqlParser.ParenthesizedPathPatternExpressionBodyContext):
        pass


    # Enter a parse tree produced by GqlParser#untilPart.
    def enterUntilPart(self, ctx:GqlParser.UntilPartContext):
        pass

    # Exit a parse tree produced by GqlParser#untilPart.
    def exitUntilPart(self, ctx:GqlParser.UntilPartContext):
        pass


    # Enter a parse tree produced by GqlParser#slidingPart.
    def enterSlidingPart(self, ctx:GqlParser.SlidingPartContext):
        pass

    # Exit a parse tree produced by GqlParser#slidingPart.
    def exitSlidingPart(self, ctx:GqlParser.SlidingPartContext):
        pass


    # Enter a parse tree produced by GqlParser#lengthPart.
    def enterLengthPart(self, ctx:GqlParser.LengthPartContext):
        pass

    # Exit a parse tree produced by GqlParser#lengthPart.
    def exitLengthPart(self, ctx:GqlParser.LengthPartContext):
        pass


    # Enter a parse tree produced by GqlParser#stepPart.
    def enterStepPart(self, ctx:GqlParser.StepPartContext):
        pass

    # Exit a parse tree produced by GqlParser#stepPart.
    def exitStepPart(self, ctx:GqlParser.StepPartContext):
        pass


    # Enter a parse tree produced by GqlParser#subpathVariableDeclaration.
    def enterSubpathVariableDeclaration(self, ctx:GqlParser.SubpathVariableDeclarationContext):
        pass

    # Exit a parse tree produced by GqlParser#subpathVariableDeclaration.
    def exitSubpathVariableDeclaration(self, ctx:GqlParser.SubpathVariableDeclarationContext):
        pass


    # Enter a parse tree produced by GqlParser#parenthesizedPathPatternWhereClause.
    def enterParenthesizedPathPatternWhereClause(self, ctx:GqlParser.ParenthesizedPathPatternWhereClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#parenthesizedPathPatternWhereClause.
    def exitParenthesizedPathPatternWhereClause(self, ctx:GqlParser.ParenthesizedPathPatternWhereClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#insertGraphPattern.
    def enterInsertGraphPattern(self, ctx:GqlParser.InsertGraphPatternContext):
        pass

    # Exit a parse tree produced by GqlParser#insertGraphPattern.
    def exitInsertGraphPattern(self, ctx:GqlParser.InsertGraphPatternContext):
        pass


    # Enter a parse tree produced by GqlParser#insertPathPatternList.
    def enterInsertPathPatternList(self, ctx:GqlParser.InsertPathPatternListContext):
        pass

    # Exit a parse tree produced by GqlParser#insertPathPatternList.
    def exitInsertPathPatternList(self, ctx:GqlParser.InsertPathPatternListContext):
        pass


    # Enter a parse tree produced by GqlParser#insertPathPattern.
    def enterInsertPathPattern(self, ctx:GqlParser.InsertPathPatternContext):
        pass

    # Exit a parse tree produced by GqlParser#insertPathPattern.
    def exitInsertPathPattern(self, ctx:GqlParser.InsertPathPatternContext):
        pass


    # Enter a parse tree produced by GqlParser#insertNodePattern.
    def enterInsertNodePattern(self, ctx:GqlParser.InsertNodePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#insertNodePattern.
    def exitInsertNodePattern(self, ctx:GqlParser.InsertNodePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#insertEdgePattern.
    def enterInsertEdgePattern(self, ctx:GqlParser.InsertEdgePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#insertEdgePattern.
    def exitInsertEdgePattern(self, ctx:GqlParser.InsertEdgePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#insertEdgePointingLeft.
    def enterInsertEdgePointingLeft(self, ctx:GqlParser.InsertEdgePointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#insertEdgePointingLeft.
    def exitInsertEdgePointingLeft(self, ctx:GqlParser.InsertEdgePointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#insertEdgePointingRight.
    def enterInsertEdgePointingRight(self, ctx:GqlParser.InsertEdgePointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#insertEdgePointingRight.
    def exitInsertEdgePointingRight(self, ctx:GqlParser.InsertEdgePointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#insertEdgeUndirected.
    def enterInsertEdgeUndirected(self, ctx:GqlParser.InsertEdgeUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#insertEdgeUndirected.
    def exitInsertEdgeUndirected(self, ctx:GqlParser.InsertEdgeUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#insertElementPatternFiller.
    def enterInsertElementPatternFiller(self, ctx:GqlParser.InsertElementPatternFillerContext):
        pass

    # Exit a parse tree produced by GqlParser#insertElementPatternFiller.
    def exitInsertElementPatternFiller(self, ctx:GqlParser.InsertElementPatternFillerContext):
        pass


    # Enter a parse tree produced by GqlParser#labelAndPropertySetSpecification.
    def enterLabelAndPropertySetSpecification(self, ctx:GqlParser.LabelAndPropertySetSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#labelAndPropertySetSpecification.
    def exitLabelAndPropertySetSpecification(self, ctx:GqlParser.LabelAndPropertySetSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#labelExpression.
    def enterLabelExpression(self, ctx:GqlParser.LabelExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#labelExpression.
    def exitLabelExpression(self, ctx:GqlParser.LabelExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#labelTerm.
    def enterLabelTerm(self, ctx:GqlParser.LabelTermContext):
        pass

    # Exit a parse tree produced by GqlParser#labelTerm.
    def exitLabelTerm(self, ctx:GqlParser.LabelTermContext):
        pass


    # Enter a parse tree produced by GqlParser#labelFactor.
    def enterLabelFactor(self, ctx:GqlParser.LabelFactorContext):
        pass

    # Exit a parse tree produced by GqlParser#labelFactor.
    def exitLabelFactor(self, ctx:GqlParser.LabelFactorContext):
        pass


    # Enter a parse tree produced by GqlParser#labelPrimary.
    def enterLabelPrimary(self, ctx:GqlParser.LabelPrimaryContext):
        pass

    # Exit a parse tree produced by GqlParser#labelPrimary.
    def exitLabelPrimary(self, ctx:GqlParser.LabelPrimaryContext):
        pass


    # Enter a parse tree produced by GqlParser#wildcardLabel.
    def enterWildcardLabel(self, ctx:GqlParser.WildcardLabelContext):
        pass

    # Exit a parse tree produced by GqlParser#wildcardLabel.
    def exitWildcardLabel(self, ctx:GqlParser.WildcardLabelContext):
        pass


    # Enter a parse tree produced by GqlParser#parenthesizedLabelExpression.
    def enterParenthesizedLabelExpression(self, ctx:GqlParser.ParenthesizedLabelExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#parenthesizedLabelExpression.
    def exitParenthesizedLabelExpression(self, ctx:GqlParser.ParenthesizedLabelExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlGraphPatternAsteriskQuantifier.
    def enterGqlGraphPatternAsteriskQuantifier(self, ctx:GqlParser.GqlGraphPatternAsteriskQuantifierContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlGraphPatternAsteriskQuantifier.
    def exitGqlGraphPatternAsteriskQuantifier(self, ctx:GqlParser.GqlGraphPatternAsteriskQuantifierContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlGraphPatternPlusSignQuantifier.
    def enterGqlGraphPatternPlusSignQuantifier(self, ctx:GqlParser.GqlGraphPatternPlusSignQuantifierContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlGraphPatternPlusSignQuantifier.
    def exitGqlGraphPatternPlusSignQuantifier(self, ctx:GqlParser.GqlGraphPatternPlusSignQuantifierContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlGraphPatternFixedQuantifier.
    def enterGqlGraphPatternFixedQuantifier(self, ctx:GqlParser.GqlGraphPatternFixedQuantifierContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlGraphPatternFixedQuantifier.
    def exitGqlGraphPatternFixedQuantifier(self, ctx:GqlParser.GqlGraphPatternFixedQuantifierContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlGraphPatternGeneralQuantifier.
    def enterGqlGraphPatternGeneralQuantifier(self, ctx:GqlParser.GqlGraphPatternGeneralQuantifierContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlGraphPatternGeneralQuantifier.
    def exitGqlGraphPatternGeneralQuantifier(self, ctx:GqlParser.GqlGraphPatternGeneralQuantifierContext):
        pass


    # Enter a parse tree produced by GqlParser#fixedQuantifier.
    def enterFixedQuantifier(self, ctx:GqlParser.FixedQuantifierContext):
        pass

    # Exit a parse tree produced by GqlParser#fixedQuantifier.
    def exitFixedQuantifier(self, ctx:GqlParser.FixedQuantifierContext):
        pass


    # Enter a parse tree produced by GqlParser#generalQuantifier.
    def enterGeneralQuantifier(self, ctx:GqlParser.GeneralQuantifierContext):
        pass

    # Exit a parse tree produced by GqlParser#generalQuantifier.
    def exitGeneralQuantifier(self, ctx:GqlParser.GeneralQuantifierContext):
        pass


    # Enter a parse tree produced by GqlParser#lowerBound.
    def enterLowerBound(self, ctx:GqlParser.LowerBoundContext):
        pass

    # Exit a parse tree produced by GqlParser#lowerBound.
    def exitLowerBound(self, ctx:GqlParser.LowerBoundContext):
        pass


    # Enter a parse tree produced by GqlParser#upperBound.
    def enterUpperBound(self, ctx:GqlParser.UpperBoundContext):
        pass

    # Exit a parse tree produced by GqlParser#upperBound.
    def exitUpperBound(self, ctx:GqlParser.UpperBoundContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedPathPatternExpression.
    def enterSimplifiedPathPatternExpression(self, ctx:GqlParser.SimplifiedPathPatternExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedPathPatternExpression.
    def exitSimplifiedPathPatternExpression(self, ctx:GqlParser.SimplifiedPathPatternExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDefaultingLeft.
    def enterSimplifiedDefaultingLeft(self, ctx:GqlParser.SimplifiedDefaultingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDefaultingLeft.
    def exitSimplifiedDefaultingLeft(self, ctx:GqlParser.SimplifiedDefaultingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDefaultingUndirected.
    def enterSimplifiedDefaultingUndirected(self, ctx:GqlParser.SimplifiedDefaultingUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDefaultingUndirected.
    def exitSimplifiedDefaultingUndirected(self, ctx:GqlParser.SimplifiedDefaultingUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDefaultingRight.
    def enterSimplifiedDefaultingRight(self, ctx:GqlParser.SimplifiedDefaultingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDefaultingRight.
    def exitSimplifiedDefaultingRight(self, ctx:GqlParser.SimplifiedDefaultingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDefaultingLeftOrUndirected.
    def enterSimplifiedDefaultingLeftOrUndirected(self, ctx:GqlParser.SimplifiedDefaultingLeftOrUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDefaultingLeftOrUndirected.
    def exitSimplifiedDefaultingLeftOrUndirected(self, ctx:GqlParser.SimplifiedDefaultingLeftOrUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDefaultingUndirectedOrRight.
    def enterSimplifiedDefaultingUndirectedOrRight(self, ctx:GqlParser.SimplifiedDefaultingUndirectedOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDefaultingUndirectedOrRight.
    def exitSimplifiedDefaultingUndirectedOrRight(self, ctx:GqlParser.SimplifiedDefaultingUndirectedOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDefaultingLeftOrRight.
    def enterSimplifiedDefaultingLeftOrRight(self, ctx:GqlParser.SimplifiedDefaultingLeftOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDefaultingLeftOrRight.
    def exitSimplifiedDefaultingLeftOrRight(self, ctx:GqlParser.SimplifiedDefaultingLeftOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDefaultingAnyDirection.
    def enterSimplifiedDefaultingAnyDirection(self, ctx:GqlParser.SimplifiedDefaultingAnyDirectionContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDefaultingAnyDirection.
    def exitSimplifiedDefaultingAnyDirection(self, ctx:GqlParser.SimplifiedDefaultingAnyDirectionContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedContents.
    def enterSimplifiedContents(self, ctx:GqlParser.SimplifiedContentsContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedContents.
    def exitSimplifiedContents(self, ctx:GqlParser.SimplifiedContentsContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedPathUnion.
    def enterSimplifiedPathUnion(self, ctx:GqlParser.SimplifiedPathUnionContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedPathUnion.
    def exitSimplifiedPathUnion(self, ctx:GqlParser.SimplifiedPathUnionContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedMultisetAlternation.
    def enterSimplifiedMultisetAlternation(self, ctx:GqlParser.SimplifiedMultisetAlternationContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedMultisetAlternation.
    def exitSimplifiedMultisetAlternation(self, ctx:GqlParser.SimplifiedMultisetAlternationContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedTerm.
    def enterSimplifiedTerm(self, ctx:GqlParser.SimplifiedTermContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedTerm.
    def exitSimplifiedTerm(self, ctx:GqlParser.SimplifiedTermContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedFactorLow.
    def enterSimplifiedFactorLow(self, ctx:GqlParser.SimplifiedFactorLowContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedFactorLow.
    def exitSimplifiedFactorLow(self, ctx:GqlParser.SimplifiedFactorLowContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedFactorHigh.
    def enterSimplifiedFactorHigh(self, ctx:GqlParser.SimplifiedFactorHighContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedFactorHigh.
    def exitSimplifiedFactorHigh(self, ctx:GqlParser.SimplifiedFactorHighContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedQuantified.
    def enterSimplifiedQuantified(self, ctx:GqlParser.SimplifiedQuantifiedContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedQuantified.
    def exitSimplifiedQuantified(self, ctx:GqlParser.SimplifiedQuantifiedContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedQuestioned.
    def enterSimplifiedQuestioned(self, ctx:GqlParser.SimplifiedQuestionedContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedQuestioned.
    def exitSimplifiedQuestioned(self, ctx:GqlParser.SimplifiedQuestionedContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedTertiary.
    def enterSimplifiedTertiary(self, ctx:GqlParser.SimplifiedTertiaryContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedTertiary.
    def exitSimplifiedTertiary(self, ctx:GqlParser.SimplifiedTertiaryContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedDirectionOverride.
    def enterSimplifiedDirectionOverride(self, ctx:GqlParser.SimplifiedDirectionOverrideContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedDirectionOverride.
    def exitSimplifiedDirectionOverride(self, ctx:GqlParser.SimplifiedDirectionOverrideContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedOverrideLeft.
    def enterSimplifiedOverrideLeft(self, ctx:GqlParser.SimplifiedOverrideLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedOverrideLeft.
    def exitSimplifiedOverrideLeft(self, ctx:GqlParser.SimplifiedOverrideLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedOverrideUndirected.
    def enterSimplifiedOverrideUndirected(self, ctx:GqlParser.SimplifiedOverrideUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedOverrideUndirected.
    def exitSimplifiedOverrideUndirected(self, ctx:GqlParser.SimplifiedOverrideUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedOverrideRight.
    def enterSimplifiedOverrideRight(self, ctx:GqlParser.SimplifiedOverrideRightContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedOverrideRight.
    def exitSimplifiedOverrideRight(self, ctx:GqlParser.SimplifiedOverrideRightContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedOverrideLeftOrUndirected.
    def enterSimplifiedOverrideLeftOrUndirected(self, ctx:GqlParser.SimplifiedOverrideLeftOrUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedOverrideLeftOrUndirected.
    def exitSimplifiedOverrideLeftOrUndirected(self, ctx:GqlParser.SimplifiedOverrideLeftOrUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedOverrideUndirectedOrRight.
    def enterSimplifiedOverrideUndirectedOrRight(self, ctx:GqlParser.SimplifiedOverrideUndirectedOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedOverrideUndirectedOrRight.
    def exitSimplifiedOverrideUndirectedOrRight(self, ctx:GqlParser.SimplifiedOverrideUndirectedOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedOverrideLeftOrRight.
    def enterSimplifiedOverrideLeftOrRight(self, ctx:GqlParser.SimplifiedOverrideLeftOrRightContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedOverrideLeftOrRight.
    def exitSimplifiedOverrideLeftOrRight(self, ctx:GqlParser.SimplifiedOverrideLeftOrRightContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedOverrideAnyDirection.
    def enterSimplifiedOverrideAnyDirection(self, ctx:GqlParser.SimplifiedOverrideAnyDirectionContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedOverrideAnyDirection.
    def exitSimplifiedOverrideAnyDirection(self, ctx:GqlParser.SimplifiedOverrideAnyDirectionContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedSecondary.
    def enterSimplifiedSecondary(self, ctx:GqlParser.SimplifiedSecondaryContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedSecondary.
    def exitSimplifiedSecondary(self, ctx:GqlParser.SimplifiedSecondaryContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedNegation.
    def enterSimplifiedNegation(self, ctx:GqlParser.SimplifiedNegationContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedNegation.
    def exitSimplifiedNegation(self, ctx:GqlParser.SimplifiedNegationContext):
        pass


    # Enter a parse tree produced by GqlParser#simplifiedPrimary.
    def enterSimplifiedPrimary(self, ctx:GqlParser.SimplifiedPrimaryContext):
        pass

    # Exit a parse tree produced by GqlParser#simplifiedPrimary.
    def exitSimplifiedPrimary(self, ctx:GqlParser.SimplifiedPrimaryContext):
        pass


    # Enter a parse tree produced by GqlParser#whereClause.
    def enterWhereClause(self, ctx:GqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#whereClause.
    def exitWhereClause(self, ctx:GqlParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#yieldClause.
    def enterYieldClause(self, ctx:GqlParser.YieldClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#yieldClause.
    def exitYieldClause(self, ctx:GqlParser.YieldClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#yieldItemList.
    def enterYieldItemList(self, ctx:GqlParser.YieldItemListContext):
        pass

    # Exit a parse tree produced by GqlParser#yieldItemList.
    def exitYieldItemList(self, ctx:GqlParser.YieldItemListContext):
        pass


    # Enter a parse tree produced by GqlParser#yieldItem.
    def enterYieldItem(self, ctx:GqlParser.YieldItemContext):
        pass

    # Exit a parse tree produced by GqlParser#yieldItem.
    def exitYieldItem(self, ctx:GqlParser.YieldItemContext):
        pass


    # Enter a parse tree produced by GqlParser#yieldItemName.
    def enterYieldItemName(self, ctx:GqlParser.YieldItemNameContext):
        pass

    # Exit a parse tree produced by GqlParser#yieldItemName.
    def exitYieldItemName(self, ctx:GqlParser.YieldItemNameContext):
        pass


    # Enter a parse tree produced by GqlParser#yieldItemAlias.
    def enterYieldItemAlias(self, ctx:GqlParser.YieldItemAliasContext):
        pass

    # Exit a parse tree produced by GqlParser#yieldItemAlias.
    def exitYieldItemAlias(self, ctx:GqlParser.YieldItemAliasContext):
        pass


    # Enter a parse tree produced by GqlParser#groupByClause.
    def enterGroupByClause(self, ctx:GqlParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#groupByClause.
    def exitGroupByClause(self, ctx:GqlParser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#groupingElementList.
    def enterGroupingElementList(self, ctx:GqlParser.GroupingElementListContext):
        pass

    # Exit a parse tree produced by GqlParser#groupingElementList.
    def exitGroupingElementList(self, ctx:GqlParser.GroupingElementListContext):
        pass


    # Enter a parse tree produced by GqlParser#groupingElement.
    def enterGroupingElement(self, ctx:GqlParser.GroupingElementContext):
        pass

    # Exit a parse tree produced by GqlParser#groupingElement.
    def exitGroupingElement(self, ctx:GqlParser.GroupingElementContext):
        pass


    # Enter a parse tree produced by GqlParser#emptyGroupingSet.
    def enterEmptyGroupingSet(self, ctx:GqlParser.EmptyGroupingSetContext):
        pass

    # Exit a parse tree produced by GqlParser#emptyGroupingSet.
    def exitEmptyGroupingSet(self, ctx:GqlParser.EmptyGroupingSetContext):
        pass


    # Enter a parse tree produced by GqlParser#orderByClause.
    def enterOrderByClause(self, ctx:GqlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#orderByClause.
    def exitOrderByClause(self, ctx:GqlParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlCountAllFunction.
    def enterGqlCountAllFunction(self, ctx:GqlParser.GqlCountAllFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlCountAllFunction.
    def exitGqlCountAllFunction(self, ctx:GqlParser.GqlCountAllFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlCountDistinctFunction.
    def enterGqlCountDistinctFunction(self, ctx:GqlParser.GqlCountDistinctFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlCountDistinctFunction.
    def exitGqlCountDistinctFunction(self, ctx:GqlParser.GqlCountDistinctFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlGeneralSetFunction.
    def enterGqlGeneralSetFunction(self, ctx:GqlParser.GqlGeneralSetFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlGeneralSetFunction.
    def exitGqlGeneralSetFunction(self, ctx:GqlParser.GqlGeneralSetFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBinarySetFunction.
    def enterGqlBinarySetFunction(self, ctx:GqlParser.GqlBinarySetFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBinarySetFunction.
    def exitGqlBinarySetFunction(self, ctx:GqlParser.GqlBinarySetFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlWindowFunction.
    def enterGqlWindowFunction(self, ctx:GqlParser.GqlWindowFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlWindowFunction.
    def exitGqlWindowFunction(self, ctx:GqlParser.GqlWindowFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlDistinctInGeneralFunction.
    def enterGqlDistinctInGeneralFunction(self, ctx:GqlParser.GqlDistinctInGeneralFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlDistinctInGeneralFunction.
    def exitGqlDistinctInGeneralFunction(self, ctx:GqlParser.GqlDistinctInGeneralFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#generalSetFunctionType.
    def enterGeneralSetFunctionType(self, ctx:GqlParser.GeneralSetFunctionTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#generalSetFunctionType.
    def exitGeneralSetFunctionType(self, ctx:GqlParser.GeneralSetFunctionTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#setQuantifier.
    def enterSetQuantifier(self, ctx:GqlParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by GqlParser#setQuantifier.
    def exitSetQuantifier(self, ctx:GqlParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by GqlParser#binarySetFunctionType.
    def enterBinarySetFunctionType(self, ctx:GqlParser.BinarySetFunctionTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#binarySetFunctionType.
    def exitBinarySetFunctionType(self, ctx:GqlParser.BinarySetFunctionTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#windowFunctionType.
    def enterWindowFunctionType(self, ctx:GqlParser.WindowFunctionTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#windowFunctionType.
    def exitWindowFunctionType(self, ctx:GqlParser.WindowFunctionTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#windowClause.
    def enterWindowClause(self, ctx:GqlParser.WindowClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#windowClause.
    def exitWindowClause(self, ctx:GqlParser.WindowClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#sortSpecificationList.
    def enterSortSpecificationList(self, ctx:GqlParser.SortSpecificationListContext):
        pass

    # Exit a parse tree produced by GqlParser#sortSpecificationList.
    def exitSortSpecificationList(self, ctx:GqlParser.SortSpecificationListContext):
        pass


    # Enter a parse tree produced by GqlParser#sortSpecification.
    def enterSortSpecification(self, ctx:GqlParser.SortSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#sortSpecification.
    def exitSortSpecification(self, ctx:GqlParser.SortSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#sortKey.
    def enterSortKey(self, ctx:GqlParser.SortKeyContext):
        pass

    # Exit a parse tree produced by GqlParser#sortKey.
    def exitSortKey(self, ctx:GqlParser.SortKeyContext):
        pass


    # Enter a parse tree produced by GqlParser#orderingSpecification.
    def enterOrderingSpecification(self, ctx:GqlParser.OrderingSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#orderingSpecification.
    def exitOrderingSpecification(self, ctx:GqlParser.OrderingSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#nullOrdering.
    def enterNullOrdering(self, ctx:GqlParser.NullOrderingContext):
        pass

    # Exit a parse tree produced by GqlParser#nullOrdering.
    def exitNullOrdering(self, ctx:GqlParser.NullOrderingContext):
        pass


    # Enter a parse tree produced by GqlParser#limitClause.
    def enterLimitClause(self, ctx:GqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#limitClause.
    def exitLimitClause(self, ctx:GqlParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#offsetClause.
    def enterOffsetClause(self, ctx:GqlParser.OffsetClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#offsetClause.
    def exitOffsetClause(self, ctx:GqlParser.OffsetClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#offsetSynonym.
    def enterOffsetSynonym(self, ctx:GqlParser.OffsetSynonymContext):
        pass

    # Exit a parse tree produced by GqlParser#offsetSynonym.
    def exitOffsetSynonym(self, ctx:GqlParser.OffsetSynonymContext):
        pass


    # Enter a parse tree produced by GqlParser#nestedGraphTypeSpecification.
    def enterNestedGraphTypeSpecification(self, ctx:GqlParser.NestedGraphTypeSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#nestedGraphTypeSpecification.
    def exitNestedGraphTypeSpecification(self, ctx:GqlParser.NestedGraphTypeSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#graphTypeSpecificationBody.
    def enterGraphTypeSpecificationBody(self, ctx:GqlParser.GraphTypeSpecificationBodyContext):
        pass

    # Exit a parse tree produced by GqlParser#graphTypeSpecificationBody.
    def exitGraphTypeSpecificationBody(self, ctx:GqlParser.GraphTypeSpecificationBodyContext):
        pass


    # Enter a parse tree produced by GqlParser#elementTypeDefinitionList.
    def enterElementTypeDefinitionList(self, ctx:GqlParser.ElementTypeDefinitionListContext):
        pass

    # Exit a parse tree produced by GqlParser#elementTypeDefinitionList.
    def exitElementTypeDefinitionList(self, ctx:GqlParser.ElementTypeDefinitionListContext):
        pass


    # Enter a parse tree produced by GqlParser#elementTypeDefinition.
    def enterElementTypeDefinition(self, ctx:GqlParser.ElementTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#elementTypeDefinition.
    def exitElementTypeDefinition(self, ctx:GqlParser.ElementTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypeDefinition.
    def enterNodeTypeDefinition(self, ctx:GqlParser.NodeTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypeDefinition.
    def exitNodeTypeDefinition(self, ctx:GqlParser.NodeTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypePattern.
    def enterNodeTypePattern(self, ctx:GqlParser.NodeTypePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypePattern.
    def exitNodeTypePattern(self, ctx:GqlParser.NodeTypePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypePhrase.
    def enterNodeTypePhrase(self, ctx:GqlParser.NodeTypePhraseContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypePhrase.
    def exitNodeTypePhrase(self, ctx:GqlParser.NodeTypePhraseContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypeName.
    def enterNodeTypeName(self, ctx:GqlParser.NodeTypeNameContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypeName.
    def exitNodeTypeName(self, ctx:GqlParser.NodeTypeNameContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypeFiller.
    def enterNodeTypeFiller(self, ctx:GqlParser.NodeTypeFillerContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypeFiller.
    def exitNodeTypeFiller(self, ctx:GqlParser.NodeTypeFillerContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypeLabelSetDefinition.
    def enterNodeTypeLabelSetDefinition(self, ctx:GqlParser.NodeTypeLabelSetDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypeLabelSetDefinition.
    def exitNodeTypeLabelSetDefinition(self, ctx:GqlParser.NodeTypeLabelSetDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypePropertyTypeSetDefinition.
    def enterNodeTypePropertyTypeSetDefinition(self, ctx:GqlParser.NodeTypePropertyTypeSetDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypePropertyTypeSetDefinition.
    def exitNodeTypePropertyTypeSetDefinition(self, ctx:GqlParser.NodeTypePropertyTypeSetDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeTypeDefinition.
    def enterEdgeTypeDefinition(self, ctx:GqlParser.EdgeTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeTypeDefinition.
    def exitEdgeTypeDefinition(self, ctx:GqlParser.EdgeTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeTypePattern.
    def enterEdgeTypePattern(self, ctx:GqlParser.EdgeTypePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeTypePattern.
    def exitEdgeTypePattern(self, ctx:GqlParser.EdgeTypePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeTypePhrase.
    def enterEdgeTypePhrase(self, ctx:GqlParser.EdgeTypePhraseContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeTypePhrase.
    def exitEdgeTypePhrase(self, ctx:GqlParser.EdgeTypePhraseContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeTypeName.
    def enterEdgeTypeName(self, ctx:GqlParser.EdgeTypeNameContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeTypeName.
    def exitEdgeTypeName(self, ctx:GqlParser.EdgeTypeNameContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeTypeFiller.
    def enterEdgeTypeFiller(self, ctx:GqlParser.EdgeTypeFillerContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeTypeFiller.
    def exitEdgeTypeFiller(self, ctx:GqlParser.EdgeTypeFillerContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeTypeLabelSetDefinition.
    def enterEdgeTypeLabelSetDefinition(self, ctx:GqlParser.EdgeTypeLabelSetDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeTypeLabelSetDefinition.
    def exitEdgeTypeLabelSetDefinition(self, ctx:GqlParser.EdgeTypeLabelSetDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeTypePropertyTypeSetDefinition.
    def enterEdgeTypePropertyTypeSetDefinition(self, ctx:GqlParser.EdgeTypePropertyTypeSetDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeTypePropertyTypeSetDefinition.
    def exitEdgeTypePropertyTypeSetDefinition(self, ctx:GqlParser.EdgeTypePropertyTypeSetDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeTypePattern.
    def enterFullEdgeTypePattern(self, ctx:GqlParser.FullEdgeTypePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeTypePattern.
    def exitFullEdgeTypePattern(self, ctx:GqlParser.FullEdgeTypePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeTypePatternPointingRight.
    def enterFullEdgeTypePatternPointingRight(self, ctx:GqlParser.FullEdgeTypePatternPointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeTypePatternPointingRight.
    def exitFullEdgeTypePatternPointingRight(self, ctx:GqlParser.FullEdgeTypePatternPointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeTypePatternPointingLeft.
    def enterFullEdgeTypePatternPointingLeft(self, ctx:GqlParser.FullEdgeTypePatternPointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeTypePatternPointingLeft.
    def exitFullEdgeTypePatternPointingLeft(self, ctx:GqlParser.FullEdgeTypePatternPointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#fullEdgeTypePatternUndirected.
    def enterFullEdgeTypePatternUndirected(self, ctx:GqlParser.FullEdgeTypePatternUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#fullEdgeTypePatternUndirected.
    def exitFullEdgeTypePatternUndirected(self, ctx:GqlParser.FullEdgeTypePatternUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#arcTypePointingRight.
    def enterArcTypePointingRight(self, ctx:GqlParser.ArcTypePointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#arcTypePointingRight.
    def exitArcTypePointingRight(self, ctx:GqlParser.ArcTypePointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#arcTypePointingLeft.
    def enterArcTypePointingLeft(self, ctx:GqlParser.ArcTypePointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#arcTypePointingLeft.
    def exitArcTypePointingLeft(self, ctx:GqlParser.ArcTypePointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#arcTypeUndirected.
    def enterArcTypeUndirected(self, ctx:GqlParser.ArcTypeUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#arcTypeUndirected.
    def exitArcTypeUndirected(self, ctx:GqlParser.ArcTypeUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#arcTypeFiller.
    def enterArcTypeFiller(self, ctx:GqlParser.ArcTypeFillerContext):
        pass

    # Exit a parse tree produced by GqlParser#arcTypeFiller.
    def exitArcTypeFiller(self, ctx:GqlParser.ArcTypeFillerContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeTypePattern.
    def enterAbbreviatedEdgeTypePattern(self, ctx:GqlParser.AbbreviatedEdgeTypePatternContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeTypePattern.
    def exitAbbreviatedEdgeTypePattern(self, ctx:GqlParser.AbbreviatedEdgeTypePatternContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeTypePatternPointingRight.
    def enterAbbreviatedEdgeTypePatternPointingRight(self, ctx:GqlParser.AbbreviatedEdgeTypePatternPointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeTypePatternPointingRight.
    def exitAbbreviatedEdgeTypePatternPointingRight(self, ctx:GqlParser.AbbreviatedEdgeTypePatternPointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeTypePatternPointingLeft.
    def enterAbbreviatedEdgeTypePatternPointingLeft(self, ctx:GqlParser.AbbreviatedEdgeTypePatternPointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeTypePatternPointingLeft.
    def exitAbbreviatedEdgeTypePatternPointingLeft(self, ctx:GqlParser.AbbreviatedEdgeTypePatternPointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#abbreviatedEdgeTypePatternUndirected.
    def enterAbbreviatedEdgeTypePatternUndirected(self, ctx:GqlParser.AbbreviatedEdgeTypePatternUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#abbreviatedEdgeTypePatternUndirected.
    def exitAbbreviatedEdgeTypePatternUndirected(self, ctx:GqlParser.AbbreviatedEdgeTypePatternUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeTypeReference.
    def enterNodeTypeReference(self, ctx:GqlParser.NodeTypeReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeTypeReference.
    def exitNodeTypeReference(self, ctx:GqlParser.NodeTypeReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#sourceNodeTypeReference.
    def enterSourceNodeTypeReference(self, ctx:GqlParser.SourceNodeTypeReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#sourceNodeTypeReference.
    def exitSourceNodeTypeReference(self, ctx:GqlParser.SourceNodeTypeReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#destinationNodeTypeReference.
    def enterDestinationNodeTypeReference(self, ctx:GqlParser.DestinationNodeTypeReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#destinationNodeTypeReference.
    def exitDestinationNodeTypeReference(self, ctx:GqlParser.DestinationNodeTypeReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeKind.
    def enterEdgeKind(self, ctx:GqlParser.EdgeKindContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeKind.
    def exitEdgeKind(self, ctx:GqlParser.EdgeKindContext):
        pass


    # Enter a parse tree produced by GqlParser#endpointDefinition.
    def enterEndpointDefinition(self, ctx:GqlParser.EndpointDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#endpointDefinition.
    def exitEndpointDefinition(self, ctx:GqlParser.EndpointDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#endpointPairDefinition.
    def enterEndpointPairDefinition(self, ctx:GqlParser.EndpointPairDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#endpointPairDefinition.
    def exitEndpointPairDefinition(self, ctx:GqlParser.EndpointPairDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#endpointPairDefinitionPointingRight.
    def enterEndpointPairDefinitionPointingRight(self, ctx:GqlParser.EndpointPairDefinitionPointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#endpointPairDefinitionPointingRight.
    def exitEndpointPairDefinitionPointingRight(self, ctx:GqlParser.EndpointPairDefinitionPointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#endpointPairDefinitionPointingLeft.
    def enterEndpointPairDefinitionPointingLeft(self, ctx:GqlParser.EndpointPairDefinitionPointingLeftContext):
        pass

    # Exit a parse tree produced by GqlParser#endpointPairDefinitionPointingLeft.
    def exitEndpointPairDefinitionPointingLeft(self, ctx:GqlParser.EndpointPairDefinitionPointingLeftContext):
        pass


    # Enter a parse tree produced by GqlParser#endpointPairDefinitionUndirected.
    def enterEndpointPairDefinitionUndirected(self, ctx:GqlParser.EndpointPairDefinitionUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#endpointPairDefinitionUndirected.
    def exitEndpointPairDefinitionUndirected(self, ctx:GqlParser.EndpointPairDefinitionUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#connectorPointingRight.
    def enterConnectorPointingRight(self, ctx:GqlParser.ConnectorPointingRightContext):
        pass

    # Exit a parse tree produced by GqlParser#connectorPointingRight.
    def exitConnectorPointingRight(self, ctx:GqlParser.ConnectorPointingRightContext):
        pass


    # Enter a parse tree produced by GqlParser#connectorUndirected.
    def enterConnectorUndirected(self, ctx:GqlParser.ConnectorUndirectedContext):
        pass

    # Exit a parse tree produced by GqlParser#connectorUndirected.
    def exitConnectorUndirected(self, ctx:GqlParser.ConnectorUndirectedContext):
        pass


    # Enter a parse tree produced by GqlParser#sourceNodeTypeName.
    def enterSourceNodeTypeName(self, ctx:GqlParser.SourceNodeTypeNameContext):
        pass

    # Exit a parse tree produced by GqlParser#sourceNodeTypeName.
    def exitSourceNodeTypeName(self, ctx:GqlParser.SourceNodeTypeNameContext):
        pass


    # Enter a parse tree produced by GqlParser#destinationNodeTypeName.
    def enterDestinationNodeTypeName(self, ctx:GqlParser.DestinationNodeTypeNameContext):
        pass

    # Exit a parse tree produced by GqlParser#destinationNodeTypeName.
    def exitDestinationNodeTypeName(self, ctx:GqlParser.DestinationNodeTypeNameContext):
        pass


    # Enter a parse tree produced by GqlParser#labelSetDefinition.
    def enterLabelSetDefinition(self, ctx:GqlParser.LabelSetDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#labelSetDefinition.
    def exitLabelSetDefinition(self, ctx:GqlParser.LabelSetDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyTypeSetDefinition.
    def enterPropertyTypeSetDefinition(self, ctx:GqlParser.PropertyTypeSetDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyTypeSetDefinition.
    def exitPropertyTypeSetDefinition(self, ctx:GqlParser.PropertyTypeSetDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyTypeDefinitionList.
    def enterPropertyTypeDefinitionList(self, ctx:GqlParser.PropertyTypeDefinitionListContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyTypeDefinitionList.
    def exitPropertyTypeDefinitionList(self, ctx:GqlParser.PropertyTypeDefinitionListContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyTypeDefinition.
    def enterPropertyTypeDefinition(self, ctx:GqlParser.PropertyTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyTypeDefinition.
    def exitPropertyTypeDefinition(self, ctx:GqlParser.PropertyTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyValueType.
    def enterPropertyValueType(self, ctx:GqlParser.PropertyValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyValueType.
    def exitPropertyValueType(self, ctx:GqlParser.PropertyValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableType.
    def enterBindingTableType(self, ctx:GqlParser.BindingTableTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableType.
    def exitBindingTableType(self, ctx:GqlParser.BindingTableTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#dynamicPropertyValueType.
    def enterDynamicPropertyValueType(self, ctx:GqlParser.DynamicPropertyValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#dynamicPropertyValueType.
    def exitDynamicPropertyValueType(self, ctx:GqlParser.DynamicPropertyValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#predefType.
    def enterPredefType(self, ctx:GqlParser.PredefTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#predefType.
    def exitPredefType(self, ctx:GqlParser.PredefTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#listType1.
    def enterListType1(self, ctx:GqlParser.ListType1Context):
        pass

    # Exit a parse tree produced by GqlParser#listType1.
    def exitListType1(self, ctx:GqlParser.ListType1Context):
        pass


    # Enter a parse tree produced by GqlParser#recordType1.
    def enterRecordType1(self, ctx:GqlParser.RecordType1Context):
        pass

    # Exit a parse tree produced by GqlParser#recordType1.
    def exitRecordType1(self, ctx:GqlParser.RecordType1Context):
        pass


    # Enter a parse tree produced by GqlParser#closedDynamicUnionType2.
    def enterClosedDynamicUnionType2(self, ctx:GqlParser.ClosedDynamicUnionType2Context):
        pass

    # Exit a parse tree produced by GqlParser#closedDynamicUnionType2.
    def exitClosedDynamicUnionType2(self, ctx:GqlParser.ClosedDynamicUnionType2Context):
        pass


    # Enter a parse tree produced by GqlParser#recordType2.
    def enterRecordType2(self, ctx:GqlParser.RecordType2Context):
        pass

    # Exit a parse tree produced by GqlParser#recordType2.
    def exitRecordType2(self, ctx:GqlParser.RecordType2Context):
        pass


    # Enter a parse tree produced by GqlParser#listType2.
    def enterListType2(self, ctx:GqlParser.ListType2Context):
        pass

    # Exit a parse tree produced by GqlParser#listType2.
    def exitListType2(self, ctx:GqlParser.ListType2Context):
        pass


    # Enter a parse tree produced by GqlParser#pathType.
    def enterPathType(self, ctx:GqlParser.PathTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#pathType.
    def exitPathType(self, ctx:GqlParser.PathTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#openDynamicUnionType.
    def enterOpenDynamicUnionType(self, ctx:GqlParser.OpenDynamicUnionTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#openDynamicUnionType.
    def exitOpenDynamicUnionType(self, ctx:GqlParser.OpenDynamicUnionTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#closedDynamicUnionType1.
    def enterClosedDynamicUnionType1(self, ctx:GqlParser.ClosedDynamicUnionType1Context):
        pass

    # Exit a parse tree produced by GqlParser#closedDynamicUnionType1.
    def exitClosedDynamicUnionType1(self, ctx:GqlParser.ClosedDynamicUnionType1Context):
        pass


    # Enter a parse tree produced by GqlParser#typed.
    def enterTyped(self, ctx:GqlParser.TypedContext):
        pass

    # Exit a parse tree produced by GqlParser#typed.
    def exitTyped(self, ctx:GqlParser.TypedContext):
        pass


    # Enter a parse tree produced by GqlParser#predefinedType.
    def enterPredefinedType(self, ctx:GqlParser.PredefinedTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#predefinedType.
    def exitPredefinedType(self, ctx:GqlParser.PredefinedTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#booleanType.
    def enterBooleanType(self, ctx:GqlParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#booleanType.
    def exitBooleanType(self, ctx:GqlParser.BooleanTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#characterStringType.
    def enterCharacterStringType(self, ctx:GqlParser.CharacterStringTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#characterStringType.
    def exitCharacterStringType(self, ctx:GqlParser.CharacterStringTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#byteStringType.
    def enterByteStringType(self, ctx:GqlParser.ByteStringTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#byteStringType.
    def exitByteStringType(self, ctx:GqlParser.ByteStringTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#minLength.
    def enterMinLength(self, ctx:GqlParser.MinLengthContext):
        pass

    # Exit a parse tree produced by GqlParser#minLength.
    def exitMinLength(self, ctx:GqlParser.MinLengthContext):
        pass


    # Enter a parse tree produced by GqlParser#maxLength.
    def enterMaxLength(self, ctx:GqlParser.MaxLengthContext):
        pass

    # Exit a parse tree produced by GqlParser#maxLength.
    def exitMaxLength(self, ctx:GqlParser.MaxLengthContext):
        pass


    # Enter a parse tree produced by GqlParser#fixedLength.
    def enterFixedLength(self, ctx:GqlParser.FixedLengthContext):
        pass

    # Exit a parse tree produced by GqlParser#fixedLength.
    def exitFixedLength(self, ctx:GqlParser.FixedLengthContext):
        pass


    # Enter a parse tree produced by GqlParser#numericType.
    def enterNumericType(self, ctx:GqlParser.NumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#numericType.
    def exitNumericType(self, ctx:GqlParser.NumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#exactNumericType.
    def enterExactNumericType(self, ctx:GqlParser.ExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#exactNumericType.
    def exitExactNumericType(self, ctx:GqlParser.ExactNumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#binaryExactNumericType.
    def enterBinaryExactNumericType(self, ctx:GqlParser.BinaryExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#binaryExactNumericType.
    def exitBinaryExactNumericType(self, ctx:GqlParser.BinaryExactNumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#signedBinaryExactNumericType.
    def enterSignedBinaryExactNumericType(self, ctx:GqlParser.SignedBinaryExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#signedBinaryExactNumericType.
    def exitSignedBinaryExactNumericType(self, ctx:GqlParser.SignedBinaryExactNumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#unsignedBinaryExactNumericType.
    def enterUnsignedBinaryExactNumericType(self, ctx:GqlParser.UnsignedBinaryExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#unsignedBinaryExactNumericType.
    def exitUnsignedBinaryExactNumericType(self, ctx:GqlParser.UnsignedBinaryExactNumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#verboseBinaryExactNumericType.
    def enterVerboseBinaryExactNumericType(self, ctx:GqlParser.VerboseBinaryExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#verboseBinaryExactNumericType.
    def exitVerboseBinaryExactNumericType(self, ctx:GqlParser.VerboseBinaryExactNumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#decimalExactNumericType.
    def enterDecimalExactNumericType(self, ctx:GqlParser.DecimalExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#decimalExactNumericType.
    def exitDecimalExactNumericType(self, ctx:GqlParser.DecimalExactNumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#precision.
    def enterPrecision(self, ctx:GqlParser.PrecisionContext):
        pass

    # Exit a parse tree produced by GqlParser#precision.
    def exitPrecision(self, ctx:GqlParser.PrecisionContext):
        pass


    # Enter a parse tree produced by GqlParser#scale.
    def enterScale(self, ctx:GqlParser.ScaleContext):
        pass

    # Exit a parse tree produced by GqlParser#scale.
    def exitScale(self, ctx:GqlParser.ScaleContext):
        pass


    # Enter a parse tree produced by GqlParser#approximateNumericType.
    def enterApproximateNumericType(self, ctx:GqlParser.ApproximateNumericTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#approximateNumericType.
    def exitApproximateNumericType(self, ctx:GqlParser.ApproximateNumericTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#temporalType.
    def enterTemporalType(self, ctx:GqlParser.TemporalTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#temporalType.
    def exitTemporalType(self, ctx:GqlParser.TemporalTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#temporalInstantType.
    def enterTemporalInstantType(self, ctx:GqlParser.TemporalInstantTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#temporalInstantType.
    def exitTemporalInstantType(self, ctx:GqlParser.TemporalInstantTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#temporalDurationType.
    def enterTemporalDurationType(self, ctx:GqlParser.TemporalDurationTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#temporalDurationType.
    def exitTemporalDurationType(self, ctx:GqlParser.TemporalDurationTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#datetimeType.
    def enterDatetimeType(self, ctx:GqlParser.DatetimeTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#datetimeType.
    def exitDatetimeType(self, ctx:GqlParser.DatetimeTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#localdatetimeType.
    def enterLocaldatetimeType(self, ctx:GqlParser.LocaldatetimeTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#localdatetimeType.
    def exitLocaldatetimeType(self, ctx:GqlParser.LocaldatetimeTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#dateType.
    def enterDateType(self, ctx:GqlParser.DateTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#dateType.
    def exitDateType(self, ctx:GqlParser.DateTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#timeType.
    def enterTimeType(self, ctx:GqlParser.TimeTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#timeType.
    def exitTimeType(self, ctx:GqlParser.TimeTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#localtimeType.
    def enterLocaltimeType(self, ctx:GqlParser.LocaltimeTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#localtimeType.
    def exitLocaltimeType(self, ctx:GqlParser.LocaltimeTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#durationType.
    def enterDurationType(self, ctx:GqlParser.DurationTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#durationType.
    def exitDurationType(self, ctx:GqlParser.DurationTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#referenceValueType.
    def enterReferenceValueType(self, ctx:GqlParser.ReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#referenceValueType.
    def exitReferenceValueType(self, ctx:GqlParser.ReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#graphReferenceValueType.
    def enterGraphReferenceValueType(self, ctx:GqlParser.GraphReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#graphReferenceValueType.
    def exitGraphReferenceValueType(self, ctx:GqlParser.GraphReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#closedGraphReferenceValueType.
    def enterClosedGraphReferenceValueType(self, ctx:GqlParser.ClosedGraphReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#closedGraphReferenceValueType.
    def exitClosedGraphReferenceValueType(self, ctx:GqlParser.ClosedGraphReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#openGraphReferenceValueType.
    def enterOpenGraphReferenceValueType(self, ctx:GqlParser.OpenGraphReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#openGraphReferenceValueType.
    def exitOpenGraphReferenceValueType(self, ctx:GqlParser.OpenGraphReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableReferenceValueType.
    def enterBindingTableReferenceValueType(self, ctx:GqlParser.BindingTableReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableReferenceValueType.
    def exitBindingTableReferenceValueType(self, ctx:GqlParser.BindingTableReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#nodeReferenceValueType.
    def enterNodeReferenceValueType(self, ctx:GqlParser.NodeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#nodeReferenceValueType.
    def exitNodeReferenceValueType(self, ctx:GqlParser.NodeReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#closedNodeReferenceValueType.
    def enterClosedNodeReferenceValueType(self, ctx:GqlParser.ClosedNodeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#closedNodeReferenceValueType.
    def exitClosedNodeReferenceValueType(self, ctx:GqlParser.ClosedNodeReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#openNodeReferenceValueType.
    def enterOpenNodeReferenceValueType(self, ctx:GqlParser.OpenNodeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#openNodeReferenceValueType.
    def exitOpenNodeReferenceValueType(self, ctx:GqlParser.OpenNodeReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#edgeReferenceValueType.
    def enterEdgeReferenceValueType(self, ctx:GqlParser.EdgeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#edgeReferenceValueType.
    def exitEdgeReferenceValueType(self, ctx:GqlParser.EdgeReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#closedEdgeReferenceValueType.
    def enterClosedEdgeReferenceValueType(self, ctx:GqlParser.ClosedEdgeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#closedEdgeReferenceValueType.
    def exitClosedEdgeReferenceValueType(self, ctx:GqlParser.ClosedEdgeReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#openEdgeReferenceValueType.
    def enterOpenEdgeReferenceValueType(self, ctx:GqlParser.OpenEdgeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#openEdgeReferenceValueType.
    def exitOpenEdgeReferenceValueType(self, ctx:GqlParser.OpenEdgeReferenceValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#listValueTypeName.
    def enterListValueTypeName(self, ctx:GqlParser.ListValueTypeNameContext):
        pass

    # Exit a parse tree produced by GqlParser#listValueTypeName.
    def exitListValueTypeName(self, ctx:GqlParser.ListValueTypeNameContext):
        pass


    # Enter a parse tree produced by GqlParser#listValueTypeNameSynonym.
    def enterListValueTypeNameSynonym(self, ctx:GqlParser.ListValueTypeNameSynonymContext):
        pass

    # Exit a parse tree produced by GqlParser#listValueTypeNameSynonym.
    def exitListValueTypeNameSynonym(self, ctx:GqlParser.ListValueTypeNameSynonymContext):
        pass


    # Enter a parse tree produced by GqlParser#fieldTypesSpecification.
    def enterFieldTypesSpecification(self, ctx:GqlParser.FieldTypesSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#fieldTypesSpecification.
    def exitFieldTypesSpecification(self, ctx:GqlParser.FieldTypesSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#fieldTypeList.
    def enterFieldTypeList(self, ctx:GqlParser.FieldTypeListContext):
        pass

    # Exit a parse tree produced by GqlParser#fieldTypeList.
    def exitFieldTypeList(self, ctx:GqlParser.FieldTypeListContext):
        pass


    # Enter a parse tree produced by GqlParser#pathValueType.
    def enterPathValueType(self, ctx:GqlParser.PathValueTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#pathValueType.
    def exitPathValueType(self, ctx:GqlParser.PathValueTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#notNull.
    def enterNotNull(self, ctx:GqlParser.NotNullContext):
        pass

    # Exit a parse tree produced by GqlParser#notNull.
    def exitNotNull(self, ctx:GqlParser.NotNullContext):
        pass


    # Enter a parse tree produced by GqlParser#fieldType.
    def enterFieldType(self, ctx:GqlParser.FieldTypeContext):
        pass

    # Exit a parse tree produced by GqlParser#fieldType.
    def exitFieldType(self, ctx:GqlParser.FieldTypeContext):
        pass


    # Enter a parse tree produced by GqlParser#schemaReference.
    def enterSchemaReference(self, ctx:GqlParser.SchemaReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#schemaReference.
    def exitSchemaReference(self, ctx:GqlParser.SchemaReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#absoluteCatalogSchemaReference.
    def enterAbsoluteCatalogSchemaReference(self, ctx:GqlParser.AbsoluteCatalogSchemaReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#absoluteCatalogSchemaReference.
    def exitAbsoluteCatalogSchemaReference(self, ctx:GqlParser.AbsoluteCatalogSchemaReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#catalogSchemaParentAndName.
    def enterCatalogSchemaParentAndName(self, ctx:GqlParser.CatalogSchemaParentAndNameContext):
        pass

    # Exit a parse tree produced by GqlParser#catalogSchemaParentAndName.
    def exitCatalogSchemaParentAndName(self, ctx:GqlParser.CatalogSchemaParentAndNameContext):
        pass


    # Enter a parse tree produced by GqlParser#relativeCatalogSchemaReference.
    def enterRelativeCatalogSchemaReference(self, ctx:GqlParser.RelativeCatalogSchemaReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#relativeCatalogSchemaReference.
    def exitRelativeCatalogSchemaReference(self, ctx:GqlParser.RelativeCatalogSchemaReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#predefinedSchemaReference.
    def enterPredefinedSchemaReference(self, ctx:GqlParser.PredefinedSchemaReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#predefinedSchemaReference.
    def exitPredefinedSchemaReference(self, ctx:GqlParser.PredefinedSchemaReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#absoluteDirectoryPath.
    def enterAbsoluteDirectoryPath(self, ctx:GqlParser.AbsoluteDirectoryPathContext):
        pass

    # Exit a parse tree produced by GqlParser#absoluteDirectoryPath.
    def exitAbsoluteDirectoryPath(self, ctx:GqlParser.AbsoluteDirectoryPathContext):
        pass


    # Enter a parse tree produced by GqlParser#relativeDirectoryPath.
    def enterRelativeDirectoryPath(self, ctx:GqlParser.RelativeDirectoryPathContext):
        pass

    # Exit a parse tree produced by GqlParser#relativeDirectoryPath.
    def exitRelativeDirectoryPath(self, ctx:GqlParser.RelativeDirectoryPathContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleDirectoryPath.
    def enterSimpleDirectoryPath(self, ctx:GqlParser.SimpleDirectoryPathContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleDirectoryPath.
    def exitSimpleDirectoryPath(self, ctx:GqlParser.SimpleDirectoryPathContext):
        pass


    # Enter a parse tree produced by GqlParser#graphReference.
    def enterGraphReference(self, ctx:GqlParser.GraphReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#graphReference.
    def exitGraphReference(self, ctx:GqlParser.GraphReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#catalogGraphParentAndName.
    def enterCatalogGraphParentAndName(self, ctx:GqlParser.CatalogGraphParentAndNameContext):
        pass

    # Exit a parse tree produced by GqlParser#catalogGraphParentAndName.
    def exitCatalogGraphParentAndName(self, ctx:GqlParser.CatalogGraphParentAndNameContext):
        pass


    # Enter a parse tree produced by GqlParser#homeGraph.
    def enterHomeGraph(self, ctx:GqlParser.HomeGraphContext):
        pass

    # Exit a parse tree produced by GqlParser#homeGraph.
    def exitHomeGraph(self, ctx:GqlParser.HomeGraphContext):
        pass


    # Enter a parse tree produced by GqlParser#graphTypeReference.
    def enterGraphTypeReference(self, ctx:GqlParser.GraphTypeReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#graphTypeReference.
    def exitGraphTypeReference(self, ctx:GqlParser.GraphTypeReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#catalogGraphTypeParentAndName.
    def enterCatalogGraphTypeParentAndName(self, ctx:GqlParser.CatalogGraphTypeParentAndNameContext):
        pass

    # Exit a parse tree produced by GqlParser#catalogGraphTypeParentAndName.
    def exitCatalogGraphTypeParentAndName(self, ctx:GqlParser.CatalogGraphTypeParentAndNameContext):
        pass


    # Enter a parse tree produced by GqlParser#bindingTableReference.
    def enterBindingTableReference(self, ctx:GqlParser.BindingTableReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#bindingTableReference.
    def exitBindingTableReference(self, ctx:GqlParser.BindingTableReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#catalogBindingTableParentAndName.
    def enterCatalogBindingTableParentAndName(self, ctx:GqlParser.CatalogBindingTableParentAndNameContext):
        pass

    # Exit a parse tree produced by GqlParser#catalogBindingTableParentAndName.
    def exitCatalogBindingTableParentAndName(self, ctx:GqlParser.CatalogBindingTableParentAndNameContext):
        pass


    # Enter a parse tree produced by GqlParser#procedureReference.
    def enterProcedureReference(self, ctx:GqlParser.ProcedureReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#procedureReference.
    def exitProcedureReference(self, ctx:GqlParser.ProcedureReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#catalogProcedureParentAndName.
    def enterCatalogProcedureParentAndName(self, ctx:GqlParser.CatalogProcedureParentAndNameContext):
        pass

    # Exit a parse tree produced by GqlParser#catalogProcedureParentAndName.
    def exitCatalogProcedureParentAndName(self, ctx:GqlParser.CatalogProcedureParentAndNameContext):
        pass


    # Enter a parse tree produced by GqlParser#catalogObjectParentReference.
    def enterCatalogObjectParentReference(self, ctx:GqlParser.CatalogObjectParentReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#catalogObjectParentReference.
    def exitCatalogObjectParentReference(self, ctx:GqlParser.CatalogObjectParentReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#referenceParameter.
    def enterReferenceParameter(self, ctx:GqlParser.ReferenceParameterContext):
        pass

    # Exit a parse tree produced by GqlParser#referenceParameter.
    def exitReferenceParameter(self, ctx:GqlParser.ReferenceParameterContext):
        pass


    # Enter a parse tree produced by GqlParser#externalObjectReference.
    def enterExternalObjectReference(self, ctx:GqlParser.ExternalObjectReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#externalObjectReference.
    def exitExternalObjectReference(self, ctx:GqlParser.ExternalObjectReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#comparisonPredicateCond.
    def enterComparisonPredicateCond(self, ctx:GqlParser.ComparisonPredicateCondContext):
        pass

    # Exit a parse tree produced by GqlParser#comparisonPredicateCond.
    def exitComparisonPredicateCond(self, ctx:GqlParser.ComparisonPredicateCondContext):
        pass


    # Enter a parse tree produced by GqlParser#compOp.
    def enterCompOp(self, ctx:GqlParser.CompOpContext):
        pass

    # Exit a parse tree produced by GqlParser#compOp.
    def exitCompOp(self, ctx:GqlParser.CompOpContext):
        pass


    # Enter a parse tree produced by GqlParser#nullPredicateCond.
    def enterNullPredicateCond(self, ctx:GqlParser.NullPredicateCondContext):
        pass

    # Exit a parse tree produced by GqlParser#nullPredicateCond.
    def exitNullPredicateCond(self, ctx:GqlParser.NullPredicateCondContext):
        pass


    # Enter a parse tree produced by GqlParser#normalizedPredicateCond.
    def enterNormalizedPredicateCond(self, ctx:GqlParser.NormalizedPredicateCondContext):
        pass

    # Exit a parse tree produced by GqlParser#normalizedPredicateCond.
    def exitNormalizedPredicateCond(self, ctx:GqlParser.NormalizedPredicateCondContext):
        pass


    # Enter a parse tree produced by GqlParser#directedPredicateCond.
    def enterDirectedPredicateCond(self, ctx:GqlParser.DirectedPredicateCondContext):
        pass

    # Exit a parse tree produced by GqlParser#directedPredicateCond.
    def exitDirectedPredicateCond(self, ctx:GqlParser.DirectedPredicateCondContext):
        pass


    # Enter a parse tree produced by GqlParser#labeledPredicateCond.
    def enterLabeledPredicateCond(self, ctx:GqlParser.LabeledPredicateCondContext):
        pass

    # Exit a parse tree produced by GqlParser#labeledPredicateCond.
    def exitLabeledPredicateCond(self, ctx:GqlParser.LabeledPredicateCondContext):
        pass


    # Enter a parse tree produced by GqlParser#sourceDestinationPredicateCond.
    def enterSourceDestinationPredicateCond(self, ctx:GqlParser.SourceDestinationPredicateCondContext):
        pass

    # Exit a parse tree produced by GqlParser#sourceDestinationPredicateCond.
    def exitSourceDestinationPredicateCond(self, ctx:GqlParser.SourceDestinationPredicateCondContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlPredicateExpression.
    def enterGqlPredicateExpression(self, ctx:GqlParser.GqlPredicateExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlPredicateExpression.
    def exitGqlPredicateExpression(self, ctx:GqlParser.GqlPredicateExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlNotExpression.
    def enterGqlNotExpression(self, ctx:GqlParser.GqlNotExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlNotExpression.
    def exitGqlNotExpression(self, ctx:GqlParser.GqlNotExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLogicalXorExpression.
    def enterGqlLogicalXorExpression(self, ctx:GqlParser.GqlLogicalXorExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLogicalXorExpression.
    def exitGqlLogicalXorExpression(self, ctx:GqlParser.GqlLogicalXorExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLogicalOrExpression.
    def enterGqlLogicalOrExpression(self, ctx:GqlParser.GqlLogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLogicalOrExpression.
    def exitGqlLogicalOrExpression(self, ctx:GqlParser.GqlLogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLogicalAndExpression.
    def enterGqlLogicalAndExpression(self, ctx:GqlParser.GqlLogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLogicalAndExpression.
    def exitGqlLogicalAndExpression(self, ctx:GqlParser.GqlLogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlAtomExpression.
    def enterGqlAtomExpression(self, ctx:GqlParser.GqlAtomExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlAtomExpression.
    def exitGqlAtomExpression(self, ctx:GqlParser.GqlAtomExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlNormalizedExpression.
    def enterGqlNormalizedExpression(self, ctx:GqlParser.GqlNormalizedExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlNormalizedExpression.
    def exitGqlNormalizedExpression(self, ctx:GqlParser.GqlNormalizedExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlSameExpression.
    def enterGqlSameExpression(self, ctx:GqlParser.GqlSameExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlSameExpression.
    def exitGqlSameExpression(self, ctx:GqlParser.GqlSameExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlDirectedExpression.
    def enterGqlDirectedExpression(self, ctx:GqlParser.GqlDirectedExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlDirectedExpression.
    def exitGqlDirectedExpression(self, ctx:GqlParser.GqlDirectedExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBetweenExpression.
    def enterGqlBetweenExpression(self, ctx:GqlParser.GqlBetweenExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBetweenExpression.
    def exitGqlBetweenExpression(self, ctx:GqlParser.GqlBetweenExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBooleanTestExpression.
    def enterGqlBooleanTestExpression(self, ctx:GqlParser.GqlBooleanTestExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBooleanTestExpression.
    def exitGqlBooleanTestExpression(self, ctx:GqlParser.GqlBooleanTestExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlGraphRefValueExpression.
    def enterGqlGraphRefValueExpression(self, ctx:GqlParser.GqlGraphRefValueExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlGraphRefValueExpression.
    def exitGqlGraphRefValueExpression(self, ctx:GqlParser.GqlGraphRefValueExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlAllDifferentExpression.
    def enterGqlAllDifferentExpression(self, ctx:GqlParser.GqlAllDifferentExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlAllDifferentExpression.
    def exitGqlAllDifferentExpression(self, ctx:GqlParser.GqlAllDifferentExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlInExpression.
    def enterGqlInExpression(self, ctx:GqlParser.GqlInExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlInExpression.
    def exitGqlInExpression(self, ctx:GqlParser.GqlInExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlExistsExpression.
    def enterGqlExistsExpression(self, ctx:GqlParser.GqlExistsExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlExistsExpression.
    def exitGqlExistsExpression(self, ctx:GqlParser.GqlExistsExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLetExpression.
    def enterGqlLetExpression(self, ctx:GqlParser.GqlLetExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLetExpression.
    def exitGqlLetExpression(self, ctx:GqlParser.GqlLetExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlComparisonExpression.
    def enterGqlComparisonExpression(self, ctx:GqlParser.GqlComparisonExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlComparisonExpression.
    def exitGqlComparisonExpression(self, ctx:GqlParser.GqlComparisonExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLikeExpression.
    def enterGqlLikeExpression(self, ctx:GqlParser.GqlLikeExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLikeExpression.
    def exitGqlLikeExpression(self, ctx:GqlParser.GqlLikeExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLabeledExpression.
    def enterGqlLabeledExpression(self, ctx:GqlParser.GqlLabeledExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLabeledExpression.
    def exitGqlLabeledExpression(self, ctx:GqlParser.GqlLabeledExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlPropertyExistExpression.
    def enterGqlPropertyExistExpression(self, ctx:GqlParser.GqlPropertyExistExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlPropertyExistExpression.
    def exitGqlPropertyExistExpression(self, ctx:GqlParser.GqlPropertyExistExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlNullExpression.
    def enterGqlNullExpression(self, ctx:GqlParser.GqlNullExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlNullExpression.
    def exitGqlNullExpression(self, ctx:GqlParser.GqlNullExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlSourceDestinationExpression.
    def enterGqlSourceDestinationExpression(self, ctx:GqlParser.GqlSourceDestinationExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlSourceDestinationExpression.
    def exitGqlSourceDestinationExpression(self, ctx:GqlParser.GqlSourceDestinationExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBindingTableValueExpression.
    def enterGqlBindingTableValueExpression(self, ctx:GqlParser.GqlBindingTableValueExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBindingTableValueExpression.
    def exitGqlBindingTableValueExpression(self, ctx:GqlParser.GqlBindingTableValueExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlUnaryExpression.
    def enterGqlUnaryExpression(self, ctx:GqlParser.GqlUnaryExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlUnaryExpression.
    def exitGqlUnaryExpression(self, ctx:GqlParser.GqlUnaryExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBitXorExpression.
    def enterGqlBitXorExpression(self, ctx:GqlParser.GqlBitXorExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBitXorExpression.
    def exitGqlBitXorExpression(self, ctx:GqlParser.GqlBitXorExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBitShiftExpression.
    def enterGqlBitShiftExpression(self, ctx:GqlParser.GqlBitShiftExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBitShiftExpression.
    def exitGqlBitShiftExpression(self, ctx:GqlParser.GqlBitShiftExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlCollectionExpression.
    def enterGqlCollectionExpression(self, ctx:GqlParser.GqlCollectionExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlCollectionExpression.
    def exitGqlCollectionExpression(self, ctx:GqlParser.GqlCollectionExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlParenthesizedExpression.
    def enterGqlParenthesizedExpression(self, ctx:GqlParser.GqlParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlParenthesizedExpression.
    def exitGqlParenthesizedExpression(self, ctx:GqlParser.GqlParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlFunctionExpression.
    def enterGqlFunctionExpression(self, ctx:GqlParser.GqlFunctionExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlFunctionExpression.
    def exitGqlFunctionExpression(self, ctx:GqlParser.GqlFunctionExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlVariableExpression.
    def enterGqlVariableExpression(self, ctx:GqlParser.GqlVariableExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlVariableExpression.
    def exitGqlVariableExpression(self, ctx:GqlParser.GqlVariableExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlParameterExpression.
    def enterGqlParameterExpression(self, ctx:GqlParser.GqlParameterExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlParameterExpression.
    def exitGqlParameterExpression(self, ctx:GqlParser.GqlParameterExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlPropertyReference.
    def enterGqlPropertyReference(self, ctx:GqlParser.GqlPropertyReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlPropertyReference.
    def exitGqlPropertyReference(self, ctx:GqlParser.GqlPropertyReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlHighArithmeticExpression.
    def enterGqlHighArithmeticExpression(self, ctx:GqlParser.GqlHighArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlHighArithmeticExpression.
    def exitGqlHighArithmeticExpression(self, ctx:GqlParser.GqlHighArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBitOrExpression.
    def enterGqlBitOrExpression(self, ctx:GqlParser.GqlBitOrExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBitOrExpression.
    def exitGqlBitOrExpression(self, ctx:GqlParser.GqlBitOrExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlSubscriptExpression.
    def enterGqlSubscriptExpression(self, ctx:GqlParser.GqlSubscriptExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlSubscriptExpression.
    def exitGqlSubscriptExpression(self, ctx:GqlParser.GqlSubscriptExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlBitAndExpression.
    def enterGqlBitAndExpression(self, ctx:GqlParser.GqlBitAndExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlBitAndExpression.
    def exitGqlBitAndExpression(self, ctx:GqlParser.GqlBitAndExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlValueQueryExpression.
    def enterGqlValueQueryExpression(self, ctx:GqlParser.GqlValueQueryExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlValueQueryExpression.
    def exitGqlValueQueryExpression(self, ctx:GqlParser.GqlValueQueryExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLiteralExpression.
    def enterGqlLiteralExpression(self, ctx:GqlParser.GqlLiteralExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLiteralExpression.
    def exitGqlLiteralExpression(self, ctx:GqlParser.GqlLiteralExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLowArithmeticExpression.
    def enterGqlLowArithmeticExpression(self, ctx:GqlParser.GqlLowArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLowArithmeticExpression.
    def exitGqlLowArithmeticExpression(self, ctx:GqlParser.GqlLowArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by GqlParser#truthValue.
    def enterTruthValue(self, ctx:GqlParser.TruthValueContext):
        pass

    # Exit a parse tree produced by GqlParser#truthValue.
    def exitTruthValue(self, ctx:GqlParser.TruthValueContext):
        pass


    # Enter a parse tree produced by GqlParser#unaryOperator.
    def enterUnaryOperator(self, ctx:GqlParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by GqlParser#unaryOperator.
    def exitUnaryOperator(self, ctx:GqlParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by GqlParser#functionCall.
    def enterFunctionCall(self, ctx:GqlParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by GqlParser#functionCall.
    def exitFunctionCall(self, ctx:GqlParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlOneArgScalarFunction.
    def enterGqlOneArgScalarFunction(self, ctx:GqlParser.GqlOneArgScalarFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlOneArgScalarFunction.
    def exitGqlOneArgScalarFunction(self, ctx:GqlParser.GqlOneArgScalarFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlTwoArgScalarFunction.
    def enterGqlTwoArgScalarFunction(self, ctx:GqlParser.GqlTwoArgScalarFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlTwoArgScalarFunction.
    def exitGqlTwoArgScalarFunction(self, ctx:GqlParser.GqlTwoArgScalarFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlIfFunction.
    def enterGqlIfFunction(self, ctx:GqlParser.GqlIfFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlIfFunction.
    def exitGqlIfFunction(self, ctx:GqlParser.GqlIfFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#functionParameter.
    def enterFunctionParameter(self, ctx:GqlParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by GqlParser#functionParameter.
    def exitFunctionParameter(self, ctx:GqlParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by GqlParser#propertyReference.
    def enterPropertyReference(self, ctx:GqlParser.PropertyReferenceContext):
        pass

    # Exit a parse tree produced by GqlParser#propertyReference.
    def exitPropertyReference(self, ctx:GqlParser.PropertyReferenceContext):
        pass


    # Enter a parse tree produced by GqlParser#oneArgNumericFunctionName.
    def enterOneArgNumericFunctionName(self, ctx:GqlParser.OneArgNumericFunctionNameContext):
        pass

    # Exit a parse tree produced by GqlParser#oneArgNumericFunctionName.
    def exitOneArgNumericFunctionName(self, ctx:GqlParser.OneArgNumericFunctionNameContext):
        pass


    # Enter a parse tree produced by GqlParser#twoArgNumericFunctionName.
    def enterTwoArgNumericFunctionName(self, ctx:GqlParser.TwoArgNumericFunctionNameContext):
        pass

    # Exit a parse tree produced by GqlParser#twoArgNumericFunctionName.
    def exitTwoArgNumericFunctionName(self, ctx:GqlParser.TwoArgNumericFunctionNameContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlSubstringFunction.
    def enterGqlSubstringFunction(self, ctx:GqlParser.GqlSubstringFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlSubstringFunction.
    def exitGqlSubstringFunction(self, ctx:GqlParser.GqlSubstringFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlLeftStringFunction.
    def enterGqlLeftStringFunction(self, ctx:GqlParser.GqlLeftStringFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlLeftStringFunction.
    def exitGqlLeftStringFunction(self, ctx:GqlParser.GqlLeftStringFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlRightStringFunction.
    def enterGqlRightStringFunction(self, ctx:GqlParser.GqlRightStringFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlRightStringFunction.
    def exitGqlRightStringFunction(self, ctx:GqlParser.GqlRightStringFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlFoldStringFunction.
    def enterGqlFoldStringFunction(self, ctx:GqlParser.GqlFoldStringFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlFoldStringFunction.
    def exitGqlFoldStringFunction(self, ctx:GqlParser.GqlFoldStringFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlSingleTrimStringFunction.
    def enterGqlSingleTrimStringFunction(self, ctx:GqlParser.GqlSingleTrimStringFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlSingleTrimStringFunction.
    def exitGqlSingleTrimStringFunction(self, ctx:GqlParser.GqlSingleTrimStringFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlMultiTrimStringFunction.
    def enterGqlMultiTrimStringFunction(self, ctx:GqlParser.GqlMultiTrimStringFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlMultiTrimStringFunction.
    def exitGqlMultiTrimStringFunction(self, ctx:GqlParser.GqlMultiTrimStringFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlNormStringFunction.
    def enterGqlNormStringFunction(self, ctx:GqlParser.GqlNormStringFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlNormStringFunction.
    def exitGqlNormStringFunction(self, ctx:GqlParser.GqlNormStringFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlListTrimFunction.
    def enterGqlListTrimFunction(self, ctx:GqlParser.GqlListTrimFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlListTrimFunction.
    def exitGqlListTrimFunction(self, ctx:GqlParser.GqlListTrimFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlElementsOfPathFunction.
    def enterGqlElementsOfPathFunction(self, ctx:GqlParser.GqlElementsOfPathFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlElementsOfPathFunction.
    def exitGqlElementsOfPathFunction(self, ctx:GqlParser.GqlElementsOfPathFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlNullIfCaseFunction.
    def enterGqlNullIfCaseFunction(self, ctx:GqlParser.GqlNullIfCaseFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlNullIfCaseFunction.
    def exitGqlNullIfCaseFunction(self, ctx:GqlParser.GqlNullIfCaseFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlCoalesceCaseFunction.
    def enterGqlCoalesceCaseFunction(self, ctx:GqlParser.GqlCoalesceCaseFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlCoalesceCaseFunction.
    def exitGqlCoalesceCaseFunction(self, ctx:GqlParser.GqlCoalesceCaseFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlSimpleCaseFunction.
    def enterGqlSimpleCaseFunction(self, ctx:GqlParser.GqlSimpleCaseFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlSimpleCaseFunction.
    def exitGqlSimpleCaseFunction(self, ctx:GqlParser.GqlSimpleCaseFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlSearchedCaseFunction.
    def enterGqlSearchedCaseFunction(self, ctx:GqlParser.GqlSearchedCaseFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlSearchedCaseFunction.
    def exitGqlSearchedCaseFunction(self, ctx:GqlParser.GqlSearchedCaseFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#simpleWhenClause.
    def enterSimpleWhenClause(self, ctx:GqlParser.SimpleWhenClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#simpleWhenClause.
    def exitSimpleWhenClause(self, ctx:GqlParser.SimpleWhenClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#searchedWhenClause.
    def enterSearchedWhenClause(self, ctx:GqlParser.SearchedWhenClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#searchedWhenClause.
    def exitSearchedWhenClause(self, ctx:GqlParser.SearchedWhenClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#elseClause.
    def enterElseClause(self, ctx:GqlParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by GqlParser#elseClause.
    def exitElseClause(self, ctx:GqlParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by GqlParser#whenOperand.
    def enterWhenOperand(self, ctx:GqlParser.WhenOperandContext):
        pass

    # Exit a parse tree produced by GqlParser#whenOperand.
    def exitWhenOperand(self, ctx:GqlParser.WhenOperandContext):
        pass


    # Enter a parse tree produced by GqlParser#castFunction.
    def enterCastFunction(self, ctx:GqlParser.CastFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#castFunction.
    def exitCastFunction(self, ctx:GqlParser.CastFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#elementFunction.
    def enterElementFunction(self, ctx:GqlParser.ElementFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#elementFunction.
    def exitElementFunction(self, ctx:GqlParser.ElementFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#elementFunctionName.
    def enterElementFunctionName(self, ctx:GqlParser.ElementFunctionNameContext):
        pass

    # Exit a parse tree produced by GqlParser#elementFunctionName.
    def exitElementFunctionName(self, ctx:GqlParser.ElementFunctionNameContext):
        pass


    # Enter a parse tree produced by GqlParser#datetimeValueFunction.
    def enterDatetimeValueFunction(self, ctx:GqlParser.DatetimeValueFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#datetimeValueFunction.
    def exitDatetimeValueFunction(self, ctx:GqlParser.DatetimeValueFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#dateFunction.
    def enterDateFunction(self, ctx:GqlParser.DateFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#dateFunction.
    def exitDateFunction(self, ctx:GqlParser.DateFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#timeFunction.
    def enterTimeFunction(self, ctx:GqlParser.TimeFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#timeFunction.
    def exitTimeFunction(self, ctx:GqlParser.TimeFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#localTimeFunction.
    def enterLocalTimeFunction(self, ctx:GqlParser.LocalTimeFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#localTimeFunction.
    def exitLocalTimeFunction(self, ctx:GqlParser.LocalTimeFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#datetimeFunction.
    def enterDatetimeFunction(self, ctx:GqlParser.DatetimeFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#datetimeFunction.
    def exitDatetimeFunction(self, ctx:GqlParser.DatetimeFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#localDatetimeFunction.
    def enterLocalDatetimeFunction(self, ctx:GqlParser.LocalDatetimeFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#localDatetimeFunction.
    def exitLocalDatetimeFunction(self, ctx:GqlParser.LocalDatetimeFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlDatetimeSubtractionFunction.
    def enterGqlDatetimeSubtractionFunction(self, ctx:GqlParser.GqlDatetimeSubtractionFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlDatetimeSubtractionFunction.
    def exitGqlDatetimeSubtractionFunction(self, ctx:GqlParser.GqlDatetimeSubtractionFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#gqlDurationFunction.
    def enterGqlDurationFunction(self, ctx:GqlParser.GqlDurationFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#gqlDurationFunction.
    def exitGqlDurationFunction(self, ctx:GqlParser.GqlDurationFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#dateFunctionParameters.
    def enterDateFunctionParameters(self, ctx:GqlParser.DateFunctionParametersContext):
        pass

    # Exit a parse tree produced by GqlParser#dateFunctionParameters.
    def exitDateFunctionParameters(self, ctx:GqlParser.DateFunctionParametersContext):
        pass


    # Enter a parse tree produced by GqlParser#timeFunctionParameters.
    def enterTimeFunctionParameters(self, ctx:GqlParser.TimeFunctionParametersContext):
        pass

    # Exit a parse tree produced by GqlParser#timeFunctionParameters.
    def exitTimeFunctionParameters(self, ctx:GqlParser.TimeFunctionParametersContext):
        pass


    # Enter a parse tree produced by GqlParser#datetimeFunctionParameters.
    def enterDatetimeFunctionParameters(self, ctx:GqlParser.DatetimeFunctionParametersContext):
        pass

    # Exit a parse tree produced by GqlParser#datetimeFunctionParameters.
    def exitDatetimeFunctionParameters(self, ctx:GqlParser.DatetimeFunctionParametersContext):
        pass


    # Enter a parse tree produced by GqlParser#dateString.
    def enterDateString(self, ctx:GqlParser.DateStringContext):
        pass

    # Exit a parse tree produced by GqlParser#dateString.
    def exitDateString(self, ctx:GqlParser.DateStringContext):
        pass


    # Enter a parse tree produced by GqlParser#timeString.
    def enterTimeString(self, ctx:GqlParser.TimeStringContext):
        pass

    # Exit a parse tree produced by GqlParser#timeString.
    def exitTimeString(self, ctx:GqlParser.TimeStringContext):
        pass


    # Enter a parse tree produced by GqlParser#datetimeString.
    def enterDatetimeString(self, ctx:GqlParser.DatetimeStringContext):
        pass

    # Exit a parse tree produced by GqlParser#datetimeString.
    def exitDatetimeString(self, ctx:GqlParser.DatetimeStringContext):
        pass


    # Enter a parse tree produced by GqlParser#durationFunctionParameters.
    def enterDurationFunctionParameters(self, ctx:GqlParser.DurationFunctionParametersContext):
        pass

    # Exit a parse tree produced by GqlParser#durationFunctionParameters.
    def exitDurationFunctionParameters(self, ctx:GqlParser.DurationFunctionParametersContext):
        pass


    # Enter a parse tree produced by GqlParser#durationString.
    def enterDurationString(self, ctx:GqlParser.DurationStringContext):
        pass

    # Exit a parse tree produced by GqlParser#durationString.
    def exitDurationString(self, ctx:GqlParser.DurationStringContext):
        pass


    # Enter a parse tree produced by GqlParser#generalFunction.
    def enterGeneralFunction(self, ctx:GqlParser.GeneralFunctionContext):
        pass

    # Exit a parse tree produced by GqlParser#generalFunction.
    def exitGeneralFunction(self, ctx:GqlParser.GeneralFunctionContext):
        pass


    # Enter a parse tree produced by GqlParser#collectionValueConstructor.
    def enterCollectionValueConstructor(self, ctx:GqlParser.CollectionValueConstructorContext):
        pass

    # Exit a parse tree produced by GqlParser#collectionValueConstructor.
    def exitCollectionValueConstructor(self, ctx:GqlParser.CollectionValueConstructorContext):
        pass


    # Enter a parse tree produced by GqlParser#trimSpecification.
    def enterTrimSpecification(self, ctx:GqlParser.TrimSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#trimSpecification.
    def exitTrimSpecification(self, ctx:GqlParser.TrimSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#normalForm.
    def enterNormalForm(self, ctx:GqlParser.NormalFormContext):
        pass

    # Exit a parse tree produced by GqlParser#normalForm.
    def exitNormalForm(self, ctx:GqlParser.NormalFormContext):
        pass


    # Enter a parse tree produced by GqlParser#listValueConstructor.
    def enterListValueConstructor(self, ctx:GqlParser.ListValueConstructorContext):
        pass

    # Exit a parse tree produced by GqlParser#listValueConstructor.
    def exitListValueConstructor(self, ctx:GqlParser.ListValueConstructorContext):
        pass


    # Enter a parse tree produced by GqlParser#listValue.
    def enterListValue(self, ctx:GqlParser.ListValueContext):
        pass

    # Exit a parse tree produced by GqlParser#listValue.
    def exitListValue(self, ctx:GqlParser.ListValueContext):
        pass


    # Enter a parse tree produced by GqlParser#recordValueConstructor.
    def enterRecordValueConstructor(self, ctx:GqlParser.RecordValueConstructorContext):
        pass

    # Exit a parse tree produced by GqlParser#recordValueConstructor.
    def exitRecordValueConstructor(self, ctx:GqlParser.RecordValueConstructorContext):
        pass


    # Enter a parse tree produced by GqlParser#field.
    def enterField(self, ctx:GqlParser.FieldContext):
        pass

    # Exit a parse tree produced by GqlParser#field.
    def exitField(self, ctx:GqlParser.FieldContext):
        pass


    # Enter a parse tree produced by GqlParser#pathValueConstructor.
    def enterPathValueConstructor(self, ctx:GqlParser.PathValueConstructorContext):
        pass

    # Exit a parse tree produced by GqlParser#pathValueConstructor.
    def exitPathValueConstructor(self, ctx:GqlParser.PathValueConstructorContext):
        pass


    # Enter a parse tree produced by GqlParser#mapValueConstructor.
    def enterMapValueConstructor(self, ctx:GqlParser.MapValueConstructorContext):
        pass

    # Exit a parse tree produced by GqlParser#mapValueConstructor.
    def exitMapValueConstructor(self, ctx:GqlParser.MapValueConstructorContext):
        pass


    # Enter a parse tree produced by GqlParser#mapElement.
    def enterMapElement(self, ctx:GqlParser.MapElementContext):
        pass

    # Exit a parse tree produced by GqlParser#mapElement.
    def exitMapElement(self, ctx:GqlParser.MapElementContext):
        pass


    # Enter a parse tree produced by GqlParser#unsignedValueSpecification.
    def enterUnsignedValueSpecification(self, ctx:GqlParser.UnsignedValueSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#unsignedValueSpecification.
    def exitUnsignedValueSpecification(self, ctx:GqlParser.UnsignedValueSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#unsignedIntegerSpecification.
    def enterUnsignedIntegerSpecification(self, ctx:GqlParser.UnsignedIntegerSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#unsignedIntegerSpecification.
    def exitUnsignedIntegerSpecification(self, ctx:GqlParser.UnsignedIntegerSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#unsignedBooleanSpecification.
    def enterUnsignedBooleanSpecification(self, ctx:GqlParser.UnsignedBooleanSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#unsignedBooleanSpecification.
    def exitUnsignedBooleanSpecification(self, ctx:GqlParser.UnsignedBooleanSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#parameterValueSpecification.
    def enterParameterValueSpecification(self, ctx:GqlParser.ParameterValueSpecificationContext):
        pass

    # Exit a parse tree produced by GqlParser#parameterValueSpecification.
    def exitParameterValueSpecification(self, ctx:GqlParser.ParameterValueSpecificationContext):
        pass


    # Enter a parse tree produced by GqlParser#predefinedParameter.
    def enterPredefinedParameter(self, ctx:GqlParser.PredefinedParameterContext):
        pass

    # Exit a parse tree produced by GqlParser#predefinedParameter.
    def exitPredefinedParameter(self, ctx:GqlParser.PredefinedParameterContext):
        pass


    # Enter a parse tree produced by GqlParser#unsignedLiteral.
    def enterUnsignedLiteral(self, ctx:GqlParser.UnsignedLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#unsignedLiteral.
    def exitUnsignedLiteral(self, ctx:GqlParser.UnsignedLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#generalLiteral.
    def enterGeneralLiteral(self, ctx:GqlParser.GeneralLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#generalLiteral.
    def exitGeneralLiteral(self, ctx:GqlParser.GeneralLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#listLiteral.
    def enterListLiteral(self, ctx:GqlParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#listLiteral.
    def exitListLiteral(self, ctx:GqlParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#mapLiteral.
    def enterMapLiteral(self, ctx:GqlParser.MapLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#mapLiteral.
    def exitMapLiteral(self, ctx:GqlParser.MapLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#mapElementLiteral.
    def enterMapElementLiteral(self, ctx:GqlParser.MapElementLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#mapElementLiteral.
    def exitMapElementLiteral(self, ctx:GqlParser.MapElementLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#recordLiteral.
    def enterRecordLiteral(self, ctx:GqlParser.RecordLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#recordLiteral.
    def exitRecordLiteral(self, ctx:GqlParser.RecordLiteralContext):
        pass


    # Enter a parse tree produced by GqlParser#recordFieldLiteral.
    def enterRecordFieldLiteral(self, ctx:GqlParser.RecordFieldLiteralContext):
        pass

    # Exit a parse tree produced by GqlParser#recordFieldLiteral.
    def exitRecordFieldLiteral(self, ctx:GqlParser.RecordFieldLiteralContext):
        pass



del GqlParser