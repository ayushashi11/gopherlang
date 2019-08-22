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


    # Visit a parse tree produced by GopherParser#exit.
    def visitExit(self, ctx:GopherParser.ExitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#preproc.
    def visitPreproc(self, ctx:GopherParser.PreprocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#valdVar.
    def visitValdVar(self, ctx:GopherParser.ValdVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#novalVar.
    def visitNovalVar(self, ctx:GopherParser.NovalVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#novalClass.
    def visitNovalClass(self, ctx:GopherParser.NovalClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#multivar.
    def visitMultivar(self, ctx:GopherParser.MultivarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#powAssgn.
    def visitPowAssgn(self, ctx:GopherParser.PowAssgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#multAssgn.
    def visitMultAssgn(self, ctx:GopherParser.MultAssgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#addAssgn.
    def visitAddAssgn(self, ctx:GopherParser.AddAssgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#appendAssgn.
    def visitAppendAssgn(self, ctx:GopherParser.AppendAssgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#popandAssgn.
    def visitPopandAssgn(self, ctx:GopherParser.PopandAssgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#indexAssgn.
    def visitIndexAssgn(self, ctx:GopherParser.IndexAssgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#decl.
    def visitDecl(self, ctx:GopherParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#print0.
    def visitPrint0(self, ctx:GopherParser.Print0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#println.
    def visitPrintln(self, ctx:GopherParser.PrintlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#fileouts.
    def visitFileouts(self, ctx:GopherParser.FileoutsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#label_def.
    def visitLabel_def(self, ctx:GopherParser.Label_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#goto_stmt.
    def visitGoto_stmt(self, ctx:GopherParser.Goto_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#class_stmt.
    def visitClass_stmt(self, ctx:GopherParser.Class_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#impl_stmt.
    def visitImpl_stmt(self, ctx:GopherParser.Impl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#class_inst.
    def visitClass_inst(self, ctx:GopherParser.Class_instContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#def_func_stmt.
    def visitDef_func_stmt(self, ctx:GopherParser.Def_func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#def_func_expr.
    def visitDef_func_expr(self, ctx:GopherParser.Def_func_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#type_name.
    def visitType_name(self, ctx:GopherParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#bin_op_def_stmt.
    def visitBin_op_def_stmt(self, ctx:GopherParser.Bin_op_def_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#prfix_op_def_stmt.
    def visitPrfix_op_def_stmt(self, ctx:GopherParser.Prfix_op_def_stmtContext):
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


    # Visit a parse tree produced by GopherParser#exprID.
    def visitExprID(self, ctx:GopherParser.ExprIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#parExpr.
    def visitParExpr(self, ctx:GopherParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#numberAtom.
    def visitNumberAtom(self, ctx:GopherParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#expnumberAtom.
    def visitExpnumberAtom(self, ctx:GopherParser.ExpnumberAtomContext):
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


    # Visit a parse tree produced by GopherParser#listspaceAtom.
    def visitListspaceAtom(self, ctx:GopherParser.ListspaceAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#nullAtom.
    def visitNullAtom(self, ctx:GopherParser.NullAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#typeOfExpr.
    def visitTypeOfExpr(self, ctx:GopherParser.TypeOfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#lenExpr.
    def visitLenExpr(self, ctx:GopherParser.LenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#id_callExpr.
    def visitId_callExpr(self, ctx:GopherParser.Id_callExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#class_instExpr.
    def visitClass_instExpr(self, ctx:GopherParser.Class_instExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#prefixOpExpr.
    def visitPrefixOpExpr(self, ctx:GopherParser.PrefixOpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#binOpExpr.
    def visitBinOpExpr(self, ctx:GopherParser.BinOpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#typeCastExpr.
    def visitTypeCastExpr(self, ctx:GopherParser.TypeCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#xorExpr.
    def visitXorExpr(self, ctx:GopherParser.XorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#listSliceExpr.
    def visitListSliceExpr(self, ctx:GopherParser.ListSliceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#switchExpr.
    def visitSwitchExpr(self, ctx:GopherParser.SwitchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#def_funcExpr.
    def visitDef_funcExpr(self, ctx:GopherParser.Def_funcExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#valueExpr.
    def visitValueExpr(self, ctx:GopherParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#unotExpr.
    def visitUnotExpr(self, ctx:GopherParser.UnotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#listIndexExpr.
    def visitListIndexExpr(self, ctx:GopherParser.ListIndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#relatExpr.
    def visitRelatExpr(self, ctx:GopherParser.RelatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#appendExpr.
    def visitAppendExpr(self, ctx:GopherParser.AppendExprContext):
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


    # Visit a parse tree produced by GopherParser#containsExpr.
    def visitContainsExpr(self, ctx:GopherParser.ContainsExprContext):
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


    # Visit a parse tree produced by GopherParser#ext_callExpr.
    def visitExt_callExpr(self, ctx:GopherParser.Ext_callExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#addExpr.
    def visitAddExpr(self, ctx:GopherParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#strcnvrtExpr.
    def visitStrcnvrtExpr(self, ctx:GopherParser.StrcnvrtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#powExpr.
    def visitPowExpr(self, ctx:GopherParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#andExpr.
    def visitAndExpr(self, ctx:GopherParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#len_expr.
    def visitLen_expr(self, ctx:GopherParser.Len_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#incl_stmt.
    def visitIncl_stmt(self, ctx:GopherParser.Incl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#load_stmt.
    def visitLoad_stmt(self, ctx:GopherParser.Load_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#singlFor.
    def visitSinglFor(self, ctx:GopherParser.SinglForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#multFor.
    def visitMultFor(self, ctx:GopherParser.MultForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopherParser#switch_stmt.
    def visitSwitch_stmt(self, ctx:GopherParser.Switch_stmtContext):
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


    # Visit a parse tree produced by GopherParser#linspace.
    def visitLinspace(self, ctx:GopherParser.LinspaceContext):
        return self.visitChildren(ctx)



del GopherParser