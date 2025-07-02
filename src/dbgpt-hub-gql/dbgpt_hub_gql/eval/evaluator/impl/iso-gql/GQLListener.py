# Generated from ./GQL.g4 by ANTLR 4.13.2
from antlr4 import ParseTreeListener

if "." in __name__:
    from .GQLParser import GQLParser
else:
    from GQLParser import GQLParser


# This class defines a complete listener for a parse tree produced by GQLParser.
class GQLListener(ParseTreeListener):
    # Enter a parse tree produced by GQLParser#gqlProgram.
    def enterGqlProgram(self, ctx: GQLParser.GqlProgramContext):
        pass

    # Exit a parse tree produced by GQLParser#gqlProgram.
    def exitGqlProgram(self, ctx: GQLParser.GqlProgramContext):
        pass

    # Enter a parse tree produced by GQLParser#programActivity.
    def enterProgramActivity(self, ctx: GQLParser.ProgramActivityContext):
        pass

    # Exit a parse tree produced by GQLParser#programActivity.
    def exitProgramActivity(self, ctx: GQLParser.ProgramActivityContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionActivity.
    def enterSessionActivity(self, ctx: GQLParser.SessionActivityContext):
        pass

    # Exit a parse tree produced by GQLParser#sessionActivity.
    def exitSessionActivity(self, ctx: GQLParser.SessionActivityContext):
        pass

    # Enter a parse tree produced by GQLParser#transactionActivity.
    def enterTransactionActivity(self, ctx: GQLParser.TransactionActivityContext):
        pass

    # Exit a parse tree produced by GQLParser#transactionActivity.
    def exitTransactionActivity(self, ctx: GQLParser.TransactionActivityContext):
        pass

    # Enter a parse tree produced by GQLParser#endTransactionCommand.
    def enterEndTransactionCommand(self, ctx: GQLParser.EndTransactionCommandContext):
        pass

    # Exit a parse tree produced by GQLParser#endTransactionCommand.
    def exitEndTransactionCommand(self, ctx: GQLParser.EndTransactionCommandContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetCommand.
    def enterSessionSetCommand(self, ctx: GQLParser.SessionSetCommandContext):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetCommand.
    def exitSessionSetCommand(self, ctx: GQLParser.SessionSetCommandContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetSchemaClause.
    def enterSessionSetSchemaClause(self, ctx: GQLParser.SessionSetSchemaClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetSchemaClause.
    def exitSessionSetSchemaClause(self, ctx: GQLParser.SessionSetSchemaClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetGraphClause.
    def enterSessionSetGraphClause(self, ctx: GQLParser.SessionSetGraphClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetGraphClause.
    def exitSessionSetGraphClause(self, ctx: GQLParser.SessionSetGraphClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetTimeZoneClause.
    def enterSessionSetTimeZoneClause(
        self, ctx: GQLParser.SessionSetTimeZoneClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetTimeZoneClause.
    def exitSessionSetTimeZoneClause(
        self, ctx: GQLParser.SessionSetTimeZoneClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#setTimeZoneValue.
    def enterSetTimeZoneValue(self, ctx: GQLParser.SetTimeZoneValueContext):
        pass

    # Exit a parse tree produced by GQLParser#setTimeZoneValue.
    def exitSetTimeZoneValue(self, ctx: GQLParser.SetTimeZoneValueContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetParameterClause.
    def enterSessionSetParameterClause(
        self, ctx: GQLParser.SessionSetParameterClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetParameterClause.
    def exitSessionSetParameterClause(
        self, ctx: GQLParser.SessionSetParameterClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetGraphParameterClause.
    def enterSessionSetGraphParameterClause(
        self, ctx: GQLParser.SessionSetGraphParameterClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetGraphParameterClause.
    def exitSessionSetGraphParameterClause(
        self, ctx: GQLParser.SessionSetGraphParameterClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetBindingTableParameterClause.
    def enterSessionSetBindingTableParameterClause(
        self, ctx: GQLParser.SessionSetBindingTableParameterClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetBindingTableParameterClause.
    def exitSessionSetBindingTableParameterClause(
        self, ctx: GQLParser.SessionSetBindingTableParameterClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetValueParameterClause.
    def enterSessionSetValueParameterClause(
        self, ctx: GQLParser.SessionSetValueParameterClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetValueParameterClause.
    def exitSessionSetValueParameterClause(
        self, ctx: GQLParser.SessionSetValueParameterClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#sessionSetParameterName.
    def enterSessionSetParameterName(
        self, ctx: GQLParser.SessionSetParameterNameContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sessionSetParameterName.
    def exitSessionSetParameterName(
        self, ctx: GQLParser.SessionSetParameterNameContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#sessionResetCommand.
    def enterSessionResetCommand(self, ctx: GQLParser.SessionResetCommandContext):
        pass

    # Exit a parse tree produced by GQLParser#sessionResetCommand.
    def exitSessionResetCommand(self, ctx: GQLParser.SessionResetCommandContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionResetArguments.
    def enterSessionResetArguments(self, ctx: GQLParser.SessionResetArgumentsContext):
        pass

    # Exit a parse tree produced by GQLParser#sessionResetArguments.
    def exitSessionResetArguments(self, ctx: GQLParser.SessionResetArgumentsContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionCloseCommand.
    def enterSessionCloseCommand(self, ctx: GQLParser.SessionCloseCommandContext):
        pass

    # Exit a parse tree produced by GQLParser#sessionCloseCommand.
    def exitSessionCloseCommand(self, ctx: GQLParser.SessionCloseCommandContext):
        pass

    # Enter a parse tree produced by GQLParser#sessionParameterSpecification.
    def enterSessionParameterSpecification(
        self, ctx: GQLParser.SessionParameterSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sessionParameterSpecification.
    def exitSessionParameterSpecification(
        self, ctx: GQLParser.SessionParameterSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#startTransactionCommand.
    def enterStartTransactionCommand(
        self, ctx: GQLParser.StartTransactionCommandContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#startTransactionCommand.
    def exitStartTransactionCommand(
        self, ctx: GQLParser.StartTransactionCommandContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#transactionCharacteristics.
    def enterTransactionCharacteristics(
        self, ctx: GQLParser.TransactionCharacteristicsContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#transactionCharacteristics.
    def exitTransactionCharacteristics(
        self, ctx: GQLParser.TransactionCharacteristicsContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#transactionMode.
    def enterTransactionMode(self, ctx: GQLParser.TransactionModeContext):
        pass

    # Exit a parse tree produced by GQLParser#transactionMode.
    def exitTransactionMode(self, ctx: GQLParser.TransactionModeContext):
        pass

    # Enter a parse tree produced by GQLParser#transactionAccessMode.
    def enterTransactionAccessMode(self, ctx: GQLParser.TransactionAccessModeContext):
        pass

    # Exit a parse tree produced by GQLParser#transactionAccessMode.
    def exitTransactionAccessMode(self, ctx: GQLParser.TransactionAccessModeContext):
        pass

    # Enter a parse tree produced by GQLParser#rollbackCommand.
    def enterRollbackCommand(self, ctx: GQLParser.RollbackCommandContext):
        pass

    # Exit a parse tree produced by GQLParser#rollbackCommand.
    def exitRollbackCommand(self, ctx: GQLParser.RollbackCommandContext):
        pass

    # Enter a parse tree produced by GQLParser#commitCommand.
    def enterCommitCommand(self, ctx: GQLParser.CommitCommandContext):
        pass

    # Exit a parse tree produced by GQLParser#commitCommand.
    def exitCommitCommand(self, ctx: GQLParser.CommitCommandContext):
        pass

    # Enter a parse tree produced by GQLParser#nestedProcedureSpecification.
    def enterNestedProcedureSpecification(
        self, ctx: GQLParser.NestedProcedureSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nestedProcedureSpecification.
    def exitNestedProcedureSpecification(
        self, ctx: GQLParser.NestedProcedureSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#procedureSpecification.
    def enterProcedureSpecification(self, ctx: GQLParser.ProcedureSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#procedureSpecification.
    def exitProcedureSpecification(self, ctx: GQLParser.ProcedureSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#nestedDataModifyingProcedureSpecification.
    def enterNestedDataModifyingProcedureSpecification(
        self, ctx: GQLParser.NestedDataModifyingProcedureSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nestedDataModifyingProcedureSpecification.
    def exitNestedDataModifyingProcedureSpecification(
        self, ctx: GQLParser.NestedDataModifyingProcedureSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nestedQuerySpecification.
    def enterNestedQuerySpecification(
        self, ctx: GQLParser.NestedQuerySpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nestedQuerySpecification.
    def exitNestedQuerySpecification(
        self, ctx: GQLParser.NestedQuerySpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#procedureBody.
    def enterProcedureBody(self, ctx: GQLParser.ProcedureBodyContext):
        pass

    # Exit a parse tree produced by GQLParser#procedureBody.
    def exitProcedureBody(self, ctx: GQLParser.ProcedureBodyContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingVariableDefinitionBlock.
    def enterBindingVariableDefinitionBlock(
        self, ctx: GQLParser.BindingVariableDefinitionBlockContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#bindingVariableDefinitionBlock.
    def exitBindingVariableDefinitionBlock(
        self, ctx: GQLParser.BindingVariableDefinitionBlockContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#bindingVariableDefinition.
    def enterBindingVariableDefinition(
        self, ctx: GQLParser.BindingVariableDefinitionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#bindingVariableDefinition.
    def exitBindingVariableDefinition(
        self, ctx: GQLParser.BindingVariableDefinitionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#statementBlock.
    def enterStatementBlock(self, ctx: GQLParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by GQLParser#statementBlock.
    def exitStatementBlock(self, ctx: GQLParser.StatementBlockContext):
        pass

    # Enter a parse tree produced by GQLParser#statement.
    def enterStatement(self, ctx: GQLParser.StatementContext):
        pass

    # Exit a parse tree produced by GQLParser#statement.
    def exitStatement(self, ctx: GQLParser.StatementContext):
        pass

    # Enter a parse tree produced by GQLParser#nextStatement.
    def enterNextStatement(self, ctx: GQLParser.NextStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#nextStatement.
    def exitNextStatement(self, ctx: GQLParser.NextStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#graphVariableDefinition.
    def enterGraphVariableDefinition(
        self, ctx: GQLParser.GraphVariableDefinitionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#graphVariableDefinition.
    def exitGraphVariableDefinition(
        self, ctx: GQLParser.GraphVariableDefinitionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#optTypedGraphInitializer.
    def enterOptTypedGraphInitializer(
        self, ctx: GQLParser.OptTypedGraphInitializerContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#optTypedGraphInitializer.
    def exitOptTypedGraphInitializer(
        self, ctx: GQLParser.OptTypedGraphInitializerContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#graphInitializer.
    def enterGraphInitializer(self, ctx: GQLParser.GraphInitializerContext):
        pass

    # Exit a parse tree produced by GQLParser#graphInitializer.
    def exitGraphInitializer(self, ctx: GQLParser.GraphInitializerContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableVariableDefinition.
    def enterBindingTableVariableDefinition(
        self, ctx: GQLParser.BindingTableVariableDefinitionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableVariableDefinition.
    def exitBindingTableVariableDefinition(
        self, ctx: GQLParser.BindingTableVariableDefinitionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#optTypedBindingTableInitializer.
    def enterOptTypedBindingTableInitializer(
        self, ctx: GQLParser.OptTypedBindingTableInitializerContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#optTypedBindingTableInitializer.
    def exitOptTypedBindingTableInitializer(
        self, ctx: GQLParser.OptTypedBindingTableInitializerContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableInitializer.
    def enterBindingTableInitializer(
        self, ctx: GQLParser.BindingTableInitializerContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableInitializer.
    def exitBindingTableInitializer(
        self, ctx: GQLParser.BindingTableInitializerContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#valueVariableDefinition.
    def enterValueVariableDefinition(
        self, ctx: GQLParser.ValueVariableDefinitionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#valueVariableDefinition.
    def exitValueVariableDefinition(
        self, ctx: GQLParser.ValueVariableDefinitionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#optTypedValueInitializer.
    def enterOptTypedValueInitializer(
        self, ctx: GQLParser.OptTypedValueInitializerContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#optTypedValueInitializer.
    def exitOptTypedValueInitializer(
        self, ctx: GQLParser.OptTypedValueInitializerContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#valueInitializer.
    def enterValueInitializer(self, ctx: GQLParser.ValueInitializerContext):
        pass

    # Exit a parse tree produced by GQLParser#valueInitializer.
    def exitValueInitializer(self, ctx: GQLParser.ValueInitializerContext):
        pass

    # Enter a parse tree produced by GQLParser#graphExpression.
    def enterGraphExpression(self, ctx: GQLParser.GraphExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#graphExpression.
    def exitGraphExpression(self, ctx: GQLParser.GraphExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#currentGraph.
    def enterCurrentGraph(self, ctx: GQLParser.CurrentGraphContext):
        pass

    # Exit a parse tree produced by GQLParser#currentGraph.
    def exitCurrentGraph(self, ctx: GQLParser.CurrentGraphContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableExpression.
    def enterBindingTableExpression(self, ctx: GQLParser.BindingTableExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableExpression.
    def exitBindingTableExpression(self, ctx: GQLParser.BindingTableExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#nestedBindingTableQuerySpecification.
    def enterNestedBindingTableQuerySpecification(
        self, ctx: GQLParser.NestedBindingTableQuerySpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nestedBindingTableQuerySpecification.
    def exitNestedBindingTableQuerySpecification(
        self, ctx: GQLParser.NestedBindingTableQuerySpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#objectExpressionPrimary.
    def enterObjectExpressionPrimary(
        self, ctx: GQLParser.ObjectExpressionPrimaryContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#objectExpressionPrimary.
    def exitObjectExpressionPrimary(
        self, ctx: GQLParser.ObjectExpressionPrimaryContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#linearCatalogModifyingStatement.
    def enterLinearCatalogModifyingStatement(
        self, ctx: GQLParser.LinearCatalogModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#linearCatalogModifyingStatement.
    def exitLinearCatalogModifyingStatement(
        self, ctx: GQLParser.LinearCatalogModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simpleCatalogModifyingStatement.
    def enterSimpleCatalogModifyingStatement(
        self, ctx: GQLParser.SimpleCatalogModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simpleCatalogModifyingStatement.
    def exitSimpleCatalogModifyingStatement(
        self, ctx: GQLParser.SimpleCatalogModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#primitiveCatalogModifyingStatement.
    def enterPrimitiveCatalogModifyingStatement(
        self, ctx: GQLParser.PrimitiveCatalogModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#primitiveCatalogModifyingStatement.
    def exitPrimitiveCatalogModifyingStatement(
        self, ctx: GQLParser.PrimitiveCatalogModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#createSchemaStatement.
    def enterCreateSchemaStatement(self, ctx: GQLParser.CreateSchemaStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#createSchemaStatement.
    def exitCreateSchemaStatement(self, ctx: GQLParser.CreateSchemaStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#dropSchemaStatement.
    def enterDropSchemaStatement(self, ctx: GQLParser.DropSchemaStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#dropSchemaStatement.
    def exitDropSchemaStatement(self, ctx: GQLParser.DropSchemaStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#createGraphStatement.
    def enterCreateGraphStatement(self, ctx: GQLParser.CreateGraphStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#createGraphStatement.
    def exitCreateGraphStatement(self, ctx: GQLParser.CreateGraphStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#openGraphType.
    def enterOpenGraphType(self, ctx: GQLParser.OpenGraphTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#openGraphType.
    def exitOpenGraphType(self, ctx: GQLParser.OpenGraphTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#ofGraphType.
    def enterOfGraphType(self, ctx: GQLParser.OfGraphTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#ofGraphType.
    def exitOfGraphType(self, ctx: GQLParser.OfGraphTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#graphTypeLikeGraph.
    def enterGraphTypeLikeGraph(self, ctx: GQLParser.GraphTypeLikeGraphContext):
        pass

    # Exit a parse tree produced by GQLParser#graphTypeLikeGraph.
    def exitGraphTypeLikeGraph(self, ctx: GQLParser.GraphTypeLikeGraphContext):
        pass

    # Enter a parse tree produced by GQLParser#graphSource.
    def enterGraphSource(self, ctx: GQLParser.GraphSourceContext):
        pass

    # Exit a parse tree produced by GQLParser#graphSource.
    def exitGraphSource(self, ctx: GQLParser.GraphSourceContext):
        pass

    # Enter a parse tree produced by GQLParser#dropGraphStatement.
    def enterDropGraphStatement(self, ctx: GQLParser.DropGraphStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#dropGraphStatement.
    def exitDropGraphStatement(self, ctx: GQLParser.DropGraphStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#createGraphTypeStatement.
    def enterCreateGraphTypeStatement(
        self, ctx: GQLParser.CreateGraphTypeStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#createGraphTypeStatement.
    def exitCreateGraphTypeStatement(
        self, ctx: GQLParser.CreateGraphTypeStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#graphTypeSource.
    def enterGraphTypeSource(self, ctx: GQLParser.GraphTypeSourceContext):
        pass

    # Exit a parse tree produced by GQLParser#graphTypeSource.
    def exitGraphTypeSource(self, ctx: GQLParser.GraphTypeSourceContext):
        pass

    # Enter a parse tree produced by GQLParser#copyOfGraphType.
    def enterCopyOfGraphType(self, ctx: GQLParser.CopyOfGraphTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#copyOfGraphType.
    def exitCopyOfGraphType(self, ctx: GQLParser.CopyOfGraphTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#dropGraphTypeStatement.
    def enterDropGraphTypeStatement(self, ctx: GQLParser.DropGraphTypeStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#dropGraphTypeStatement.
    def exitDropGraphTypeStatement(self, ctx: GQLParser.DropGraphTypeStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#callCatalogModifyingProcedureStatement.
    def enterCallCatalogModifyingProcedureStatement(
        self, ctx: GQLParser.CallCatalogModifyingProcedureStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#callCatalogModifyingProcedureStatement.
    def exitCallCatalogModifyingProcedureStatement(
        self, ctx: GQLParser.CallCatalogModifyingProcedureStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#linearDataModifyingStatement.
    def enterLinearDataModifyingStatement(
        self, ctx: GQLParser.LinearDataModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#linearDataModifyingStatement.
    def exitLinearDataModifyingStatement(
        self, ctx: GQLParser.LinearDataModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#focusedLinearDataModifyingStatement.
    def enterFocusedLinearDataModifyingStatement(
        self, ctx: GQLParser.FocusedLinearDataModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedLinearDataModifyingStatement.
    def exitFocusedLinearDataModifyingStatement(
        self, ctx: GQLParser.FocusedLinearDataModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#focusedLinearDataModifyingStatementBody.
    def enterFocusedLinearDataModifyingStatementBody(
        self, ctx: GQLParser.FocusedLinearDataModifyingStatementBodyContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedLinearDataModifyingStatementBody.
    def exitFocusedLinearDataModifyingStatementBody(
        self, ctx: GQLParser.FocusedLinearDataModifyingStatementBodyContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#focusedNestedDataModifyingProcedureSpecification.
    def enterFocusedNestedDataModifyingProcedureSpecification(
        self, ctx: GQLParser.FocusedNestedDataModifyingProcedureSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedNestedDataModifyingProcedureSpecification.
    def exitFocusedNestedDataModifyingProcedureSpecification(
        self, ctx: GQLParser.FocusedNestedDataModifyingProcedureSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#ambientLinearDataModifyingStatement.
    def enterAmbientLinearDataModifyingStatement(
        self, ctx: GQLParser.AmbientLinearDataModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#ambientLinearDataModifyingStatement.
    def exitAmbientLinearDataModifyingStatement(
        self, ctx: GQLParser.AmbientLinearDataModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#ambientLinearDataModifyingStatementBody.
    def enterAmbientLinearDataModifyingStatementBody(
        self, ctx: GQLParser.AmbientLinearDataModifyingStatementBodyContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#ambientLinearDataModifyingStatementBody.
    def exitAmbientLinearDataModifyingStatementBody(
        self, ctx: GQLParser.AmbientLinearDataModifyingStatementBodyContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simpleLinearDataAccessingStatement.
    def enterSimpleLinearDataAccessingStatement(
        self, ctx: GQLParser.SimpleLinearDataAccessingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simpleLinearDataAccessingStatement.
    def exitSimpleLinearDataAccessingStatement(
        self, ctx: GQLParser.SimpleLinearDataAccessingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simpleDataAccessingStatement.
    def enterSimpleDataAccessingStatement(
        self, ctx: GQLParser.SimpleDataAccessingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simpleDataAccessingStatement.
    def exitSimpleDataAccessingStatement(
        self, ctx: GQLParser.SimpleDataAccessingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simpleDataModifyingStatement.
    def enterSimpleDataModifyingStatement(
        self, ctx: GQLParser.SimpleDataModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simpleDataModifyingStatement.
    def exitSimpleDataModifyingStatement(
        self, ctx: GQLParser.SimpleDataModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#primitiveDataModifyingStatement.
    def enterPrimitiveDataModifyingStatement(
        self, ctx: GQLParser.PrimitiveDataModifyingStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#primitiveDataModifyingStatement.
    def exitPrimitiveDataModifyingStatement(
        self, ctx: GQLParser.PrimitiveDataModifyingStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#insertStatement.
    def enterInsertStatement(self, ctx: GQLParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#insertStatement.
    def exitInsertStatement(self, ctx: GQLParser.InsertStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#setStatement.
    def enterSetStatement(self, ctx: GQLParser.SetStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#setStatement.
    def exitSetStatement(self, ctx: GQLParser.SetStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#setItemList.
    def enterSetItemList(self, ctx: GQLParser.SetItemListContext):
        pass

    # Exit a parse tree produced by GQLParser#setItemList.
    def exitSetItemList(self, ctx: GQLParser.SetItemListContext):
        pass

    # Enter a parse tree produced by GQLParser#setItem.
    def enterSetItem(self, ctx: GQLParser.SetItemContext):
        pass

    # Exit a parse tree produced by GQLParser#setItem.
    def exitSetItem(self, ctx: GQLParser.SetItemContext):
        pass

    # Enter a parse tree produced by GQLParser#setPropertyItem.
    def enterSetPropertyItem(self, ctx: GQLParser.SetPropertyItemContext):
        pass

    # Exit a parse tree produced by GQLParser#setPropertyItem.
    def exitSetPropertyItem(self, ctx: GQLParser.SetPropertyItemContext):
        pass

    # Enter a parse tree produced by GQLParser#setAllPropertiesItem.
    def enterSetAllPropertiesItem(self, ctx: GQLParser.SetAllPropertiesItemContext):
        pass

    # Exit a parse tree produced by GQLParser#setAllPropertiesItem.
    def exitSetAllPropertiesItem(self, ctx: GQLParser.SetAllPropertiesItemContext):
        pass

    # Enter a parse tree produced by GQLParser#setLabelItem.
    def enterSetLabelItem(self, ctx: GQLParser.SetLabelItemContext):
        pass

    # Exit a parse tree produced by GQLParser#setLabelItem.
    def exitSetLabelItem(self, ctx: GQLParser.SetLabelItemContext):
        pass

    # Enter a parse tree produced by GQLParser#removeStatement.
    def enterRemoveStatement(self, ctx: GQLParser.RemoveStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#removeStatement.
    def exitRemoveStatement(self, ctx: GQLParser.RemoveStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#removeItemList.
    def enterRemoveItemList(self, ctx: GQLParser.RemoveItemListContext):
        pass

    # Exit a parse tree produced by GQLParser#removeItemList.
    def exitRemoveItemList(self, ctx: GQLParser.RemoveItemListContext):
        pass

    # Enter a parse tree produced by GQLParser#removeItem.
    def enterRemoveItem(self, ctx: GQLParser.RemoveItemContext):
        pass

    # Exit a parse tree produced by GQLParser#removeItem.
    def exitRemoveItem(self, ctx: GQLParser.RemoveItemContext):
        pass

    # Enter a parse tree produced by GQLParser#removePropertyItem.
    def enterRemovePropertyItem(self, ctx: GQLParser.RemovePropertyItemContext):
        pass

    # Exit a parse tree produced by GQLParser#removePropertyItem.
    def exitRemovePropertyItem(self, ctx: GQLParser.RemovePropertyItemContext):
        pass

    # Enter a parse tree produced by GQLParser#removeLabelItem.
    def enterRemoveLabelItem(self, ctx: GQLParser.RemoveLabelItemContext):
        pass

    # Exit a parse tree produced by GQLParser#removeLabelItem.
    def exitRemoveLabelItem(self, ctx: GQLParser.RemoveLabelItemContext):
        pass

    # Enter a parse tree produced by GQLParser#deleteStatement.
    def enterDeleteStatement(self, ctx: GQLParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#deleteStatement.
    def exitDeleteStatement(self, ctx: GQLParser.DeleteStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#deleteItemList.
    def enterDeleteItemList(self, ctx: GQLParser.DeleteItemListContext):
        pass

    # Exit a parse tree produced by GQLParser#deleteItemList.
    def exitDeleteItemList(self, ctx: GQLParser.DeleteItemListContext):
        pass

    # Enter a parse tree produced by GQLParser#deleteItem.
    def enterDeleteItem(self, ctx: GQLParser.DeleteItemContext):
        pass

    # Exit a parse tree produced by GQLParser#deleteItem.
    def exitDeleteItem(self, ctx: GQLParser.DeleteItemContext):
        pass

    # Enter a parse tree produced by GQLParser#callDataModifyingProcedureStatement.
    def enterCallDataModifyingProcedureStatement(
        self, ctx: GQLParser.CallDataModifyingProcedureStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#callDataModifyingProcedureStatement.
    def exitCallDataModifyingProcedureStatement(
        self, ctx: GQLParser.CallDataModifyingProcedureStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#compositeQueryStatement.
    def enterCompositeQueryStatement(
        self, ctx: GQLParser.CompositeQueryStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#compositeQueryStatement.
    def exitCompositeQueryStatement(
        self, ctx: GQLParser.CompositeQueryStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#compositeQueryExpression.
    def enterCompositeQueryExpression(
        self, ctx: GQLParser.CompositeQueryExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#compositeQueryExpression.
    def exitCompositeQueryExpression(
        self, ctx: GQLParser.CompositeQueryExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#queryConjunction.
    def enterQueryConjunction(self, ctx: GQLParser.QueryConjunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#queryConjunction.
    def exitQueryConjunction(self, ctx: GQLParser.QueryConjunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#setOperator.
    def enterSetOperator(self, ctx: GQLParser.SetOperatorContext):
        pass

    # Exit a parse tree produced by GQLParser#setOperator.
    def exitSetOperator(self, ctx: GQLParser.SetOperatorContext):
        pass

    # Enter a parse tree produced by GQLParser#compositeQueryPrimary.
    def enterCompositeQueryPrimary(self, ctx: GQLParser.CompositeQueryPrimaryContext):
        pass

    # Exit a parse tree produced by GQLParser#compositeQueryPrimary.
    def exitCompositeQueryPrimary(self, ctx: GQLParser.CompositeQueryPrimaryContext):
        pass

    # Enter a parse tree produced by GQLParser#linearQueryStatement.
    def enterLinearQueryStatement(self, ctx: GQLParser.LinearQueryStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#linearQueryStatement.
    def exitLinearQueryStatement(self, ctx: GQLParser.LinearQueryStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#focusedLinearQueryStatement.
    def enterFocusedLinearQueryStatement(
        self, ctx: GQLParser.FocusedLinearQueryStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedLinearQueryStatement.
    def exitFocusedLinearQueryStatement(
        self, ctx: GQLParser.FocusedLinearQueryStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#focusedLinearQueryStatementPart.
    def enterFocusedLinearQueryStatementPart(
        self, ctx: GQLParser.FocusedLinearQueryStatementPartContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedLinearQueryStatementPart.
    def exitFocusedLinearQueryStatementPart(
        self, ctx: GQLParser.FocusedLinearQueryStatementPartContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#focusedLinearQueryAndPrimitiveResultStatementPart.
    def enterFocusedLinearQueryAndPrimitiveResultStatementPart(
        self, ctx: GQLParser.FocusedLinearQueryAndPrimitiveResultStatementPartContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedLinearQueryAndPrimitiveResultStatementPart.
    def exitFocusedLinearQueryAndPrimitiveResultStatementPart(
        self, ctx: GQLParser.FocusedLinearQueryAndPrimitiveResultStatementPartContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#focusedPrimitiveResultStatement.
    def enterFocusedPrimitiveResultStatement(
        self, ctx: GQLParser.FocusedPrimitiveResultStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedPrimitiveResultStatement.
    def exitFocusedPrimitiveResultStatement(
        self, ctx: GQLParser.FocusedPrimitiveResultStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#focusedNestedQuerySpecification.
    def enterFocusedNestedQuerySpecification(
        self, ctx: GQLParser.FocusedNestedQuerySpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#focusedNestedQuerySpecification.
    def exitFocusedNestedQuerySpecification(
        self, ctx: GQLParser.FocusedNestedQuerySpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#ambientLinearQueryStatement.
    def enterAmbientLinearQueryStatement(
        self, ctx: GQLParser.AmbientLinearQueryStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#ambientLinearQueryStatement.
    def exitAmbientLinearQueryStatement(
        self, ctx: GQLParser.AmbientLinearQueryStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simpleLinearQueryStatement.
    def enterSimpleLinearQueryStatement(
        self, ctx: GQLParser.SimpleLinearQueryStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simpleLinearQueryStatement.
    def exitSimpleLinearQueryStatement(
        self, ctx: GQLParser.SimpleLinearQueryStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simpleQueryStatement.
    def enterSimpleQueryStatement(self, ctx: GQLParser.SimpleQueryStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#simpleQueryStatement.
    def exitSimpleQueryStatement(self, ctx: GQLParser.SimpleQueryStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#primitiveQueryStatement.
    def enterPrimitiveQueryStatement(
        self, ctx: GQLParser.PrimitiveQueryStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#primitiveQueryStatement.
    def exitPrimitiveQueryStatement(
        self, ctx: GQLParser.PrimitiveQueryStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#matchStatement.
    def enterMatchStatement(self, ctx: GQLParser.MatchStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#matchStatement.
    def exitMatchStatement(self, ctx: GQLParser.MatchStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#simpleMatchStatement.
    def enterSimpleMatchStatement(self, ctx: GQLParser.SimpleMatchStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#simpleMatchStatement.
    def exitSimpleMatchStatement(self, ctx: GQLParser.SimpleMatchStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#optionalMatchStatement.
    def enterOptionalMatchStatement(self, ctx: GQLParser.OptionalMatchStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#optionalMatchStatement.
    def exitOptionalMatchStatement(self, ctx: GQLParser.OptionalMatchStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#optionalOperand.
    def enterOptionalOperand(self, ctx: GQLParser.OptionalOperandContext):
        pass

    # Exit a parse tree produced by GQLParser#optionalOperand.
    def exitOptionalOperand(self, ctx: GQLParser.OptionalOperandContext):
        pass

    # Enter a parse tree produced by GQLParser#matchStatementBlock.
    def enterMatchStatementBlock(self, ctx: GQLParser.MatchStatementBlockContext):
        pass

    # Exit a parse tree produced by GQLParser#matchStatementBlock.
    def exitMatchStatementBlock(self, ctx: GQLParser.MatchStatementBlockContext):
        pass

    # Enter a parse tree produced by GQLParser#callQueryStatement.
    def enterCallQueryStatement(self, ctx: GQLParser.CallQueryStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#callQueryStatement.
    def exitCallQueryStatement(self, ctx: GQLParser.CallQueryStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#filterStatement.
    def enterFilterStatement(self, ctx: GQLParser.FilterStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#filterStatement.
    def exitFilterStatement(self, ctx: GQLParser.FilterStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#letStatement.
    def enterLetStatement(self, ctx: GQLParser.LetStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#letStatement.
    def exitLetStatement(self, ctx: GQLParser.LetStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#letVariableDefinitionList.
    def enterLetVariableDefinitionList(
        self, ctx: GQLParser.LetVariableDefinitionListContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#letVariableDefinitionList.
    def exitLetVariableDefinitionList(
        self, ctx: GQLParser.LetVariableDefinitionListContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#letVariableDefinition.
    def enterLetVariableDefinition(self, ctx: GQLParser.LetVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GQLParser#letVariableDefinition.
    def exitLetVariableDefinition(self, ctx: GQLParser.LetVariableDefinitionContext):
        pass

    # Enter a parse tree produced by GQLParser#forStatement.
    def enterForStatement(self, ctx: GQLParser.ForStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#forStatement.
    def exitForStatement(self, ctx: GQLParser.ForStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#forItem.
    def enterForItem(self, ctx: GQLParser.ForItemContext):
        pass

    # Exit a parse tree produced by GQLParser#forItem.
    def exitForItem(self, ctx: GQLParser.ForItemContext):
        pass

    # Enter a parse tree produced by GQLParser#forItemAlias.
    def enterForItemAlias(self, ctx: GQLParser.ForItemAliasContext):
        pass

    # Exit a parse tree produced by GQLParser#forItemAlias.
    def exitForItemAlias(self, ctx: GQLParser.ForItemAliasContext):
        pass

    # Enter a parse tree produced by GQLParser#forItemSource.
    def enterForItemSource(self, ctx: GQLParser.ForItemSourceContext):
        pass

    # Exit a parse tree produced by GQLParser#forItemSource.
    def exitForItemSource(self, ctx: GQLParser.ForItemSourceContext):
        pass

    # Enter a parse tree produced by GQLParser#forOrdinalityOrOffset.
    def enterForOrdinalityOrOffset(self, ctx: GQLParser.ForOrdinalityOrOffsetContext):
        pass

    # Exit a parse tree produced by GQLParser#forOrdinalityOrOffset.
    def exitForOrdinalityOrOffset(self, ctx: GQLParser.ForOrdinalityOrOffsetContext):
        pass

    # Enter a parse tree produced by GQLParser#orderByAndPageStatement.
    def enterOrderByAndPageStatement(
        self, ctx: GQLParser.OrderByAndPageStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#orderByAndPageStatement.
    def exitOrderByAndPageStatement(
        self, ctx: GQLParser.OrderByAndPageStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#primitiveResultStatement.
    def enterPrimitiveResultStatement(
        self, ctx: GQLParser.PrimitiveResultStatementContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#primitiveResultStatement.
    def exitPrimitiveResultStatement(
        self, ctx: GQLParser.PrimitiveResultStatementContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#returnStatement.
    def enterReturnStatement(self, ctx: GQLParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#returnStatement.
    def exitReturnStatement(self, ctx: GQLParser.ReturnStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#returnStatementBody.
    def enterReturnStatementBody(self, ctx: GQLParser.ReturnStatementBodyContext):
        pass

    # Exit a parse tree produced by GQLParser#returnStatementBody.
    def exitReturnStatementBody(self, ctx: GQLParser.ReturnStatementBodyContext):
        pass

    # Enter a parse tree produced by GQLParser#returnItemList.
    def enterReturnItemList(self, ctx: GQLParser.ReturnItemListContext):
        pass

    # Exit a parse tree produced by GQLParser#returnItemList.
    def exitReturnItemList(self, ctx: GQLParser.ReturnItemListContext):
        pass

    # Enter a parse tree produced by GQLParser#returnItem.
    def enterReturnItem(self, ctx: GQLParser.ReturnItemContext):
        pass

    # Exit a parse tree produced by GQLParser#returnItem.
    def exitReturnItem(self, ctx: GQLParser.ReturnItemContext):
        pass

    # Enter a parse tree produced by GQLParser#returnItemAlias.
    def enterReturnItemAlias(self, ctx: GQLParser.ReturnItemAliasContext):
        pass

    # Exit a parse tree produced by GQLParser#returnItemAlias.
    def exitReturnItemAlias(self, ctx: GQLParser.ReturnItemAliasContext):
        pass

    # Enter a parse tree produced by GQLParser#selectStatement.
    def enterSelectStatement(self, ctx: GQLParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#selectStatement.
    def exitSelectStatement(self, ctx: GQLParser.SelectStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#selectItemList.
    def enterSelectItemList(self, ctx: GQLParser.SelectItemListContext):
        pass

    # Exit a parse tree produced by GQLParser#selectItemList.
    def exitSelectItemList(self, ctx: GQLParser.SelectItemListContext):
        pass

    # Enter a parse tree produced by GQLParser#selectItem.
    def enterSelectItem(self, ctx: GQLParser.SelectItemContext):
        pass

    # Exit a parse tree produced by GQLParser#selectItem.
    def exitSelectItem(self, ctx: GQLParser.SelectItemContext):
        pass

    # Enter a parse tree produced by GQLParser#selectItemAlias.
    def enterSelectItemAlias(self, ctx: GQLParser.SelectItemAliasContext):
        pass

    # Exit a parse tree produced by GQLParser#selectItemAlias.
    def exitSelectItemAlias(self, ctx: GQLParser.SelectItemAliasContext):
        pass

    # Enter a parse tree produced by GQLParser#havingClause.
    def enterHavingClause(self, ctx: GQLParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#havingClause.
    def exitHavingClause(self, ctx: GQLParser.HavingClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#selectStatementBody.
    def enterSelectStatementBody(self, ctx: GQLParser.SelectStatementBodyContext):
        pass

    # Exit a parse tree produced by GQLParser#selectStatementBody.
    def exitSelectStatementBody(self, ctx: GQLParser.SelectStatementBodyContext):
        pass

    # Enter a parse tree produced by GQLParser#selectGraphMatchList.
    def enterSelectGraphMatchList(self, ctx: GQLParser.SelectGraphMatchListContext):
        pass

    # Exit a parse tree produced by GQLParser#selectGraphMatchList.
    def exitSelectGraphMatchList(self, ctx: GQLParser.SelectGraphMatchListContext):
        pass

    # Enter a parse tree produced by GQLParser#selectGraphMatch.
    def enterSelectGraphMatch(self, ctx: GQLParser.SelectGraphMatchContext):
        pass

    # Exit a parse tree produced by GQLParser#selectGraphMatch.
    def exitSelectGraphMatch(self, ctx: GQLParser.SelectGraphMatchContext):
        pass

    # Enter a parse tree produced by GQLParser#selectQuerySpecification.
    def enterSelectQuerySpecification(
        self, ctx: GQLParser.SelectQuerySpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#selectQuerySpecification.
    def exitSelectQuerySpecification(
        self, ctx: GQLParser.SelectQuerySpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#callProcedureStatement.
    def enterCallProcedureStatement(self, ctx: GQLParser.CallProcedureStatementContext):
        pass

    # Exit a parse tree produced by GQLParser#callProcedureStatement.
    def exitCallProcedureStatement(self, ctx: GQLParser.CallProcedureStatementContext):
        pass

    # Enter a parse tree produced by GQLParser#procedureCall.
    def enterProcedureCall(self, ctx: GQLParser.ProcedureCallContext):
        pass

    # Exit a parse tree produced by GQLParser#procedureCall.
    def exitProcedureCall(self, ctx: GQLParser.ProcedureCallContext):
        pass

    # Enter a parse tree produced by GQLParser#inlineProcedureCall.
    def enterInlineProcedureCall(self, ctx: GQLParser.InlineProcedureCallContext):
        pass

    # Exit a parse tree produced by GQLParser#inlineProcedureCall.
    def exitInlineProcedureCall(self, ctx: GQLParser.InlineProcedureCallContext):
        pass

    # Enter a parse tree produced by GQLParser#variableScopeClause.
    def enterVariableScopeClause(self, ctx: GQLParser.VariableScopeClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#variableScopeClause.
    def exitVariableScopeClause(self, ctx: GQLParser.VariableScopeClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingVariableReferenceList.
    def enterBindingVariableReferenceList(
        self, ctx: GQLParser.BindingVariableReferenceListContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#bindingVariableReferenceList.
    def exitBindingVariableReferenceList(
        self, ctx: GQLParser.BindingVariableReferenceListContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#namedProcedureCall.
    def enterNamedProcedureCall(self, ctx: GQLParser.NamedProcedureCallContext):
        pass

    # Exit a parse tree produced by GQLParser#namedProcedureCall.
    def exitNamedProcedureCall(self, ctx: GQLParser.NamedProcedureCallContext):
        pass

    # Enter a parse tree produced by GQLParser#procedureArgumentList.
    def enterProcedureArgumentList(self, ctx: GQLParser.ProcedureArgumentListContext):
        pass

    # Exit a parse tree produced by GQLParser#procedureArgumentList.
    def exitProcedureArgumentList(self, ctx: GQLParser.ProcedureArgumentListContext):
        pass

    # Enter a parse tree produced by GQLParser#procedureArgument.
    def enterProcedureArgument(self, ctx: GQLParser.ProcedureArgumentContext):
        pass

    # Exit a parse tree produced by GQLParser#procedureArgument.
    def exitProcedureArgument(self, ctx: GQLParser.ProcedureArgumentContext):
        pass

    # Enter a parse tree produced by GQLParser#atSchemaClause.
    def enterAtSchemaClause(self, ctx: GQLParser.AtSchemaClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#atSchemaClause.
    def exitAtSchemaClause(self, ctx: GQLParser.AtSchemaClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#useGraphClause.
    def enterUseGraphClause(self, ctx: GQLParser.UseGraphClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#useGraphClause.
    def exitUseGraphClause(self, ctx: GQLParser.UseGraphClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#graphPatternBindingTable.
    def enterGraphPatternBindingTable(
        self, ctx: GQLParser.GraphPatternBindingTableContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#graphPatternBindingTable.
    def exitGraphPatternBindingTable(
        self, ctx: GQLParser.GraphPatternBindingTableContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#graphPatternYieldClause.
    def enterGraphPatternYieldClause(
        self, ctx: GQLParser.GraphPatternYieldClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#graphPatternYieldClause.
    def exitGraphPatternYieldClause(
        self, ctx: GQLParser.GraphPatternYieldClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#graphPatternYieldItemList.
    def enterGraphPatternYieldItemList(
        self, ctx: GQLParser.GraphPatternYieldItemListContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#graphPatternYieldItemList.
    def exitGraphPatternYieldItemList(
        self, ctx: GQLParser.GraphPatternYieldItemListContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#graphPatternYieldItem.
    def enterGraphPatternYieldItem(self, ctx: GQLParser.GraphPatternYieldItemContext):
        pass

    # Exit a parse tree produced by GQLParser#graphPatternYieldItem.
    def exitGraphPatternYieldItem(self, ctx: GQLParser.GraphPatternYieldItemContext):
        pass

    # Enter a parse tree produced by GQLParser#graphPattern.
    def enterGraphPattern(self, ctx: GQLParser.GraphPatternContext):
        pass

    # Exit a parse tree produced by GQLParser#graphPattern.
    def exitGraphPattern(self, ctx: GQLParser.GraphPatternContext):
        pass

    # Enter a parse tree produced by GQLParser#matchMode.
    def enterMatchMode(self, ctx: GQLParser.MatchModeContext):
        pass

    # Exit a parse tree produced by GQLParser#matchMode.
    def exitMatchMode(self, ctx: GQLParser.MatchModeContext):
        pass

    # Enter a parse tree produced by GQLParser#repeatableElementsMatchMode.
    def enterRepeatableElementsMatchMode(
        self, ctx: GQLParser.RepeatableElementsMatchModeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#repeatableElementsMatchMode.
    def exitRepeatableElementsMatchMode(
        self, ctx: GQLParser.RepeatableElementsMatchModeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#differentEdgesMatchMode.
    def enterDifferentEdgesMatchMode(
        self, ctx: GQLParser.DifferentEdgesMatchModeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#differentEdgesMatchMode.
    def exitDifferentEdgesMatchMode(
        self, ctx: GQLParser.DifferentEdgesMatchModeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#elementBindingsOrElements.
    def enterElementBindingsOrElements(
        self, ctx: GQLParser.ElementBindingsOrElementsContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#elementBindingsOrElements.
    def exitElementBindingsOrElements(
        self, ctx: GQLParser.ElementBindingsOrElementsContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeBindingsOrEdges.
    def enterEdgeBindingsOrEdges(self, ctx: GQLParser.EdgeBindingsOrEdgesContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeBindingsOrEdges.
    def exitEdgeBindingsOrEdges(self, ctx: GQLParser.EdgeBindingsOrEdgesContext):
        pass

    # Enter a parse tree produced by GQLParser#pathPatternList.
    def enterPathPatternList(self, ctx: GQLParser.PathPatternListContext):
        pass

    # Exit a parse tree produced by GQLParser#pathPatternList.
    def exitPathPatternList(self, ctx: GQLParser.PathPatternListContext):
        pass

    # Enter a parse tree produced by GQLParser#pathPattern.
    def enterPathPattern(self, ctx: GQLParser.PathPatternContext):
        pass

    # Exit a parse tree produced by GQLParser#pathPattern.
    def exitPathPattern(self, ctx: GQLParser.PathPatternContext):
        pass

    # Enter a parse tree produced by GQLParser#pathVariableDeclaration.
    def enterPathVariableDeclaration(
        self, ctx: GQLParser.PathVariableDeclarationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#pathVariableDeclaration.
    def exitPathVariableDeclaration(
        self, ctx: GQLParser.PathVariableDeclarationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#keepClause.
    def enterKeepClause(self, ctx: GQLParser.KeepClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#keepClause.
    def exitKeepClause(self, ctx: GQLParser.KeepClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#graphPatternWhereClause.
    def enterGraphPatternWhereClause(
        self, ctx: GQLParser.GraphPatternWhereClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#graphPatternWhereClause.
    def exitGraphPatternWhereClause(
        self, ctx: GQLParser.GraphPatternWhereClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#insertGraphPattern.
    def enterInsertGraphPattern(self, ctx: GQLParser.InsertGraphPatternContext):
        pass

    # Exit a parse tree produced by GQLParser#insertGraphPattern.
    def exitInsertGraphPattern(self, ctx: GQLParser.InsertGraphPatternContext):
        pass

    # Enter a parse tree produced by GQLParser#insertPathPatternList.
    def enterInsertPathPatternList(self, ctx: GQLParser.InsertPathPatternListContext):
        pass

    # Exit a parse tree produced by GQLParser#insertPathPatternList.
    def exitInsertPathPatternList(self, ctx: GQLParser.InsertPathPatternListContext):
        pass

    # Enter a parse tree produced by GQLParser#insertPathPattern.
    def enterInsertPathPattern(self, ctx: GQLParser.InsertPathPatternContext):
        pass

    # Exit a parse tree produced by GQLParser#insertPathPattern.
    def exitInsertPathPattern(self, ctx: GQLParser.InsertPathPatternContext):
        pass

    # Enter a parse tree produced by GQLParser#insertNodePattern.
    def enterInsertNodePattern(self, ctx: GQLParser.InsertNodePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#insertNodePattern.
    def exitInsertNodePattern(self, ctx: GQLParser.InsertNodePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#insertEdgePattern.
    def enterInsertEdgePattern(self, ctx: GQLParser.InsertEdgePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#insertEdgePattern.
    def exitInsertEdgePattern(self, ctx: GQLParser.InsertEdgePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#insertEdgePointingLeft.
    def enterInsertEdgePointingLeft(self, ctx: GQLParser.InsertEdgePointingLeftContext):
        pass

    # Exit a parse tree produced by GQLParser#insertEdgePointingLeft.
    def exitInsertEdgePointingLeft(self, ctx: GQLParser.InsertEdgePointingLeftContext):
        pass

    # Enter a parse tree produced by GQLParser#insertEdgePointingRight.
    def enterInsertEdgePointingRight(
        self, ctx: GQLParser.InsertEdgePointingRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#insertEdgePointingRight.
    def exitInsertEdgePointingRight(
        self, ctx: GQLParser.InsertEdgePointingRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#insertEdgeUndirected.
    def enterInsertEdgeUndirected(self, ctx: GQLParser.InsertEdgeUndirectedContext):
        pass

    # Exit a parse tree produced by GQLParser#insertEdgeUndirected.
    def exitInsertEdgeUndirected(self, ctx: GQLParser.InsertEdgeUndirectedContext):
        pass

    # Enter a parse tree produced by GQLParser#insertElementPatternFiller.
    def enterInsertElementPatternFiller(
        self, ctx: GQLParser.InsertElementPatternFillerContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#insertElementPatternFiller.
    def exitInsertElementPatternFiller(
        self, ctx: GQLParser.InsertElementPatternFillerContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelAndPropertySetSpecification.
    def enterLabelAndPropertySetSpecification(
        self, ctx: GQLParser.LabelAndPropertySetSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#labelAndPropertySetSpecification.
    def exitLabelAndPropertySetSpecification(
        self, ctx: GQLParser.LabelAndPropertySetSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#pathPatternPrefix.
    def enterPathPatternPrefix(self, ctx: GQLParser.PathPatternPrefixContext):
        pass

    # Exit a parse tree produced by GQLParser#pathPatternPrefix.
    def exitPathPatternPrefix(self, ctx: GQLParser.PathPatternPrefixContext):
        pass

    # Enter a parse tree produced by GQLParser#pathModePrefix.
    def enterPathModePrefix(self, ctx: GQLParser.PathModePrefixContext):
        pass

    # Exit a parse tree produced by GQLParser#pathModePrefix.
    def exitPathModePrefix(self, ctx: GQLParser.PathModePrefixContext):
        pass

    # Enter a parse tree produced by GQLParser#pathMode.
    def enterPathMode(self, ctx: GQLParser.PathModeContext):
        pass

    # Exit a parse tree produced by GQLParser#pathMode.
    def exitPathMode(self, ctx: GQLParser.PathModeContext):
        pass

    # Enter a parse tree produced by GQLParser#pathSearchPrefix.
    def enterPathSearchPrefix(self, ctx: GQLParser.PathSearchPrefixContext):
        pass

    # Exit a parse tree produced by GQLParser#pathSearchPrefix.
    def exitPathSearchPrefix(self, ctx: GQLParser.PathSearchPrefixContext):
        pass

    # Enter a parse tree produced by GQLParser#allPathSearch.
    def enterAllPathSearch(self, ctx: GQLParser.AllPathSearchContext):
        pass

    # Exit a parse tree produced by GQLParser#allPathSearch.
    def exitAllPathSearch(self, ctx: GQLParser.AllPathSearchContext):
        pass

    # Enter a parse tree produced by GQLParser#pathOrPaths.
    def enterPathOrPaths(self, ctx: GQLParser.PathOrPathsContext):
        pass

    # Exit a parse tree produced by GQLParser#pathOrPaths.
    def exitPathOrPaths(self, ctx: GQLParser.PathOrPathsContext):
        pass

    # Enter a parse tree produced by GQLParser#anyPathSearch.
    def enterAnyPathSearch(self, ctx: GQLParser.AnyPathSearchContext):
        pass

    # Exit a parse tree produced by GQLParser#anyPathSearch.
    def exitAnyPathSearch(self, ctx: GQLParser.AnyPathSearchContext):
        pass

    # Enter a parse tree produced by GQLParser#numberOfPaths.
    def enterNumberOfPaths(self, ctx: GQLParser.NumberOfPathsContext):
        pass

    # Exit a parse tree produced by GQLParser#numberOfPaths.
    def exitNumberOfPaths(self, ctx: GQLParser.NumberOfPathsContext):
        pass

    # Enter a parse tree produced by GQLParser#shortestPathSearch.
    def enterShortestPathSearch(self, ctx: GQLParser.ShortestPathSearchContext):
        pass

    # Exit a parse tree produced by GQLParser#shortestPathSearch.
    def exitShortestPathSearch(self, ctx: GQLParser.ShortestPathSearchContext):
        pass

    # Enter a parse tree produced by GQLParser#allShortestPathSearch.
    def enterAllShortestPathSearch(self, ctx: GQLParser.AllShortestPathSearchContext):
        pass

    # Exit a parse tree produced by GQLParser#allShortestPathSearch.
    def exitAllShortestPathSearch(self, ctx: GQLParser.AllShortestPathSearchContext):
        pass

    # Enter a parse tree produced by GQLParser#anyShortestPathSearch.
    def enterAnyShortestPathSearch(self, ctx: GQLParser.AnyShortestPathSearchContext):
        pass

    # Exit a parse tree produced by GQLParser#anyShortestPathSearch.
    def exitAnyShortestPathSearch(self, ctx: GQLParser.AnyShortestPathSearchContext):
        pass

    # Enter a parse tree produced by GQLParser#countedShortestPathSearch.
    def enterCountedShortestPathSearch(
        self, ctx: GQLParser.CountedShortestPathSearchContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#countedShortestPathSearch.
    def exitCountedShortestPathSearch(
        self, ctx: GQLParser.CountedShortestPathSearchContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#countedShortestGroupSearch.
    def enterCountedShortestGroupSearch(
        self, ctx: GQLParser.CountedShortestGroupSearchContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#countedShortestGroupSearch.
    def exitCountedShortestGroupSearch(
        self, ctx: GQLParser.CountedShortestGroupSearchContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#numberOfGroups.
    def enterNumberOfGroups(self, ctx: GQLParser.NumberOfGroupsContext):
        pass

    # Exit a parse tree produced by GQLParser#numberOfGroups.
    def exitNumberOfGroups(self, ctx: GQLParser.NumberOfGroupsContext):
        pass

    # Enter a parse tree produced by GQLParser#ppePathTerm.
    def enterPpePathTerm(self, ctx: GQLParser.PpePathTermContext):
        pass

    # Exit a parse tree produced by GQLParser#ppePathTerm.
    def exitPpePathTerm(self, ctx: GQLParser.PpePathTermContext):
        pass

    # Enter a parse tree produced by GQLParser#ppeMultisetAlternation.
    def enterPpeMultisetAlternation(self, ctx: GQLParser.PpeMultisetAlternationContext):
        pass

    # Exit a parse tree produced by GQLParser#ppeMultisetAlternation.
    def exitPpeMultisetAlternation(self, ctx: GQLParser.PpeMultisetAlternationContext):
        pass

    # Enter a parse tree produced by GQLParser#ppePatternUnion.
    def enterPpePatternUnion(self, ctx: GQLParser.PpePatternUnionContext):
        pass

    # Exit a parse tree produced by GQLParser#ppePatternUnion.
    def exitPpePatternUnion(self, ctx: GQLParser.PpePatternUnionContext):
        pass

    # Enter a parse tree produced by GQLParser#pathTerm.
    def enterPathTerm(self, ctx: GQLParser.PathTermContext):
        pass

    # Exit a parse tree produced by GQLParser#pathTerm.
    def exitPathTerm(self, ctx: GQLParser.PathTermContext):
        pass

    # Enter a parse tree produced by GQLParser#pfPathPrimary.
    def enterPfPathPrimary(self, ctx: GQLParser.PfPathPrimaryContext):
        pass

    # Exit a parse tree produced by GQLParser#pfPathPrimary.
    def exitPfPathPrimary(self, ctx: GQLParser.PfPathPrimaryContext):
        pass

    # Enter a parse tree produced by GQLParser#pfQuantifiedPathPrimary.
    def enterPfQuantifiedPathPrimary(
        self, ctx: GQLParser.PfQuantifiedPathPrimaryContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#pfQuantifiedPathPrimary.
    def exitPfQuantifiedPathPrimary(
        self, ctx: GQLParser.PfQuantifiedPathPrimaryContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#pfQuestionedPathPrimary.
    def enterPfQuestionedPathPrimary(
        self, ctx: GQLParser.PfQuestionedPathPrimaryContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#pfQuestionedPathPrimary.
    def exitPfQuestionedPathPrimary(
        self, ctx: GQLParser.PfQuestionedPathPrimaryContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#ppElementPattern.
    def enterPpElementPattern(self, ctx: GQLParser.PpElementPatternContext):
        pass

    # Exit a parse tree produced by GQLParser#ppElementPattern.
    def exitPpElementPattern(self, ctx: GQLParser.PpElementPatternContext):
        pass

    # Enter a parse tree produced by GQLParser#ppParenthesizedPathPatternExpression.
    def enterPpParenthesizedPathPatternExpression(
        self, ctx: GQLParser.PpParenthesizedPathPatternExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#ppParenthesizedPathPatternExpression.
    def exitPpParenthesizedPathPatternExpression(
        self, ctx: GQLParser.PpParenthesizedPathPatternExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#ppSimplifiedPathPatternExpression.
    def enterPpSimplifiedPathPatternExpression(
        self, ctx: GQLParser.PpSimplifiedPathPatternExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#ppSimplifiedPathPatternExpression.
    def exitPpSimplifiedPathPatternExpression(
        self, ctx: GQLParser.PpSimplifiedPathPatternExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#elementPattern.
    def enterElementPattern(self, ctx: GQLParser.ElementPatternContext):
        pass

    # Exit a parse tree produced by GQLParser#elementPattern.
    def exitElementPattern(self, ctx: GQLParser.ElementPatternContext):
        pass

    # Enter a parse tree produced by GQLParser#nodePattern.
    def enterNodePattern(self, ctx: GQLParser.NodePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#nodePattern.
    def exitNodePattern(self, ctx: GQLParser.NodePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#elementPatternFiller.
    def enterElementPatternFiller(self, ctx: GQLParser.ElementPatternFillerContext):
        pass

    # Exit a parse tree produced by GQLParser#elementPatternFiller.
    def exitElementPatternFiller(self, ctx: GQLParser.ElementPatternFillerContext):
        pass

    # Enter a parse tree produced by GQLParser#elementVariableDeclaration.
    def enterElementVariableDeclaration(
        self, ctx: GQLParser.ElementVariableDeclarationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#elementVariableDeclaration.
    def exitElementVariableDeclaration(
        self, ctx: GQLParser.ElementVariableDeclarationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#isLabelExpression.
    def enterIsLabelExpression(self, ctx: GQLParser.IsLabelExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#isLabelExpression.
    def exitIsLabelExpression(self, ctx: GQLParser.IsLabelExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#isOrColon.
    def enterIsOrColon(self, ctx: GQLParser.IsOrColonContext):
        pass

    # Exit a parse tree produced by GQLParser#isOrColon.
    def exitIsOrColon(self, ctx: GQLParser.IsOrColonContext):
        pass

    # Enter a parse tree produced by GQLParser#elementPatternPredicate.
    def enterElementPatternPredicate(
        self, ctx: GQLParser.ElementPatternPredicateContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#elementPatternPredicate.
    def exitElementPatternPredicate(
        self, ctx: GQLParser.ElementPatternPredicateContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#elementPatternWhereClause.
    def enterElementPatternWhereClause(
        self, ctx: GQLParser.ElementPatternWhereClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#elementPatternWhereClause.
    def exitElementPatternWhereClause(
        self, ctx: GQLParser.ElementPatternWhereClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#elementPropertySpecification.
    def enterElementPropertySpecification(
        self, ctx: GQLParser.ElementPropertySpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#elementPropertySpecification.
    def exitElementPropertySpecification(
        self, ctx: GQLParser.ElementPropertySpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#propertyKeyValuePairList.
    def enterPropertyKeyValuePairList(
        self, ctx: GQLParser.PropertyKeyValuePairListContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#propertyKeyValuePairList.
    def exitPropertyKeyValuePairList(
        self, ctx: GQLParser.PropertyKeyValuePairListContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#propertyKeyValuePair.
    def enterPropertyKeyValuePair(self, ctx: GQLParser.PropertyKeyValuePairContext):
        pass

    # Exit a parse tree produced by GQLParser#propertyKeyValuePair.
    def exitPropertyKeyValuePair(self, ctx: GQLParser.PropertyKeyValuePairContext):
        pass

    # Enter a parse tree produced by GQLParser#edgePattern.
    def enterEdgePattern(self, ctx: GQLParser.EdgePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#edgePattern.
    def exitEdgePattern(self, ctx: GQLParser.EdgePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgePattern.
    def enterFullEdgePattern(self, ctx: GQLParser.FullEdgePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgePattern.
    def exitFullEdgePattern(self, ctx: GQLParser.FullEdgePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgePointingLeft.
    def enterFullEdgePointingLeft(self, ctx: GQLParser.FullEdgePointingLeftContext):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgePointingLeft.
    def exitFullEdgePointingLeft(self, ctx: GQLParser.FullEdgePointingLeftContext):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgeUndirected.
    def enterFullEdgeUndirected(self, ctx: GQLParser.FullEdgeUndirectedContext):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgeUndirected.
    def exitFullEdgeUndirected(self, ctx: GQLParser.FullEdgeUndirectedContext):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgePointingRight.
    def enterFullEdgePointingRight(self, ctx: GQLParser.FullEdgePointingRightContext):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgePointingRight.
    def exitFullEdgePointingRight(self, ctx: GQLParser.FullEdgePointingRightContext):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgeLeftOrUndirected.
    def enterFullEdgeLeftOrUndirected(
        self, ctx: GQLParser.FullEdgeLeftOrUndirectedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgeLeftOrUndirected.
    def exitFullEdgeLeftOrUndirected(
        self, ctx: GQLParser.FullEdgeLeftOrUndirectedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgeUndirectedOrRight.
    def enterFullEdgeUndirectedOrRight(
        self, ctx: GQLParser.FullEdgeUndirectedOrRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgeUndirectedOrRight.
    def exitFullEdgeUndirectedOrRight(
        self, ctx: GQLParser.FullEdgeUndirectedOrRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgeLeftOrRight.
    def enterFullEdgeLeftOrRight(self, ctx: GQLParser.FullEdgeLeftOrRightContext):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgeLeftOrRight.
    def exitFullEdgeLeftOrRight(self, ctx: GQLParser.FullEdgeLeftOrRightContext):
        pass

    # Enter a parse tree produced by GQLParser#fullEdgeAnyDirection.
    def enterFullEdgeAnyDirection(self, ctx: GQLParser.FullEdgeAnyDirectionContext):
        pass

    # Exit a parse tree produced by GQLParser#fullEdgeAnyDirection.
    def exitFullEdgeAnyDirection(self, ctx: GQLParser.FullEdgeAnyDirectionContext):
        pass

    # Enter a parse tree produced by GQLParser#abbreviatedEdgePattern.
    def enterAbbreviatedEdgePattern(self, ctx: GQLParser.AbbreviatedEdgePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#abbreviatedEdgePattern.
    def exitAbbreviatedEdgePattern(self, ctx: GQLParser.AbbreviatedEdgePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#parenthesizedPathPatternExpression.
    def enterParenthesizedPathPatternExpression(
        self, ctx: GQLParser.ParenthesizedPathPatternExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#parenthesizedPathPatternExpression.
    def exitParenthesizedPathPatternExpression(
        self, ctx: GQLParser.ParenthesizedPathPatternExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#subpathVariableDeclaration.
    def enterSubpathVariableDeclaration(
        self, ctx: GQLParser.SubpathVariableDeclarationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#subpathVariableDeclaration.
    def exitSubpathVariableDeclaration(
        self, ctx: GQLParser.SubpathVariableDeclarationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#parenthesizedPathPatternWhereClause.
    def enterParenthesizedPathPatternWhereClause(
        self, ctx: GQLParser.ParenthesizedPathPatternWhereClauseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#parenthesizedPathPatternWhereClause.
    def exitParenthesizedPathPatternWhereClause(
        self, ctx: GQLParser.ParenthesizedPathPatternWhereClauseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelExpressionNegation.
    def enterLabelExpressionNegation(
        self, ctx: GQLParser.LabelExpressionNegationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#labelExpressionNegation.
    def exitLabelExpressionNegation(
        self, ctx: GQLParser.LabelExpressionNegationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelExpressionDisjunction.
    def enterLabelExpressionDisjunction(
        self, ctx: GQLParser.LabelExpressionDisjunctionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#labelExpressionDisjunction.
    def exitLabelExpressionDisjunction(
        self, ctx: GQLParser.LabelExpressionDisjunctionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelExpressionParenthesized.
    def enterLabelExpressionParenthesized(
        self, ctx: GQLParser.LabelExpressionParenthesizedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#labelExpressionParenthesized.
    def exitLabelExpressionParenthesized(
        self, ctx: GQLParser.LabelExpressionParenthesizedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelExpressionWildcard.
    def enterLabelExpressionWildcard(
        self, ctx: GQLParser.LabelExpressionWildcardContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#labelExpressionWildcard.
    def exitLabelExpressionWildcard(
        self, ctx: GQLParser.LabelExpressionWildcardContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelExpressionConjunction.
    def enterLabelExpressionConjunction(
        self, ctx: GQLParser.LabelExpressionConjunctionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#labelExpressionConjunction.
    def exitLabelExpressionConjunction(
        self, ctx: GQLParser.LabelExpressionConjunctionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelExpressionName.
    def enterLabelExpressionName(self, ctx: GQLParser.LabelExpressionNameContext):
        pass

    # Exit a parse tree produced by GQLParser#labelExpressionName.
    def exitLabelExpressionName(self, ctx: GQLParser.LabelExpressionNameContext):
        pass

    # Enter a parse tree produced by GQLParser#pathVariableReference.
    def enterPathVariableReference(self, ctx: GQLParser.PathVariableReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#pathVariableReference.
    def exitPathVariableReference(self, ctx: GQLParser.PathVariableReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#elementVariableReference.
    def enterElementVariableReference(
        self, ctx: GQLParser.ElementVariableReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#elementVariableReference.
    def exitElementVariableReference(
        self, ctx: GQLParser.ElementVariableReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#graphPatternQuantifier.
    def enterGraphPatternQuantifier(self, ctx: GQLParser.GraphPatternQuantifierContext):
        pass

    # Exit a parse tree produced by GQLParser#graphPatternQuantifier.
    def exitGraphPatternQuantifier(self, ctx: GQLParser.GraphPatternQuantifierContext):
        pass

    # Enter a parse tree produced by GQLParser#fixedQuantifier.
    def enterFixedQuantifier(self, ctx: GQLParser.FixedQuantifierContext):
        pass

    # Exit a parse tree produced by GQLParser#fixedQuantifier.
    def exitFixedQuantifier(self, ctx: GQLParser.FixedQuantifierContext):
        pass

    # Enter a parse tree produced by GQLParser#generalQuantifier.
    def enterGeneralQuantifier(self, ctx: GQLParser.GeneralQuantifierContext):
        pass

    # Exit a parse tree produced by GQLParser#generalQuantifier.
    def exitGeneralQuantifier(self, ctx: GQLParser.GeneralQuantifierContext):
        pass

    # Enter a parse tree produced by GQLParser#lowerBound.
    def enterLowerBound(self, ctx: GQLParser.LowerBoundContext):
        pass

    # Exit a parse tree produced by GQLParser#lowerBound.
    def exitLowerBound(self, ctx: GQLParser.LowerBoundContext):
        pass

    # Enter a parse tree produced by GQLParser#upperBound.
    def enterUpperBound(self, ctx: GQLParser.UpperBoundContext):
        pass

    # Exit a parse tree produced by GQLParser#upperBound.
    def exitUpperBound(self, ctx: GQLParser.UpperBoundContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedPathPatternExpression.
    def enterSimplifiedPathPatternExpression(
        self, ctx: GQLParser.SimplifiedPathPatternExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedPathPatternExpression.
    def exitSimplifiedPathPatternExpression(
        self, ctx: GQLParser.SimplifiedPathPatternExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDefaultingLeft.
    def enterSimplifiedDefaultingLeft(
        self, ctx: GQLParser.SimplifiedDefaultingLeftContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDefaultingLeft.
    def exitSimplifiedDefaultingLeft(
        self, ctx: GQLParser.SimplifiedDefaultingLeftContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDefaultingUndirected.
    def enterSimplifiedDefaultingUndirected(
        self, ctx: GQLParser.SimplifiedDefaultingUndirectedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDefaultingUndirected.
    def exitSimplifiedDefaultingUndirected(
        self, ctx: GQLParser.SimplifiedDefaultingUndirectedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDefaultingRight.
    def enterSimplifiedDefaultingRight(
        self, ctx: GQLParser.SimplifiedDefaultingRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDefaultingRight.
    def exitSimplifiedDefaultingRight(
        self, ctx: GQLParser.SimplifiedDefaultingRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDefaultingLeftOrUndirected.
    def enterSimplifiedDefaultingLeftOrUndirected(
        self, ctx: GQLParser.SimplifiedDefaultingLeftOrUndirectedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDefaultingLeftOrUndirected.
    def exitSimplifiedDefaultingLeftOrUndirected(
        self, ctx: GQLParser.SimplifiedDefaultingLeftOrUndirectedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDefaultingUndirectedOrRight.
    def enterSimplifiedDefaultingUndirectedOrRight(
        self, ctx: GQLParser.SimplifiedDefaultingUndirectedOrRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDefaultingUndirectedOrRight.
    def exitSimplifiedDefaultingUndirectedOrRight(
        self, ctx: GQLParser.SimplifiedDefaultingUndirectedOrRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDefaultingLeftOrRight.
    def enterSimplifiedDefaultingLeftOrRight(
        self, ctx: GQLParser.SimplifiedDefaultingLeftOrRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDefaultingLeftOrRight.
    def exitSimplifiedDefaultingLeftOrRight(
        self, ctx: GQLParser.SimplifiedDefaultingLeftOrRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDefaultingAnyDirection.
    def enterSimplifiedDefaultingAnyDirection(
        self, ctx: GQLParser.SimplifiedDefaultingAnyDirectionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDefaultingAnyDirection.
    def exitSimplifiedDefaultingAnyDirection(
        self, ctx: GQLParser.SimplifiedDefaultingAnyDirectionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedContents.
    def enterSimplifiedContents(self, ctx: GQLParser.SimplifiedContentsContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedContents.
    def exitSimplifiedContents(self, ctx: GQLParser.SimplifiedContentsContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedPathUnion.
    def enterSimplifiedPathUnion(self, ctx: GQLParser.SimplifiedPathUnionContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedPathUnion.
    def exitSimplifiedPathUnion(self, ctx: GQLParser.SimplifiedPathUnionContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedMultisetAlternation.
    def enterSimplifiedMultisetAlternation(
        self, ctx: GQLParser.SimplifiedMultisetAlternationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedMultisetAlternation.
    def exitSimplifiedMultisetAlternation(
        self, ctx: GQLParser.SimplifiedMultisetAlternationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedFactorLowLabel.
    def enterSimplifiedFactorLowLabel(
        self, ctx: GQLParser.SimplifiedFactorLowLabelContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedFactorLowLabel.
    def exitSimplifiedFactorLowLabel(
        self, ctx: GQLParser.SimplifiedFactorLowLabelContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedConcatenationLabel.
    def enterSimplifiedConcatenationLabel(
        self, ctx: GQLParser.SimplifiedConcatenationLabelContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedConcatenationLabel.
    def exitSimplifiedConcatenationLabel(
        self, ctx: GQLParser.SimplifiedConcatenationLabelContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedConjunctionLabel.
    def enterSimplifiedConjunctionLabel(
        self, ctx: GQLParser.SimplifiedConjunctionLabelContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedConjunctionLabel.
    def exitSimplifiedConjunctionLabel(
        self, ctx: GQLParser.SimplifiedConjunctionLabelContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedFactorHighLabel.
    def enterSimplifiedFactorHighLabel(
        self, ctx: GQLParser.SimplifiedFactorHighLabelContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedFactorHighLabel.
    def exitSimplifiedFactorHighLabel(
        self, ctx: GQLParser.SimplifiedFactorHighLabelContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedFactorHigh.
    def enterSimplifiedFactorHigh(self, ctx: GQLParser.SimplifiedFactorHighContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedFactorHigh.
    def exitSimplifiedFactorHigh(self, ctx: GQLParser.SimplifiedFactorHighContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedQuantified.
    def enterSimplifiedQuantified(self, ctx: GQLParser.SimplifiedQuantifiedContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedQuantified.
    def exitSimplifiedQuantified(self, ctx: GQLParser.SimplifiedQuantifiedContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedQuestioned.
    def enterSimplifiedQuestioned(self, ctx: GQLParser.SimplifiedQuestionedContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedQuestioned.
    def exitSimplifiedQuestioned(self, ctx: GQLParser.SimplifiedQuestionedContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedTertiary.
    def enterSimplifiedTertiary(self, ctx: GQLParser.SimplifiedTertiaryContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedTertiary.
    def exitSimplifiedTertiary(self, ctx: GQLParser.SimplifiedTertiaryContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedDirectionOverride.
    def enterSimplifiedDirectionOverride(
        self, ctx: GQLParser.SimplifiedDirectionOverrideContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedDirectionOverride.
    def exitSimplifiedDirectionOverride(
        self, ctx: GQLParser.SimplifiedDirectionOverrideContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedOverrideLeft.
    def enterSimplifiedOverrideLeft(self, ctx: GQLParser.SimplifiedOverrideLeftContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedOverrideLeft.
    def exitSimplifiedOverrideLeft(self, ctx: GQLParser.SimplifiedOverrideLeftContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedOverrideUndirected.
    def enterSimplifiedOverrideUndirected(
        self, ctx: GQLParser.SimplifiedOverrideUndirectedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedOverrideUndirected.
    def exitSimplifiedOverrideUndirected(
        self, ctx: GQLParser.SimplifiedOverrideUndirectedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedOverrideRight.
    def enterSimplifiedOverrideRight(
        self, ctx: GQLParser.SimplifiedOverrideRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedOverrideRight.
    def exitSimplifiedOverrideRight(
        self, ctx: GQLParser.SimplifiedOverrideRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedOverrideLeftOrUndirected.
    def enterSimplifiedOverrideLeftOrUndirected(
        self, ctx: GQLParser.SimplifiedOverrideLeftOrUndirectedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedOverrideLeftOrUndirected.
    def exitSimplifiedOverrideLeftOrUndirected(
        self, ctx: GQLParser.SimplifiedOverrideLeftOrUndirectedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedOverrideUndirectedOrRight.
    def enterSimplifiedOverrideUndirectedOrRight(
        self, ctx: GQLParser.SimplifiedOverrideUndirectedOrRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedOverrideUndirectedOrRight.
    def exitSimplifiedOverrideUndirectedOrRight(
        self, ctx: GQLParser.SimplifiedOverrideUndirectedOrRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedOverrideLeftOrRight.
    def enterSimplifiedOverrideLeftOrRight(
        self, ctx: GQLParser.SimplifiedOverrideLeftOrRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedOverrideLeftOrRight.
    def exitSimplifiedOverrideLeftOrRight(
        self, ctx: GQLParser.SimplifiedOverrideLeftOrRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedOverrideAnyDirection.
    def enterSimplifiedOverrideAnyDirection(
        self, ctx: GQLParser.SimplifiedOverrideAnyDirectionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedOverrideAnyDirection.
    def exitSimplifiedOverrideAnyDirection(
        self, ctx: GQLParser.SimplifiedOverrideAnyDirectionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedSecondary.
    def enterSimplifiedSecondary(self, ctx: GQLParser.SimplifiedSecondaryContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedSecondary.
    def exitSimplifiedSecondary(self, ctx: GQLParser.SimplifiedSecondaryContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedNegation.
    def enterSimplifiedNegation(self, ctx: GQLParser.SimplifiedNegationContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedNegation.
    def exitSimplifiedNegation(self, ctx: GQLParser.SimplifiedNegationContext):
        pass

    # Enter a parse tree produced by GQLParser#simplifiedPrimary.
    def enterSimplifiedPrimary(self, ctx: GQLParser.SimplifiedPrimaryContext):
        pass

    # Exit a parse tree produced by GQLParser#simplifiedPrimary.
    def exitSimplifiedPrimary(self, ctx: GQLParser.SimplifiedPrimaryContext):
        pass

    # Enter a parse tree produced by GQLParser#whereClause.
    def enterWhereClause(self, ctx: GQLParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#whereClause.
    def exitWhereClause(self, ctx: GQLParser.WhereClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#yieldClause.
    def enterYieldClause(self, ctx: GQLParser.YieldClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#yieldClause.
    def exitYieldClause(self, ctx: GQLParser.YieldClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#yieldItemList.
    def enterYieldItemList(self, ctx: GQLParser.YieldItemListContext):
        pass

    # Exit a parse tree produced by GQLParser#yieldItemList.
    def exitYieldItemList(self, ctx: GQLParser.YieldItemListContext):
        pass

    # Enter a parse tree produced by GQLParser#yieldItem.
    def enterYieldItem(self, ctx: GQLParser.YieldItemContext):
        pass

    # Exit a parse tree produced by GQLParser#yieldItem.
    def exitYieldItem(self, ctx: GQLParser.YieldItemContext):
        pass

    # Enter a parse tree produced by GQLParser#yieldItemName.
    def enterYieldItemName(self, ctx: GQLParser.YieldItemNameContext):
        pass

    # Exit a parse tree produced by GQLParser#yieldItemName.
    def exitYieldItemName(self, ctx: GQLParser.YieldItemNameContext):
        pass

    # Enter a parse tree produced by GQLParser#yieldItemAlias.
    def enterYieldItemAlias(self, ctx: GQLParser.YieldItemAliasContext):
        pass

    # Exit a parse tree produced by GQLParser#yieldItemAlias.
    def exitYieldItemAlias(self, ctx: GQLParser.YieldItemAliasContext):
        pass

    # Enter a parse tree produced by GQLParser#groupByClause.
    def enterGroupByClause(self, ctx: GQLParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#groupByClause.
    def exitGroupByClause(self, ctx: GQLParser.GroupByClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#groupingElementList.
    def enterGroupingElementList(self, ctx: GQLParser.GroupingElementListContext):
        pass

    # Exit a parse tree produced by GQLParser#groupingElementList.
    def exitGroupingElementList(self, ctx: GQLParser.GroupingElementListContext):
        pass

    # Enter a parse tree produced by GQLParser#groupingElement.
    def enterGroupingElement(self, ctx: GQLParser.GroupingElementContext):
        pass

    # Exit a parse tree produced by GQLParser#groupingElement.
    def exitGroupingElement(self, ctx: GQLParser.GroupingElementContext):
        pass

    # Enter a parse tree produced by GQLParser#emptyGroupingSet.
    def enterEmptyGroupingSet(self, ctx: GQLParser.EmptyGroupingSetContext):
        pass

    # Exit a parse tree produced by GQLParser#emptyGroupingSet.
    def exitEmptyGroupingSet(self, ctx: GQLParser.EmptyGroupingSetContext):
        pass

    # Enter a parse tree produced by GQLParser#orderByClause.
    def enterOrderByClause(self, ctx: GQLParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#orderByClause.
    def exitOrderByClause(self, ctx: GQLParser.OrderByClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#sortSpecificationList.
    def enterSortSpecificationList(self, ctx: GQLParser.SortSpecificationListContext):
        pass

    # Exit a parse tree produced by GQLParser#sortSpecificationList.
    def exitSortSpecificationList(self, ctx: GQLParser.SortSpecificationListContext):
        pass

    # Enter a parse tree produced by GQLParser#sortSpecification.
    def enterSortSpecification(self, ctx: GQLParser.SortSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#sortSpecification.
    def exitSortSpecification(self, ctx: GQLParser.SortSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#sortKey.
    def enterSortKey(self, ctx: GQLParser.SortKeyContext):
        pass

    # Exit a parse tree produced by GQLParser#sortKey.
    def exitSortKey(self, ctx: GQLParser.SortKeyContext):
        pass

    # Enter a parse tree produced by GQLParser#orderingSpecification.
    def enterOrderingSpecification(self, ctx: GQLParser.OrderingSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#orderingSpecification.
    def exitOrderingSpecification(self, ctx: GQLParser.OrderingSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#nullOrdering.
    def enterNullOrdering(self, ctx: GQLParser.NullOrderingContext):
        pass

    # Exit a parse tree produced by GQLParser#nullOrdering.
    def exitNullOrdering(self, ctx: GQLParser.NullOrderingContext):
        pass

    # Enter a parse tree produced by GQLParser#limitClause.
    def enterLimitClause(self, ctx: GQLParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#limitClause.
    def exitLimitClause(self, ctx: GQLParser.LimitClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#offsetClause.
    def enterOffsetClause(self, ctx: GQLParser.OffsetClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#offsetClause.
    def exitOffsetClause(self, ctx: GQLParser.OffsetClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#offsetSynonym.
    def enterOffsetSynonym(self, ctx: GQLParser.OffsetSynonymContext):
        pass

    # Exit a parse tree produced by GQLParser#offsetSynonym.
    def exitOffsetSynonym(self, ctx: GQLParser.OffsetSynonymContext):
        pass

    # Enter a parse tree produced by GQLParser#schemaReference.
    def enterSchemaReference(self, ctx: GQLParser.SchemaReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#schemaReference.
    def exitSchemaReference(self, ctx: GQLParser.SchemaReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#absoluteCatalogSchemaReference.
    def enterAbsoluteCatalogSchemaReference(
        self, ctx: GQLParser.AbsoluteCatalogSchemaReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#absoluteCatalogSchemaReference.
    def exitAbsoluteCatalogSchemaReference(
        self, ctx: GQLParser.AbsoluteCatalogSchemaReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#catalogSchemaParentAndName.
    def enterCatalogSchemaParentAndName(
        self, ctx: GQLParser.CatalogSchemaParentAndNameContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#catalogSchemaParentAndName.
    def exitCatalogSchemaParentAndName(
        self, ctx: GQLParser.CatalogSchemaParentAndNameContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#relativeCatalogSchemaReference.
    def enterRelativeCatalogSchemaReference(
        self, ctx: GQLParser.RelativeCatalogSchemaReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#relativeCatalogSchemaReference.
    def exitRelativeCatalogSchemaReference(
        self, ctx: GQLParser.RelativeCatalogSchemaReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#predefinedSchemaReference.
    def enterPredefinedSchemaReference(
        self, ctx: GQLParser.PredefinedSchemaReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#predefinedSchemaReference.
    def exitPredefinedSchemaReference(
        self, ctx: GQLParser.PredefinedSchemaReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#absoluteDirectoryPath.
    def enterAbsoluteDirectoryPath(self, ctx: GQLParser.AbsoluteDirectoryPathContext):
        pass

    # Exit a parse tree produced by GQLParser#absoluteDirectoryPath.
    def exitAbsoluteDirectoryPath(self, ctx: GQLParser.AbsoluteDirectoryPathContext):
        pass

    # Enter a parse tree produced by GQLParser#relativeDirectoryPath.
    def enterRelativeDirectoryPath(self, ctx: GQLParser.RelativeDirectoryPathContext):
        pass

    # Exit a parse tree produced by GQLParser#relativeDirectoryPath.
    def exitRelativeDirectoryPath(self, ctx: GQLParser.RelativeDirectoryPathContext):
        pass

    # Enter a parse tree produced by GQLParser#simpleDirectoryPath.
    def enterSimpleDirectoryPath(self, ctx: GQLParser.SimpleDirectoryPathContext):
        pass

    # Exit a parse tree produced by GQLParser#simpleDirectoryPath.
    def exitSimpleDirectoryPath(self, ctx: GQLParser.SimpleDirectoryPathContext):
        pass

    # Enter a parse tree produced by GQLParser#graphReference.
    def enterGraphReference(self, ctx: GQLParser.GraphReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#graphReference.
    def exitGraphReference(self, ctx: GQLParser.GraphReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#catalogGraphParentAndName.
    def enterCatalogGraphParentAndName(
        self, ctx: GQLParser.CatalogGraphParentAndNameContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#catalogGraphParentAndName.
    def exitCatalogGraphParentAndName(
        self, ctx: GQLParser.CatalogGraphParentAndNameContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#homeGraph.
    def enterHomeGraph(self, ctx: GQLParser.HomeGraphContext):
        pass

    # Exit a parse tree produced by GQLParser#homeGraph.
    def exitHomeGraph(self, ctx: GQLParser.HomeGraphContext):
        pass

    # Enter a parse tree produced by GQLParser#graphTypeReference.
    def enterGraphTypeReference(self, ctx: GQLParser.GraphTypeReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#graphTypeReference.
    def exitGraphTypeReference(self, ctx: GQLParser.GraphTypeReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#catalogGraphTypeParentAndName.
    def enterCatalogGraphTypeParentAndName(
        self, ctx: GQLParser.CatalogGraphTypeParentAndNameContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#catalogGraphTypeParentAndName.
    def exitCatalogGraphTypeParentAndName(
        self, ctx: GQLParser.CatalogGraphTypeParentAndNameContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableReference.
    def enterBindingTableReference(self, ctx: GQLParser.BindingTableReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableReference.
    def exitBindingTableReference(self, ctx: GQLParser.BindingTableReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#procedureReference.
    def enterProcedureReference(self, ctx: GQLParser.ProcedureReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#procedureReference.
    def exitProcedureReference(self, ctx: GQLParser.ProcedureReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#catalogProcedureParentAndName.
    def enterCatalogProcedureParentAndName(
        self, ctx: GQLParser.CatalogProcedureParentAndNameContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#catalogProcedureParentAndName.
    def exitCatalogProcedureParentAndName(
        self, ctx: GQLParser.CatalogProcedureParentAndNameContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#catalogObjectParentReference.
    def enterCatalogObjectParentReference(
        self, ctx: GQLParser.CatalogObjectParentReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#catalogObjectParentReference.
    def exitCatalogObjectParentReference(
        self, ctx: GQLParser.CatalogObjectParentReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#referenceParameterSpecification.
    def enterReferenceParameterSpecification(
        self, ctx: GQLParser.ReferenceParameterSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#referenceParameterSpecification.
    def exitReferenceParameterSpecification(
        self, ctx: GQLParser.ReferenceParameterSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nestedGraphTypeSpecification.
    def enterNestedGraphTypeSpecification(
        self, ctx: GQLParser.NestedGraphTypeSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nestedGraphTypeSpecification.
    def exitNestedGraphTypeSpecification(
        self, ctx: GQLParser.NestedGraphTypeSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#graphTypeSpecificationBody.
    def enterGraphTypeSpecificationBody(
        self, ctx: GQLParser.GraphTypeSpecificationBodyContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#graphTypeSpecificationBody.
    def exitGraphTypeSpecificationBody(
        self, ctx: GQLParser.GraphTypeSpecificationBodyContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#elementTypeList.
    def enterElementTypeList(self, ctx: GQLParser.ElementTypeListContext):
        pass

    # Exit a parse tree produced by GQLParser#elementTypeList.
    def exitElementTypeList(self, ctx: GQLParser.ElementTypeListContext):
        pass

    # Enter a parse tree produced by GQLParser#elementTypeSpecification.
    def enterElementTypeSpecification(
        self, ctx: GQLParser.ElementTypeSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#elementTypeSpecification.
    def exitElementTypeSpecification(
        self, ctx: GQLParser.ElementTypeSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypeSpecification.
    def enterNodeTypeSpecification(self, ctx: GQLParser.NodeTypeSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypeSpecification.
    def exitNodeTypeSpecification(self, ctx: GQLParser.NodeTypeSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypePattern.
    def enterNodeTypePattern(self, ctx: GQLParser.NodeTypePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypePattern.
    def exitNodeTypePattern(self, ctx: GQLParser.NodeTypePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypePhrase.
    def enterNodeTypePhrase(self, ctx: GQLParser.NodeTypePhraseContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypePhrase.
    def exitNodeTypePhrase(self, ctx: GQLParser.NodeTypePhraseContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypePhraseFiller.
    def enterNodeTypePhraseFiller(self, ctx: GQLParser.NodeTypePhraseFillerContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypePhraseFiller.
    def exitNodeTypePhraseFiller(self, ctx: GQLParser.NodeTypePhraseFillerContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypeFiller.
    def enterNodeTypeFiller(self, ctx: GQLParser.NodeTypeFillerContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypeFiller.
    def exitNodeTypeFiller(self, ctx: GQLParser.NodeTypeFillerContext):
        pass

    # Enter a parse tree produced by GQLParser#localNodeTypeAlias.
    def enterLocalNodeTypeAlias(self, ctx: GQLParser.LocalNodeTypeAliasContext):
        pass

    # Exit a parse tree produced by GQLParser#localNodeTypeAlias.
    def exitLocalNodeTypeAlias(self, ctx: GQLParser.LocalNodeTypeAliasContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypeImpliedContent.
    def enterNodeTypeImpliedContent(self, ctx: GQLParser.NodeTypeImpliedContentContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypeImpliedContent.
    def exitNodeTypeImpliedContent(self, ctx: GQLParser.NodeTypeImpliedContentContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypeKeyLabelSet.
    def enterNodeTypeKeyLabelSet(self, ctx: GQLParser.NodeTypeKeyLabelSetContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypeKeyLabelSet.
    def exitNodeTypeKeyLabelSet(self, ctx: GQLParser.NodeTypeKeyLabelSetContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypeLabelSet.
    def enterNodeTypeLabelSet(self, ctx: GQLParser.NodeTypeLabelSetContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypeLabelSet.
    def exitNodeTypeLabelSet(self, ctx: GQLParser.NodeTypeLabelSetContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypePropertyTypes.
    def enterNodeTypePropertyTypes(self, ctx: GQLParser.NodeTypePropertyTypesContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypePropertyTypes.
    def exitNodeTypePropertyTypes(self, ctx: GQLParser.NodeTypePropertyTypesContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypeSpecification.
    def enterEdgeTypeSpecification(self, ctx: GQLParser.EdgeTypeSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypeSpecification.
    def exitEdgeTypeSpecification(self, ctx: GQLParser.EdgeTypeSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePattern.
    def enterEdgeTypePattern(self, ctx: GQLParser.EdgeTypePatternContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePattern.
    def exitEdgeTypePattern(self, ctx: GQLParser.EdgeTypePatternContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePhrase.
    def enterEdgeTypePhrase(self, ctx: GQLParser.EdgeTypePhraseContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePhrase.
    def exitEdgeTypePhrase(self, ctx: GQLParser.EdgeTypePhraseContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePhraseFiller.
    def enterEdgeTypePhraseFiller(self, ctx: GQLParser.EdgeTypePhraseFillerContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePhraseFiller.
    def exitEdgeTypePhraseFiller(self, ctx: GQLParser.EdgeTypePhraseFillerContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypeFiller.
    def enterEdgeTypeFiller(self, ctx: GQLParser.EdgeTypeFillerContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypeFiller.
    def exitEdgeTypeFiller(self, ctx: GQLParser.EdgeTypeFillerContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypeImpliedContent.
    def enterEdgeTypeImpliedContent(self, ctx: GQLParser.EdgeTypeImpliedContentContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypeImpliedContent.
    def exitEdgeTypeImpliedContent(self, ctx: GQLParser.EdgeTypeImpliedContentContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypeKeyLabelSet.
    def enterEdgeTypeKeyLabelSet(self, ctx: GQLParser.EdgeTypeKeyLabelSetContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypeKeyLabelSet.
    def exitEdgeTypeKeyLabelSet(self, ctx: GQLParser.EdgeTypeKeyLabelSetContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypeLabelSet.
    def enterEdgeTypeLabelSet(self, ctx: GQLParser.EdgeTypeLabelSetContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypeLabelSet.
    def exitEdgeTypeLabelSet(self, ctx: GQLParser.EdgeTypeLabelSetContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePropertyTypes.
    def enterEdgeTypePropertyTypes(self, ctx: GQLParser.EdgeTypePropertyTypesContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePropertyTypes.
    def exitEdgeTypePropertyTypes(self, ctx: GQLParser.EdgeTypePropertyTypesContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePatternDirected.
    def enterEdgeTypePatternDirected(
        self, ctx: GQLParser.EdgeTypePatternDirectedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePatternDirected.
    def exitEdgeTypePatternDirected(
        self, ctx: GQLParser.EdgeTypePatternDirectedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePatternPointingRight.
    def enterEdgeTypePatternPointingRight(
        self, ctx: GQLParser.EdgeTypePatternPointingRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePatternPointingRight.
    def exitEdgeTypePatternPointingRight(
        self, ctx: GQLParser.EdgeTypePatternPointingRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePatternPointingLeft.
    def enterEdgeTypePatternPointingLeft(
        self, ctx: GQLParser.EdgeTypePatternPointingLeftContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePatternPointingLeft.
    def exitEdgeTypePatternPointingLeft(
        self, ctx: GQLParser.EdgeTypePatternPointingLeftContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypePatternUndirected.
    def enterEdgeTypePatternUndirected(
        self, ctx: GQLParser.EdgeTypePatternUndirectedContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypePatternUndirected.
    def exitEdgeTypePatternUndirected(
        self, ctx: GQLParser.EdgeTypePatternUndirectedContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#arcTypePointingRight.
    def enterArcTypePointingRight(self, ctx: GQLParser.ArcTypePointingRightContext):
        pass

    # Exit a parse tree produced by GQLParser#arcTypePointingRight.
    def exitArcTypePointingRight(self, ctx: GQLParser.ArcTypePointingRightContext):
        pass

    # Enter a parse tree produced by GQLParser#arcTypePointingLeft.
    def enterArcTypePointingLeft(self, ctx: GQLParser.ArcTypePointingLeftContext):
        pass

    # Exit a parse tree produced by GQLParser#arcTypePointingLeft.
    def exitArcTypePointingLeft(self, ctx: GQLParser.ArcTypePointingLeftContext):
        pass

    # Enter a parse tree produced by GQLParser#arcTypeUndirected.
    def enterArcTypeUndirected(self, ctx: GQLParser.ArcTypeUndirectedContext):
        pass

    # Exit a parse tree produced by GQLParser#arcTypeUndirected.
    def exitArcTypeUndirected(self, ctx: GQLParser.ArcTypeUndirectedContext):
        pass

    # Enter a parse tree produced by GQLParser#sourceNodeTypeReference.
    def enterSourceNodeTypeReference(
        self, ctx: GQLParser.SourceNodeTypeReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sourceNodeTypeReference.
    def exitSourceNodeTypeReference(
        self, ctx: GQLParser.SourceNodeTypeReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#destinationNodeTypeReference.
    def enterDestinationNodeTypeReference(
        self, ctx: GQLParser.DestinationNodeTypeReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#destinationNodeTypeReference.
    def exitDestinationNodeTypeReference(
        self, ctx: GQLParser.DestinationNodeTypeReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeKind.
    def enterEdgeKind(self, ctx: GQLParser.EdgeKindContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeKind.
    def exitEdgeKind(self, ctx: GQLParser.EdgeKindContext):
        pass

    # Enter a parse tree produced by GQLParser#endpointPairPhrase.
    def enterEndpointPairPhrase(self, ctx: GQLParser.EndpointPairPhraseContext):
        pass

    # Exit a parse tree produced by GQLParser#endpointPairPhrase.
    def exitEndpointPairPhrase(self, ctx: GQLParser.EndpointPairPhraseContext):
        pass

    # Enter a parse tree produced by GQLParser#endpointPair.
    def enterEndpointPair(self, ctx: GQLParser.EndpointPairContext):
        pass

    # Exit a parse tree produced by GQLParser#endpointPair.
    def exitEndpointPair(self, ctx: GQLParser.EndpointPairContext):
        pass

    # Enter a parse tree produced by GQLParser#endpointPairDirected.
    def enterEndpointPairDirected(self, ctx: GQLParser.EndpointPairDirectedContext):
        pass

    # Exit a parse tree produced by GQLParser#endpointPairDirected.
    def exitEndpointPairDirected(self, ctx: GQLParser.EndpointPairDirectedContext):
        pass

    # Enter a parse tree produced by GQLParser#endpointPairPointingRight.
    def enterEndpointPairPointingRight(
        self, ctx: GQLParser.EndpointPairPointingRightContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#endpointPairPointingRight.
    def exitEndpointPairPointingRight(
        self, ctx: GQLParser.EndpointPairPointingRightContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#endpointPairPointingLeft.
    def enterEndpointPairPointingLeft(
        self, ctx: GQLParser.EndpointPairPointingLeftContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#endpointPairPointingLeft.
    def exitEndpointPairPointingLeft(
        self, ctx: GQLParser.EndpointPairPointingLeftContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#endpointPairUndirected.
    def enterEndpointPairUndirected(self, ctx: GQLParser.EndpointPairUndirectedContext):
        pass

    # Exit a parse tree produced by GQLParser#endpointPairUndirected.
    def exitEndpointPairUndirected(self, ctx: GQLParser.EndpointPairUndirectedContext):
        pass

    # Enter a parse tree produced by GQLParser#connectorPointingRight.
    def enterConnectorPointingRight(self, ctx: GQLParser.ConnectorPointingRightContext):
        pass

    # Exit a parse tree produced by GQLParser#connectorPointingRight.
    def exitConnectorPointingRight(self, ctx: GQLParser.ConnectorPointingRightContext):
        pass

    # Enter a parse tree produced by GQLParser#connectorUndirected.
    def enterConnectorUndirected(self, ctx: GQLParser.ConnectorUndirectedContext):
        pass

    # Exit a parse tree produced by GQLParser#connectorUndirected.
    def exitConnectorUndirected(self, ctx: GQLParser.ConnectorUndirectedContext):
        pass

    # Enter a parse tree produced by GQLParser#sourceNodeTypeAlias.
    def enterSourceNodeTypeAlias(self, ctx: GQLParser.SourceNodeTypeAliasContext):
        pass

    # Exit a parse tree produced by GQLParser#sourceNodeTypeAlias.
    def exitSourceNodeTypeAlias(self, ctx: GQLParser.SourceNodeTypeAliasContext):
        pass

    # Enter a parse tree produced by GQLParser#destinationNodeTypeAlias.
    def enterDestinationNodeTypeAlias(
        self, ctx: GQLParser.DestinationNodeTypeAliasContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#destinationNodeTypeAlias.
    def exitDestinationNodeTypeAlias(
        self, ctx: GQLParser.DestinationNodeTypeAliasContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#labelSetPhrase.
    def enterLabelSetPhrase(self, ctx: GQLParser.LabelSetPhraseContext):
        pass

    # Exit a parse tree produced by GQLParser#labelSetPhrase.
    def exitLabelSetPhrase(self, ctx: GQLParser.LabelSetPhraseContext):
        pass

    # Enter a parse tree produced by GQLParser#labelSetSpecification.
    def enterLabelSetSpecification(self, ctx: GQLParser.LabelSetSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#labelSetSpecification.
    def exitLabelSetSpecification(self, ctx: GQLParser.LabelSetSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#propertyTypesSpecification.
    def enterPropertyTypesSpecification(
        self, ctx: GQLParser.PropertyTypesSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#propertyTypesSpecification.
    def exitPropertyTypesSpecification(
        self, ctx: GQLParser.PropertyTypesSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#propertyTypeList.
    def enterPropertyTypeList(self, ctx: GQLParser.PropertyTypeListContext):
        pass

    # Exit a parse tree produced by GQLParser#propertyTypeList.
    def exitPropertyTypeList(self, ctx: GQLParser.PropertyTypeListContext):
        pass

    # Enter a parse tree produced by GQLParser#propertyType.
    def enterPropertyType(self, ctx: GQLParser.PropertyTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#propertyType.
    def exitPropertyType(self, ctx: GQLParser.PropertyTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#propertyValueType.
    def enterPropertyValueType(self, ctx: GQLParser.PropertyValueTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#propertyValueType.
    def exitPropertyValueType(self, ctx: GQLParser.PropertyValueTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableType.
    def enterBindingTableType(self, ctx: GQLParser.BindingTableTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableType.
    def exitBindingTableType(self, ctx: GQLParser.BindingTableTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#dynamicPropertyValueTypeLabel.
    def enterDynamicPropertyValueTypeLabel(
        self, ctx: GQLParser.DynamicPropertyValueTypeLabelContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#dynamicPropertyValueTypeLabel.
    def exitDynamicPropertyValueTypeLabel(
        self, ctx: GQLParser.DynamicPropertyValueTypeLabelContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#closedDynamicUnionTypeAtl1.
    def enterClosedDynamicUnionTypeAtl1(
        self, ctx: GQLParser.ClosedDynamicUnionTypeAtl1Context
    ):
        pass

    # Exit a parse tree produced by GQLParser#closedDynamicUnionTypeAtl1.
    def exitClosedDynamicUnionTypeAtl1(
        self, ctx: GQLParser.ClosedDynamicUnionTypeAtl1Context
    ):
        pass

    # Enter a parse tree produced by GQLParser#closedDynamicUnionTypeAtl2.
    def enterClosedDynamicUnionTypeAtl2(
        self, ctx: GQLParser.ClosedDynamicUnionTypeAtl2Context
    ):
        pass

    # Exit a parse tree produced by GQLParser#closedDynamicUnionTypeAtl2.
    def exitClosedDynamicUnionTypeAtl2(
        self, ctx: GQLParser.ClosedDynamicUnionTypeAtl2Context
    ):
        pass

    # Enter a parse tree produced by GQLParser#pathValueTypeLabel.
    def enterPathValueTypeLabel(self, ctx: GQLParser.PathValueTypeLabelContext):
        pass

    # Exit a parse tree produced by GQLParser#pathValueTypeLabel.
    def exitPathValueTypeLabel(self, ctx: GQLParser.PathValueTypeLabelContext):
        pass

    # Enter a parse tree produced by GQLParser#listValueTypeAlt3.
    def enterListValueTypeAlt3(self, ctx: GQLParser.ListValueTypeAlt3Context):
        pass

    # Exit a parse tree produced by GQLParser#listValueTypeAlt3.
    def exitListValueTypeAlt3(self, ctx: GQLParser.ListValueTypeAlt3Context):
        pass

    # Enter a parse tree produced by GQLParser#listValueTypeAlt2.
    def enterListValueTypeAlt2(self, ctx: GQLParser.ListValueTypeAlt2Context):
        pass

    # Exit a parse tree produced by GQLParser#listValueTypeAlt2.
    def exitListValueTypeAlt2(self, ctx: GQLParser.ListValueTypeAlt2Context):
        pass

    # Enter a parse tree produced by GQLParser#listValueTypeAlt1.
    def enterListValueTypeAlt1(self, ctx: GQLParser.ListValueTypeAlt1Context):
        pass

    # Exit a parse tree produced by GQLParser#listValueTypeAlt1.
    def exitListValueTypeAlt1(self, ctx: GQLParser.ListValueTypeAlt1Context):
        pass

    # Enter a parse tree produced by GQLParser#predefinedTypeLabel.
    def enterPredefinedTypeLabel(self, ctx: GQLParser.PredefinedTypeLabelContext):
        pass

    # Exit a parse tree produced by GQLParser#predefinedTypeLabel.
    def exitPredefinedTypeLabel(self, ctx: GQLParser.PredefinedTypeLabelContext):
        pass

    # Enter a parse tree produced by GQLParser#recordTypeLabel.
    def enterRecordTypeLabel(self, ctx: GQLParser.RecordTypeLabelContext):
        pass

    # Exit a parse tree produced by GQLParser#recordTypeLabel.
    def exitRecordTypeLabel(self, ctx: GQLParser.RecordTypeLabelContext):
        pass

    # Enter a parse tree produced by GQLParser#openDynamicUnionTypeLabel.
    def enterOpenDynamicUnionTypeLabel(
        self, ctx: GQLParser.OpenDynamicUnionTypeLabelContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#openDynamicUnionTypeLabel.
    def exitOpenDynamicUnionTypeLabel(
        self, ctx: GQLParser.OpenDynamicUnionTypeLabelContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#typed.
    def enterTyped(self, ctx: GQLParser.TypedContext):
        pass

    # Exit a parse tree produced by GQLParser#typed.
    def exitTyped(self, ctx: GQLParser.TypedContext):
        pass

    # Enter a parse tree produced by GQLParser#predefinedType.
    def enterPredefinedType(self, ctx: GQLParser.PredefinedTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#predefinedType.
    def exitPredefinedType(self, ctx: GQLParser.PredefinedTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#booleanType.
    def enterBooleanType(self, ctx: GQLParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#booleanType.
    def exitBooleanType(self, ctx: GQLParser.BooleanTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#characterStringType.
    def enterCharacterStringType(self, ctx: GQLParser.CharacterStringTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#characterStringType.
    def exitCharacterStringType(self, ctx: GQLParser.CharacterStringTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#byteStringType.
    def enterByteStringType(self, ctx: GQLParser.ByteStringTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#byteStringType.
    def exitByteStringType(self, ctx: GQLParser.ByteStringTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#minLength.
    def enterMinLength(self, ctx: GQLParser.MinLengthContext):
        pass

    # Exit a parse tree produced by GQLParser#minLength.
    def exitMinLength(self, ctx: GQLParser.MinLengthContext):
        pass

    # Enter a parse tree produced by GQLParser#maxLength.
    def enterMaxLength(self, ctx: GQLParser.MaxLengthContext):
        pass

    # Exit a parse tree produced by GQLParser#maxLength.
    def exitMaxLength(self, ctx: GQLParser.MaxLengthContext):
        pass

    # Enter a parse tree produced by GQLParser#fixedLength.
    def enterFixedLength(self, ctx: GQLParser.FixedLengthContext):
        pass

    # Exit a parse tree produced by GQLParser#fixedLength.
    def exitFixedLength(self, ctx: GQLParser.FixedLengthContext):
        pass

    # Enter a parse tree produced by GQLParser#numericType.
    def enterNumericType(self, ctx: GQLParser.NumericTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#numericType.
    def exitNumericType(self, ctx: GQLParser.NumericTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#exactNumericType.
    def enterExactNumericType(self, ctx: GQLParser.ExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#exactNumericType.
    def exitExactNumericType(self, ctx: GQLParser.ExactNumericTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#binaryExactNumericType.
    def enterBinaryExactNumericType(self, ctx: GQLParser.BinaryExactNumericTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#binaryExactNumericType.
    def exitBinaryExactNumericType(self, ctx: GQLParser.BinaryExactNumericTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#signedBinaryExactNumericType.
    def enterSignedBinaryExactNumericType(
        self, ctx: GQLParser.SignedBinaryExactNumericTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#signedBinaryExactNumericType.
    def exitSignedBinaryExactNumericType(
        self, ctx: GQLParser.SignedBinaryExactNumericTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#unsignedBinaryExactNumericType.
    def enterUnsignedBinaryExactNumericType(
        self, ctx: GQLParser.UnsignedBinaryExactNumericTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#unsignedBinaryExactNumericType.
    def exitUnsignedBinaryExactNumericType(
        self, ctx: GQLParser.UnsignedBinaryExactNumericTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#verboseBinaryExactNumericType.
    def enterVerboseBinaryExactNumericType(
        self, ctx: GQLParser.VerboseBinaryExactNumericTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#verboseBinaryExactNumericType.
    def exitVerboseBinaryExactNumericType(
        self, ctx: GQLParser.VerboseBinaryExactNumericTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#decimalExactNumericType.
    def enterDecimalExactNumericType(
        self, ctx: GQLParser.DecimalExactNumericTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#decimalExactNumericType.
    def exitDecimalExactNumericType(
        self, ctx: GQLParser.DecimalExactNumericTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#precision.
    def enterPrecision(self, ctx: GQLParser.PrecisionContext):
        pass

    # Exit a parse tree produced by GQLParser#precision.
    def exitPrecision(self, ctx: GQLParser.PrecisionContext):
        pass

    # Enter a parse tree produced by GQLParser#scale.
    def enterScale(self, ctx: GQLParser.ScaleContext):
        pass

    # Exit a parse tree produced by GQLParser#scale.
    def exitScale(self, ctx: GQLParser.ScaleContext):
        pass

    # Enter a parse tree produced by GQLParser#approximateNumericType.
    def enterApproximateNumericType(self, ctx: GQLParser.ApproximateNumericTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#approximateNumericType.
    def exitApproximateNumericType(self, ctx: GQLParser.ApproximateNumericTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#temporalType.
    def enterTemporalType(self, ctx: GQLParser.TemporalTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#temporalType.
    def exitTemporalType(self, ctx: GQLParser.TemporalTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#temporalInstantType.
    def enterTemporalInstantType(self, ctx: GQLParser.TemporalInstantTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#temporalInstantType.
    def exitTemporalInstantType(self, ctx: GQLParser.TemporalInstantTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#datetimeType.
    def enterDatetimeType(self, ctx: GQLParser.DatetimeTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#datetimeType.
    def exitDatetimeType(self, ctx: GQLParser.DatetimeTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#localdatetimeType.
    def enterLocaldatetimeType(self, ctx: GQLParser.LocaldatetimeTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#localdatetimeType.
    def exitLocaldatetimeType(self, ctx: GQLParser.LocaldatetimeTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#dateType.
    def enterDateType(self, ctx: GQLParser.DateTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#dateType.
    def exitDateType(self, ctx: GQLParser.DateTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#timeType.
    def enterTimeType(self, ctx: GQLParser.TimeTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#timeType.
    def exitTimeType(self, ctx: GQLParser.TimeTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#localtimeType.
    def enterLocaltimeType(self, ctx: GQLParser.LocaltimeTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#localtimeType.
    def exitLocaltimeType(self, ctx: GQLParser.LocaltimeTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#temporalDurationType.
    def enterTemporalDurationType(self, ctx: GQLParser.TemporalDurationTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#temporalDurationType.
    def exitTemporalDurationType(self, ctx: GQLParser.TemporalDurationTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#temporalDurationQualifier.
    def enterTemporalDurationQualifier(
        self, ctx: GQLParser.TemporalDurationQualifierContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#temporalDurationQualifier.
    def exitTemporalDurationQualifier(
        self, ctx: GQLParser.TemporalDurationQualifierContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#referenceValueType.
    def enterReferenceValueType(self, ctx: GQLParser.ReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#referenceValueType.
    def exitReferenceValueType(self, ctx: GQLParser.ReferenceValueTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#immaterialValueType.
    def enterImmaterialValueType(self, ctx: GQLParser.ImmaterialValueTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#immaterialValueType.
    def exitImmaterialValueType(self, ctx: GQLParser.ImmaterialValueTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#nullType.
    def enterNullType(self, ctx: GQLParser.NullTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#nullType.
    def exitNullType(self, ctx: GQLParser.NullTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#emptyType.
    def enterEmptyType(self, ctx: GQLParser.EmptyTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#emptyType.
    def exitEmptyType(self, ctx: GQLParser.EmptyTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#graphReferenceValueType.
    def enterGraphReferenceValueType(
        self, ctx: GQLParser.GraphReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#graphReferenceValueType.
    def exitGraphReferenceValueType(
        self, ctx: GQLParser.GraphReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#closedGraphReferenceValueType.
    def enterClosedGraphReferenceValueType(
        self, ctx: GQLParser.ClosedGraphReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#closedGraphReferenceValueType.
    def exitClosedGraphReferenceValueType(
        self, ctx: GQLParser.ClosedGraphReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#openGraphReferenceValueType.
    def enterOpenGraphReferenceValueType(
        self, ctx: GQLParser.OpenGraphReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#openGraphReferenceValueType.
    def exitOpenGraphReferenceValueType(
        self, ctx: GQLParser.OpenGraphReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableReferenceValueType.
    def enterBindingTableReferenceValueType(
        self, ctx: GQLParser.BindingTableReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableReferenceValueType.
    def exitBindingTableReferenceValueType(
        self, ctx: GQLParser.BindingTableReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nodeReferenceValueType.
    def enterNodeReferenceValueType(self, ctx: GQLParser.NodeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeReferenceValueType.
    def exitNodeReferenceValueType(self, ctx: GQLParser.NodeReferenceValueTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#closedNodeReferenceValueType.
    def enterClosedNodeReferenceValueType(
        self, ctx: GQLParser.ClosedNodeReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#closedNodeReferenceValueType.
    def exitClosedNodeReferenceValueType(
        self, ctx: GQLParser.ClosedNodeReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#openNodeReferenceValueType.
    def enterOpenNodeReferenceValueType(
        self, ctx: GQLParser.OpenNodeReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#openNodeReferenceValueType.
    def exitOpenNodeReferenceValueType(
        self, ctx: GQLParser.OpenNodeReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeReferenceValueType.
    def enterEdgeReferenceValueType(self, ctx: GQLParser.EdgeReferenceValueTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeReferenceValueType.
    def exitEdgeReferenceValueType(self, ctx: GQLParser.EdgeReferenceValueTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#closedEdgeReferenceValueType.
    def enterClosedEdgeReferenceValueType(
        self, ctx: GQLParser.ClosedEdgeReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#closedEdgeReferenceValueType.
    def exitClosedEdgeReferenceValueType(
        self, ctx: GQLParser.ClosedEdgeReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#openEdgeReferenceValueType.
    def enterOpenEdgeReferenceValueType(
        self, ctx: GQLParser.OpenEdgeReferenceValueTypeContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#openEdgeReferenceValueType.
    def exitOpenEdgeReferenceValueType(
        self, ctx: GQLParser.OpenEdgeReferenceValueTypeContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#pathValueType.
    def enterPathValueType(self, ctx: GQLParser.PathValueTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#pathValueType.
    def exitPathValueType(self, ctx: GQLParser.PathValueTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#listValueTypeName.
    def enterListValueTypeName(self, ctx: GQLParser.ListValueTypeNameContext):
        pass

    # Exit a parse tree produced by GQLParser#listValueTypeName.
    def exitListValueTypeName(self, ctx: GQLParser.ListValueTypeNameContext):
        pass

    # Enter a parse tree produced by GQLParser#listValueTypeNameSynonym.
    def enterListValueTypeNameSynonym(
        self, ctx: GQLParser.ListValueTypeNameSynonymContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#listValueTypeNameSynonym.
    def exitListValueTypeNameSynonym(
        self, ctx: GQLParser.ListValueTypeNameSynonymContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#recordType.
    def enterRecordType(self, ctx: GQLParser.RecordTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#recordType.
    def exitRecordType(self, ctx: GQLParser.RecordTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#fieldTypesSpecification.
    def enterFieldTypesSpecification(
        self, ctx: GQLParser.FieldTypesSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#fieldTypesSpecification.
    def exitFieldTypesSpecification(
        self, ctx: GQLParser.FieldTypesSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#fieldTypeList.
    def enterFieldTypeList(self, ctx: GQLParser.FieldTypeListContext):
        pass

    # Exit a parse tree produced by GQLParser#fieldTypeList.
    def exitFieldTypeList(self, ctx: GQLParser.FieldTypeListContext):
        pass

    # Enter a parse tree produced by GQLParser#notNull.
    def enterNotNull(self, ctx: GQLParser.NotNullContext):
        pass

    # Exit a parse tree produced by GQLParser#notNull.
    def exitNotNull(self, ctx: GQLParser.NotNullContext):
        pass

    # Enter a parse tree produced by GQLParser#fieldType.
    def enterFieldType(self, ctx: GQLParser.FieldTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#fieldType.
    def exitFieldType(self, ctx: GQLParser.FieldTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#searchCondition.
    def enterSearchCondition(self, ctx: GQLParser.SearchConditionContext):
        pass

    # Exit a parse tree produced by GQLParser#searchCondition.
    def exitSearchCondition(self, ctx: GQLParser.SearchConditionContext):
        pass

    # Enter a parse tree produced by GQLParser#predicate.
    def enterPredicate(self, ctx: GQLParser.PredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#predicate.
    def exitPredicate(self, ctx: GQLParser.PredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#compOp.
    def enterCompOp(self, ctx: GQLParser.CompOpContext):
        pass

    # Exit a parse tree produced by GQLParser#compOp.
    def exitCompOp(self, ctx: GQLParser.CompOpContext):
        pass

    # Enter a parse tree produced by GQLParser#existsPredicate.
    def enterExistsPredicate(self, ctx: GQLParser.ExistsPredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#existsPredicate.
    def exitExistsPredicate(self, ctx: GQLParser.ExistsPredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#nullPredicate.
    def enterNullPredicate(self, ctx: GQLParser.NullPredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#nullPredicate.
    def exitNullPredicate(self, ctx: GQLParser.NullPredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#nullPredicatePart2.
    def enterNullPredicatePart2(self, ctx: GQLParser.NullPredicatePart2Context):
        pass

    # Exit a parse tree produced by GQLParser#nullPredicatePart2.
    def exitNullPredicatePart2(self, ctx: GQLParser.NullPredicatePart2Context):
        pass

    # Enter a parse tree produced by GQLParser#valueTypePredicate.
    def enterValueTypePredicate(self, ctx: GQLParser.ValueTypePredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#valueTypePredicate.
    def exitValueTypePredicate(self, ctx: GQLParser.ValueTypePredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#valueTypePredicatePart2.
    def enterValueTypePredicatePart2(
        self, ctx: GQLParser.ValueTypePredicatePart2Context
    ):
        pass

    # Exit a parse tree produced by GQLParser#valueTypePredicatePart2.
    def exitValueTypePredicatePart2(
        self, ctx: GQLParser.ValueTypePredicatePart2Context
    ):
        pass

    # Enter a parse tree produced by GQLParser#normalizedPredicatePart2.
    def enterNormalizedPredicatePart2(
        self, ctx: GQLParser.NormalizedPredicatePart2Context
    ):
        pass

    # Exit a parse tree produced by GQLParser#normalizedPredicatePart2.
    def exitNormalizedPredicatePart2(
        self, ctx: GQLParser.NormalizedPredicatePart2Context
    ):
        pass

    # Enter a parse tree produced by GQLParser#directedPredicate.
    def enterDirectedPredicate(self, ctx: GQLParser.DirectedPredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#directedPredicate.
    def exitDirectedPredicate(self, ctx: GQLParser.DirectedPredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#directedPredicatePart2.
    def enterDirectedPredicatePart2(self, ctx: GQLParser.DirectedPredicatePart2Context):
        pass

    # Exit a parse tree produced by GQLParser#directedPredicatePart2.
    def exitDirectedPredicatePart2(self, ctx: GQLParser.DirectedPredicatePart2Context):
        pass

    # Enter a parse tree produced by GQLParser#labeledPredicate.
    def enterLabeledPredicate(self, ctx: GQLParser.LabeledPredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#labeledPredicate.
    def exitLabeledPredicate(self, ctx: GQLParser.LabeledPredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#labeledPredicatePart2.
    def enterLabeledPredicatePart2(self, ctx: GQLParser.LabeledPredicatePart2Context):
        pass

    # Exit a parse tree produced by GQLParser#labeledPredicatePart2.
    def exitLabeledPredicatePart2(self, ctx: GQLParser.LabeledPredicatePart2Context):
        pass

    # Enter a parse tree produced by GQLParser#isLabeledOrColon.
    def enterIsLabeledOrColon(self, ctx: GQLParser.IsLabeledOrColonContext):
        pass

    # Exit a parse tree produced by GQLParser#isLabeledOrColon.
    def exitIsLabeledOrColon(self, ctx: GQLParser.IsLabeledOrColonContext):
        pass

    # Enter a parse tree produced by GQLParser#sourceDestinationPredicate.
    def enterSourceDestinationPredicate(
        self, ctx: GQLParser.SourceDestinationPredicateContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#sourceDestinationPredicate.
    def exitSourceDestinationPredicate(
        self, ctx: GQLParser.SourceDestinationPredicateContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nodeReference.
    def enterNodeReference(self, ctx: GQLParser.NodeReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeReference.
    def exitNodeReference(self, ctx: GQLParser.NodeReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#sourcePredicatePart2.
    def enterSourcePredicatePart2(self, ctx: GQLParser.SourcePredicatePart2Context):
        pass

    # Exit a parse tree produced by GQLParser#sourcePredicatePart2.
    def exitSourcePredicatePart2(self, ctx: GQLParser.SourcePredicatePart2Context):
        pass

    # Enter a parse tree produced by GQLParser#destinationPredicatePart2.
    def enterDestinationPredicatePart2(
        self, ctx: GQLParser.DestinationPredicatePart2Context
    ):
        pass

    # Exit a parse tree produced by GQLParser#destinationPredicatePart2.
    def exitDestinationPredicatePart2(
        self, ctx: GQLParser.DestinationPredicatePart2Context
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeReference.
    def enterEdgeReference(self, ctx: GQLParser.EdgeReferenceContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeReference.
    def exitEdgeReference(self, ctx: GQLParser.EdgeReferenceContext):
        pass

    # Enter a parse tree produced by GQLParser#all_differentPredicate.
    def enterAll_differentPredicate(self, ctx: GQLParser.All_differentPredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#all_differentPredicate.
    def exitAll_differentPredicate(self, ctx: GQLParser.All_differentPredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#samePredicate.
    def enterSamePredicate(self, ctx: GQLParser.SamePredicateContext):
        pass

    # Exit a parse tree produced by GQLParser#samePredicate.
    def exitSamePredicate(self, ctx: GQLParser.SamePredicateContext):
        pass

    # Enter a parse tree produced by GQLParser#property_existsPredicate.
    def enterProperty_existsPredicate(
        self, ctx: GQLParser.Property_existsPredicateContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#property_existsPredicate.
    def exitProperty_existsPredicate(
        self, ctx: GQLParser.Property_existsPredicateContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#conjunctiveExprAlt.
    def enterConjunctiveExprAlt(self, ctx: GQLParser.ConjunctiveExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#conjunctiveExprAlt.
    def exitConjunctiveExprAlt(self, ctx: GQLParser.ConjunctiveExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#propertyGraphExprAlt.
    def enterPropertyGraphExprAlt(self, ctx: GQLParser.PropertyGraphExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#propertyGraphExprAlt.
    def exitPropertyGraphExprAlt(self, ctx: GQLParser.PropertyGraphExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#multDivExprAlt.
    def enterMultDivExprAlt(self, ctx: GQLParser.MultDivExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#multDivExprAlt.
    def exitMultDivExprAlt(self, ctx: GQLParser.MultDivExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableExprAlt.
    def enterBindingTableExprAlt(self, ctx: GQLParser.BindingTableExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableExprAlt.
    def exitBindingTableExprAlt(self, ctx: GQLParser.BindingTableExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#signedExprAlt.
    def enterSignedExprAlt(self, ctx: GQLParser.SignedExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#signedExprAlt.
    def exitSignedExprAlt(self, ctx: GQLParser.SignedExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#isNotExprAlt.
    def enterIsNotExprAlt(self, ctx: GQLParser.IsNotExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#isNotExprAlt.
    def exitIsNotExprAlt(self, ctx: GQLParser.IsNotExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#normalizedPredicateExprAlt.
    def enterNormalizedPredicateExprAlt(
        self, ctx: GQLParser.NormalizedPredicateExprAltContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#normalizedPredicateExprAlt.
    def exitNormalizedPredicateExprAlt(
        self, ctx: GQLParser.NormalizedPredicateExprAltContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#notExprAlt.
    def enterNotExprAlt(self, ctx: GQLParser.NotExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#notExprAlt.
    def exitNotExprAlt(self, ctx: GQLParser.NotExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#valueFunctionExprAlt.
    def enterValueFunctionExprAlt(self, ctx: GQLParser.ValueFunctionExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#valueFunctionExprAlt.
    def exitValueFunctionExprAlt(self, ctx: GQLParser.ValueFunctionExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#concatenationExprAlt.
    def enterConcatenationExprAlt(self, ctx: GQLParser.ConcatenationExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#concatenationExprAlt.
    def exitConcatenationExprAlt(self, ctx: GQLParser.ConcatenationExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#disjunctiveExprAlt.
    def enterDisjunctiveExprAlt(self, ctx: GQLParser.DisjunctiveExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#disjunctiveExprAlt.
    def exitDisjunctiveExprAlt(self, ctx: GQLParser.DisjunctiveExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#comparisonExprAlt.
    def enterComparisonExprAlt(self, ctx: GQLParser.ComparisonExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#comparisonExprAlt.
    def exitComparisonExprAlt(self, ctx: GQLParser.ComparisonExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#primaryExprAlt.
    def enterPrimaryExprAlt(self, ctx: GQLParser.PrimaryExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#primaryExprAlt.
    def exitPrimaryExprAlt(self, ctx: GQLParser.PrimaryExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#addSubtractExprAlt.
    def enterAddSubtractExprAlt(self, ctx: GQLParser.AddSubtractExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#addSubtractExprAlt.
    def exitAddSubtractExprAlt(self, ctx: GQLParser.AddSubtractExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#predicateExprAlt.
    def enterPredicateExprAlt(self, ctx: GQLParser.PredicateExprAltContext):
        pass

    # Exit a parse tree produced by GQLParser#predicateExprAlt.
    def exitPredicateExprAlt(self, ctx: GQLParser.PredicateExprAltContext):
        pass

    # Enter a parse tree produced by GQLParser#valueFunction.
    def enterValueFunction(self, ctx: GQLParser.ValueFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#valueFunction.
    def exitValueFunction(self, ctx: GQLParser.ValueFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#booleanValueExpression.
    def enterBooleanValueExpression(self, ctx: GQLParser.BooleanValueExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#booleanValueExpression.
    def exitBooleanValueExpression(self, ctx: GQLParser.BooleanValueExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#characterOrByteStringFunction.
    def enterCharacterOrByteStringFunction(
        self, ctx: GQLParser.CharacterOrByteStringFunctionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#characterOrByteStringFunction.
    def exitCharacterOrByteStringFunction(
        self, ctx: GQLParser.CharacterOrByteStringFunctionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#subCharacterOrByteString.
    def enterSubCharacterOrByteString(
        self, ctx: GQLParser.SubCharacterOrByteStringContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#subCharacterOrByteString.
    def exitSubCharacterOrByteString(
        self, ctx: GQLParser.SubCharacterOrByteStringContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#trimSingleCharacterOrByteString.
    def enterTrimSingleCharacterOrByteString(
        self, ctx: GQLParser.TrimSingleCharacterOrByteStringContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#trimSingleCharacterOrByteString.
    def exitTrimSingleCharacterOrByteString(
        self, ctx: GQLParser.TrimSingleCharacterOrByteStringContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#foldCharacterString.
    def enterFoldCharacterString(self, ctx: GQLParser.FoldCharacterStringContext):
        pass

    # Exit a parse tree produced by GQLParser#foldCharacterString.
    def exitFoldCharacterString(self, ctx: GQLParser.FoldCharacterStringContext):
        pass

    # Enter a parse tree produced by GQLParser#trimMultiCharacterCharacterString.
    def enterTrimMultiCharacterCharacterString(
        self, ctx: GQLParser.TrimMultiCharacterCharacterStringContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#trimMultiCharacterCharacterString.
    def exitTrimMultiCharacterCharacterString(
        self, ctx: GQLParser.TrimMultiCharacterCharacterStringContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#normalizeCharacterString.
    def enterNormalizeCharacterString(
        self, ctx: GQLParser.NormalizeCharacterStringContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#normalizeCharacterString.
    def exitNormalizeCharacterString(
        self, ctx: GQLParser.NormalizeCharacterStringContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nodeReferenceValueExpression.
    def enterNodeReferenceValueExpression(
        self, ctx: GQLParser.NodeReferenceValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nodeReferenceValueExpression.
    def exitNodeReferenceValueExpression(
        self, ctx: GQLParser.NodeReferenceValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#edgeReferenceValueExpression.
    def enterEdgeReferenceValueExpression(
        self, ctx: GQLParser.EdgeReferenceValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#edgeReferenceValueExpression.
    def exitEdgeReferenceValueExpression(
        self, ctx: GQLParser.EdgeReferenceValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#aggregatingValueExpression.
    def enterAggregatingValueExpression(
        self, ctx: GQLParser.AggregatingValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#aggregatingValueExpression.
    def exitAggregatingValueExpression(
        self, ctx: GQLParser.AggregatingValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#valueExpressionPrimary.
    def enterValueExpressionPrimary(self, ctx: GQLParser.ValueExpressionPrimaryContext):
        pass

    # Exit a parse tree produced by GQLParser#valueExpressionPrimary.
    def exitValueExpressionPrimary(self, ctx: GQLParser.ValueExpressionPrimaryContext):
        pass

    # Enter a parse tree produced by GQLParser#parenthesizedValueExpression.
    def enterParenthesizedValueExpression(
        self, ctx: GQLParser.ParenthesizedValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#parenthesizedValueExpression.
    def exitParenthesizedValueExpression(
        self, ctx: GQLParser.ParenthesizedValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nonParenthesizedValueExpressionPrimary.
    def enterNonParenthesizedValueExpressionPrimary(
        self, ctx: GQLParser.NonParenthesizedValueExpressionPrimaryContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nonParenthesizedValueExpressionPrimary.
    def exitNonParenthesizedValueExpressionPrimary(
        self, ctx: GQLParser.NonParenthesizedValueExpressionPrimaryContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nonParenthesizedValueExpressionPrimarySpecialCase.
    def enterNonParenthesizedValueExpressionPrimarySpecialCase(
        self, ctx: GQLParser.NonParenthesizedValueExpressionPrimarySpecialCaseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nonParenthesizedValueExpressionPrimarySpecialCase.
    def exitNonParenthesizedValueExpressionPrimarySpecialCase(
        self, ctx: GQLParser.NonParenthesizedValueExpressionPrimarySpecialCaseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#unsignedValueSpecification.
    def enterUnsignedValueSpecification(
        self, ctx: GQLParser.UnsignedValueSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#unsignedValueSpecification.
    def exitUnsignedValueSpecification(
        self, ctx: GQLParser.UnsignedValueSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#nonNegativeIntegerSpecification.
    def enterNonNegativeIntegerSpecification(
        self, ctx: GQLParser.NonNegativeIntegerSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#nonNegativeIntegerSpecification.
    def exitNonNegativeIntegerSpecification(
        self, ctx: GQLParser.NonNegativeIntegerSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#generalValueSpecification.
    def enterGeneralValueSpecification(
        self, ctx: GQLParser.GeneralValueSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#generalValueSpecification.
    def exitGeneralValueSpecification(
        self, ctx: GQLParser.GeneralValueSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#dynamicParameterSpecification.
    def enterDynamicParameterSpecification(
        self, ctx: GQLParser.DynamicParameterSpecificationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#dynamicParameterSpecification.
    def exitDynamicParameterSpecification(
        self, ctx: GQLParser.DynamicParameterSpecificationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#letValueExpression.
    def enterLetValueExpression(self, ctx: GQLParser.LetValueExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#letValueExpression.
    def exitLetValueExpression(self, ctx: GQLParser.LetValueExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#valueQueryExpression.
    def enterValueQueryExpression(self, ctx: GQLParser.ValueQueryExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#valueQueryExpression.
    def exitValueQueryExpression(self, ctx: GQLParser.ValueQueryExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#caseExpression.
    def enterCaseExpression(self, ctx: GQLParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#caseExpression.
    def exitCaseExpression(self, ctx: GQLParser.CaseExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#caseAbbreviation.
    def enterCaseAbbreviation(self, ctx: GQLParser.CaseAbbreviationContext):
        pass

    # Exit a parse tree produced by GQLParser#caseAbbreviation.
    def exitCaseAbbreviation(self, ctx: GQLParser.CaseAbbreviationContext):
        pass

    # Enter a parse tree produced by GQLParser#caseSpecification.
    def enterCaseSpecification(self, ctx: GQLParser.CaseSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#caseSpecification.
    def exitCaseSpecification(self, ctx: GQLParser.CaseSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#simpleCase.
    def enterSimpleCase(self, ctx: GQLParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by GQLParser#simpleCase.
    def exitSimpleCase(self, ctx: GQLParser.SimpleCaseContext):
        pass

    # Enter a parse tree produced by GQLParser#searchedCase.
    def enterSearchedCase(self, ctx: GQLParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by GQLParser#searchedCase.
    def exitSearchedCase(self, ctx: GQLParser.SearchedCaseContext):
        pass

    # Enter a parse tree produced by GQLParser#simpleWhenClause.
    def enterSimpleWhenClause(self, ctx: GQLParser.SimpleWhenClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#simpleWhenClause.
    def exitSimpleWhenClause(self, ctx: GQLParser.SimpleWhenClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#searchedWhenClause.
    def enterSearchedWhenClause(self, ctx: GQLParser.SearchedWhenClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#searchedWhenClause.
    def exitSearchedWhenClause(self, ctx: GQLParser.SearchedWhenClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#elseClause.
    def enterElseClause(self, ctx: GQLParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by GQLParser#elseClause.
    def exitElseClause(self, ctx: GQLParser.ElseClauseContext):
        pass

    # Enter a parse tree produced by GQLParser#caseOperand.
    def enterCaseOperand(self, ctx: GQLParser.CaseOperandContext):
        pass

    # Exit a parse tree produced by GQLParser#caseOperand.
    def exitCaseOperand(self, ctx: GQLParser.CaseOperandContext):
        pass

    # Enter a parse tree produced by GQLParser#whenOperandList.
    def enterWhenOperandList(self, ctx: GQLParser.WhenOperandListContext):
        pass

    # Exit a parse tree produced by GQLParser#whenOperandList.
    def exitWhenOperandList(self, ctx: GQLParser.WhenOperandListContext):
        pass

    # Enter a parse tree produced by GQLParser#whenOperand.
    def enterWhenOperand(self, ctx: GQLParser.WhenOperandContext):
        pass

    # Exit a parse tree produced by GQLParser#whenOperand.
    def exitWhenOperand(self, ctx: GQLParser.WhenOperandContext):
        pass

    # Enter a parse tree produced by GQLParser#result.
    def enterResult(self, ctx: GQLParser.ResultContext):
        pass

    # Exit a parse tree produced by GQLParser#result.
    def exitResult(self, ctx: GQLParser.ResultContext):
        pass

    # Enter a parse tree produced by GQLParser#resultExpression.
    def enterResultExpression(self, ctx: GQLParser.ResultExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#resultExpression.
    def exitResultExpression(self, ctx: GQLParser.ResultExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#castSpecification.
    def enterCastSpecification(self, ctx: GQLParser.CastSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#castSpecification.
    def exitCastSpecification(self, ctx: GQLParser.CastSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#castOperand.
    def enterCastOperand(self, ctx: GQLParser.CastOperandContext):
        pass

    # Exit a parse tree produced by GQLParser#castOperand.
    def exitCastOperand(self, ctx: GQLParser.CastOperandContext):
        pass

    # Enter a parse tree produced by GQLParser#castTarget.
    def enterCastTarget(self, ctx: GQLParser.CastTargetContext):
        pass

    # Exit a parse tree produced by GQLParser#castTarget.
    def exitCastTarget(self, ctx: GQLParser.CastTargetContext):
        pass

    # Enter a parse tree produced by GQLParser#aggregateFunction.
    def enterAggregateFunction(self, ctx: GQLParser.AggregateFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#aggregateFunction.
    def exitAggregateFunction(self, ctx: GQLParser.AggregateFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#generalSetFunction.
    def enterGeneralSetFunction(self, ctx: GQLParser.GeneralSetFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#generalSetFunction.
    def exitGeneralSetFunction(self, ctx: GQLParser.GeneralSetFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#binarySetFunction.
    def enterBinarySetFunction(self, ctx: GQLParser.BinarySetFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#binarySetFunction.
    def exitBinarySetFunction(self, ctx: GQLParser.BinarySetFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#generalSetFunctionType.
    def enterGeneralSetFunctionType(self, ctx: GQLParser.GeneralSetFunctionTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#generalSetFunctionType.
    def exitGeneralSetFunctionType(self, ctx: GQLParser.GeneralSetFunctionTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#setQuantifier.
    def enterSetQuantifier(self, ctx: GQLParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by GQLParser#setQuantifier.
    def exitSetQuantifier(self, ctx: GQLParser.SetQuantifierContext):
        pass

    # Enter a parse tree produced by GQLParser#binarySetFunctionType.
    def enterBinarySetFunctionType(self, ctx: GQLParser.BinarySetFunctionTypeContext):
        pass

    # Exit a parse tree produced by GQLParser#binarySetFunctionType.
    def exitBinarySetFunctionType(self, ctx: GQLParser.BinarySetFunctionTypeContext):
        pass

    # Enter a parse tree produced by GQLParser#dependentValueExpression.
    def enterDependentValueExpression(
        self, ctx: GQLParser.DependentValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#dependentValueExpression.
    def exitDependentValueExpression(
        self, ctx: GQLParser.DependentValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#independentValueExpression.
    def enterIndependentValueExpression(
        self, ctx: GQLParser.IndependentValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#independentValueExpression.
    def exitIndependentValueExpression(
        self, ctx: GQLParser.IndependentValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#element_idFunction.
    def enterElement_idFunction(self, ctx: GQLParser.Element_idFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#element_idFunction.
    def exitElement_idFunction(self, ctx: GQLParser.Element_idFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingVariableReference.
    def enterBindingVariableReference(
        self, ctx: GQLParser.BindingVariableReferenceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#bindingVariableReference.
    def exitBindingVariableReference(
        self, ctx: GQLParser.BindingVariableReferenceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#pathValueExpression.
    def enterPathValueExpression(self, ctx: GQLParser.PathValueExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#pathValueExpression.
    def exitPathValueExpression(self, ctx: GQLParser.PathValueExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#pathValueConstructor.
    def enterPathValueConstructor(self, ctx: GQLParser.PathValueConstructorContext):
        pass

    # Exit a parse tree produced by GQLParser#pathValueConstructor.
    def exitPathValueConstructor(self, ctx: GQLParser.PathValueConstructorContext):
        pass

    # Enter a parse tree produced by GQLParser#pathValueConstructorByEnumeration.
    def enterPathValueConstructorByEnumeration(
        self, ctx: GQLParser.PathValueConstructorByEnumerationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#pathValueConstructorByEnumeration.
    def exitPathValueConstructorByEnumeration(
        self, ctx: GQLParser.PathValueConstructorByEnumerationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#pathElementList.
    def enterPathElementList(self, ctx: GQLParser.PathElementListContext):
        pass

    # Exit a parse tree produced by GQLParser#pathElementList.
    def exitPathElementList(self, ctx: GQLParser.PathElementListContext):
        pass

    # Enter a parse tree produced by GQLParser#pathElementListStart.
    def enterPathElementListStart(self, ctx: GQLParser.PathElementListStartContext):
        pass

    # Exit a parse tree produced by GQLParser#pathElementListStart.
    def exitPathElementListStart(self, ctx: GQLParser.PathElementListStartContext):
        pass

    # Enter a parse tree produced by GQLParser#pathElementListStep.
    def enterPathElementListStep(self, ctx: GQLParser.PathElementListStepContext):
        pass

    # Exit a parse tree produced by GQLParser#pathElementListStep.
    def exitPathElementListStep(self, ctx: GQLParser.PathElementListStepContext):
        pass

    # Enter a parse tree produced by GQLParser#listValueExpression.
    def enterListValueExpression(self, ctx: GQLParser.ListValueExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#listValueExpression.
    def exitListValueExpression(self, ctx: GQLParser.ListValueExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#listValueFunction.
    def enterListValueFunction(self, ctx: GQLParser.ListValueFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#listValueFunction.
    def exitListValueFunction(self, ctx: GQLParser.ListValueFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#trimListFunction.
    def enterTrimListFunction(self, ctx: GQLParser.TrimListFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#trimListFunction.
    def exitTrimListFunction(self, ctx: GQLParser.TrimListFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#elementsFunction.
    def enterElementsFunction(self, ctx: GQLParser.ElementsFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#elementsFunction.
    def exitElementsFunction(self, ctx: GQLParser.ElementsFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#listValueConstructor.
    def enterListValueConstructor(self, ctx: GQLParser.ListValueConstructorContext):
        pass

    # Exit a parse tree produced by GQLParser#listValueConstructor.
    def exitListValueConstructor(self, ctx: GQLParser.ListValueConstructorContext):
        pass

    # Enter a parse tree produced by GQLParser#listValueConstructorByEnumeration.
    def enterListValueConstructorByEnumeration(
        self, ctx: GQLParser.ListValueConstructorByEnumerationContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#listValueConstructorByEnumeration.
    def exitListValueConstructorByEnumeration(
        self, ctx: GQLParser.ListValueConstructorByEnumerationContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#listElementList.
    def enterListElementList(self, ctx: GQLParser.ListElementListContext):
        pass

    # Exit a parse tree produced by GQLParser#listElementList.
    def exitListElementList(self, ctx: GQLParser.ListElementListContext):
        pass

    # Enter a parse tree produced by GQLParser#listElement.
    def enterListElement(self, ctx: GQLParser.ListElementContext):
        pass

    # Exit a parse tree produced by GQLParser#listElement.
    def exitListElement(self, ctx: GQLParser.ListElementContext):
        pass

    # Enter a parse tree produced by GQLParser#recordConstructor.
    def enterRecordConstructor(self, ctx: GQLParser.RecordConstructorContext):
        pass

    # Exit a parse tree produced by GQLParser#recordConstructor.
    def exitRecordConstructor(self, ctx: GQLParser.RecordConstructorContext):
        pass

    # Enter a parse tree produced by GQLParser#fieldsSpecification.
    def enterFieldsSpecification(self, ctx: GQLParser.FieldsSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#fieldsSpecification.
    def exitFieldsSpecification(self, ctx: GQLParser.FieldsSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#fieldList.
    def enterFieldList(self, ctx: GQLParser.FieldListContext):
        pass

    # Exit a parse tree produced by GQLParser#fieldList.
    def exitFieldList(self, ctx: GQLParser.FieldListContext):
        pass

    # Enter a parse tree produced by GQLParser#field.
    def enterField(self, ctx: GQLParser.FieldContext):
        pass

    # Exit a parse tree produced by GQLParser#field.
    def exitField(self, ctx: GQLParser.FieldContext):
        pass

    # Enter a parse tree produced by GQLParser#truthValue.
    def enterTruthValue(self, ctx: GQLParser.TruthValueContext):
        pass

    # Exit a parse tree produced by GQLParser#truthValue.
    def exitTruthValue(self, ctx: GQLParser.TruthValueContext):
        pass

    # Enter a parse tree produced by GQLParser#numericValueExpression.
    def enterNumericValueExpression(self, ctx: GQLParser.NumericValueExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#numericValueExpression.
    def exitNumericValueExpression(self, ctx: GQLParser.NumericValueExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#numericValueFunction.
    def enterNumericValueFunction(self, ctx: GQLParser.NumericValueFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#numericValueFunction.
    def exitNumericValueFunction(self, ctx: GQLParser.NumericValueFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#lengthExpression.
    def enterLengthExpression(self, ctx: GQLParser.LengthExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#lengthExpression.
    def exitLengthExpression(self, ctx: GQLParser.LengthExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#cardinalityExpression.
    def enterCardinalityExpression(self, ctx: GQLParser.CardinalityExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#cardinalityExpression.
    def exitCardinalityExpression(self, ctx: GQLParser.CardinalityExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#cardinalityExpressionArgument.
    def enterCardinalityExpressionArgument(
        self, ctx: GQLParser.CardinalityExpressionArgumentContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#cardinalityExpressionArgument.
    def exitCardinalityExpressionArgument(
        self, ctx: GQLParser.CardinalityExpressionArgumentContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#charLengthExpression.
    def enterCharLengthExpression(self, ctx: GQLParser.CharLengthExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#charLengthExpression.
    def exitCharLengthExpression(self, ctx: GQLParser.CharLengthExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#byteLengthExpression.
    def enterByteLengthExpression(self, ctx: GQLParser.ByteLengthExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#byteLengthExpression.
    def exitByteLengthExpression(self, ctx: GQLParser.ByteLengthExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#pathLengthExpression.
    def enterPathLengthExpression(self, ctx: GQLParser.PathLengthExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#pathLengthExpression.
    def exitPathLengthExpression(self, ctx: GQLParser.PathLengthExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#absoluteValueExpression.
    def enterAbsoluteValueExpression(
        self, ctx: GQLParser.AbsoluteValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#absoluteValueExpression.
    def exitAbsoluteValueExpression(
        self, ctx: GQLParser.AbsoluteValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#modulusExpression.
    def enterModulusExpression(self, ctx: GQLParser.ModulusExpressionContext):
        pass

    # Exit a parse tree produced by GQLParser#modulusExpression.
    def exitModulusExpression(self, ctx: GQLParser.ModulusExpressionContext):
        pass

    # Enter a parse tree produced by GQLParser#numericValueExpressionDividend.
    def enterNumericValueExpressionDividend(
        self, ctx: GQLParser.NumericValueExpressionDividendContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#numericValueExpressionDividend.
    def exitNumericValueExpressionDividend(
        self, ctx: GQLParser.NumericValueExpressionDividendContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#numericValueExpressionDivisor.
    def enterNumericValueExpressionDivisor(
        self, ctx: GQLParser.NumericValueExpressionDivisorContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#numericValueExpressionDivisor.
    def exitNumericValueExpressionDivisor(
        self, ctx: GQLParser.NumericValueExpressionDivisorContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#trigonometricFunction.
    def enterTrigonometricFunction(self, ctx: GQLParser.TrigonometricFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#trigonometricFunction.
    def exitTrigonometricFunction(self, ctx: GQLParser.TrigonometricFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#trigonometricFunctionName.
    def enterTrigonometricFunctionName(
        self, ctx: GQLParser.TrigonometricFunctionNameContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#trigonometricFunctionName.
    def exitTrigonometricFunctionName(
        self, ctx: GQLParser.TrigonometricFunctionNameContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#generalLogarithmFunction.
    def enterGeneralLogarithmFunction(
        self, ctx: GQLParser.GeneralLogarithmFunctionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#generalLogarithmFunction.
    def exitGeneralLogarithmFunction(
        self, ctx: GQLParser.GeneralLogarithmFunctionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#generalLogarithmBase.
    def enterGeneralLogarithmBase(self, ctx: GQLParser.GeneralLogarithmBaseContext):
        pass

    # Exit a parse tree produced by GQLParser#generalLogarithmBase.
    def exitGeneralLogarithmBase(self, ctx: GQLParser.GeneralLogarithmBaseContext):
        pass

    # Enter a parse tree produced by GQLParser#generalLogarithmArgument.
    def enterGeneralLogarithmArgument(
        self, ctx: GQLParser.GeneralLogarithmArgumentContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#generalLogarithmArgument.
    def exitGeneralLogarithmArgument(
        self, ctx: GQLParser.GeneralLogarithmArgumentContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#commonLogarithm.
    def enterCommonLogarithm(self, ctx: GQLParser.CommonLogarithmContext):
        pass

    # Exit a parse tree produced by GQLParser#commonLogarithm.
    def exitCommonLogarithm(self, ctx: GQLParser.CommonLogarithmContext):
        pass

    # Enter a parse tree produced by GQLParser#naturalLogarithm.
    def enterNaturalLogarithm(self, ctx: GQLParser.NaturalLogarithmContext):
        pass

    # Exit a parse tree produced by GQLParser#naturalLogarithm.
    def exitNaturalLogarithm(self, ctx: GQLParser.NaturalLogarithmContext):
        pass

    # Enter a parse tree produced by GQLParser#exponentialFunction.
    def enterExponentialFunction(self, ctx: GQLParser.ExponentialFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#exponentialFunction.
    def exitExponentialFunction(self, ctx: GQLParser.ExponentialFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#powerFunction.
    def enterPowerFunction(self, ctx: GQLParser.PowerFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#powerFunction.
    def exitPowerFunction(self, ctx: GQLParser.PowerFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#numericValueExpressionBase.
    def enterNumericValueExpressionBase(
        self, ctx: GQLParser.NumericValueExpressionBaseContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#numericValueExpressionBase.
    def exitNumericValueExpressionBase(
        self, ctx: GQLParser.NumericValueExpressionBaseContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#numericValueExpressionExponent.
    def enterNumericValueExpressionExponent(
        self, ctx: GQLParser.NumericValueExpressionExponentContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#numericValueExpressionExponent.
    def exitNumericValueExpressionExponent(
        self, ctx: GQLParser.NumericValueExpressionExponentContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#squareRoot.
    def enterSquareRoot(self, ctx: GQLParser.SquareRootContext):
        pass

    # Exit a parse tree produced by GQLParser#squareRoot.
    def exitSquareRoot(self, ctx: GQLParser.SquareRootContext):
        pass

    # Enter a parse tree produced by GQLParser#floorFunction.
    def enterFloorFunction(self, ctx: GQLParser.FloorFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#floorFunction.
    def exitFloorFunction(self, ctx: GQLParser.FloorFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#ceilingFunction.
    def enterCeilingFunction(self, ctx: GQLParser.CeilingFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#ceilingFunction.
    def exitCeilingFunction(self, ctx: GQLParser.CeilingFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#characterStringValueExpression.
    def enterCharacterStringValueExpression(
        self, ctx: GQLParser.CharacterStringValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#characterStringValueExpression.
    def exitCharacterStringValueExpression(
        self, ctx: GQLParser.CharacterStringValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#byteStringValueExpression.
    def enterByteStringValueExpression(
        self, ctx: GQLParser.ByteStringValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#byteStringValueExpression.
    def exitByteStringValueExpression(
        self, ctx: GQLParser.ByteStringValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#trimOperands.
    def enterTrimOperands(self, ctx: GQLParser.TrimOperandsContext):
        pass

    # Exit a parse tree produced by GQLParser#trimOperands.
    def exitTrimOperands(self, ctx: GQLParser.TrimOperandsContext):
        pass

    # Enter a parse tree produced by GQLParser#trimCharacterOrByteStringSource.
    def enterTrimCharacterOrByteStringSource(
        self, ctx: GQLParser.TrimCharacterOrByteStringSourceContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#trimCharacterOrByteStringSource.
    def exitTrimCharacterOrByteStringSource(
        self, ctx: GQLParser.TrimCharacterOrByteStringSourceContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#trimSpecification.
    def enterTrimSpecification(self, ctx: GQLParser.TrimSpecificationContext):
        pass

    # Exit a parse tree produced by GQLParser#trimSpecification.
    def exitTrimSpecification(self, ctx: GQLParser.TrimSpecificationContext):
        pass

    # Enter a parse tree produced by GQLParser#trimCharacterOrByteString.
    def enterTrimCharacterOrByteString(
        self, ctx: GQLParser.TrimCharacterOrByteStringContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#trimCharacterOrByteString.
    def exitTrimCharacterOrByteString(
        self, ctx: GQLParser.TrimCharacterOrByteStringContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#normalForm.
    def enterNormalForm(self, ctx: GQLParser.NormalFormContext):
        pass

    # Exit a parse tree produced by GQLParser#normalForm.
    def exitNormalForm(self, ctx: GQLParser.NormalFormContext):
        pass

    # Enter a parse tree produced by GQLParser#stringLength.
    def enterStringLength(self, ctx: GQLParser.StringLengthContext):
        pass

    # Exit a parse tree produced by GQLParser#stringLength.
    def exitStringLength(self, ctx: GQLParser.StringLengthContext):
        pass

    # Enter a parse tree produced by GQLParser#datetimeValueExpression.
    def enterDatetimeValueExpression(
        self, ctx: GQLParser.DatetimeValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#datetimeValueExpression.
    def exitDatetimeValueExpression(
        self, ctx: GQLParser.DatetimeValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#datetimeValueFunction.
    def enterDatetimeValueFunction(self, ctx: GQLParser.DatetimeValueFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#datetimeValueFunction.
    def exitDatetimeValueFunction(self, ctx: GQLParser.DatetimeValueFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#dateFunction.
    def enterDateFunction(self, ctx: GQLParser.DateFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#dateFunction.
    def exitDateFunction(self, ctx: GQLParser.DateFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#timeFunction.
    def enterTimeFunction(self, ctx: GQLParser.TimeFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#timeFunction.
    def exitTimeFunction(self, ctx: GQLParser.TimeFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#localtimeFunction.
    def enterLocaltimeFunction(self, ctx: GQLParser.LocaltimeFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#localtimeFunction.
    def exitLocaltimeFunction(self, ctx: GQLParser.LocaltimeFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#datetimeFunction.
    def enterDatetimeFunction(self, ctx: GQLParser.DatetimeFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#datetimeFunction.
    def exitDatetimeFunction(self, ctx: GQLParser.DatetimeFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#localdatetimeFunction.
    def enterLocaldatetimeFunction(self, ctx: GQLParser.LocaldatetimeFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#localdatetimeFunction.
    def exitLocaldatetimeFunction(self, ctx: GQLParser.LocaldatetimeFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#dateFunctionParameters.
    def enterDateFunctionParameters(self, ctx: GQLParser.DateFunctionParametersContext):
        pass

    # Exit a parse tree produced by GQLParser#dateFunctionParameters.
    def exitDateFunctionParameters(self, ctx: GQLParser.DateFunctionParametersContext):
        pass

    # Enter a parse tree produced by GQLParser#timeFunctionParameters.
    def enterTimeFunctionParameters(self, ctx: GQLParser.TimeFunctionParametersContext):
        pass

    # Exit a parse tree produced by GQLParser#timeFunctionParameters.
    def exitTimeFunctionParameters(self, ctx: GQLParser.TimeFunctionParametersContext):
        pass

    # Enter a parse tree produced by GQLParser#datetimeFunctionParameters.
    def enterDatetimeFunctionParameters(
        self, ctx: GQLParser.DatetimeFunctionParametersContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#datetimeFunctionParameters.
    def exitDatetimeFunctionParameters(
        self, ctx: GQLParser.DatetimeFunctionParametersContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#durationValueExpression.
    def enterDurationValueExpression(
        self, ctx: GQLParser.DurationValueExpressionContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#durationValueExpression.
    def exitDurationValueExpression(
        self, ctx: GQLParser.DurationValueExpressionContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#datetimeSubtraction.
    def enterDatetimeSubtraction(self, ctx: GQLParser.DatetimeSubtractionContext):
        pass

    # Exit a parse tree produced by GQLParser#datetimeSubtraction.
    def exitDatetimeSubtraction(self, ctx: GQLParser.DatetimeSubtractionContext):
        pass

    # Enter a parse tree produced by GQLParser#datetimeSubtractionParameters.
    def enterDatetimeSubtractionParameters(
        self, ctx: GQLParser.DatetimeSubtractionParametersContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#datetimeSubtractionParameters.
    def exitDatetimeSubtractionParameters(
        self, ctx: GQLParser.DatetimeSubtractionParametersContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#datetimeValueExpression1.
    def enterDatetimeValueExpression1(
        self, ctx: GQLParser.DatetimeValueExpression1Context
    ):
        pass

    # Exit a parse tree produced by GQLParser#datetimeValueExpression1.
    def exitDatetimeValueExpression1(
        self, ctx: GQLParser.DatetimeValueExpression1Context
    ):
        pass

    # Enter a parse tree produced by GQLParser#datetimeValueExpression2.
    def enterDatetimeValueExpression2(
        self, ctx: GQLParser.DatetimeValueExpression2Context
    ):
        pass

    # Exit a parse tree produced by GQLParser#datetimeValueExpression2.
    def exitDatetimeValueExpression2(
        self, ctx: GQLParser.DatetimeValueExpression2Context
    ):
        pass

    # Enter a parse tree produced by GQLParser#durationValueFunction.
    def enterDurationValueFunction(self, ctx: GQLParser.DurationValueFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#durationValueFunction.
    def exitDurationValueFunction(self, ctx: GQLParser.DurationValueFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#durationFunction.
    def enterDurationFunction(self, ctx: GQLParser.DurationFunctionContext):
        pass

    # Exit a parse tree produced by GQLParser#durationFunction.
    def exitDurationFunction(self, ctx: GQLParser.DurationFunctionContext):
        pass

    # Enter a parse tree produced by GQLParser#durationFunctionParameters.
    def enterDurationFunctionParameters(
        self, ctx: GQLParser.DurationFunctionParametersContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#durationFunctionParameters.
    def exitDurationFunctionParameters(
        self, ctx: GQLParser.DurationFunctionParametersContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#objectName.
    def enterObjectName(self, ctx: GQLParser.ObjectNameContext):
        pass

    # Exit a parse tree produced by GQLParser#objectName.
    def exitObjectName(self, ctx: GQLParser.ObjectNameContext):
        pass

    # Enter a parse tree produced by GQLParser#objectNameOrBindingVariable.
    def enterObjectNameOrBindingVariable(
        self, ctx: GQLParser.ObjectNameOrBindingVariableContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#objectNameOrBindingVariable.
    def exitObjectNameOrBindingVariable(
        self, ctx: GQLParser.ObjectNameOrBindingVariableContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#directoryName.
    def enterDirectoryName(self, ctx: GQLParser.DirectoryNameContext):
        pass

    # Exit a parse tree produced by GQLParser#directoryName.
    def exitDirectoryName(self, ctx: GQLParser.DirectoryNameContext):
        pass

    # Enter a parse tree produced by GQLParser#schemaName.
    def enterSchemaName(self, ctx: GQLParser.SchemaNameContext):
        pass

    # Exit a parse tree produced by GQLParser#schemaName.
    def exitSchemaName(self, ctx: GQLParser.SchemaNameContext):
        pass

    # Enter a parse tree produced by GQLParser#graphName.
    def enterGraphName(self, ctx: GQLParser.GraphNameContext):
        pass

    # Exit a parse tree produced by GQLParser#graphName.
    def exitGraphName(self, ctx: GQLParser.GraphNameContext):
        pass

    # Enter a parse tree produced by GQLParser#delimitedGraphName.
    def enterDelimitedGraphName(self, ctx: GQLParser.DelimitedGraphNameContext):
        pass

    # Exit a parse tree produced by GQLParser#delimitedGraphName.
    def exitDelimitedGraphName(self, ctx: GQLParser.DelimitedGraphNameContext):
        pass

    # Enter a parse tree produced by GQLParser#graphTypeName.
    def enterGraphTypeName(self, ctx: GQLParser.GraphTypeNameContext):
        pass

    # Exit a parse tree produced by GQLParser#graphTypeName.
    def exitGraphTypeName(self, ctx: GQLParser.GraphTypeNameContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeTypeName.
    def enterNodeTypeName(self, ctx: GQLParser.NodeTypeNameContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeTypeName.
    def exitNodeTypeName(self, ctx: GQLParser.NodeTypeNameContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeTypeName.
    def enterEdgeTypeName(self, ctx: GQLParser.EdgeTypeNameContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeTypeName.
    def exitEdgeTypeName(self, ctx: GQLParser.EdgeTypeNameContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingTableName.
    def enterBindingTableName(self, ctx: GQLParser.BindingTableNameContext):
        pass

    # Exit a parse tree produced by GQLParser#bindingTableName.
    def exitBindingTableName(self, ctx: GQLParser.BindingTableNameContext):
        pass

    # Enter a parse tree produced by GQLParser#delimitedBindingTableName.
    def enterDelimitedBindingTableName(
        self, ctx: GQLParser.DelimitedBindingTableNameContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#delimitedBindingTableName.
    def exitDelimitedBindingTableName(
        self, ctx: GQLParser.DelimitedBindingTableNameContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#procedureName.
    def enterProcedureName(self, ctx: GQLParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by GQLParser#procedureName.
    def exitProcedureName(self, ctx: GQLParser.ProcedureNameContext):
        pass

    # Enter a parse tree produced by GQLParser#labelName.
    def enterLabelName(self, ctx: GQLParser.LabelNameContext):
        pass

    # Exit a parse tree produced by GQLParser#labelName.
    def exitLabelName(self, ctx: GQLParser.LabelNameContext):
        pass

    # Enter a parse tree produced by GQLParser#propertyName.
    def enterPropertyName(self, ctx: GQLParser.PropertyNameContext):
        pass

    # Exit a parse tree produced by GQLParser#propertyName.
    def exitPropertyName(self, ctx: GQLParser.PropertyNameContext):
        pass

    # Enter a parse tree produced by GQLParser#fieldName.
    def enterFieldName(self, ctx: GQLParser.FieldNameContext):
        pass

    # Exit a parse tree produced by GQLParser#fieldName.
    def exitFieldName(self, ctx: GQLParser.FieldNameContext):
        pass

    # Enter a parse tree produced by GQLParser#elementVariable.
    def enterElementVariable(self, ctx: GQLParser.ElementVariableContext):
        pass

    # Exit a parse tree produced by GQLParser#elementVariable.
    def exitElementVariable(self, ctx: GQLParser.ElementVariableContext):
        pass

    # Enter a parse tree produced by GQLParser#pathVariable.
    def enterPathVariable(self, ctx: GQLParser.PathVariableContext):
        pass

    # Exit a parse tree produced by GQLParser#pathVariable.
    def exitPathVariable(self, ctx: GQLParser.PathVariableContext):
        pass

    # Enter a parse tree produced by GQLParser#subpathVariable.
    def enterSubpathVariable(self, ctx: GQLParser.SubpathVariableContext):
        pass

    # Exit a parse tree produced by GQLParser#subpathVariable.
    def exitSubpathVariable(self, ctx: GQLParser.SubpathVariableContext):
        pass

    # Enter a parse tree produced by GQLParser#bindingVariable.
    def enterBindingVariable(self, ctx: GQLParser.BindingVariableContext):
        pass

    # Exit a parse tree produced by GQLParser#bindingVariable.
    def exitBindingVariable(self, ctx: GQLParser.BindingVariableContext):
        pass

    # Enter a parse tree produced by GQLParser#unsignedLiteral.
    def enterUnsignedLiteral(self, ctx: GQLParser.UnsignedLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#unsignedLiteral.
    def exitUnsignedLiteral(self, ctx: GQLParser.UnsignedLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#generalLiteral.
    def enterGeneralLiteral(self, ctx: GQLParser.GeneralLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#generalLiteral.
    def exitGeneralLiteral(self, ctx: GQLParser.GeneralLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#temporalLiteral.
    def enterTemporalLiteral(self, ctx: GQLParser.TemporalLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#temporalLiteral.
    def exitTemporalLiteral(self, ctx: GQLParser.TemporalLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#dateLiteral.
    def enterDateLiteral(self, ctx: GQLParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#dateLiteral.
    def exitDateLiteral(self, ctx: GQLParser.DateLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#timeLiteral.
    def enterTimeLiteral(self, ctx: GQLParser.TimeLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#timeLiteral.
    def exitTimeLiteral(self, ctx: GQLParser.TimeLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#datetimeLiteral.
    def enterDatetimeLiteral(self, ctx: GQLParser.DatetimeLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#datetimeLiteral.
    def exitDatetimeLiteral(self, ctx: GQLParser.DatetimeLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#listLiteral.
    def enterListLiteral(self, ctx: GQLParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#listLiteral.
    def exitListLiteral(self, ctx: GQLParser.ListLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#recordLiteral.
    def enterRecordLiteral(self, ctx: GQLParser.RecordLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#recordLiteral.
    def exitRecordLiteral(self, ctx: GQLParser.RecordLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#identifier.
    def enterIdentifier(self, ctx: GQLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GQLParser#identifier.
    def exitIdentifier(self, ctx: GQLParser.IdentifierContext):
        pass

    # Enter a parse tree produced by GQLParser#regularIdentifier.
    def enterRegularIdentifier(self, ctx: GQLParser.RegularIdentifierContext):
        pass

    # Exit a parse tree produced by GQLParser#regularIdentifier.
    def exitRegularIdentifier(self, ctx: GQLParser.RegularIdentifierContext):
        pass

    # Enter a parse tree produced by GQLParser#timeZoneString.
    def enterTimeZoneString(self, ctx: GQLParser.TimeZoneStringContext):
        pass

    # Exit a parse tree produced by GQLParser#timeZoneString.
    def exitTimeZoneString(self, ctx: GQLParser.TimeZoneStringContext):
        pass

    # Enter a parse tree produced by GQLParser#characterStringLiteral.
    def enterCharacterStringLiteral(self, ctx: GQLParser.CharacterStringLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#characterStringLiteral.
    def exitCharacterStringLiteral(self, ctx: GQLParser.CharacterStringLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#unsignedNumericLiteral.
    def enterUnsignedNumericLiteral(self, ctx: GQLParser.UnsignedNumericLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#unsignedNumericLiteral.
    def exitUnsignedNumericLiteral(self, ctx: GQLParser.UnsignedNumericLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#exactNumericLiteral.
    def enterExactNumericLiteral(self, ctx: GQLParser.ExactNumericLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#exactNumericLiteral.
    def exitExactNumericLiteral(self, ctx: GQLParser.ExactNumericLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#approximateNumericLiteral.
    def enterApproximateNumericLiteral(
        self, ctx: GQLParser.ApproximateNumericLiteralContext
    ):
        pass

    # Exit a parse tree produced by GQLParser#approximateNumericLiteral.
    def exitApproximateNumericLiteral(
        self, ctx: GQLParser.ApproximateNumericLiteralContext
    ):
        pass

    # Enter a parse tree produced by GQLParser#unsignedInteger.
    def enterUnsignedInteger(self, ctx: GQLParser.UnsignedIntegerContext):
        pass

    # Exit a parse tree produced by GQLParser#unsignedInteger.
    def exitUnsignedInteger(self, ctx: GQLParser.UnsignedIntegerContext):
        pass

    # Enter a parse tree produced by GQLParser#unsignedDecimalInteger.
    def enterUnsignedDecimalInteger(self, ctx: GQLParser.UnsignedDecimalIntegerContext):
        pass

    # Exit a parse tree produced by GQLParser#unsignedDecimalInteger.
    def exitUnsignedDecimalInteger(self, ctx: GQLParser.UnsignedDecimalIntegerContext):
        pass

    # Enter a parse tree produced by GQLParser#nullLiteral.
    def enterNullLiteral(self, ctx: GQLParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#nullLiteral.
    def exitNullLiteral(self, ctx: GQLParser.NullLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#dateString.
    def enterDateString(self, ctx: GQLParser.DateStringContext):
        pass

    # Exit a parse tree produced by GQLParser#dateString.
    def exitDateString(self, ctx: GQLParser.DateStringContext):
        pass

    # Enter a parse tree produced by GQLParser#timeString.
    def enterTimeString(self, ctx: GQLParser.TimeStringContext):
        pass

    # Exit a parse tree produced by GQLParser#timeString.
    def exitTimeString(self, ctx: GQLParser.TimeStringContext):
        pass

    # Enter a parse tree produced by GQLParser#datetimeString.
    def enterDatetimeString(self, ctx: GQLParser.DatetimeStringContext):
        pass

    # Exit a parse tree produced by GQLParser#datetimeString.
    def exitDatetimeString(self, ctx: GQLParser.DatetimeStringContext):
        pass

    # Enter a parse tree produced by GQLParser#durationLiteral.
    def enterDurationLiteral(self, ctx: GQLParser.DurationLiteralContext):
        pass

    # Exit a parse tree produced by GQLParser#durationLiteral.
    def exitDurationLiteral(self, ctx: GQLParser.DurationLiteralContext):
        pass

    # Enter a parse tree produced by GQLParser#durationString.
    def enterDurationString(self, ctx: GQLParser.DurationStringContext):
        pass

    # Exit a parse tree produced by GQLParser#durationString.
    def exitDurationString(self, ctx: GQLParser.DurationStringContext):
        pass

    # Enter a parse tree produced by GQLParser#nodeSynonym.
    def enterNodeSynonym(self, ctx: GQLParser.NodeSynonymContext):
        pass

    # Exit a parse tree produced by GQLParser#nodeSynonym.
    def exitNodeSynonym(self, ctx: GQLParser.NodeSynonymContext):
        pass

    # Enter a parse tree produced by GQLParser#edgesSynonym.
    def enterEdgesSynonym(self, ctx: GQLParser.EdgesSynonymContext):
        pass

    # Exit a parse tree produced by GQLParser#edgesSynonym.
    def exitEdgesSynonym(self, ctx: GQLParser.EdgesSynonymContext):
        pass

    # Enter a parse tree produced by GQLParser#edgeSynonym.
    def enterEdgeSynonym(self, ctx: GQLParser.EdgeSynonymContext):
        pass

    # Exit a parse tree produced by GQLParser#edgeSynonym.
    def exitEdgeSynonym(self, ctx: GQLParser.EdgeSynonymContext):
        pass

    # Enter a parse tree produced by GQLParser#nonReservedWords.
    def enterNonReservedWords(self, ctx: GQLParser.NonReservedWordsContext):
        pass

    # Exit a parse tree produced by GQLParser#nonReservedWords.
    def exitNonReservedWords(self, ctx: GQLParser.NonReservedWordsContext):
        pass


del GQLParser
