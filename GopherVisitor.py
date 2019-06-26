# Generated from Gopher.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GopherParser import GopherParser
else:
    from GopherParser import GopherParser

# This class defines a complete generic visitor for a parse tree produced by GopherParser.

class GopherVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GopherParser#program.
    def visitProgram(self, ctx:GopherParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#block.
    def visitBlock(self, ctx:GopherParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#stmt.
    def visitStmt(self, ctx:GopherParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#key.
    def visitKey(self, ctx:GopherParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#var.
    def visitVar(self, ctx:GopherParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#preproc.
    def visitPreproc(self, ctx:GopherParser.PreprocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#print0.
    def visitPrint0(self, ctx:GopherParser.Print0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#println.
    def visitPrintln(self, ctx:GopherParser.PrintlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#label_def.
    def visitLabel_def(self, ctx:GopherParser.Label_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#goto_stmt.
    def visitGoto_stmt(self, ctx:GopherParser.Goto_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#def_func_stmt.
    def visitDef_func_stmt(self, ctx:GopherParser.Def_func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#id_call.
    def visitId_call(self, ctx:GopherParser.Id_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#ext_call.
    def visitExt_call(self, ctx:GopherParser.Ext_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#recID.
    def visitRecID(self, ctx:GopherParser.RecIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#parExpr.
    def visitParExpr(self, ctx:GopherParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#numberAtom.
    def visitNumberAtom(self, ctx:GopherParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#boolAtom.
    def visitBoolAtom(self, ctx:GopherParser.BoolAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#idAtom.
    def visitIdAtom(self, ctx:GopherParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#stringAtom.
    def visitStringAtom(self, ctx:GopherParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#listAtom.
    def visitListAtom(self, ctx:GopherParser.ListAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#nullAtom.
    def visitNullAtom(self, ctx:GopherParser.NullAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#id_callExpr.
    def visitId_callExpr(self, ctx:GopherParser.Id_callExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#inputExpr.
    def visitInputExpr(self, ctx:GopherParser.InputExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#uminusExpr.
    def visitUminusExpr(self, ctx:GopherParser.UminusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#orExpr.
    def visitOrExpr(self, ctx:GopherParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#multExpr.
    def visitMultExpr(self, ctx:GopherParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#eqExpr.
    def visitEqExpr(self, ctx:GopherParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#tern_opExpr.
    def visitTern_opExpr(self, ctx:GopherParser.Tern_opExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#valueExpr.
    def visitValueExpr(self, ctx:GopherParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#ext_callExpr.
    def visitExt_callExpr(self, ctx:GopherParser.Ext_callExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#addExpr.
    def visitAddExpr(self, ctx:GopherParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#unotExpr.
    def visitUnotExpr(self, ctx:GopherParser.UnotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#relatExpr.
    def visitRelatExpr(self, ctx:GopherParser.RelatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#powExpr.
    def visitPowExpr(self, ctx:GopherParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#andExpr.
    def visitAndExpr(self, ctx:GopherParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#incl_stmt.
    def visitIncl_stmt(self, ctx:GopherParser.Incl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#load_stmt.
    def visitLoad_stmt(self, ctx:GopherParser.Load_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#for_stmt.
    def visitFor_stmt(self, ctx:GopherParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#until_stmt.
    def visitUntil_stmt(self, ctx:GopherParser.Until_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#while_stmt.
    def visitWhile_stmt(self, ctx:GopherParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#if_stmt.
    def visitIf_stmt(self, ctx:GopherParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#condition_block.
    def visitCondition_block(self, ctx:GopherParser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#stmt_block.
    def visitStmt_block(self, ctx:GopherParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#return_stmt.
    def visitReturn_stmt(self, ctx:GopherParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#list_var.
    def visitList_var(self, ctx:GopherParser.List_varContext):
        return self.visitChildren(ctx)



del GopherParser