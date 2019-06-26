# Generated from Gopher.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GopherParser import GopherParser
else:
    from GopherParser import GopherParser

# This class defines a complete listener for a parse tree produced by GopherParser.
class GopherListener(ParseTreeListener):

    # Enter a parse tree produced by GopherParser#program.
    def enterProgram(self, ctx:GopherParser.ProgramContext):
        pass

    # Exit a parse tree produced by GopherParser#program.
    def exitProgram(self, ctx:GopherParser.ProgramContext):
        pass


    # Enter a parse tree produced by GopherParser#block.
    def enterBlock(self, ctx:GopherParser.BlockContext):
        pass

    # Exit a parse tree produced by GopherParser#block.
    def exitBlock(self, ctx:GopherParser.BlockContext):
        pass


    # Enter a parse tree produced by GopherParser#stmt.
    def enterStmt(self, ctx:GopherParser.StmtContext):
        pass

    # Exit a parse tree produced by GopherParser#stmt.
    def exitStmt(self, ctx:GopherParser.StmtContext):
        pass


    # Enter a parse tree produced by GopherParser#key.
    def enterKey(self, ctx:GopherParser.KeyContext):
        pass

    # Exit a parse tree produced by GopherParser#key.
    def exitKey(self, ctx:GopherParser.KeyContext):
        pass


    # Enter a parse tree produced by GopherParser#var.
    def enterVar(self, ctx:GopherParser.VarContext):
        pass

    # Exit a parse tree produced by GopherParser#var.
    def exitVar(self, ctx:GopherParser.VarContext):
        pass


    # Enter a parse tree produced by GopherParser#preproc.
    def enterPreproc(self, ctx:GopherParser.PreprocContext):
        pass

    # Exit a parse tree produced by GopherParser#preproc.
    def exitPreproc(self, ctx:GopherParser.PreprocContext):
        pass


    # Enter a parse tree produced by GopherParser#print0.
    def enterPrint0(self, ctx:GopherParser.Print0Context):
        pass

    # Exit a parse tree produced by GopherParser#print0.
    def exitPrint0(self, ctx:GopherParser.Print0Context):
        pass


    # Enter a parse tree produced by GopherParser#println.
    def enterPrintln(self, ctx:GopherParser.PrintlnContext):
        pass

    # Exit a parse tree produced by GopherParser#println.
    def exitPrintln(self, ctx:GopherParser.PrintlnContext):
        pass


    # Enter a parse tree produced by GopherParser#label_def.
    def enterLabel_def(self, ctx:GopherParser.Label_defContext):
        pass

    # Exit a parse tree produced by GopherParser#label_def.
    def exitLabel_def(self, ctx:GopherParser.Label_defContext):
        pass


    # Enter a parse tree produced by GopherParser#goto_stmt.
    def enterGoto_stmt(self, ctx:GopherParser.Goto_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#goto_stmt.
    def exitGoto_stmt(self, ctx:GopherParser.Goto_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#def_func_stmt.
    def enterDef_func_stmt(self, ctx:GopherParser.Def_func_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#def_func_stmt.
    def exitDef_func_stmt(self, ctx:GopherParser.Def_func_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#id_call.
    def enterId_call(self, ctx:GopherParser.Id_callContext):
        pass

    # Exit a parse tree produced by GopherParser#id_call.
    def exitId_call(self, ctx:GopherParser.Id_callContext):
        pass


    # Enter a parse tree produced by GopherParser#ext_call.
    def enterExt_call(self, ctx:GopherParser.Ext_callContext):
        pass

    # Exit a parse tree produced by GopherParser#ext_call.
    def exitExt_call(self, ctx:GopherParser.Ext_callContext):
        pass


    # Enter a parse tree produced by GopherParser#recID.
    def enterRecID(self, ctx:GopherParser.RecIDContext):
        pass

    # Exit a parse tree produced by GopherParser#recID.
    def exitRecID(self, ctx:GopherParser.RecIDContext):
        pass


    # Enter a parse tree produced by GopherParser#parExpr.
    def enterParExpr(self, ctx:GopherParser.ParExprContext):
        pass

    # Exit a parse tree produced by GopherParser#parExpr.
    def exitParExpr(self, ctx:GopherParser.ParExprContext):
        pass


    # Enter a parse tree produced by GopherParser#numberAtom.
    def enterNumberAtom(self, ctx:GopherParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#numberAtom.
    def exitNumberAtom(self, ctx:GopherParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#boolAtom.
    def enterBoolAtom(self, ctx:GopherParser.BoolAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#boolAtom.
    def exitBoolAtom(self, ctx:GopherParser.BoolAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#idAtom.
    def enterIdAtom(self, ctx:GopherParser.IdAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#idAtom.
    def exitIdAtom(self, ctx:GopherParser.IdAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#stringAtom.
    def enterStringAtom(self, ctx:GopherParser.StringAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#stringAtom.
    def exitStringAtom(self, ctx:GopherParser.StringAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#listAtom.
    def enterListAtom(self, ctx:GopherParser.ListAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#listAtom.
    def exitListAtom(self, ctx:GopherParser.ListAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#nullAtom.
    def enterNullAtom(self, ctx:GopherParser.NullAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#nullAtom.
    def exitNullAtom(self, ctx:GopherParser.NullAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#id_callExpr.
    def enterId_callExpr(self, ctx:GopherParser.Id_callExprContext):
        pass

    # Exit a parse tree produced by GopherParser#id_callExpr.
    def exitId_callExpr(self, ctx:GopherParser.Id_callExprContext):
        pass


    # Enter a parse tree produced by GopherParser#inputExpr.
    def enterInputExpr(self, ctx:GopherParser.InputExprContext):
        pass

    # Exit a parse tree produced by GopherParser#inputExpr.
    def exitInputExpr(self, ctx:GopherParser.InputExprContext):
        pass


    # Enter a parse tree produced by GopherParser#uminusExpr.
    def enterUminusExpr(self, ctx:GopherParser.UminusExprContext):
        pass

    # Exit a parse tree produced by GopherParser#uminusExpr.
    def exitUminusExpr(self, ctx:GopherParser.UminusExprContext):
        pass


    # Enter a parse tree produced by GopherParser#orExpr.
    def enterOrExpr(self, ctx:GopherParser.OrExprContext):
        pass

    # Exit a parse tree produced by GopherParser#orExpr.
    def exitOrExpr(self, ctx:GopherParser.OrExprContext):
        pass


    # Enter a parse tree produced by GopherParser#multExpr.
    def enterMultExpr(self, ctx:GopherParser.MultExprContext):
        pass

    # Exit a parse tree produced by GopherParser#multExpr.
    def exitMultExpr(self, ctx:GopherParser.MultExprContext):
        pass


    # Enter a parse tree produced by GopherParser#eqExpr.
    def enterEqExpr(self, ctx:GopherParser.EqExprContext):
        pass

    # Exit a parse tree produced by GopherParser#eqExpr.
    def exitEqExpr(self, ctx:GopherParser.EqExprContext):
        pass


    # Enter a parse tree produced by GopherParser#tern_opExpr.
    def enterTern_opExpr(self, ctx:GopherParser.Tern_opExprContext):
        pass

    # Exit a parse tree produced by GopherParser#tern_opExpr.
    def exitTern_opExpr(self, ctx:GopherParser.Tern_opExprContext):
        pass


    # Enter a parse tree produced by GopherParser#valueExpr.
    def enterValueExpr(self, ctx:GopherParser.ValueExprContext):
        pass

    # Exit a parse tree produced by GopherParser#valueExpr.
    def exitValueExpr(self, ctx:GopherParser.ValueExprContext):
        pass


    # Enter a parse tree produced by GopherParser#ext_callExpr.
    def enterExt_callExpr(self, ctx:GopherParser.Ext_callExprContext):
        pass

    # Exit a parse tree produced by GopherParser#ext_callExpr.
    def exitExt_callExpr(self, ctx:GopherParser.Ext_callExprContext):
        pass


    # Enter a parse tree produced by GopherParser#addExpr.
    def enterAddExpr(self, ctx:GopherParser.AddExprContext):
        pass

    # Exit a parse tree produced by GopherParser#addExpr.
    def exitAddExpr(self, ctx:GopherParser.AddExprContext):
        pass


    # Enter a parse tree produced by GopherParser#unotExpr.
    def enterUnotExpr(self, ctx:GopherParser.UnotExprContext):
        pass

    # Exit a parse tree produced by GopherParser#unotExpr.
    def exitUnotExpr(self, ctx:GopherParser.UnotExprContext):
        pass


    # Enter a parse tree produced by GopherParser#relatExpr.
    def enterRelatExpr(self, ctx:GopherParser.RelatExprContext):
        pass

    # Exit a parse tree produced by GopherParser#relatExpr.
    def exitRelatExpr(self, ctx:GopherParser.RelatExprContext):
        pass


    # Enter a parse tree produced by GopherParser#powExpr.
    def enterPowExpr(self, ctx:GopherParser.PowExprContext):
        pass

    # Exit a parse tree produced by GopherParser#powExpr.
    def exitPowExpr(self, ctx:GopherParser.PowExprContext):
        pass


    # Enter a parse tree produced by GopherParser#andExpr.
    def enterAndExpr(self, ctx:GopherParser.AndExprContext):
        pass

    # Exit a parse tree produced by GopherParser#andExpr.
    def exitAndExpr(self, ctx:GopherParser.AndExprContext):
        pass


    # Enter a parse tree produced by GopherParser#incl_stmt.
    def enterIncl_stmt(self, ctx:GopherParser.Incl_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#incl_stmt.
    def exitIncl_stmt(self, ctx:GopherParser.Incl_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#load_stmt.
    def enterLoad_stmt(self, ctx:GopherParser.Load_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#load_stmt.
    def exitLoad_stmt(self, ctx:GopherParser.Load_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#for_stmt.
    def enterFor_stmt(self, ctx:GopherParser.For_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#for_stmt.
    def exitFor_stmt(self, ctx:GopherParser.For_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#until_stmt.
    def enterUntil_stmt(self, ctx:GopherParser.Until_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#until_stmt.
    def exitUntil_stmt(self, ctx:GopherParser.Until_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#while_stmt.
    def enterWhile_stmt(self, ctx:GopherParser.While_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#while_stmt.
    def exitWhile_stmt(self, ctx:GopherParser.While_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#if_stmt.
    def enterIf_stmt(self, ctx:GopherParser.If_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#if_stmt.
    def exitIf_stmt(self, ctx:GopherParser.If_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#condition_block.
    def enterCondition_block(self, ctx:GopherParser.Condition_blockContext):
        pass

    # Exit a parse tree produced by GopherParser#condition_block.
    def exitCondition_block(self, ctx:GopherParser.Condition_blockContext):
        pass


    # Enter a parse tree produced by GopherParser#stmt_block.
    def enterStmt_block(self, ctx:GopherParser.Stmt_blockContext):
        pass

    # Exit a parse tree produced by GopherParser#stmt_block.
    def exitStmt_block(self, ctx:GopherParser.Stmt_blockContext):
        pass


    # Enter a parse tree produced by GopherParser#return_stmt.
    def enterReturn_stmt(self, ctx:GopherParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#return_stmt.
    def exitReturn_stmt(self, ctx:GopherParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#list_var.
    def enterList_var(self, ctx:GopherParser.List_varContext):
        pass

    # Exit a parse tree produced by GopherParser#list_var.
    def exitList_var(self, ctx:GopherParser.List_varContext):
        pass


