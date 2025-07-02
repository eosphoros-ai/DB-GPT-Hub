# Generated from ./GQL.g4 by ANTLR 4.13.2
from antlr4 import ParseTreeVisitor

if "." in __name__:
    from .GQLParser import GQLParser
else:
    from GQLParser import GQLParser

# This class defines a complete generic visitor for a parse tree produced by GQLParser.


class GQLVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by GQLParser#gqlProgram.
    def visitGqlProgram(self, ctx: GQLParser.GqlProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#programActivity.
    def visitProgramActivity(self, ctx: GQLParser.ProgramActivityContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionActivity.
    def visitSessionActivity(self, ctx: GQLParser.SessionActivityContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#transactionActivity.
    def visitTransactionActivity(self, ctx: GQLParser.TransactionActivityContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#endTransactionCommand.
    def visitEndTransactionCommand(self, ctx: GQLParser.EndTransactionCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetCommand.
    def visitSessionSetCommand(self, ctx: GQLParser.SessionSetCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetSchemaClause.
    def visitSessionSetSchemaClause(self, ctx: GQLParser.SessionSetSchemaClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetGraphClause.
    def visitSessionSetGraphClause(self, ctx: GQLParser.SessionSetGraphClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetTimeZoneClause.
    def visitSessionSetTimeZoneClause(
        self, ctx: GQLParser.SessionSetTimeZoneClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setTimeZoneValue.
    def visitSetTimeZoneValue(self, ctx: GQLParser.SetTimeZoneValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetParameterClause.
    def visitSessionSetParameterClause(
        self, ctx: GQLParser.SessionSetParameterClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetGraphParameterClause.
    def visitSessionSetGraphParameterClause(
        self, ctx: GQLParser.SessionSetGraphParameterClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetBindingTableParameterClause.
    def visitSessionSetBindingTableParameterClause(
        self, ctx: GQLParser.SessionSetBindingTableParameterClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetValueParameterClause.
    def visitSessionSetValueParameterClause(
        self, ctx: GQLParser.SessionSetValueParameterClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionSetParameterName.
    def visitSessionSetParameterName(
        self, ctx: GQLParser.SessionSetParameterNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionResetCommand.
    def visitSessionResetCommand(self, ctx: GQLParser.SessionResetCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionResetArguments.
    def visitSessionResetArguments(self, ctx: GQLParser.SessionResetArgumentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionCloseCommand.
    def visitSessionCloseCommand(self, ctx: GQLParser.SessionCloseCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sessionParameterSpecification.
    def visitSessionParameterSpecification(
        self, ctx: GQLParser.SessionParameterSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#startTransactionCommand.
    def visitStartTransactionCommand(
        self, ctx: GQLParser.StartTransactionCommandContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#transactionCharacteristics.
    def visitTransactionCharacteristics(
        self, ctx: GQLParser.TransactionCharacteristicsContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#transactionMode.
    def visitTransactionMode(self, ctx: GQLParser.TransactionModeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#transactionAccessMode.
    def visitTransactionAccessMode(self, ctx: GQLParser.TransactionAccessModeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#rollbackCommand.
    def visitRollbackCommand(self, ctx: GQLParser.RollbackCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#commitCommand.
    def visitCommitCommand(self, ctx: GQLParser.CommitCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nestedProcedureSpecification.
    def visitNestedProcedureSpecification(
        self, ctx: GQLParser.NestedProcedureSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#procedureSpecification.
    def visitProcedureSpecification(self, ctx: GQLParser.ProcedureSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nestedDataModifyingProcedureSpecification.
    def visitNestedDataModifyingProcedureSpecification(
        self, ctx: GQLParser.NestedDataModifyingProcedureSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nestedQuerySpecification.
    def visitNestedQuerySpecification(
        self, ctx: GQLParser.NestedQuerySpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#procedureBody.
    def visitProcedureBody(self, ctx: GQLParser.ProcedureBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingVariableDefinitionBlock.
    def visitBindingVariableDefinitionBlock(
        self, ctx: GQLParser.BindingVariableDefinitionBlockContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingVariableDefinition.
    def visitBindingVariableDefinition(
        self, ctx: GQLParser.BindingVariableDefinitionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#statementBlock.
    def visitStatementBlock(self, ctx: GQLParser.StatementBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#statement.
    def visitStatement(self, ctx: GQLParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nextStatement.
    def visitNextStatement(self, ctx: GQLParser.NextStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphVariableDefinition.
    def visitGraphVariableDefinition(
        self, ctx: GQLParser.GraphVariableDefinitionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#optTypedGraphInitializer.
    def visitOptTypedGraphInitializer(
        self, ctx: GQLParser.OptTypedGraphInitializerContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphInitializer.
    def visitGraphInitializer(self, ctx: GQLParser.GraphInitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableVariableDefinition.
    def visitBindingTableVariableDefinition(
        self, ctx: GQLParser.BindingTableVariableDefinitionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#optTypedBindingTableInitializer.
    def visitOptTypedBindingTableInitializer(
        self, ctx: GQLParser.OptTypedBindingTableInitializerContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableInitializer.
    def visitBindingTableInitializer(
        self, ctx: GQLParser.BindingTableInitializerContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueVariableDefinition.
    def visitValueVariableDefinition(
        self, ctx: GQLParser.ValueVariableDefinitionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#optTypedValueInitializer.
    def visitOptTypedValueInitializer(
        self, ctx: GQLParser.OptTypedValueInitializerContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueInitializer.
    def visitValueInitializer(self, ctx: GQLParser.ValueInitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphExpression.
    def visitGraphExpression(self, ctx: GQLParser.GraphExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#currentGraph.
    def visitCurrentGraph(self, ctx: GQLParser.CurrentGraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableExpression.
    def visitBindingTableExpression(self, ctx: GQLParser.BindingTableExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nestedBindingTableQuerySpecification.
    def visitNestedBindingTableQuerySpecification(
        self, ctx: GQLParser.NestedBindingTableQuerySpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#objectExpressionPrimary.
    def visitObjectExpressionPrimary(
        self, ctx: GQLParser.ObjectExpressionPrimaryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#linearCatalogModifyingStatement.
    def visitLinearCatalogModifyingStatement(
        self, ctx: GQLParser.LinearCatalogModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleCatalogModifyingStatement.
    def visitSimpleCatalogModifyingStatement(
        self, ctx: GQLParser.SimpleCatalogModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#primitiveCatalogModifyingStatement.
    def visitPrimitiveCatalogModifyingStatement(
        self, ctx: GQLParser.PrimitiveCatalogModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#createSchemaStatement.
    def visitCreateSchemaStatement(self, ctx: GQLParser.CreateSchemaStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dropSchemaStatement.
    def visitDropSchemaStatement(self, ctx: GQLParser.DropSchemaStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#createGraphStatement.
    def visitCreateGraphStatement(self, ctx: GQLParser.CreateGraphStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#openGraphType.
    def visitOpenGraphType(self, ctx: GQLParser.OpenGraphTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ofGraphType.
    def visitOfGraphType(self, ctx: GQLParser.OfGraphTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphTypeLikeGraph.
    def visitGraphTypeLikeGraph(self, ctx: GQLParser.GraphTypeLikeGraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphSource.
    def visitGraphSource(self, ctx: GQLParser.GraphSourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dropGraphStatement.
    def visitDropGraphStatement(self, ctx: GQLParser.DropGraphStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#createGraphTypeStatement.
    def visitCreateGraphTypeStatement(
        self, ctx: GQLParser.CreateGraphTypeStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphTypeSource.
    def visitGraphTypeSource(self, ctx: GQLParser.GraphTypeSourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#copyOfGraphType.
    def visitCopyOfGraphType(self, ctx: GQLParser.CopyOfGraphTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dropGraphTypeStatement.
    def visitDropGraphTypeStatement(self, ctx: GQLParser.DropGraphTypeStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#callCatalogModifyingProcedureStatement.
    def visitCallCatalogModifyingProcedureStatement(
        self, ctx: GQLParser.CallCatalogModifyingProcedureStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#linearDataModifyingStatement.
    def visitLinearDataModifyingStatement(
        self, ctx: GQLParser.LinearDataModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedLinearDataModifyingStatement.
    def visitFocusedLinearDataModifyingStatement(
        self, ctx: GQLParser.FocusedLinearDataModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedLinearDataModifyingStatementBody.
    def visitFocusedLinearDataModifyingStatementBody(
        self, ctx: GQLParser.FocusedLinearDataModifyingStatementBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedNestedDataModifyingProcedureSpecification.
    def visitFocusedNestedDataModifyingProcedureSpecification(
        self, ctx: GQLParser.FocusedNestedDataModifyingProcedureSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ambientLinearDataModifyingStatement.
    def visitAmbientLinearDataModifyingStatement(
        self, ctx: GQLParser.AmbientLinearDataModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ambientLinearDataModifyingStatementBody.
    def visitAmbientLinearDataModifyingStatementBody(
        self, ctx: GQLParser.AmbientLinearDataModifyingStatementBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleLinearDataAccessingStatement.
    def visitSimpleLinearDataAccessingStatement(
        self, ctx: GQLParser.SimpleLinearDataAccessingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleDataAccessingStatement.
    def visitSimpleDataAccessingStatement(
        self, ctx: GQLParser.SimpleDataAccessingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleDataModifyingStatement.
    def visitSimpleDataModifyingStatement(
        self, ctx: GQLParser.SimpleDataModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#primitiveDataModifyingStatement.
    def visitPrimitiveDataModifyingStatement(
        self, ctx: GQLParser.PrimitiveDataModifyingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertStatement.
    def visitInsertStatement(self, ctx: GQLParser.InsertStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setStatement.
    def visitSetStatement(self, ctx: GQLParser.SetStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setItemList.
    def visitSetItemList(self, ctx: GQLParser.SetItemListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setItem.
    def visitSetItem(self, ctx: GQLParser.SetItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setPropertyItem.
    def visitSetPropertyItem(self, ctx: GQLParser.SetPropertyItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setAllPropertiesItem.
    def visitSetAllPropertiesItem(self, ctx: GQLParser.SetAllPropertiesItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setLabelItem.
    def visitSetLabelItem(self, ctx: GQLParser.SetLabelItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#removeStatement.
    def visitRemoveStatement(self, ctx: GQLParser.RemoveStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#removeItemList.
    def visitRemoveItemList(self, ctx: GQLParser.RemoveItemListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#removeItem.
    def visitRemoveItem(self, ctx: GQLParser.RemoveItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#removePropertyItem.
    def visitRemovePropertyItem(self, ctx: GQLParser.RemovePropertyItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#removeLabelItem.
    def visitRemoveLabelItem(self, ctx: GQLParser.RemoveLabelItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#deleteStatement.
    def visitDeleteStatement(self, ctx: GQLParser.DeleteStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#deleteItemList.
    def visitDeleteItemList(self, ctx: GQLParser.DeleteItemListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#deleteItem.
    def visitDeleteItem(self, ctx: GQLParser.DeleteItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#callDataModifyingProcedureStatement.
    def visitCallDataModifyingProcedureStatement(
        self, ctx: GQLParser.CallDataModifyingProcedureStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#compositeQueryStatement.
    def visitCompositeQueryStatement(
        self, ctx: GQLParser.CompositeQueryStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#compositeQueryExpression.
    def visitCompositeQueryExpression(
        self, ctx: GQLParser.CompositeQueryExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#queryConjunction.
    def visitQueryConjunction(self, ctx: GQLParser.QueryConjunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setOperator.
    def visitSetOperator(self, ctx: GQLParser.SetOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#compositeQueryPrimary.
    def visitCompositeQueryPrimary(self, ctx: GQLParser.CompositeQueryPrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#linearQueryStatement.
    def visitLinearQueryStatement(self, ctx: GQLParser.LinearQueryStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedLinearQueryStatement.
    def visitFocusedLinearQueryStatement(
        self, ctx: GQLParser.FocusedLinearQueryStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedLinearQueryStatementPart.
    def visitFocusedLinearQueryStatementPart(
        self, ctx: GQLParser.FocusedLinearQueryStatementPartContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedLinearQueryAndPrimitiveResultStatementPart.
    def visitFocusedLinearQueryAndPrimitiveResultStatementPart(
        self, ctx: GQLParser.FocusedLinearQueryAndPrimitiveResultStatementPartContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedPrimitiveResultStatement.
    def visitFocusedPrimitiveResultStatement(
        self, ctx: GQLParser.FocusedPrimitiveResultStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#focusedNestedQuerySpecification.
    def visitFocusedNestedQuerySpecification(
        self, ctx: GQLParser.FocusedNestedQuerySpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ambientLinearQueryStatement.
    def visitAmbientLinearQueryStatement(
        self, ctx: GQLParser.AmbientLinearQueryStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleLinearQueryStatement.
    def visitSimpleLinearQueryStatement(
        self, ctx: GQLParser.SimpleLinearQueryStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleQueryStatement.
    def visitSimpleQueryStatement(self, ctx: GQLParser.SimpleQueryStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#primitiveQueryStatement.
    def visitPrimitiveQueryStatement(
        self, ctx: GQLParser.PrimitiveQueryStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#matchStatement.
    def visitMatchStatement(self, ctx: GQLParser.MatchStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleMatchStatement.
    def visitSimpleMatchStatement(self, ctx: GQLParser.SimpleMatchStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#optionalMatchStatement.
    def visitOptionalMatchStatement(self, ctx: GQLParser.OptionalMatchStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#optionalOperand.
    def visitOptionalOperand(self, ctx: GQLParser.OptionalOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#matchStatementBlock.
    def visitMatchStatementBlock(self, ctx: GQLParser.MatchStatementBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#callQueryStatement.
    def visitCallQueryStatement(self, ctx: GQLParser.CallQueryStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#filterStatement.
    def visitFilterStatement(self, ctx: GQLParser.FilterStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#letStatement.
    def visitLetStatement(self, ctx: GQLParser.LetStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#letVariableDefinitionList.
    def visitLetVariableDefinitionList(
        self, ctx: GQLParser.LetVariableDefinitionListContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#letVariableDefinition.
    def visitLetVariableDefinition(self, ctx: GQLParser.LetVariableDefinitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#forStatement.
    def visitForStatement(self, ctx: GQLParser.ForStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#forItem.
    def visitForItem(self, ctx: GQLParser.ForItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#forItemAlias.
    def visitForItemAlias(self, ctx: GQLParser.ForItemAliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#forItemSource.
    def visitForItemSource(self, ctx: GQLParser.ForItemSourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#forOrdinalityOrOffset.
    def visitForOrdinalityOrOffset(self, ctx: GQLParser.ForOrdinalityOrOffsetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#orderByAndPageStatement.
    def visitOrderByAndPageStatement(
        self, ctx: GQLParser.OrderByAndPageStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#primitiveResultStatement.
    def visitPrimitiveResultStatement(
        self, ctx: GQLParser.PrimitiveResultStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#returnStatement.
    def visitReturnStatement(self, ctx: GQLParser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#returnStatementBody.
    def visitReturnStatementBody(self, ctx: GQLParser.ReturnStatementBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#returnItemList.
    def visitReturnItemList(self, ctx: GQLParser.ReturnItemListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#returnItem.
    def visitReturnItem(self, ctx: GQLParser.ReturnItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#returnItemAlias.
    def visitReturnItemAlias(self, ctx: GQLParser.ReturnItemAliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectStatement.
    def visitSelectStatement(self, ctx: GQLParser.SelectStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectItemList.
    def visitSelectItemList(self, ctx: GQLParser.SelectItemListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectItem.
    def visitSelectItem(self, ctx: GQLParser.SelectItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectItemAlias.
    def visitSelectItemAlias(self, ctx: GQLParser.SelectItemAliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#havingClause.
    def visitHavingClause(self, ctx: GQLParser.HavingClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectStatementBody.
    def visitSelectStatementBody(self, ctx: GQLParser.SelectStatementBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectGraphMatchList.
    def visitSelectGraphMatchList(self, ctx: GQLParser.SelectGraphMatchListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectGraphMatch.
    def visitSelectGraphMatch(self, ctx: GQLParser.SelectGraphMatchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#selectQuerySpecification.
    def visitSelectQuerySpecification(
        self, ctx: GQLParser.SelectQuerySpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#callProcedureStatement.
    def visitCallProcedureStatement(self, ctx: GQLParser.CallProcedureStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#procedureCall.
    def visitProcedureCall(self, ctx: GQLParser.ProcedureCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#inlineProcedureCall.
    def visitInlineProcedureCall(self, ctx: GQLParser.InlineProcedureCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#variableScopeClause.
    def visitVariableScopeClause(self, ctx: GQLParser.VariableScopeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingVariableReferenceList.
    def visitBindingVariableReferenceList(
        self, ctx: GQLParser.BindingVariableReferenceListContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#namedProcedureCall.
    def visitNamedProcedureCall(self, ctx: GQLParser.NamedProcedureCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#procedureArgumentList.
    def visitProcedureArgumentList(self, ctx: GQLParser.ProcedureArgumentListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#procedureArgument.
    def visitProcedureArgument(self, ctx: GQLParser.ProcedureArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#atSchemaClause.
    def visitAtSchemaClause(self, ctx: GQLParser.AtSchemaClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#useGraphClause.
    def visitUseGraphClause(self, ctx: GQLParser.UseGraphClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphPatternBindingTable.
    def visitGraphPatternBindingTable(
        self, ctx: GQLParser.GraphPatternBindingTableContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphPatternYieldClause.
    def visitGraphPatternYieldClause(
        self, ctx: GQLParser.GraphPatternYieldClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphPatternYieldItemList.
    def visitGraphPatternYieldItemList(
        self, ctx: GQLParser.GraphPatternYieldItemListContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphPatternYieldItem.
    def visitGraphPatternYieldItem(self, ctx: GQLParser.GraphPatternYieldItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphPattern.
    def visitGraphPattern(self, ctx: GQLParser.GraphPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#matchMode.
    def visitMatchMode(self, ctx: GQLParser.MatchModeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#repeatableElementsMatchMode.
    def visitRepeatableElementsMatchMode(
        self, ctx: GQLParser.RepeatableElementsMatchModeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#differentEdgesMatchMode.
    def visitDifferentEdgesMatchMode(
        self, ctx: GQLParser.DifferentEdgesMatchModeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementBindingsOrElements.
    def visitElementBindingsOrElements(
        self, ctx: GQLParser.ElementBindingsOrElementsContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeBindingsOrEdges.
    def visitEdgeBindingsOrEdges(self, ctx: GQLParser.EdgeBindingsOrEdgesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathPatternList.
    def visitPathPatternList(self, ctx: GQLParser.PathPatternListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathPattern.
    def visitPathPattern(self, ctx: GQLParser.PathPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathVariableDeclaration.
    def visitPathVariableDeclaration(
        self, ctx: GQLParser.PathVariableDeclarationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#keepClause.
    def visitKeepClause(self, ctx: GQLParser.KeepClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphPatternWhereClause.
    def visitGraphPatternWhereClause(
        self, ctx: GQLParser.GraphPatternWhereClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertGraphPattern.
    def visitInsertGraphPattern(self, ctx: GQLParser.InsertGraphPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertPathPatternList.
    def visitInsertPathPatternList(self, ctx: GQLParser.InsertPathPatternListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertPathPattern.
    def visitInsertPathPattern(self, ctx: GQLParser.InsertPathPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertNodePattern.
    def visitInsertNodePattern(self, ctx: GQLParser.InsertNodePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertEdgePattern.
    def visitInsertEdgePattern(self, ctx: GQLParser.InsertEdgePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertEdgePointingLeft.
    def visitInsertEdgePointingLeft(self, ctx: GQLParser.InsertEdgePointingLeftContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertEdgePointingRight.
    def visitInsertEdgePointingRight(
        self, ctx: GQLParser.InsertEdgePointingRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertEdgeUndirected.
    def visitInsertEdgeUndirected(self, ctx: GQLParser.InsertEdgeUndirectedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#insertElementPatternFiller.
    def visitInsertElementPatternFiller(
        self, ctx: GQLParser.InsertElementPatternFillerContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelAndPropertySetSpecification.
    def visitLabelAndPropertySetSpecification(
        self, ctx: GQLParser.LabelAndPropertySetSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathPatternPrefix.
    def visitPathPatternPrefix(self, ctx: GQLParser.PathPatternPrefixContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathModePrefix.
    def visitPathModePrefix(self, ctx: GQLParser.PathModePrefixContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathMode.
    def visitPathMode(self, ctx: GQLParser.PathModeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathSearchPrefix.
    def visitPathSearchPrefix(self, ctx: GQLParser.PathSearchPrefixContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#allPathSearch.
    def visitAllPathSearch(self, ctx: GQLParser.AllPathSearchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathOrPaths.
    def visitPathOrPaths(self, ctx: GQLParser.PathOrPathsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#anyPathSearch.
    def visitAnyPathSearch(self, ctx: GQLParser.AnyPathSearchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numberOfPaths.
    def visitNumberOfPaths(self, ctx: GQLParser.NumberOfPathsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#shortestPathSearch.
    def visitShortestPathSearch(self, ctx: GQLParser.ShortestPathSearchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#allShortestPathSearch.
    def visitAllShortestPathSearch(self, ctx: GQLParser.AllShortestPathSearchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#anyShortestPathSearch.
    def visitAnyShortestPathSearch(self, ctx: GQLParser.AnyShortestPathSearchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#countedShortestPathSearch.
    def visitCountedShortestPathSearch(
        self, ctx: GQLParser.CountedShortestPathSearchContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#countedShortestGroupSearch.
    def visitCountedShortestGroupSearch(
        self, ctx: GQLParser.CountedShortestGroupSearchContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numberOfGroups.
    def visitNumberOfGroups(self, ctx: GQLParser.NumberOfGroupsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ppePathTerm.
    def visitPpePathTerm(self, ctx: GQLParser.PpePathTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ppeMultisetAlternation.
    def visitPpeMultisetAlternation(self, ctx: GQLParser.PpeMultisetAlternationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ppePatternUnion.
    def visitPpePatternUnion(self, ctx: GQLParser.PpePatternUnionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathTerm.
    def visitPathTerm(self, ctx: GQLParser.PathTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pfPathPrimary.
    def visitPfPathPrimary(self, ctx: GQLParser.PfPathPrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pfQuantifiedPathPrimary.
    def visitPfQuantifiedPathPrimary(
        self, ctx: GQLParser.PfQuantifiedPathPrimaryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pfQuestionedPathPrimary.
    def visitPfQuestionedPathPrimary(
        self, ctx: GQLParser.PfQuestionedPathPrimaryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ppElementPattern.
    def visitPpElementPattern(self, ctx: GQLParser.PpElementPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ppParenthesizedPathPatternExpression.
    def visitPpParenthesizedPathPatternExpression(
        self, ctx: GQLParser.PpParenthesizedPathPatternExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ppSimplifiedPathPatternExpression.
    def visitPpSimplifiedPathPatternExpression(
        self, ctx: GQLParser.PpSimplifiedPathPatternExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementPattern.
    def visitElementPattern(self, ctx: GQLParser.ElementPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodePattern.
    def visitNodePattern(self, ctx: GQLParser.NodePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementPatternFiller.
    def visitElementPatternFiller(self, ctx: GQLParser.ElementPatternFillerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementVariableDeclaration.
    def visitElementVariableDeclaration(
        self, ctx: GQLParser.ElementVariableDeclarationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#isLabelExpression.
    def visitIsLabelExpression(self, ctx: GQLParser.IsLabelExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#isOrColon.
    def visitIsOrColon(self, ctx: GQLParser.IsOrColonContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementPatternPredicate.
    def visitElementPatternPredicate(
        self, ctx: GQLParser.ElementPatternPredicateContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementPatternWhereClause.
    def visitElementPatternWhereClause(
        self, ctx: GQLParser.ElementPatternWhereClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementPropertySpecification.
    def visitElementPropertySpecification(
        self, ctx: GQLParser.ElementPropertySpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyKeyValuePairList.
    def visitPropertyKeyValuePairList(
        self, ctx: GQLParser.PropertyKeyValuePairListContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyKeyValuePair.
    def visitPropertyKeyValuePair(self, ctx: GQLParser.PropertyKeyValuePairContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgePattern.
    def visitEdgePattern(self, ctx: GQLParser.EdgePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgePattern.
    def visitFullEdgePattern(self, ctx: GQLParser.FullEdgePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgePointingLeft.
    def visitFullEdgePointingLeft(self, ctx: GQLParser.FullEdgePointingLeftContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgeUndirected.
    def visitFullEdgeUndirected(self, ctx: GQLParser.FullEdgeUndirectedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgePointingRight.
    def visitFullEdgePointingRight(self, ctx: GQLParser.FullEdgePointingRightContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgeLeftOrUndirected.
    def visitFullEdgeLeftOrUndirected(
        self, ctx: GQLParser.FullEdgeLeftOrUndirectedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgeUndirectedOrRight.
    def visitFullEdgeUndirectedOrRight(
        self, ctx: GQLParser.FullEdgeUndirectedOrRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgeLeftOrRight.
    def visitFullEdgeLeftOrRight(self, ctx: GQLParser.FullEdgeLeftOrRightContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fullEdgeAnyDirection.
    def visitFullEdgeAnyDirection(self, ctx: GQLParser.FullEdgeAnyDirectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#abbreviatedEdgePattern.
    def visitAbbreviatedEdgePattern(self, ctx: GQLParser.AbbreviatedEdgePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#parenthesizedPathPatternExpression.
    def visitParenthesizedPathPatternExpression(
        self, ctx: GQLParser.ParenthesizedPathPatternExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#subpathVariableDeclaration.
    def visitSubpathVariableDeclaration(
        self, ctx: GQLParser.SubpathVariableDeclarationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#parenthesizedPathPatternWhereClause.
    def visitParenthesizedPathPatternWhereClause(
        self, ctx: GQLParser.ParenthesizedPathPatternWhereClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelExpressionNegation.
    def visitLabelExpressionNegation(
        self, ctx: GQLParser.LabelExpressionNegationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelExpressionDisjunction.
    def visitLabelExpressionDisjunction(
        self, ctx: GQLParser.LabelExpressionDisjunctionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelExpressionParenthesized.
    def visitLabelExpressionParenthesized(
        self, ctx: GQLParser.LabelExpressionParenthesizedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelExpressionWildcard.
    def visitLabelExpressionWildcard(
        self, ctx: GQLParser.LabelExpressionWildcardContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelExpressionConjunction.
    def visitLabelExpressionConjunction(
        self, ctx: GQLParser.LabelExpressionConjunctionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelExpressionName.
    def visitLabelExpressionName(self, ctx: GQLParser.LabelExpressionNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathVariableReference.
    def visitPathVariableReference(self, ctx: GQLParser.PathVariableReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementVariableReference.
    def visitElementVariableReference(
        self, ctx: GQLParser.ElementVariableReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphPatternQuantifier.
    def visitGraphPatternQuantifier(self, ctx: GQLParser.GraphPatternQuantifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fixedQuantifier.
    def visitFixedQuantifier(self, ctx: GQLParser.FixedQuantifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalQuantifier.
    def visitGeneralQuantifier(self, ctx: GQLParser.GeneralQuantifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#lowerBound.
    def visitLowerBound(self, ctx: GQLParser.LowerBoundContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#upperBound.
    def visitUpperBound(self, ctx: GQLParser.UpperBoundContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedPathPatternExpression.
    def visitSimplifiedPathPatternExpression(
        self, ctx: GQLParser.SimplifiedPathPatternExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDefaultingLeft.
    def visitSimplifiedDefaultingLeft(
        self, ctx: GQLParser.SimplifiedDefaultingLeftContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDefaultingUndirected.
    def visitSimplifiedDefaultingUndirected(
        self, ctx: GQLParser.SimplifiedDefaultingUndirectedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDefaultingRight.
    def visitSimplifiedDefaultingRight(
        self, ctx: GQLParser.SimplifiedDefaultingRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDefaultingLeftOrUndirected.
    def visitSimplifiedDefaultingLeftOrUndirected(
        self, ctx: GQLParser.SimplifiedDefaultingLeftOrUndirectedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDefaultingUndirectedOrRight.
    def visitSimplifiedDefaultingUndirectedOrRight(
        self, ctx: GQLParser.SimplifiedDefaultingUndirectedOrRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDefaultingLeftOrRight.
    def visitSimplifiedDefaultingLeftOrRight(
        self, ctx: GQLParser.SimplifiedDefaultingLeftOrRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDefaultingAnyDirection.
    def visitSimplifiedDefaultingAnyDirection(
        self, ctx: GQLParser.SimplifiedDefaultingAnyDirectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedContents.
    def visitSimplifiedContents(self, ctx: GQLParser.SimplifiedContentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedPathUnion.
    def visitSimplifiedPathUnion(self, ctx: GQLParser.SimplifiedPathUnionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedMultisetAlternation.
    def visitSimplifiedMultisetAlternation(
        self, ctx: GQLParser.SimplifiedMultisetAlternationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedFactorLowLabel.
    def visitSimplifiedFactorLowLabel(
        self, ctx: GQLParser.SimplifiedFactorLowLabelContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedConcatenationLabel.
    def visitSimplifiedConcatenationLabel(
        self, ctx: GQLParser.SimplifiedConcatenationLabelContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedConjunctionLabel.
    def visitSimplifiedConjunctionLabel(
        self, ctx: GQLParser.SimplifiedConjunctionLabelContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedFactorHighLabel.
    def visitSimplifiedFactorHighLabel(
        self, ctx: GQLParser.SimplifiedFactorHighLabelContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedFactorHigh.
    def visitSimplifiedFactorHigh(self, ctx: GQLParser.SimplifiedFactorHighContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedQuantified.
    def visitSimplifiedQuantified(self, ctx: GQLParser.SimplifiedQuantifiedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedQuestioned.
    def visitSimplifiedQuestioned(self, ctx: GQLParser.SimplifiedQuestionedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedTertiary.
    def visitSimplifiedTertiary(self, ctx: GQLParser.SimplifiedTertiaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedDirectionOverride.
    def visitSimplifiedDirectionOverride(
        self, ctx: GQLParser.SimplifiedDirectionOverrideContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedOverrideLeft.
    def visitSimplifiedOverrideLeft(self, ctx: GQLParser.SimplifiedOverrideLeftContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedOverrideUndirected.
    def visitSimplifiedOverrideUndirected(
        self, ctx: GQLParser.SimplifiedOverrideUndirectedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedOverrideRight.
    def visitSimplifiedOverrideRight(
        self, ctx: GQLParser.SimplifiedOverrideRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedOverrideLeftOrUndirected.
    def visitSimplifiedOverrideLeftOrUndirected(
        self, ctx: GQLParser.SimplifiedOverrideLeftOrUndirectedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedOverrideUndirectedOrRight.
    def visitSimplifiedOverrideUndirectedOrRight(
        self, ctx: GQLParser.SimplifiedOverrideUndirectedOrRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedOverrideLeftOrRight.
    def visitSimplifiedOverrideLeftOrRight(
        self, ctx: GQLParser.SimplifiedOverrideLeftOrRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedOverrideAnyDirection.
    def visitSimplifiedOverrideAnyDirection(
        self, ctx: GQLParser.SimplifiedOverrideAnyDirectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedSecondary.
    def visitSimplifiedSecondary(self, ctx: GQLParser.SimplifiedSecondaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedNegation.
    def visitSimplifiedNegation(self, ctx: GQLParser.SimplifiedNegationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simplifiedPrimary.
    def visitSimplifiedPrimary(self, ctx: GQLParser.SimplifiedPrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#whereClause.
    def visitWhereClause(self, ctx: GQLParser.WhereClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#yieldClause.
    def visitYieldClause(self, ctx: GQLParser.YieldClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#yieldItemList.
    def visitYieldItemList(self, ctx: GQLParser.YieldItemListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#yieldItem.
    def visitYieldItem(self, ctx: GQLParser.YieldItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#yieldItemName.
    def visitYieldItemName(self, ctx: GQLParser.YieldItemNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#yieldItemAlias.
    def visitYieldItemAlias(self, ctx: GQLParser.YieldItemAliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#groupByClause.
    def visitGroupByClause(self, ctx: GQLParser.GroupByClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#groupingElementList.
    def visitGroupingElementList(self, ctx: GQLParser.GroupingElementListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#groupingElement.
    def visitGroupingElement(self, ctx: GQLParser.GroupingElementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#emptyGroupingSet.
    def visitEmptyGroupingSet(self, ctx: GQLParser.EmptyGroupingSetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#orderByClause.
    def visitOrderByClause(self, ctx: GQLParser.OrderByClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sortSpecificationList.
    def visitSortSpecificationList(self, ctx: GQLParser.SortSpecificationListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sortSpecification.
    def visitSortSpecification(self, ctx: GQLParser.SortSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sortKey.
    def visitSortKey(self, ctx: GQLParser.SortKeyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#orderingSpecification.
    def visitOrderingSpecification(self, ctx: GQLParser.OrderingSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nullOrdering.
    def visitNullOrdering(self, ctx: GQLParser.NullOrderingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#limitClause.
    def visitLimitClause(self, ctx: GQLParser.LimitClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#offsetClause.
    def visitOffsetClause(self, ctx: GQLParser.OffsetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#offsetSynonym.
    def visitOffsetSynonym(self, ctx: GQLParser.OffsetSynonymContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#schemaReference.
    def visitSchemaReference(self, ctx: GQLParser.SchemaReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#absoluteCatalogSchemaReference.
    def visitAbsoluteCatalogSchemaReference(
        self, ctx: GQLParser.AbsoluteCatalogSchemaReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#catalogSchemaParentAndName.
    def visitCatalogSchemaParentAndName(
        self, ctx: GQLParser.CatalogSchemaParentAndNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#relativeCatalogSchemaReference.
    def visitRelativeCatalogSchemaReference(
        self, ctx: GQLParser.RelativeCatalogSchemaReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#predefinedSchemaReference.
    def visitPredefinedSchemaReference(
        self, ctx: GQLParser.PredefinedSchemaReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#absoluteDirectoryPath.
    def visitAbsoluteDirectoryPath(self, ctx: GQLParser.AbsoluteDirectoryPathContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#relativeDirectoryPath.
    def visitRelativeDirectoryPath(self, ctx: GQLParser.RelativeDirectoryPathContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleDirectoryPath.
    def visitSimpleDirectoryPath(self, ctx: GQLParser.SimpleDirectoryPathContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphReference.
    def visitGraphReference(self, ctx: GQLParser.GraphReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#catalogGraphParentAndName.
    def visitCatalogGraphParentAndName(
        self, ctx: GQLParser.CatalogGraphParentAndNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#homeGraph.
    def visitHomeGraph(self, ctx: GQLParser.HomeGraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphTypeReference.
    def visitGraphTypeReference(self, ctx: GQLParser.GraphTypeReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#catalogGraphTypeParentAndName.
    def visitCatalogGraphTypeParentAndName(
        self, ctx: GQLParser.CatalogGraphTypeParentAndNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableReference.
    def visitBindingTableReference(self, ctx: GQLParser.BindingTableReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#procedureReference.
    def visitProcedureReference(self, ctx: GQLParser.ProcedureReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#catalogProcedureParentAndName.
    def visitCatalogProcedureParentAndName(
        self, ctx: GQLParser.CatalogProcedureParentAndNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#catalogObjectParentReference.
    def visitCatalogObjectParentReference(
        self, ctx: GQLParser.CatalogObjectParentReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#referenceParameterSpecification.
    def visitReferenceParameterSpecification(
        self, ctx: GQLParser.ReferenceParameterSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nestedGraphTypeSpecification.
    def visitNestedGraphTypeSpecification(
        self, ctx: GQLParser.NestedGraphTypeSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphTypeSpecificationBody.
    def visitGraphTypeSpecificationBody(
        self, ctx: GQLParser.GraphTypeSpecificationBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementTypeList.
    def visitElementTypeList(self, ctx: GQLParser.ElementTypeListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementTypeSpecification.
    def visitElementTypeSpecification(
        self, ctx: GQLParser.ElementTypeSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypeSpecification.
    def visitNodeTypeSpecification(self, ctx: GQLParser.NodeTypeSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypePattern.
    def visitNodeTypePattern(self, ctx: GQLParser.NodeTypePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypePhrase.
    def visitNodeTypePhrase(self, ctx: GQLParser.NodeTypePhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypePhraseFiller.
    def visitNodeTypePhraseFiller(self, ctx: GQLParser.NodeTypePhraseFillerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypeFiller.
    def visitNodeTypeFiller(self, ctx: GQLParser.NodeTypeFillerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#localNodeTypeAlias.
    def visitLocalNodeTypeAlias(self, ctx: GQLParser.LocalNodeTypeAliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypeImpliedContent.
    def visitNodeTypeImpliedContent(self, ctx: GQLParser.NodeTypeImpliedContentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypeKeyLabelSet.
    def visitNodeTypeKeyLabelSet(self, ctx: GQLParser.NodeTypeKeyLabelSetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypeLabelSet.
    def visitNodeTypeLabelSet(self, ctx: GQLParser.NodeTypeLabelSetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypePropertyTypes.
    def visitNodeTypePropertyTypes(self, ctx: GQLParser.NodeTypePropertyTypesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypeSpecification.
    def visitEdgeTypeSpecification(self, ctx: GQLParser.EdgeTypeSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePattern.
    def visitEdgeTypePattern(self, ctx: GQLParser.EdgeTypePatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePhrase.
    def visitEdgeTypePhrase(self, ctx: GQLParser.EdgeTypePhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePhraseFiller.
    def visitEdgeTypePhraseFiller(self, ctx: GQLParser.EdgeTypePhraseFillerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypeFiller.
    def visitEdgeTypeFiller(self, ctx: GQLParser.EdgeTypeFillerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypeImpliedContent.
    def visitEdgeTypeImpliedContent(self, ctx: GQLParser.EdgeTypeImpliedContentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypeKeyLabelSet.
    def visitEdgeTypeKeyLabelSet(self, ctx: GQLParser.EdgeTypeKeyLabelSetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypeLabelSet.
    def visitEdgeTypeLabelSet(self, ctx: GQLParser.EdgeTypeLabelSetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePropertyTypes.
    def visitEdgeTypePropertyTypes(self, ctx: GQLParser.EdgeTypePropertyTypesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePatternDirected.
    def visitEdgeTypePatternDirected(
        self, ctx: GQLParser.EdgeTypePatternDirectedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePatternPointingRight.
    def visitEdgeTypePatternPointingRight(
        self, ctx: GQLParser.EdgeTypePatternPointingRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePatternPointingLeft.
    def visitEdgeTypePatternPointingLeft(
        self, ctx: GQLParser.EdgeTypePatternPointingLeftContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypePatternUndirected.
    def visitEdgeTypePatternUndirected(
        self, ctx: GQLParser.EdgeTypePatternUndirectedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#arcTypePointingRight.
    def visitArcTypePointingRight(self, ctx: GQLParser.ArcTypePointingRightContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#arcTypePointingLeft.
    def visitArcTypePointingLeft(self, ctx: GQLParser.ArcTypePointingLeftContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#arcTypeUndirected.
    def visitArcTypeUndirected(self, ctx: GQLParser.ArcTypeUndirectedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sourceNodeTypeReference.
    def visitSourceNodeTypeReference(
        self, ctx: GQLParser.SourceNodeTypeReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#destinationNodeTypeReference.
    def visitDestinationNodeTypeReference(
        self, ctx: GQLParser.DestinationNodeTypeReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeKind.
    def visitEdgeKind(self, ctx: GQLParser.EdgeKindContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#endpointPairPhrase.
    def visitEndpointPairPhrase(self, ctx: GQLParser.EndpointPairPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#endpointPair.
    def visitEndpointPair(self, ctx: GQLParser.EndpointPairContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#endpointPairDirected.
    def visitEndpointPairDirected(self, ctx: GQLParser.EndpointPairDirectedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#endpointPairPointingRight.
    def visitEndpointPairPointingRight(
        self, ctx: GQLParser.EndpointPairPointingRightContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#endpointPairPointingLeft.
    def visitEndpointPairPointingLeft(
        self, ctx: GQLParser.EndpointPairPointingLeftContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#endpointPairUndirected.
    def visitEndpointPairUndirected(self, ctx: GQLParser.EndpointPairUndirectedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#connectorPointingRight.
    def visitConnectorPointingRight(self, ctx: GQLParser.ConnectorPointingRightContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#connectorUndirected.
    def visitConnectorUndirected(self, ctx: GQLParser.ConnectorUndirectedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sourceNodeTypeAlias.
    def visitSourceNodeTypeAlias(self, ctx: GQLParser.SourceNodeTypeAliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#destinationNodeTypeAlias.
    def visitDestinationNodeTypeAlias(
        self, ctx: GQLParser.DestinationNodeTypeAliasContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelSetPhrase.
    def visitLabelSetPhrase(self, ctx: GQLParser.LabelSetPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelSetSpecification.
    def visitLabelSetSpecification(self, ctx: GQLParser.LabelSetSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyTypesSpecification.
    def visitPropertyTypesSpecification(
        self, ctx: GQLParser.PropertyTypesSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyTypeList.
    def visitPropertyTypeList(self, ctx: GQLParser.PropertyTypeListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyType.
    def visitPropertyType(self, ctx: GQLParser.PropertyTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyValueType.
    def visitPropertyValueType(self, ctx: GQLParser.PropertyValueTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableType.
    def visitBindingTableType(self, ctx: GQLParser.BindingTableTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dynamicPropertyValueTypeLabel.
    def visitDynamicPropertyValueTypeLabel(
        self, ctx: GQLParser.DynamicPropertyValueTypeLabelContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#closedDynamicUnionTypeAtl1.
    def visitClosedDynamicUnionTypeAtl1(
        self, ctx: GQLParser.ClosedDynamicUnionTypeAtl1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#closedDynamicUnionTypeAtl2.
    def visitClosedDynamicUnionTypeAtl2(
        self, ctx: GQLParser.ClosedDynamicUnionTypeAtl2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathValueTypeLabel.
    def visitPathValueTypeLabel(self, ctx: GQLParser.PathValueTypeLabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueTypeAlt3.
    def visitListValueTypeAlt3(self, ctx: GQLParser.ListValueTypeAlt3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueTypeAlt2.
    def visitListValueTypeAlt2(self, ctx: GQLParser.ListValueTypeAlt2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueTypeAlt1.
    def visitListValueTypeAlt1(self, ctx: GQLParser.ListValueTypeAlt1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#predefinedTypeLabel.
    def visitPredefinedTypeLabel(self, ctx: GQLParser.PredefinedTypeLabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#recordTypeLabel.
    def visitRecordTypeLabel(self, ctx: GQLParser.RecordTypeLabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#openDynamicUnionTypeLabel.
    def visitOpenDynamicUnionTypeLabel(
        self, ctx: GQLParser.OpenDynamicUnionTypeLabelContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#typed.
    def visitTyped(self, ctx: GQLParser.TypedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#predefinedType.
    def visitPredefinedType(self, ctx: GQLParser.PredefinedTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#booleanType.
    def visitBooleanType(self, ctx: GQLParser.BooleanTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#characterStringType.
    def visitCharacterStringType(self, ctx: GQLParser.CharacterStringTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#byteStringType.
    def visitByteStringType(self, ctx: GQLParser.ByteStringTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#minLength.
    def visitMinLength(self, ctx: GQLParser.MinLengthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#maxLength.
    def visitMaxLength(self, ctx: GQLParser.MaxLengthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fixedLength.
    def visitFixedLength(self, ctx: GQLParser.FixedLengthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numericType.
    def visitNumericType(self, ctx: GQLParser.NumericTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#exactNumericType.
    def visitExactNumericType(self, ctx: GQLParser.ExactNumericTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#binaryExactNumericType.
    def visitBinaryExactNumericType(self, ctx: GQLParser.BinaryExactNumericTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#signedBinaryExactNumericType.
    def visitSignedBinaryExactNumericType(
        self, ctx: GQLParser.SignedBinaryExactNumericTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#unsignedBinaryExactNumericType.
    def visitUnsignedBinaryExactNumericType(
        self, ctx: GQLParser.UnsignedBinaryExactNumericTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#verboseBinaryExactNumericType.
    def visitVerboseBinaryExactNumericType(
        self, ctx: GQLParser.VerboseBinaryExactNumericTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#decimalExactNumericType.
    def visitDecimalExactNumericType(
        self, ctx: GQLParser.DecimalExactNumericTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#precision.
    def visitPrecision(self, ctx: GQLParser.PrecisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#scale.
    def visitScale(self, ctx: GQLParser.ScaleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#approximateNumericType.
    def visitApproximateNumericType(self, ctx: GQLParser.ApproximateNumericTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#temporalType.
    def visitTemporalType(self, ctx: GQLParser.TemporalTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#temporalInstantType.
    def visitTemporalInstantType(self, ctx: GQLParser.TemporalInstantTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeType.
    def visitDatetimeType(self, ctx: GQLParser.DatetimeTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#localdatetimeType.
    def visitLocaldatetimeType(self, ctx: GQLParser.LocaldatetimeTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dateType.
    def visitDateType(self, ctx: GQLParser.DateTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#timeType.
    def visitTimeType(self, ctx: GQLParser.TimeTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#localtimeType.
    def visitLocaltimeType(self, ctx: GQLParser.LocaltimeTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#temporalDurationType.
    def visitTemporalDurationType(self, ctx: GQLParser.TemporalDurationTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#temporalDurationQualifier.
    def visitTemporalDurationQualifier(
        self, ctx: GQLParser.TemporalDurationQualifierContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#referenceValueType.
    def visitReferenceValueType(self, ctx: GQLParser.ReferenceValueTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#immaterialValueType.
    def visitImmaterialValueType(self, ctx: GQLParser.ImmaterialValueTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nullType.
    def visitNullType(self, ctx: GQLParser.NullTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#emptyType.
    def visitEmptyType(self, ctx: GQLParser.EmptyTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphReferenceValueType.
    def visitGraphReferenceValueType(
        self, ctx: GQLParser.GraphReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#closedGraphReferenceValueType.
    def visitClosedGraphReferenceValueType(
        self, ctx: GQLParser.ClosedGraphReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#openGraphReferenceValueType.
    def visitOpenGraphReferenceValueType(
        self, ctx: GQLParser.OpenGraphReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableReferenceValueType.
    def visitBindingTableReferenceValueType(
        self, ctx: GQLParser.BindingTableReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeReferenceValueType.
    def visitNodeReferenceValueType(self, ctx: GQLParser.NodeReferenceValueTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#closedNodeReferenceValueType.
    def visitClosedNodeReferenceValueType(
        self, ctx: GQLParser.ClosedNodeReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#openNodeReferenceValueType.
    def visitOpenNodeReferenceValueType(
        self, ctx: GQLParser.OpenNodeReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeReferenceValueType.
    def visitEdgeReferenceValueType(self, ctx: GQLParser.EdgeReferenceValueTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#closedEdgeReferenceValueType.
    def visitClosedEdgeReferenceValueType(
        self, ctx: GQLParser.ClosedEdgeReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#openEdgeReferenceValueType.
    def visitOpenEdgeReferenceValueType(
        self, ctx: GQLParser.OpenEdgeReferenceValueTypeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathValueType.
    def visitPathValueType(self, ctx: GQLParser.PathValueTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueTypeName.
    def visitListValueTypeName(self, ctx: GQLParser.ListValueTypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueTypeNameSynonym.
    def visitListValueTypeNameSynonym(
        self, ctx: GQLParser.ListValueTypeNameSynonymContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#recordType.
    def visitRecordType(self, ctx: GQLParser.RecordTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fieldTypesSpecification.
    def visitFieldTypesSpecification(
        self, ctx: GQLParser.FieldTypesSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fieldTypeList.
    def visitFieldTypeList(self, ctx: GQLParser.FieldTypeListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#notNull.
    def visitNotNull(self, ctx: GQLParser.NotNullContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fieldType.
    def visitFieldType(self, ctx: GQLParser.FieldTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#searchCondition.
    def visitSearchCondition(self, ctx: GQLParser.SearchConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#predicate.
    def visitPredicate(self, ctx: GQLParser.PredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#compOp.
    def visitCompOp(self, ctx: GQLParser.CompOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#existsPredicate.
    def visitExistsPredicate(self, ctx: GQLParser.ExistsPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nullPredicate.
    def visitNullPredicate(self, ctx: GQLParser.NullPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nullPredicatePart2.
    def visitNullPredicatePart2(self, ctx: GQLParser.NullPredicatePart2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueTypePredicate.
    def visitValueTypePredicate(self, ctx: GQLParser.ValueTypePredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueTypePredicatePart2.
    def visitValueTypePredicatePart2(
        self, ctx: GQLParser.ValueTypePredicatePart2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#normalizedPredicatePart2.
    def visitNormalizedPredicatePart2(
        self, ctx: GQLParser.NormalizedPredicatePart2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#directedPredicate.
    def visitDirectedPredicate(self, ctx: GQLParser.DirectedPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#directedPredicatePart2.
    def visitDirectedPredicatePart2(self, ctx: GQLParser.DirectedPredicatePart2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labeledPredicate.
    def visitLabeledPredicate(self, ctx: GQLParser.LabeledPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labeledPredicatePart2.
    def visitLabeledPredicatePart2(self, ctx: GQLParser.LabeledPredicatePart2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#isLabeledOrColon.
    def visitIsLabeledOrColon(self, ctx: GQLParser.IsLabeledOrColonContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sourceDestinationPredicate.
    def visitSourceDestinationPredicate(
        self, ctx: GQLParser.SourceDestinationPredicateContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeReference.
    def visitNodeReference(self, ctx: GQLParser.NodeReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#sourcePredicatePart2.
    def visitSourcePredicatePart2(self, ctx: GQLParser.SourcePredicatePart2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#destinationPredicatePart2.
    def visitDestinationPredicatePart2(
        self, ctx: GQLParser.DestinationPredicatePart2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeReference.
    def visitEdgeReference(self, ctx: GQLParser.EdgeReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#all_differentPredicate.
    def visitAll_differentPredicate(self, ctx: GQLParser.All_differentPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#samePredicate.
    def visitSamePredicate(self, ctx: GQLParser.SamePredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#property_existsPredicate.
    def visitProperty_existsPredicate(
        self, ctx: GQLParser.Property_existsPredicateContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#conjunctiveExprAlt.
    def visitConjunctiveExprAlt(self, ctx: GQLParser.ConjunctiveExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyGraphExprAlt.
    def visitPropertyGraphExprAlt(self, ctx: GQLParser.PropertyGraphExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#multDivExprAlt.
    def visitMultDivExprAlt(self, ctx: GQLParser.MultDivExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableExprAlt.
    def visitBindingTableExprAlt(self, ctx: GQLParser.BindingTableExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#signedExprAlt.
    def visitSignedExprAlt(self, ctx: GQLParser.SignedExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#isNotExprAlt.
    def visitIsNotExprAlt(self, ctx: GQLParser.IsNotExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#normalizedPredicateExprAlt.
    def visitNormalizedPredicateExprAlt(
        self, ctx: GQLParser.NormalizedPredicateExprAltContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#notExprAlt.
    def visitNotExprAlt(self, ctx: GQLParser.NotExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueFunctionExprAlt.
    def visitValueFunctionExprAlt(self, ctx: GQLParser.ValueFunctionExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#concatenationExprAlt.
    def visitConcatenationExprAlt(self, ctx: GQLParser.ConcatenationExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#disjunctiveExprAlt.
    def visitDisjunctiveExprAlt(self, ctx: GQLParser.DisjunctiveExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#comparisonExprAlt.
    def visitComparisonExprAlt(self, ctx: GQLParser.ComparisonExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#primaryExprAlt.
    def visitPrimaryExprAlt(self, ctx: GQLParser.PrimaryExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#addSubtractExprAlt.
    def visitAddSubtractExprAlt(self, ctx: GQLParser.AddSubtractExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#predicateExprAlt.
    def visitPredicateExprAlt(self, ctx: GQLParser.PredicateExprAltContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueFunction.
    def visitValueFunction(self, ctx: GQLParser.ValueFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#booleanValueExpression.
    def visitBooleanValueExpression(self, ctx: GQLParser.BooleanValueExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#characterOrByteStringFunction.
    def visitCharacterOrByteStringFunction(
        self, ctx: GQLParser.CharacterOrByteStringFunctionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#subCharacterOrByteString.
    def visitSubCharacterOrByteString(
        self, ctx: GQLParser.SubCharacterOrByteStringContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trimSingleCharacterOrByteString.
    def visitTrimSingleCharacterOrByteString(
        self, ctx: GQLParser.TrimSingleCharacterOrByteStringContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#foldCharacterString.
    def visitFoldCharacterString(self, ctx: GQLParser.FoldCharacterStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trimMultiCharacterCharacterString.
    def visitTrimMultiCharacterCharacterString(
        self, ctx: GQLParser.TrimMultiCharacterCharacterStringContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#normalizeCharacterString.
    def visitNormalizeCharacterString(
        self, ctx: GQLParser.NormalizeCharacterStringContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeReferenceValueExpression.
    def visitNodeReferenceValueExpression(
        self, ctx: GQLParser.NodeReferenceValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeReferenceValueExpression.
    def visitEdgeReferenceValueExpression(
        self, ctx: GQLParser.EdgeReferenceValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#aggregatingValueExpression.
    def visitAggregatingValueExpression(
        self, ctx: GQLParser.AggregatingValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueExpressionPrimary.
    def visitValueExpressionPrimary(self, ctx: GQLParser.ValueExpressionPrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#parenthesizedValueExpression.
    def visitParenthesizedValueExpression(
        self, ctx: GQLParser.ParenthesizedValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nonParenthesizedValueExpressionPrimary.
    def visitNonParenthesizedValueExpressionPrimary(
        self, ctx: GQLParser.NonParenthesizedValueExpressionPrimaryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nonParenthesizedValueExpressionPrimarySpecialCase.
    def visitNonParenthesizedValueExpressionPrimarySpecialCase(
        self, ctx: GQLParser.NonParenthesizedValueExpressionPrimarySpecialCaseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#unsignedValueSpecification.
    def visitUnsignedValueSpecification(
        self, ctx: GQLParser.UnsignedValueSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nonNegativeIntegerSpecification.
    def visitNonNegativeIntegerSpecification(
        self, ctx: GQLParser.NonNegativeIntegerSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalValueSpecification.
    def visitGeneralValueSpecification(
        self, ctx: GQLParser.GeneralValueSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dynamicParameterSpecification.
    def visitDynamicParameterSpecification(
        self, ctx: GQLParser.DynamicParameterSpecificationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#letValueExpression.
    def visitLetValueExpression(self, ctx: GQLParser.LetValueExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#valueQueryExpression.
    def visitValueQueryExpression(self, ctx: GQLParser.ValueQueryExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#caseExpression.
    def visitCaseExpression(self, ctx: GQLParser.CaseExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#caseAbbreviation.
    def visitCaseAbbreviation(self, ctx: GQLParser.CaseAbbreviationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#caseSpecification.
    def visitCaseSpecification(self, ctx: GQLParser.CaseSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleCase.
    def visitSimpleCase(self, ctx: GQLParser.SimpleCaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#searchedCase.
    def visitSearchedCase(self, ctx: GQLParser.SearchedCaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#simpleWhenClause.
    def visitSimpleWhenClause(self, ctx: GQLParser.SimpleWhenClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#searchedWhenClause.
    def visitSearchedWhenClause(self, ctx: GQLParser.SearchedWhenClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elseClause.
    def visitElseClause(self, ctx: GQLParser.ElseClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#caseOperand.
    def visitCaseOperand(self, ctx: GQLParser.CaseOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#whenOperandList.
    def visitWhenOperandList(self, ctx: GQLParser.WhenOperandListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#whenOperand.
    def visitWhenOperand(self, ctx: GQLParser.WhenOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#result.
    def visitResult(self, ctx: GQLParser.ResultContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#resultExpression.
    def visitResultExpression(self, ctx: GQLParser.ResultExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#castSpecification.
    def visitCastSpecification(self, ctx: GQLParser.CastSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#castOperand.
    def visitCastOperand(self, ctx: GQLParser.CastOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#castTarget.
    def visitCastTarget(self, ctx: GQLParser.CastTargetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#aggregateFunction.
    def visitAggregateFunction(self, ctx: GQLParser.AggregateFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalSetFunction.
    def visitGeneralSetFunction(self, ctx: GQLParser.GeneralSetFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#binarySetFunction.
    def visitBinarySetFunction(self, ctx: GQLParser.BinarySetFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalSetFunctionType.
    def visitGeneralSetFunctionType(self, ctx: GQLParser.GeneralSetFunctionTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#setQuantifier.
    def visitSetQuantifier(self, ctx: GQLParser.SetQuantifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#binarySetFunctionType.
    def visitBinarySetFunctionType(self, ctx: GQLParser.BinarySetFunctionTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dependentValueExpression.
    def visitDependentValueExpression(
        self, ctx: GQLParser.DependentValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#independentValueExpression.
    def visitIndependentValueExpression(
        self, ctx: GQLParser.IndependentValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#element_idFunction.
    def visitElement_idFunction(self, ctx: GQLParser.Element_idFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingVariableReference.
    def visitBindingVariableReference(
        self, ctx: GQLParser.BindingVariableReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathValueExpression.
    def visitPathValueExpression(self, ctx: GQLParser.PathValueExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathValueConstructor.
    def visitPathValueConstructor(self, ctx: GQLParser.PathValueConstructorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathValueConstructorByEnumeration.
    def visitPathValueConstructorByEnumeration(
        self, ctx: GQLParser.PathValueConstructorByEnumerationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathElementList.
    def visitPathElementList(self, ctx: GQLParser.PathElementListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathElementListStart.
    def visitPathElementListStart(self, ctx: GQLParser.PathElementListStartContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathElementListStep.
    def visitPathElementListStep(self, ctx: GQLParser.PathElementListStepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueExpression.
    def visitListValueExpression(self, ctx: GQLParser.ListValueExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueFunction.
    def visitListValueFunction(self, ctx: GQLParser.ListValueFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trimListFunction.
    def visitTrimListFunction(self, ctx: GQLParser.TrimListFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementsFunction.
    def visitElementsFunction(self, ctx: GQLParser.ElementsFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueConstructor.
    def visitListValueConstructor(self, ctx: GQLParser.ListValueConstructorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listValueConstructorByEnumeration.
    def visitListValueConstructorByEnumeration(
        self, ctx: GQLParser.ListValueConstructorByEnumerationContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listElementList.
    def visitListElementList(self, ctx: GQLParser.ListElementListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listElement.
    def visitListElement(self, ctx: GQLParser.ListElementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#recordConstructor.
    def visitRecordConstructor(self, ctx: GQLParser.RecordConstructorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fieldsSpecification.
    def visitFieldsSpecification(self, ctx: GQLParser.FieldsSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fieldList.
    def visitFieldList(self, ctx: GQLParser.FieldListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#field.
    def visitField(self, ctx: GQLParser.FieldContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#truthValue.
    def visitTruthValue(self, ctx: GQLParser.TruthValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numericValueExpression.
    def visitNumericValueExpression(self, ctx: GQLParser.NumericValueExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numericValueFunction.
    def visitNumericValueFunction(self, ctx: GQLParser.NumericValueFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#lengthExpression.
    def visitLengthExpression(self, ctx: GQLParser.LengthExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#cardinalityExpression.
    def visitCardinalityExpression(self, ctx: GQLParser.CardinalityExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#cardinalityExpressionArgument.
    def visitCardinalityExpressionArgument(
        self, ctx: GQLParser.CardinalityExpressionArgumentContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#charLengthExpression.
    def visitCharLengthExpression(self, ctx: GQLParser.CharLengthExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#byteLengthExpression.
    def visitByteLengthExpression(self, ctx: GQLParser.ByteLengthExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathLengthExpression.
    def visitPathLengthExpression(self, ctx: GQLParser.PathLengthExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#absoluteValueExpression.
    def visitAbsoluteValueExpression(
        self, ctx: GQLParser.AbsoluteValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#modulusExpression.
    def visitModulusExpression(self, ctx: GQLParser.ModulusExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numericValueExpressionDividend.
    def visitNumericValueExpressionDividend(
        self, ctx: GQLParser.NumericValueExpressionDividendContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numericValueExpressionDivisor.
    def visitNumericValueExpressionDivisor(
        self, ctx: GQLParser.NumericValueExpressionDivisorContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trigonometricFunction.
    def visitTrigonometricFunction(self, ctx: GQLParser.TrigonometricFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trigonometricFunctionName.
    def visitTrigonometricFunctionName(
        self, ctx: GQLParser.TrigonometricFunctionNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalLogarithmFunction.
    def visitGeneralLogarithmFunction(
        self, ctx: GQLParser.GeneralLogarithmFunctionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalLogarithmBase.
    def visitGeneralLogarithmBase(self, ctx: GQLParser.GeneralLogarithmBaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalLogarithmArgument.
    def visitGeneralLogarithmArgument(
        self, ctx: GQLParser.GeneralLogarithmArgumentContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#commonLogarithm.
    def visitCommonLogarithm(self, ctx: GQLParser.CommonLogarithmContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#naturalLogarithm.
    def visitNaturalLogarithm(self, ctx: GQLParser.NaturalLogarithmContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#exponentialFunction.
    def visitExponentialFunction(self, ctx: GQLParser.ExponentialFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#powerFunction.
    def visitPowerFunction(self, ctx: GQLParser.PowerFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numericValueExpressionBase.
    def visitNumericValueExpressionBase(
        self, ctx: GQLParser.NumericValueExpressionBaseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#numericValueExpressionExponent.
    def visitNumericValueExpressionExponent(
        self, ctx: GQLParser.NumericValueExpressionExponentContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#squareRoot.
    def visitSquareRoot(self, ctx: GQLParser.SquareRootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#floorFunction.
    def visitFloorFunction(self, ctx: GQLParser.FloorFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#ceilingFunction.
    def visitCeilingFunction(self, ctx: GQLParser.CeilingFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#characterStringValueExpression.
    def visitCharacterStringValueExpression(
        self, ctx: GQLParser.CharacterStringValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#byteStringValueExpression.
    def visitByteStringValueExpression(
        self, ctx: GQLParser.ByteStringValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trimOperands.
    def visitTrimOperands(self, ctx: GQLParser.TrimOperandsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trimCharacterOrByteStringSource.
    def visitTrimCharacterOrByteStringSource(
        self, ctx: GQLParser.TrimCharacterOrByteStringSourceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trimSpecification.
    def visitTrimSpecification(self, ctx: GQLParser.TrimSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#trimCharacterOrByteString.
    def visitTrimCharacterOrByteString(
        self, ctx: GQLParser.TrimCharacterOrByteStringContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#normalForm.
    def visitNormalForm(self, ctx: GQLParser.NormalFormContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#stringLength.
    def visitStringLength(self, ctx: GQLParser.StringLengthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeValueExpression.
    def visitDatetimeValueExpression(
        self, ctx: GQLParser.DatetimeValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeValueFunction.
    def visitDatetimeValueFunction(self, ctx: GQLParser.DatetimeValueFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dateFunction.
    def visitDateFunction(self, ctx: GQLParser.DateFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#timeFunction.
    def visitTimeFunction(self, ctx: GQLParser.TimeFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#localtimeFunction.
    def visitLocaltimeFunction(self, ctx: GQLParser.LocaltimeFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeFunction.
    def visitDatetimeFunction(self, ctx: GQLParser.DatetimeFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#localdatetimeFunction.
    def visitLocaldatetimeFunction(self, ctx: GQLParser.LocaldatetimeFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dateFunctionParameters.
    def visitDateFunctionParameters(self, ctx: GQLParser.DateFunctionParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#timeFunctionParameters.
    def visitTimeFunctionParameters(self, ctx: GQLParser.TimeFunctionParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeFunctionParameters.
    def visitDatetimeFunctionParameters(
        self, ctx: GQLParser.DatetimeFunctionParametersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#durationValueExpression.
    def visitDurationValueExpression(
        self, ctx: GQLParser.DurationValueExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeSubtraction.
    def visitDatetimeSubtraction(self, ctx: GQLParser.DatetimeSubtractionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeSubtractionParameters.
    def visitDatetimeSubtractionParameters(
        self, ctx: GQLParser.DatetimeSubtractionParametersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeValueExpression1.
    def visitDatetimeValueExpression1(
        self, ctx: GQLParser.DatetimeValueExpression1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeValueExpression2.
    def visitDatetimeValueExpression2(
        self, ctx: GQLParser.DatetimeValueExpression2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#durationValueFunction.
    def visitDurationValueFunction(self, ctx: GQLParser.DurationValueFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#durationFunction.
    def visitDurationFunction(self, ctx: GQLParser.DurationFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#durationFunctionParameters.
    def visitDurationFunctionParameters(
        self, ctx: GQLParser.DurationFunctionParametersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#objectName.
    def visitObjectName(self, ctx: GQLParser.ObjectNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#objectNameOrBindingVariable.
    def visitObjectNameOrBindingVariable(
        self, ctx: GQLParser.ObjectNameOrBindingVariableContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#directoryName.
    def visitDirectoryName(self, ctx: GQLParser.DirectoryNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#schemaName.
    def visitSchemaName(self, ctx: GQLParser.SchemaNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphName.
    def visitGraphName(self, ctx: GQLParser.GraphNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#delimitedGraphName.
    def visitDelimitedGraphName(self, ctx: GQLParser.DelimitedGraphNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#graphTypeName.
    def visitGraphTypeName(self, ctx: GQLParser.GraphTypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeTypeName.
    def visitNodeTypeName(self, ctx: GQLParser.NodeTypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeTypeName.
    def visitEdgeTypeName(self, ctx: GQLParser.EdgeTypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingTableName.
    def visitBindingTableName(self, ctx: GQLParser.BindingTableNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#delimitedBindingTableName.
    def visitDelimitedBindingTableName(
        self, ctx: GQLParser.DelimitedBindingTableNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#procedureName.
    def visitProcedureName(self, ctx: GQLParser.ProcedureNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#labelName.
    def visitLabelName(self, ctx: GQLParser.LabelNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#propertyName.
    def visitPropertyName(self, ctx: GQLParser.PropertyNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#fieldName.
    def visitFieldName(self, ctx: GQLParser.FieldNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#elementVariable.
    def visitElementVariable(self, ctx: GQLParser.ElementVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#pathVariable.
    def visitPathVariable(self, ctx: GQLParser.PathVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#subpathVariable.
    def visitSubpathVariable(self, ctx: GQLParser.SubpathVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#bindingVariable.
    def visitBindingVariable(self, ctx: GQLParser.BindingVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#unsignedLiteral.
    def visitUnsignedLiteral(self, ctx: GQLParser.UnsignedLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#generalLiteral.
    def visitGeneralLiteral(self, ctx: GQLParser.GeneralLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#temporalLiteral.
    def visitTemporalLiteral(self, ctx: GQLParser.TemporalLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dateLiteral.
    def visitDateLiteral(self, ctx: GQLParser.DateLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#timeLiteral.
    def visitTimeLiteral(self, ctx: GQLParser.TimeLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeLiteral.
    def visitDatetimeLiteral(self, ctx: GQLParser.DatetimeLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#listLiteral.
    def visitListLiteral(self, ctx: GQLParser.ListLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#recordLiteral.
    def visitRecordLiteral(self, ctx: GQLParser.RecordLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#identifier.
    def visitIdentifier(self, ctx: GQLParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#regularIdentifier.
    def visitRegularIdentifier(self, ctx: GQLParser.RegularIdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#timeZoneString.
    def visitTimeZoneString(self, ctx: GQLParser.TimeZoneStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#characterStringLiteral.
    def visitCharacterStringLiteral(self, ctx: GQLParser.CharacterStringLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#unsignedNumericLiteral.
    def visitUnsignedNumericLiteral(self, ctx: GQLParser.UnsignedNumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#exactNumericLiteral.
    def visitExactNumericLiteral(self, ctx: GQLParser.ExactNumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#approximateNumericLiteral.
    def visitApproximateNumericLiteral(
        self, ctx: GQLParser.ApproximateNumericLiteralContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#unsignedInteger.
    def visitUnsignedInteger(self, ctx: GQLParser.UnsignedIntegerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#unsignedDecimalInteger.
    def visitUnsignedDecimalInteger(self, ctx: GQLParser.UnsignedDecimalIntegerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nullLiteral.
    def visitNullLiteral(self, ctx: GQLParser.NullLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#dateString.
    def visitDateString(self, ctx: GQLParser.DateStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#timeString.
    def visitTimeString(self, ctx: GQLParser.TimeStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#datetimeString.
    def visitDatetimeString(self, ctx: GQLParser.DatetimeStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#durationLiteral.
    def visitDurationLiteral(self, ctx: GQLParser.DurationLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#durationString.
    def visitDurationString(self, ctx: GQLParser.DurationStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nodeSynonym.
    def visitNodeSynonym(self, ctx: GQLParser.NodeSynonymContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgesSynonym.
    def visitEdgesSynonym(self, ctx: GQLParser.EdgesSynonymContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#edgeSynonym.
    def visitEdgeSynonym(self, ctx: GQLParser.EdgeSynonymContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GQLParser#nonReservedWords.
    def visitNonReservedWords(self, ctx: GQLParser.NonReservedWordsContext):
        return self.visitChildren(ctx)


del GQLParser
