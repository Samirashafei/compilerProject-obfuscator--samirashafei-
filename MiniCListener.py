# Generated from MiniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#structDefinition.
    def enterStructDefinition(self, ctx:MiniCParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#structDefinition.
    def exitStructDefinition(self, ctx:MiniCParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameterList.
    def enterParameterList(self, ctx:MiniCParser.ParameterListContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameterList.
    def exitParameterList(self, ctx:MiniCParser.ParameterListContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameter.
    def enterParameter(self, ctx:MiniCParser.ParameterContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameter.
    def exitParameter(self, ctx:MiniCParser.ParameterContext):
        pass


    # Enter a parse tree produced by MiniCParser#declaration.
    def enterDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#declaration.
    def exitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by MiniCParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by MiniCParser#initDeclarator.
    def enterInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#initDeclarator.
    def exitInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by MiniCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by MiniCParser#pointerSpecifier.
    def enterPointerSpecifier(self, ctx:MiniCParser.PointerSpecifierContext):
        pass

    # Exit a parse tree produced by MiniCParser#pointerSpecifier.
    def exitPointerSpecifier(self, ctx:MiniCParser.PointerSpecifierContext):
        pass


    # Enter a parse tree produced by MiniCParser#compoundStatement.
    def enterCompoundStatement(self, ctx:MiniCParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#compoundStatement.
    def exitCompoundStatement(self, ctx:MiniCParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#statement.
    def enterStatement(self, ctx:MiniCParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#statement.
    def exitStatement(self, ctx:MiniCParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#selectionStatement.
    def enterSelectionStatement(self, ctx:MiniCParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#selectionStatement.
    def exitSelectionStatement(self, ctx:MiniCParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#iterationStatement.
    def enterIterationStatement(self, ctx:MiniCParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#iterationStatement.
    def exitIterationStatement(self, ctx:MiniCParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#jumpStatement.
    def enterJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#jumpStatement.
    def exitJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#ioStatement.
    def enterIoStatement(self, ctx:MiniCParser.IoStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#ioStatement.
    def exitIoStatement(self, ctx:MiniCParser.IoStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#expression.
    def enterExpression(self, ctx:MiniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#expression.
    def exitExpression(self, ctx:MiniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#postfixExpression.
    def enterPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#postfixExpression.
    def exitPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#argumentList.
    def enterArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MiniCParser#argumentList.
    def exitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass



del MiniCParser