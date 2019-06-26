from importlib import __import__ as load
from antlr4 import *
from GopherLexer import GopherLexer
from GopherParser import GopherParser
from GopherVisitor import GopherVisitor


class Gophisitor(GopherVisitor):

    memory = {'': 0}

    def visitIncl_stmt(self, ctx: GopherParser.Incl_stmtContext):
        path = ''
        if ctx.recID() != None:
            mid = None
            ids = ctx.recID().ID()
            path += str(ids[0])
            for pid in ids[1:]:
                mid = str(pid)
                path += '/' + mid
            path += '.gopr'
        else:
            mid = str(ctx.ID())
            path += mid + '.gopr'
        inclexer = GopherLexer(FileStream(path))
        inclstream = CommonTokenStream(inclexer)
        inclparser = GopherParser(inclstream)
        incltree = inclparser.program()
        inclgophisitor = Gophisitor()
        inclgophisitor.visit(incltree)
        self.memory[mid] = inclgophisitor.memory
        self.memory[mid]['type'] = 'module' + mid
    
    def visitLoad_stmt(self, ctx: GopherParser.Load_stmtContext):
        path = ''
        if ctx.recID() != None:
            mid = None
            ids = ctx.recID().ID()
            path += str(ids[0])
            for pid in ids[1:]:
                mid = str(pid)
                path += '.' + mid
            mod = load(path).__dict__
            for pid in ids[1:]:
                mod = mod[str(pid)].__dict__
            self.memory[mid] = mod
        else:
            mid = str(ctx.ID())
            mod = load(mid).__dict__
            self.memory[mid] = mod
            
    def visitVar(self, ctx: GopherParser.VarContext):
        id = str(ctx.ID())
        value = self.visit(ctx.expr())
        self.memory[id] = value
        return value

    def visitRecID(self, ctx: GopherParser.RecIDContext):
        ids = ctx.ID()
        val = self.memory[str(ids[0])]
        for vid in ids[1:]:
            prevval = val
            val = val[str(vid)]
        return val
    
    def visitIdAtom(self, ctx: GopherParser.IdAtomContext):
        if ctx.recID() != None:
            return self.visit(ctx.recID())
        else:
            id = str(ctx.ID())
            return self.memory[id]
    
    def visitStringAtom(self, ctx: GopherParser.StringAtomContext):
        outstr = str(ctx.STRING())
        return outstr[1:len(outstr)-1]
    
    def visitNumberAtom(self, ctx: GopherParser.NumberAtomContext):
        outflt = float(str(ctx.DECIMAL()))
        return outflt
    
    def visitBoolAtom(self, ctx: GopherParser.BoolAtomContext):
        bltxt = str(ctx.BOOL())
        if bltxt == "false":
            return False
        else: 
            return True
    
    def visitNullAtom(self, ctx: GopherParser.NullAtomContext):
        return None
    
    def visitParExpr(self, ctx: GopherParser.ParExprContext):
        return self.visit(ctx.expr())

    def visitPowExpr(self, ctx: GopherParser.PowExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left**right

    def visitUminusExpr(self, ctx: GopherParser.UminusExprContext):
        val = self.visit(ctx.expr())
        if isinstance(val, str):
            val = list(val)
            val.reverse()
            return ''.join(val)
        elif isinstance(val, bool):
            return not val
        else:
            return -val
    
    def visitUnotExpr(self, ctx: GopherParser.UnotExprContext):
        return not (self.visit(ctx.expr()))
    
    def visitMultExpr(self, ctx: GopherParser.MultExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        if op == GopherParser.MULT:
            if isinstance(left, str):
                return int(right) * left
            elif isinstance(right, str):
                return int(left) * right
            else:
                return left * right
        elif op == GopherParser.DIV:
            return left / right
        elif op == GopherParser.MOD:
            return left % right
        else:
            raise SyntaxError(op.getText()+"is not an operator")
 
    def visitAddExpr(self, ctx: GopherParser.AddExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        if op == GopherParser.PLUS:
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            else:
                return left + right
        elif op == GopherParser.MINUS:
            return float(left)-float(right)
        else:
            raise SyntaxError(op.getText()+"is not a valid operator")
    
    def visitRelatExpr(self, ctx: GopherParser.RelatExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        if op == GopherParser.LT:
            return left < right
        elif op == GopherParser.LTEQ:
            return left <= right
        elif op == GopherParser.GT:
            return left > right
        elif op == GopherParser.GTEQ:
            return left >= right
        else:
            raise SyntaxError(op.getText()+"is not a valid operator")
    
    def visitEqExpr(self, ctx: GopherParser.EqExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        if op == GopherParser.EQ:
            return left == right
        elif op == GopherParser.NEQ:
            return left != right
        else:
            raise SyntaxError(str(op)+"is not a valid operator")
    
    def visitAndExpr(self, ctx: GopherParser.AddExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left & right
    
    def visitOrExpr(self, ctx: GopherParser.OrExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left | right
    
    def visitPrint0(self, ctx: GopherParser.Print0Context):
        print(self.visit(ctx.expr()), end='')
        return None
    
    def visitPrintln(self, ctx: GopherParser.PrintlnContext):
        print(self.visit(ctx.expr()), end='\n\r')
        return None
    
    def visitValueExpr(self, ctx: GopherParser.ValueExprContext):
        return self.visit(ctx.value())

    def visitKey(self, ctx: GopherParser.KeyContext):
        input()
        return None
    
    def visitInputExpr(self, ctx: GopherParser.InputExprContext):
        return input(self.visit(ctx.expr()))
    
    def visitIf_stmt(self, ctx: GopherParser.If_stmtContext):
        conditions = ctx.condition_block()
        evalt = False
        retval = "ji"
        for condition in conditions:
            if self.visit(condition.expr()):
                evalt = True
                retval = self.visit(condition.stmt_block())
                if isinstance(retval, tuple):
                    return retval
                break
        if (not evalt) and (ctx.stmt_block() != None):
            retval = self.visit(ctx.stmt_block())
            if isinstance(retval, tuple):
                return retval
        return retval
    
    def visitWhile_stmt(self, ctx: GopherParser.While_stmtContext):
        retval = "ji"
        val = self.visit(ctx.expr())
        while val:
            retval = self.visit(ctx.stmt_block())
            if isinstance(retval, tuple):
                return retval
            val = self.visit(ctx.expr())
        return retval
    
    def visitUntil_stmt(self, ctx: GopherParser.Until_stmtContext):
        retval = "ji"
        val = self.visit(ctx.expr())
        while not val:
            retval = self.visit(ctx.stmt_block())
            if isinstance(retval, tuple):
                return retval
            val = self.visit(ctx.expr())
        return retval
    
    def visitListAtom(self, ctx: GopherParser.ListAtomContext):
        lis = ctx.list_var().expr()
        ret = []
        for expr in lis:
            ret.append(self.visit(expr))
        return ret

    def visitFor_stmt(self, ctx: GopherParser.For_stmtContext):
        retval = "ji"
        var = str(ctx.ID())
        lis = self.visit(ctx.expr())
        for val in lis:
            self.memory[var] = val
            retval = self.visit(ctx.stmt_block())
            if isinstance(retval, tuple):
                return retval
        return retval
    
    def visitTern_opExpr(self, ctx: GopherParser.Tern_opExprContext):
        if self.visit(ctx.condexpr):
            return self.visit(ctx.truexpr)
        else:
            return self.visit(ctx.falsexpr)
    
    def visitLabel_def(self, ctx: GopherParser.Label_defContext):
        lblid = str(ctx.ID())
        self.memory[lblid] = ctx.stmt_block()

    def visitGoto_stmt(self, ctx: GopherParser.Goto_stmtContext):
        lblid = str(ctx.ID())
        val = self.visit(self.memory[lblid])
        if isinstance(val, tuple):
            return val
        return val
    
    def visitDef_func_stmt(self, ctx: GopherParser.Def_func_stmtContext):
        funcdata = ctx.ID()
        funcid = str(funcdata[0])
        varlist = []
        for varid in funcdata[1:]:
            varlist.append(str(varid))
        namedvarlist = dict()
        for nid, val in zip(ctx.ID(), ctx.value()):
            namedvarlist[str(nid)] = self.visit(val)
        self.memory[funcid] = {'call':
                               {'varlist':
                                varlist,
                                'block':
                                ctx.stmt_block(),
                                'namedvarlist':
                                namedvarlist},
                               'type': 'function'}
        return self.memory[funcid]
    
    def visitId_call(self, ctx: GopherParser.Id_callContext):
        if ctx.recID() != None:
            data = self.visit(ctx.recID())['call']
        else:
            data = self.memory[str(ctx.ID())]['call']
        exprlis = []
        for expr in ctx.expr():
            exprlis.append(self.visit(expr))
        if (len(data['varlist']) + len(data['namedvarlist'])) < len(exprlis):
            raise TypeError
        self.memory.update(dict(zip(data['varlist'] +
                                    list(data['namedvarlist'].keys())[
                                        :len(exprlis)-len(data['varlist'])
                                        ],
                                    exprlis +
                                    list(data['namedvarlist'].values())[
                                        len(exprlis) - len(data['varlist']):
                                    ])))
        retval = self.visit(data['block'])
        if isinstance(retval, tuple):
            return retval[0]
        else:
            return retval
    
    def visitId_callExpr(self, ctx: GopherParser.Id_callExprContext):
        return self.visit(ctx.id_call())
    
    def visitStmt_block(self, ctx: GopherParser.Stmt_blockContext):
        return self.visit(ctx.block())

    def visitBlock(self, ctx: GopherParser.BlockContext):
        retval = "ji"
        for stmt in ctx.stmt():
            if stmt.return_stmt() != None:
                return (self.visit(stmt.return_stmt().expr()),)
            else:
                retval = self.visit(stmt)
                if isinstance(retval, tuple):
                    return retval
        return retval

        def visitExt_callExpr(self, ctx: GopherParser.Ext_callExprContext):
            return self.visit(ctx.ext_call())
        
        def visitExt_call(self, ctx: GopherParser.Ext_callContext):
            func = ''
            if ctx.recID() is not None:
                func = self.visit(cxt.recID())
            else:
                func = self.visit(ctx.ID())
            evalstr = 'func('
            exprlis = ctx.expr()
            print(self.visit(exprlis[0]))
            evalstr += str(self.visit(exprlis[0]))
            for expr in exprlis[1:]:
                evalstr += ',' + str(self.visit(expr))
            return eval(evalstr + ')')
