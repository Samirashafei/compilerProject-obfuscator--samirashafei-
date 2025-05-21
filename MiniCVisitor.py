# Generated from MiniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structDefinition.
    def visitStructDefinition(self, ctx:MiniCParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameterList.
    def visitParameterList(self, ctx:MiniCParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter.
    def visitParameter(self, ctx:MiniCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#declaration.
    def visitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initDeclarator.
    def visitInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#pointerSpecifier.
    def visitPointerSpecifier(self, ctx:MiniCParser.PointerSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MiniCParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#selectionStatement.
    def visitSelectionStatement(self, ctx:MiniCParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#iterationStatement.
    def visitIterationStatement(self, ctx:MiniCParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#jumpStatement.
    def visitJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ioStatement.
    def visitIoStatement(self, ctx:MiniCParser.IoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expression.
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#equalityExpression.
    def visitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#postfixExpression.
    def visitPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#argumentList.
    def visitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        return self.visitChildren(ctx)



del MiniCParser