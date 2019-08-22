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


    # Enter a parse tree produced by GopherParser#exit.
    def enterExit(self, ctx:GopherParser.ExitContext):
        pass

    # Exit a parse tree produced by GopherParser#exit.
    def exitExit(self, ctx:GopherParser.ExitContext):
        pass


    # Enter a parse tree produced by GopherParser#preproc.
    def enterPreproc(self, ctx:GopherParser.PreprocContext):
        pass

    # Exit a parse tree produced by GopherParser#preproc.
    def exitPreproc(self, ctx:GopherParser.PreprocContext):
        pass


    # Enter a parse tree produced by GopherParser#valdVar.
    def enterValdVar(self, ctx:GopherParser.ValdVarContext):
        pass

    # Exit a parse tree produced by GopherParser#valdVar.
    def exitValdVar(self, ctx:GopherParser.ValdVarContext):
        pass


    # Enter a parse tree produced by GopherParser#novalVar.
    def enterNovalVar(self, ctx:GopherParser.NovalVarContext):
        pass

    # Exit a parse tree produced by GopherParser#novalVar.
    def exitNovalVar(self, ctx:GopherParser.NovalVarContext):
        pass


    # Enter a parse tree produced by GopherParser#novalClass.
    def enterNovalClass(self, ctx:GopherParser.NovalClassContext):
        pass

    # Exit a parse tree produced by GopherParser#novalClass.
    def exitNovalClass(self, ctx:GopherParser.NovalClassContext):
        pass


    # Enter a parse tree produced by GopherParser#multivar.
    def enterMultivar(self, ctx:GopherParser.MultivarContext):
        pass

    # Exit a parse tree produced by GopherParser#multivar.
    def exitMultivar(self, ctx:GopherParser.MultivarContext):
        pass


    # Enter a parse tree produced by GopherParser#powAssgn.
    def enterPowAssgn(self, ctx:GopherParser.PowAssgnContext):
        pass

    # Exit a parse tree produced by GopherParser#powAssgn.
    def exitPowAssgn(self, ctx:GopherParser.PowAssgnContext):
        pass


    # Enter a parse tree produced by GopherParser#multAssgn.
    def enterMultAssgn(self, ctx:GopherParser.MultAssgnContext):
        pass

    # Exit a parse tree produced by GopherParser#multAssgn.
    def exitMultAssgn(self, ctx:GopherParser.MultAssgnContext):
        pass


    # Enter a parse tree produced by GopherParser#addAssgn.
    def enterAddAssgn(self, ctx:GopherParser.AddAssgnContext):
        pass

    # Exit a parse tree produced by GopherParser#addAssgn.
    def exitAddAssgn(self, ctx:GopherParser.AddAssgnContext):
        pass


    # Enter a parse tree produced by GopherParser#appendAssgn.
    def enterAppendAssgn(self, ctx:GopherParser.AppendAssgnContext):
        pass

    # Exit a parse tree produced by GopherParser#appendAssgn.
    def exitAppendAssgn(self, ctx:GopherParser.AppendAssgnContext):
        pass


    # Enter a parse tree produced by GopherParser#popandAssgn.
    def enterPopandAssgn(self, ctx:GopherParser.PopandAssgnContext):
        pass

    # Exit a parse tree produced by GopherParser#popandAssgn.
    def exitPopandAssgn(self, ctx:GopherParser.PopandAssgnContext):
        pass


    # Enter a parse tree produced by GopherParser#indexAssgn.
    def enterIndexAssgn(self, ctx:GopherParser.IndexAssgnContext):
        pass

    # Exit a parse tree produced by GopherParser#indexAssgn.
    def exitIndexAssgn(self, ctx:GopherParser.IndexAssgnContext):
        pass


    # Enter a parse tree produced by GopherParser#decl.
    def enterDecl(self, ctx:GopherParser.DeclContext):
        pass

    # Exit a parse tree produced by GopherParser#decl.
    def exitDecl(self, ctx:GopherParser.DeclContext):
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


    # Enter a parse tree produced by GopherParser#fileouts.
    def enterFileouts(self, ctx:GopherParser.FileoutsContext):
        pass

    # Exit a parse tree produced by GopherParser#fileouts.
    def exitFileouts(self, ctx:GopherParser.FileoutsContext):
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


    # Enter a parse tree produced by GopherParser#class_stmt.
    def enterClass_stmt(self, ctx:GopherParser.Class_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#class_stmt.
    def exitClass_stmt(self, ctx:GopherParser.Class_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#impl_stmt.
    def enterImpl_stmt(self, ctx:GopherParser.Impl_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#impl_stmt.
    def exitImpl_stmt(self, ctx:GopherParser.Impl_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#class_inst.
    def enterClass_inst(self, ctx:GopherParser.Class_instContext):
        pass

    # Exit a parse tree produced by GopherParser#class_inst.
    def exitClass_inst(self, ctx:GopherParser.Class_instContext):
        pass


    # Enter a parse tree produced by GopherParser#def_func_stmt.
    def enterDef_func_stmt(self, ctx:GopherParser.Def_func_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#def_func_stmt.
    def exitDef_func_stmt(self, ctx:GopherParser.Def_func_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#def_func_expr.
    def enterDef_func_expr(self, ctx:GopherParser.Def_func_exprContext):
        pass

    # Exit a parse tree produced by GopherParser#def_func_expr.
    def exitDef_func_expr(self, ctx:GopherParser.Def_func_exprContext):
        pass


    # Enter a parse tree produced by GopherParser#type_name.
    def enterType_name(self, ctx:GopherParser.Type_nameContext):
        pass

    # Exit a parse tree produced by GopherParser#type_name.
    def exitType_name(self, ctx:GopherParser.Type_nameContext):
        pass


    # Enter a parse tree produced by GopherParser#bin_op_def_stmt.
    def enterBin_op_def_stmt(self, ctx:GopherParser.Bin_op_def_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#bin_op_def_stmt.
    def exitBin_op_def_stmt(self, ctx:GopherParser.Bin_op_def_stmtContext):
        pass


    # Enter a parse tree produced by GopherParser#prfix_op_def_stmt.
    def enterPrfix_op_def_stmt(self, ctx:GopherParser.Prfix_op_def_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#prfix_op_def_stmt.
    def exitPrfix_op_def_stmt(self, ctx:GopherParser.Prfix_op_def_stmtContext):
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


    # Enter a parse tree produced by GopherParser#exprID.
    def enterExprID(self, ctx:GopherParser.ExprIDContext):
        pass

    # Exit a parse tree produced by GopherParser#exprID.
    def exitExprID(self, ctx:GopherParser.ExprIDContext):
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


    # Enter a parse tree produced by GopherParser#expnumberAtom.
    def enterExpnumberAtom(self, ctx:GopherParser.ExpnumberAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#expnumberAtom.
    def exitExpnumberAtom(self, ctx:GopherParser.ExpnumberAtomContext):
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


    # Enter a parse tree produced by GopherParser#listspaceAtom.
    def enterListspaceAtom(self, ctx:GopherParser.ListspaceAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#listspaceAtom.
    def exitListspaceAtom(self, ctx:GopherParser.ListspaceAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#nullAtom.
    def enterNullAtom(self, ctx:GopherParser.NullAtomContext):
        pass

    # Exit a parse tree produced by GopherParser#nullAtom.
    def exitNullAtom(self, ctx:GopherParser.NullAtomContext):
        pass


    # Enter a parse tree produced by GopherParser#typeOfExpr.
    def enterTypeOfExpr(self, ctx:GopherParser.TypeOfExprContext):
        pass

    # Exit a parse tree produced by GopherParser#typeOfExpr.
    def exitTypeOfExpr(self, ctx:GopherParser.TypeOfExprContext):
        pass


    # Enter a parse tree produced by GopherParser#lenExpr.
    def enterLenExpr(self, ctx:GopherParser.LenExprContext):
        pass

    # Exit a parse tree produced by GopherParser#lenExpr.
    def exitLenExpr(self, ctx:GopherParser.LenExprContext):
        pass


    # Enter a parse tree produced by GopherParser#id_callExpr.
    def enterId_callExpr(self, ctx:GopherParser.Id_callExprContext):
        pass

    # Exit a parse tree produced by GopherParser#id_callExpr.
    def exitId_callExpr(self, ctx:GopherParser.Id_callExprContext):
        pass


    # Enter a parse tree produced by GopherParser#class_instExpr.
    def enterClass_instExpr(self, ctx:GopherParser.Class_instExprContext):
        pass

    # Exit a parse tree produced by GopherParser#class_instExpr.
    def exitClass_instExpr(self, ctx:GopherParser.Class_instExprContext):
        pass


    # Enter a parse tree produced by GopherParser#prefixOpExpr.
    def enterPrefixOpExpr(self, ctx:GopherParser.PrefixOpExprContext):
        pass

    # Exit a parse tree produced by GopherParser#prefixOpExpr.
    def exitPrefixOpExpr(self, ctx:GopherParser.PrefixOpExprContext):
        pass


    # Enter a parse tree produced by GopherParser#binOpExpr.
    def enterBinOpExpr(self, ctx:GopherParser.BinOpExprContext):
        pass

    # Exit a parse tree produced by GopherParser#binOpExpr.
    def exitBinOpExpr(self, ctx:GopherParser.BinOpExprContext):
        pass


    # Enter a parse tree produced by GopherParser#typeCastExpr.
    def enterTypeCastExpr(self, ctx:GopherParser.TypeCastExprContext):
        pass

    # Exit a parse tree produced by GopherParser#typeCastExpr.
    def exitTypeCastExpr(self, ctx:GopherParser.TypeCastExprContext):
        pass


    # Enter a parse tree produced by GopherParser#xorExpr.
    def enterXorExpr(self, ctx:GopherParser.XorExprContext):
        pass

    # Exit a parse tree produced by GopherParser#xorExpr.
    def exitXorExpr(self, ctx:GopherParser.XorExprContext):
        pass


    # Enter a parse tree produced by GopherParser#listSliceExpr.
    def enterListSliceExpr(self, ctx:GopherParser.ListSliceExprContext):
        pass

    # Exit a parse tree produced by GopherParser#listSliceExpr.
    def exitListSliceExpr(self, ctx:GopherParser.ListSliceExprContext):
        pass


    # Enter a parse tree produced by GopherParser#switchExpr.
    def enterSwitchExpr(self, ctx:GopherParser.SwitchExprContext):
        pass

    # Exit a parse tree produced by GopherParser#switchExpr.
    def exitSwitchExpr(self, ctx:GopherParser.SwitchExprContext):
        pass


    # Enter a parse tree produced by GopherParser#def_funcExpr.
    def enterDef_funcExpr(self, ctx:GopherParser.Def_funcExprContext):
        pass

    # Exit a parse tree produced by GopherParser#def_funcExpr.
    def exitDef_funcExpr(self, ctx:GopherParser.Def_funcExprContext):
        pass


    # Enter a parse tree produced by GopherParser#valueExpr.
    def enterValueExpr(self, ctx:GopherParser.ValueExprContext):
        pass

    # Exit a parse tree produced by GopherParser#valueExpr.
    def exitValueExpr(self, ctx:GopherParser.ValueExprContext):
        pass


    # Enter a parse tree produced by GopherParser#unotExpr.
    def enterUnotExpr(self, ctx:GopherParser.UnotExprContext):
        pass

    # Exit a parse tree produced by GopherParser#unotExpr.
    def exitUnotExpr(self, ctx:GopherParser.UnotExprContext):
        pass


    # Enter a parse tree produced by GopherParser#listIndexExpr.
    def enterListIndexExpr(self, ctx:GopherParser.ListIndexExprContext):
        pass

    # Exit a parse tree produced by GopherParser#listIndexExpr.
    def exitListIndexExpr(self, ctx:GopherParser.ListIndexExprContext):
        pass


    # Enter a parse tree produced by GopherParser#relatExpr.
    def enterRelatExpr(self, ctx:GopherParser.RelatExprContext):
        pass

    # Exit a parse tree produced by GopherParser#relatExpr.
    def exitRelatExpr(self, ctx:GopherParser.RelatExprContext):
        pass


    # Enter a parse tree produced by GopherParser#appendExpr.
    def enterAppendExpr(self, ctx:GopherParser.AppendExprContext):
        pass

    # Exit a parse tree produced by GopherParser#appendExpr.
    def exitAppendExpr(self, ctx:GopherParser.AppendExprContext):
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


    # Enter a parse tree produced by GopherParser#containsExpr.
    def enterContainsExpr(self, ctx:GopherParser.ContainsExprContext):
        pass

    # Exit a parse tree produced by GopherParser#containsExpr.
    def exitContainsExpr(self, ctx:GopherParser.ContainsExprContext):
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


    # Enter a parse tree produced by GopherParser#strcnvrtExpr.
    def enterStrcnvrtExpr(self, ctx:GopherParser.StrcnvrtExprContext):
        pass

    # Exit a parse tree produced by GopherParser#strcnvrtExpr.
    def exitStrcnvrtExpr(self, ctx:GopherParser.StrcnvrtExprContext):
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


    # Enter a parse tree produced by GopherParser#len_expr.
    def enterLen_expr(self, ctx:GopherParser.Len_exprContext):
        pass

    # Exit a parse tree produced by GopherParser#len_expr.
    def exitLen_expr(self, ctx:GopherParser.Len_exprContext):
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


    # Enter a parse tree produced by GopherParser#singlFor.
    def enterSinglFor(self, ctx:GopherParser.SinglForContext):
        pass

    # Exit a parse tree produced by GopherParser#singlFor.
    def exitSinglFor(self, ctx:GopherParser.SinglForContext):
        pass


    # Enter a parse tree produced by GopherParser#multFor.
    def enterMultFor(self, ctx:GopherParser.MultForContext):
        pass

    # Exit a parse tree produced by GopherParser#multFor.
    def exitMultFor(self, ctx:GopherParser.MultForContext):
        pass


    # Enter a parse tree produced by GopherParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:GopherParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by GopherParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:GopherParser.Switch_stmtContext):
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


    # Enter a parse tree produced by GopherParser#linspace.
    def enterLinspace(self, ctx:GopherParser.LinspaceContext):
        pass

    # Exit a parse tree produced by GopherParser#linspace.
    def exitLinspace(self, ctx:GopherParser.LinspaceContext):
        pass


