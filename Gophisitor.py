from importlib import __import__ as load
from antlr4 import *
import antlr4.tree as tr
import numpy as np
from GopherLexer import GopherLexer
from GopherParser import GopherParser
from GopherVisitor import GopherVisitor
import fmt
import fncalls
import GopherTypes
tid = id
ftype = {'float': float,
         'str': str,
         'bool': bool,
         'list': list,
         'any': (lambda x: x)}


class DeclVisitor(GopherVisitor):

    memory = {0: ''}

    def visitPreproc(self, ctx: GopherParser.PreprocContext):
        for child in list(ctx.getChildren())[1:-1]:
            print(str(child)[1:-1])

    def visitLabel_def(self, ctx: GopherParser.Label_defContext):
        lblid = str(ctx.ID())
        self.memory[lblid] = ctx.stmt_block()
    
    def visitDef_func_stmt(self, ctx: GopherParser.Def_func_stmtContext):
        if ctx.type_name() is not None:
            rtype = self.visit(ctx.type_name())
        else:
            rtype = 'any'
        funcdata = ctx.ID()
        funcid = str(funcdata[0])
        varlist = []
        for varid in funcdata[1:]:
            varlist.append(str(varid))
        namedvarlist = dict()
        for op_arg in ctx.var():
            namedvarlist[str(op_arg.ID())] = self.visit(op_arg.expr())
        self.memory[funcid] = {'call':
                               {'varlist':
                                varlist,
                                'block':
                                ctx.stmt_block(),
                                'namedvarlist':
                                namedvarlist},
                               'rtype': rtype,
                               'type': 'function'}
        return self.memory[funcid]
    
    def visitClass_stmt(self, ctx: GopherParser.Class_stmtContext):
        cid = str(ctx.ID(0))
        extendeds = []
        if ctx.EID is not None:
            extendeds = ctx.EID()
        varbls = ctx.var()
        temp = self.memory
        self.memory = dict()
        for var in varbls:
            self.visit(var)
        temp[cid], temp[cid]["vars"] = 2*(self.memory,)
        self.memory = temp
    
    def visitImpl_stmt(self, ctx: GopherParser.Impl_stmtContext):
        cid = str(ctx.ID())
        varbls = ctx.def_func_stmt()
        temp = self.memory
        self.memory = dict()
        for var in varbls:
            self.visit(var)
        try:
            self.memory['call'] = self.memory['__init']['call']
        except KeyError:
            pass
        temp[cid].update(self.memory)
        self.memory = temp
    
    def visitBin_op_def_stmt(self, ctx: GopherParser.Bin_op_def_stmtContext):
        op = str(ctx.OPERATOR())
        t1 = self.visit(ctx.type_name(0))
        t2 = self.visit(ctx.type_name(1))
        if t1 == 'any' or t2 == 'any':
            mid = op
        else:
            mid = op+','+t1+','+t2
        self.memory[mid] = ctx.stmt_block()
    
    def visitPrfix_op_def_stmt(self, ctx: GopherParser.Prfix_op_def_stmtContext):
        op = str(ctx.OPERATOR())
        t1 = self.visit(ctx.type_name())
        if t1 == 'any':
            mid = op
        else:
            mid = op+','+t1
        self.memory[mid] = ctx.stmt_block()
    
    def visitType_name(self, ctx: GopherParser.Type_nameContext):
        if ctx.DT() is not None:
            return str(ctx.DT())
        elif ctx.ID() is not None:
            return str(ctx.ID())
        else:
            return str(ctx.recID().ID()[-1])


class Gophisitor(GopherVisitor):

    memory = {'__name': {'val': '__main', 'type': 'str'}}

    def visitErrorNode(self, eri):
        print('err at', eri.getText(), eri.parentCtx.__dict__)

    def visitProgram(self, ctx: GopherParser.ProgramContext):
        declvsr = DeclVisitor()
        declvsr.visit(ctx)
        self.memory.update(declvsr.memory)
        return self.visit(ctx.block())

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
        inclgophisitor.memory['__name'] = {'val': '__'+mid, 'type': 'str'}
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
            mod = load(path)
            #mod = load(path).__dict__
            #for pid in ids[1:]:
                #mod = mod[str(pid)].__dict__
            self.memory[mid] = {'val': mod, 'type': 'extmod'+mid}
        else:
            mid = str(ctx.ID())
            mod = load(mid)
            #mod = load(mid).__dict__
            self.memory[mid] = {'val': mod, 'type': 'extmod'+mid}
            
    def visitValdVar(self, ctx: GopherParser.ValdVarContext):
        id = str(ctx.ID())
        value = dict(self.visit(ctx.expr()))
        dt = ''
        if ctx.type_name() != None:
            dt = self.visit(ctx.type_name())
        else:
            try:
                dt = self.memory[id]['type']
            except:
                dt = 'any'
        if (value['type'] != dt) and (dt != 'any'):
            value = fncalls.cnvrt(self, value, dt)
        elif dt == 'any':
            value['type'] = dt
        return fncalls.assgn(self, value, id, dt, ctx.CONSTASSIGN())

    def visitRecID(self, ctx: GopherParser.RecIDContext):
        ids = ctx.ID()
        val = self.memory[str(ids[0])]
        for vid in ids[1:]:
            prevval = val
            val = val[str(vid)]
            try:
                val['parent'] = prevval
            except:
                pass
        return val
    
    def visitExprID(self, ctx: GopherParser.ExprIDContext):
        expr = self.visit(ctx.expr())
        val = expr
        if ctx.ID() is not None:
            self.memory['this'] = val
            return val[str(ctx.ID())]

    def visitIdAtom(self, ctx: GopherParser.IdAtomContext):
        if ctx.exprID() != None:
            return self.visit(ctx.exprID())
        elif ctx.recID() != None:
            return self.visit(ctx.recID())
        else:
            id = str(ctx.ID())
            return self.memory[id]
    
    def visitStringAtom(self, ctx: GopherParser.StringAtomContext):
        out = str(ctx.STRING())
        out = out[1:-1]
        out = out.replace('\\\\', '\\').replace('\\n', '\n').replace('\\r',
                '\r').replace('\\"', '"').replace("\\'", "'").replace("\\a",
                "\a").replace("\\b", "\b")
        return {'val': out,
                'type': 'str'}
    
    def visitNumberAtom(self, ctx: GopherParser.NumberAtomContext):
        outflt = float(str(ctx.DECIMAL()))
        return {'val': outflt, 'type': 'float'}
    
    def visitBoolAtom(self, ctx: GopherParser.BoolAtomContext):
        bltxt = str(ctx.BOOL())
        if bltxt == "false":
            return {'val': False, 'type': 'bool'}
        else: 
            return {'val': True, 'type': 'bool'}
    
    def visitNullAtom(self, ctx: GopherParser.NullAtomContext):
        return {'val': None, 'type': 'null'}
    
    def visitParExpr(self, ctx: GopherParser.ParExprContext):
        return self.visit(ctx.expr())

    def visitPowExpr(self, ctx: GopherParser.PowExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        return {'val': float(left)**float(right), 'type': 'float'}

    def visitUminusExpr(self, ctx: GopherParser.UminusExprContext):
        val = self.visit(ctx.expr())['val']
        if isinstance(val, str):
            val = list(val)
            val.reverse()
            return {'val': ''.join(val), 'type': 'str'}
        elif isinstance(val, bool):
            return {'val': not val, 'type': 'bool'}
        elif isinstance(val, list):
            ret = list(val)
            ret.reverse()
            return {'val': ret, 'type': 'list'}
        else:
            return {'val': -val, 'type': 'float'}
    
    def visitUnotExpr(self, ctx: GopherParser.UnotExprContext):
        return {'val': not (self.visit(ctx.expr()))['val'], 'type': 'bool'}
    
    def visitMultExpr(self, ctx: GopherParser.MultExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        op = ctx.op.type
        if op == GopherParser.MULT:
            if isinstance(left, (str, list)):
                return {'val': int(right) * left,
                        'type': ('str' if type(left) == str else 'list')}
            elif isinstance(right, (str, list)):
                return {'val': int(left) * right,
                        'type': ('str' if type(right) == str else 'list')}
            else:
                return {'val':  left * right, 'type': 'float'}
        elif op == GopherParser.DIV:
            return {'val':  left / right, 'type': 'float'}
        elif op == GopherParser.MOD:
            return {'val':  left % right, 'type': 'float'}
        else:
            raise SyntaxError(op.getText()+"is not an operator")
 
    def visitAddExpr(self, ctx: GopherParser.AddExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        op = ctx.op.type
        if op == GopherParser.PLUS:
            if isinstance(left, (str)) or isinstance(right, str):
                return {'val': str(left) + str(right), 'type': 'str'}
            else:
                return {'val': left + right,
                        'type':
                        ('float' if type(left + right) != list else 'list')}
        elif op == GopherParser.MINUS:
            return {'val': float(left)-float(right), 'type': 'float'}
        else:
            raise SyntaxError(op.getText()+"is not a valid operator")
    
    def visitRelatExpr(self, ctx: GopherParser.RelatExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        if isinstance(left, list):
            left = fmt.pythonify_lis(left)
        if isinstance(right, list):
            right = fmt.pythonify_lis(right)
        op = ctx.op.type
        if op == GopherParser.LT:
            return {'val': left < right, 'type': 'bool'}
        elif op == GopherParser.LTEQ:
            return {'val': left <= right, 'type': 'bool'}
        elif op == GopherParser.GT:
            return {'val': left > right, 'type': 'bool'}
        elif op == GopherParser.GTEQ:
            return {'val': left >= right, 'type': 'bool'}
        else:
            raise SyntaxError(op.getText()+"is not a valid operator")
    
    def visitEqExpr(self, ctx: GopherParser.EqExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        op = ctx.op.type
        if op == GopherParser.EQ:
            return {'val': left == right, 'type': 'bool'}
        elif op == GopherParser.NEQ:
            return {'val': left != right, 'type': 'bool'}
        else:
            raise SyntaxError(str(op)+"is not a valid operator")
    
    def visitAndExpr(self, ctx: GopherParser.AddExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        return {'val': left & right}
    
    def visitOrExpr(self, ctx: GopherParser.OrExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        return \
            {'val': left | right,
             'type':
             'bool' if ((type(left) == bool) & (type(right) == bool)) \
             else 'float'}
    
    def visitPrint0(self, ctx: GopherParser.Print0Context):
        val = self.visit(ctx.expr())
        try:
            rc = fmt.printitem(val, end='')
            if rc == 12:
                t = 0
                try:
                    t = self.memory['this']
                except:
                    pass
                self.memory['this'] = val
                self.visit(val['__print']['call']['block'])
                self.memory.pop('this')
                try:
                    assert t != 0
                    self.memory['this'] = t
                except:
                    pass
        except (TypeError, KeyError):
            print(val[0], end='')
        except (TypeError, IndexError, KeyError):
            print(val, end='')
        return val
    
    def visitPrintln(self, ctx: GopherParser.PrintlnContext):
        val = self.visit(ctx.expr())
        try:
            rc = fmt.printitem(val, end='\n')
            if rc == 12:
                t = 0
                try:
                    t = self.memory['this']
                except:
                    pass
                self.memory['this'] = val
                self.visit(val['__print']['call']['block'])
                self.memory.pop('this')
                try:
                    assert t != 0
                    self.memory['this'] = t
                except:
                    pass

        except (TypeError, KeyError):
            print(val[0])
        except (TypeError, IndexError, KeyError):
            print(val)
        return val
    
    def visitValueExpr(self, ctx: GopherParser.ValueExprContext):
        return self.visit(ctx.value())

    def visitKey(self, ctx: GopherParser.KeyContext):
        input()
        return None
    
    def visitInputExpr(self, ctx: GopherParser.InputExprContext):
        fmt.printitem(self.visit(ctx.expr()), end='')
        return {'val': input(), 'type': 'str'}
    
    def visitIf_stmt(self, ctx: GopherParser.If_stmtContext):
        conditions = ctx.condition_block()
        evalt = False
        retval = {'val': None, 'type': 'null'}
        for condition in conditions:
            if self.visit(condition.expr())['val']:
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
        retval = {'val': None, 'type': 'null'}
        val = self.visit(ctx.expr())['val']
        while val:
            retval = self.visit(ctx.stmt_block())
            if isinstance(retval, tuple):
                return retval
            val = self.visit(ctx.expr())['val']
        return retval
    
    def visitUntil_stmt(self, ctx: GopherParser.Until_stmtContext):
        retval = {'val': None, 'type': 'null'}
        val = self.visit(ctx.expr())['val']
        while not val:
            retval = self.visit(ctx.stmt_block())
            if isinstance(retval, tuple):
                return retval
            val = self.visit(ctx.expr())['val']
        return retval
    
    def visitListAtom(self, ctx: GopherParser.ListAtomContext):
        lis = ctx.list_var().expr()
        ret = []
        for expr in lis:
            ret.append(self.visit(expr))
        return {'val': ret, 'type': 'list'}

    def visitListspaceAtom(self, ctx: GopherParser.ListspaceAtomContext):
        exprlis = ctx.linspace().expr()
        val = list(np.linspace(
                                self.visit(exprlis[1])['val'],
                                self.visit(exprlis[2])['val'],
                                self.visit(exprlis[0])['val']))
        val = list(map(lambda x: {'val': x, 'type': 'float'}, val))
        return {'val': val, 'type': 'list', 'dtype': 'float'}

    def visitSinglFor(self, ctx: GopherParser.SinglForContext):
        retval = {'val': None, 'type': 'null'}
        var = str(ctx.ID())
        lis = self.visit(ctx.expr())
        if ctx.type_name() is not None:
            dt = self.visit(ctx.type_name())
        else:
            dt = 'any'
        for val in lis['val']:
            fncalls.assgn(self, val, var, dt)
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
        if ctx.type_name() is not None:
            rtype = self.visit(ctx.type_name())
        else:
            rtype = 'any'
        funcdata = ctx.ID()
        funcid = str(funcdata[0])
        varlist = []
        for varid in funcdata[1:]:
            varlist.append(str(varid))
        namedvarlist = dict()
        for op_arg in ctx.var():
            namedvarlist[str(op_arg.ID())] = self.visit(op_arg.expr())
        self.memory[funcid] = {'call':
                               {'varlist':
                                varlist,
                                'block':
                                ctx.stmt_block(),
                                'namedvarlist':
                                namedvarlist},
                               'rtype': rtype,
                               'type': 'function'}
        return self.memory[funcid]
    
    def visitDef_func_expr(self, ctx: GopherParser.Def_func_exprContext):
        funcdata = ctx.ID()
        varlist = []
        for varid in funcdata:
            varlist.append(str(varid))
        namedvarlist = dict()
        for op_arg in ctx.var():
            namedvarlist[str(op_arg.ID())] = self.visit(op_arg.expr())
        return {'call':
                {'varlist':
                 varlist,
                 'block':
                 ctx.stmt_block(),
                 'namedvarlist':
                 namedvarlist},
                'type': 'function'}
    
    def visitFileouts(self, ctx: GopherParser.FileoutsContext):
        exprlis = ctx.expr()
        val = self.visit(exprlis[0])['val']
        filename = self.visit(exprlis[1])
        mode = self.visit(exprlis[2])['val']
        if mode in ('w', 'a', 'x'):
            fil = open(filename['val'], mode)
            fil.write(str(val))
        else:
            print(f"{mode} is an invalid write mode")
        return filename
    
    def visitId_call(self, ctx: GopherParser.Id_callContext):
        if ctx.exprID() != None:
            data = self.visit(ctx.exprID())
            rt = data['rtype']

        elif ctx.recID() != None:
            data = self.visit(ctx.recID())
            rt = data['rtype']
            self.memory['this'] = data['parent']
            data = data['call']
        else:
            data = self.memory[str(ctx.ID())]
            rt = data['rtype']
            self.memory['this'] = data
            data = data['call']
        poplist = data['varlist']+list(data['namedvarlist'].keys())
        exprlis = []
        for expr in ctx.expr():
            exp = self.visit(expr)
            #print(exp)
            exprlis.append(exp)
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
        for vid in poplist[:len(poplist)-1]:
            self.memory.pop(vid)
        try:
            self.memory.pop('this')
        except KeyError:
            pass
        if isinstance(retval, tuple):
            return (
                fncalls.cnvrt(self, retval[0], rt) if rt != 'any' else retval[0]
                )
        else:
            return (
                fncalls.cnvrt(self, retval, rt) if rt != 'any' else retval
            )
    
    def visitId_callExpr(self, ctx: GopherParser.Id_callExprContext):
        return self.visit(ctx.id_call())
    
    def visitStmt_block(self, ctx: GopherParser.Stmt_blockContext):
        return self.visit(ctx.block())

    def visitExt_call(self, ctx: GopherParser.Ext_callContext):
        func = ''
        val, err = None, None
        if ctx.recID() is not None:
            ids = ctx.recID().ID()
            func = self.memory[str(ids[0])]['val']
            for vid in ids[1:]:
                func = func.__dict__[str(vid)]
        else:
            func = self.visit(ctx.ID())
        evalstr = 'func('
        exprlis = ctx.expr()
        if len(exprlis):
            evalstr += str(self.visit(exprlis[0])['val'])
            for expr in exprlis[1:]:
                evalstr += ',' + str(self.visit(expr)['val'])
        try:
            val = eval(evalstr + ')')
        except BaseException as e:
            err = e.args
        return {'val': [
                {'val': val, 'type': 'any'},
                {'val': err, 'type': 'any'}
                ],
                'type': 'list'}
        
    def visitBlock(self, ctx: GopherParser.BlockContext):
        retval = {'val': None, 'type': 'null'}
        for stmt in ctx.stmt():
            if stmt.return_stmt() != None:
                return (self.visit(stmt.return_stmt().expr()),)
            else:
                retval = self.visit(stmt)
                if isinstance(retval, tuple):
                    return retval
        return retval

    def visitDecl(self, ctx: GopherParser.DeclContext):
        vid = self.visit(ctx.recID())
        val = self.visit(ctx.expr())
        if val['const']:
            raise TypeError('can\'t assign to const')
        vid['val'] = val['val']
        vid['type'] = val['type']
        return val

    def visitClass_stmt(self, ctx: GopherParser.Class_stmtContext):
        cid = str(ctx.ID(0))
        extendeds = []
        if ctx.EID is not None:
            extendeds = ctx.EID()
        varbls = ctx.var()
        temp = self.memory
        self.memory = dict()
        for var in varbls:
            self.visit(var)
        temp[cid].update(self.memory)
        temp[cid]["vars"] = self.memory
        self.memory = temp
    
    def visitImpl_stmt(self, ctx: GopherParser.Impl_stmtContext):
        cid = str(ctx.ID())
        varbls = ctx.def_func_stmt()
        temp = self.memory
        self.memory = dict()
        for var in varbls:
            self.visit(var)
        try:
            self.memory['call'] = self.memory['__call']['call']
        except KeyError:
            pass
        temp[cid].update(self.memory)
        self.memory = temp
    
    def visitClass_inst(self, ctx: GopherParser.Class_instContext):
        exprlis = []
        if ctx.recID() is not None:
            dat = self.visit(ctx.recID())
            nm = str(ctx.recID().ID()[-1])
        else:
            dat = self.memory[str(ctx.ID())]
            nm = str(ctx.ID())
        vardat = dict(dat)
        vardat.pop("vars")
        for expr in ctx.expr():
            exprlis.append(self.visit(expr))
        for k, v in zip(dat['vars'], exprlis):
            if (dat['vars'][k]['type'] == v['type']) or (dat['vars'][k]['type'] == 'any'):
                vardat[k] = v
            else:
                vardat[k] = {
                            'val': ftype[dat['vars'][k]['type']](v['val']),
                            'type': dat['vars'][k]['type']
                }
        try:
            vardat["call"] = vardat["__call"]["call"]
        except: 
            pass
        vardat["val"] = "object@"+str(tid(vardat))
        vardat["type"] = nm
        return vardat
    
    def visitExpnumberAtom(self, ctx: GopherParser.ExpnumberAtomContext):
        num = str(ctx.EXPDECIMAL())
        return {'val': float(num), 'type': 'float'}

    def visitSwitch_stmt(self, ctx: GopherParser.Switch_stmtContext):
        pattern = self.visit(ctx.expr())
        matches = ctx.condition_block()
        elseblck = ctx.stmt_block()
        for match in matches:
            res = self.visit(match.expr())
            if res["type"] == "list":
                if pattern in res['val']:
                    try:
                        return self.visit(match.stmt_block())[0]
                    except KeyError:
                        return self.visit(match.stmt_block())
            else:
                if res == pattern:
                    try:
                        return self.visit(match.stmt_block())[0]
                    except KeyError:
                        return self.visit(match.stmt_block())
        else:
            if elseblck is not None:
                try:
                    return self.visit(elseblck)[0]
                except:
                    return self.visit(elseblck)
            else:
                return {'val': None, 'type': 'null'}

    def visitXorExpr(self, ctx: GopherParser.XorExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        if (type(left) == bool) and (type(right) == bool):
            return {'val': left ^ right, "type": "bool"}
        else:
            return {'val': int(left) ^ int(right), 'type': 'float'}
    
    def visitContainsExpr(self, ctx: GopherParser.ContainsExprContext):
        left = self.visit(ctx.expr(0))['val']
        right = self.visit(ctx.expr(1))['val']
        return {'val': left in right, 'type': 'bool'}

    def visitListIndexExpr(self, ctx: GopherParser.ListIndexExprContext):
        lis = self.visit(ctx.expr(0))
        indxs = self.visit(ctx.expr(1))
        if indxs['type'] == 'list':
            ret = []
            for indx in indxs['val']:
                ret.append(lis['val'][int(indx['val'])])
            return {'val': ret, 'type': 'list'}
        else:
            return lis['val'][int(indxs['val'])]
    
    def visitListSliceExpr(this, ctx: GopherParser.ListSliceExprContext):
        lis = this.visit(ctx.expr(0))
        start, end = int(this.visit(ctx.expr(1))['val']), \
            int(this.visit(ctx.expr(2))['val'])
        return {'val': lis['val'][start:end], 'type': 'list'}
    
    def visitNovalVar(self, ctx: GopherParser.NovalVarContext):
        dt = ctx.DT()
        ids = ctx.ID()
        for vid in ids:
            self.memory[str(vid)] = {'val': GopherTypes.GopherNoVal(),
                                     "type": str(dt)}

    def visitNovalClass(self, ctx: GopherParser.NovalClassContext):
        f1 = False
        ids = ctx.ID()
        if ctx.recID() is not None:
            dat = self.visit(ctx.recID())
            nm = str(ctx.recID().ID()[-1])
        else:
            dat = self.memory[str(ids[0])]
            nm = str(ids[0])
            f1 = True
        vardat = dict(dat)
        vardat.pop("vars")
        for k in dat["vars"]:
            vardat[k] = GopherTypes.GopherNoVal()
        vardat["val"] = GopherTypes.GopherNoVal()
        vardat["type"] = nm
        for vid in (ids[1:] if f1 else ids):
            self.memory[str(vid)] = vardat
    
    def visitAppendExpr(self, ctx: GopherParser.AppendExprContext):
        left = list(self.visit(ctx.expr(0))['val'])
        right = self.visit(ctx.expr(1))
        left.append(right)
        return {'val': left, 'type': 'list'}
    
    def visitTypeOfExpr(self, ctx: GopherParser.TypeOfExprContext):
        typ = self.visit(ctx.expr())['type']
        return {'val': typ, 'type': 'str'}
    
    def visitMultAssgn(self, ctx: GopherParser.MultAssgnContext):
        vid = str(ctx.ID())
        right = self.visit(ctx.expr())['val']
        op = ctx.op.type
        left = self.memory[vid]['val']
        if op == GopherParser.MULTEQ:
            if isinstance(left, (str, list)):
                prod = {'val': int(right) * left,
                        'type': ('str' if type(left) == str else 'list')}
            elif isinstance(right, (str, list)):
                prod = {'val': int(left) * right,
                        'type': ('str' if type(right) == str else 'list')}
            else:
                prod = {'val':  left * right, 'type': 'float'}
        elif op == GopherParser.DIVEQ:
            prod = {'val':  left / right, 'type': 'float'}
        elif op == GopherParser.MODEQ:
            prod = {'val':  left % right, 'type': 'float'}
        else:
            raise SyntaxError(op.getText()+"is not an operator")
        self.memory[vid] = prod
    
    def visitAddAssgn(self, ctx: GopherParser.AddAssgnContext):
        vid = str(ctx.ID())
        right = self.visit(ctx.expr())['val']
        op = ctx.op.type
        left = self.memory[vid]['val']
        if op == GopherParser.PLUSEQ:
            if isinstance(left, (str)) or isinstance(right, str):
                sm = {'val': str(left) + str(right), 'type': 'str'}
            else:
                sm = {'val': left + right,
                        'type':
                        ('float' if type(left + right) != list else 'list')}
        elif op == GopherParser.MINUSEQ:
            sm = {'val': float(left)-float(right), 'type': 'float'}
        else:
            raise SyntaxError(op.getText()+"is not a valid operator")
        self.memory[vid] = sm
    
    def visitPowAssgn(self, ctx: GopherParser.PowAssgnContext):
        vid = str(ctx.ID())
        right = self.visit(ctx.expr())['val']
        left = self.memory[vid]['val']
        self.memory[vid] = {'val': float(left)**float(right), 'type': 'float'}
    
    def visitPopandAssgn(self, ctx: GopherParser.PopandAssgnContext):
        vid = str(ctx.ID())
        right = self.visit(ctx.expr())
        self.memory[vid] = right['val'].pop()
    
    def visitAppendAssgn(self, ctx: GopherParser.AppendAssgnContext):
        vid = str(ctx.ID())
        left = list(self.memory[vid]['val'])
        right = self.visit(ctx.expr())
        left.append(right)
        self.memory[vid] = {"val": left, "type": "list"}
    
    def visitMultivar(self, ctx: GopherParser.MultivarContext):
        ids = ctx.ID()
        values = list(self.visit(ctx.expr())['val'])
        if len(ids) > len(values):
            raise Exception("lesser values than variables")
        for id in (ids[:-2] if len(values) > len(ids) else ids):
            id = str(id)
            value, values = values[0], values[1:]
            dt = ''
            if ctx.DT() != None:
                dt = str(ctx.DT())
            else:
                try:
                    dt = self.memory[id]['type']
                except:
                    dt = 'any'
            fncalls.assgn(self, value, id, dt)
        if len(values) > len(ids):
            id = str(ids[-1])
            value = {'val': values, 'type': 'list'}
            dt = ''
            if ctx.DT() != None:
                dt = str(ctx.DT())
            else:
                try:
                    dt = self.memory[id]['type']
                except:
                    dt = 'any'
            fncalls.assgn(self, values, id, dt)
    
    def visitExit(self, ctx: GopherParser.ExitContext):
        exit(int(self.visit(ctx.expr())['val']))
    
    def visitTypeCastExpr(self, ctx: GopherParser.TypeCastExprContext):
        val = dict(self.visit(ctx.expr()))
        dt = str(ctx.DT())
        return fncalls.cnvrt(self, value, dt)
    
    def visitLen_expr(self, ctx: GopherParser.Len_exprContext):
        val = self.visit(ctx.expr())
        return {'val': float(len(val['val'])), 'type': 'float'}

    def visitStrcnvrtExpr(self, ctx: GopherParser.StrcnvrtExprContext):
        val = self.visit(ctx.expr())
        return fncalls.cnvrt(self, val, 'str')
    
    def visitPrefixOpExpr(self, ctx: GopherParser.PrefixOpExprContext):
        op = str(ctx.OPERATOR())
        val = self.visit(ctx.expr())
        t1 = val['type']
        mid = op + ',' + t1
        try:
            blck = self.memory[mid]
        except KeyError:
            blck = self.memory[op]
        self.memory['value'] = val
        res = self.visit(blck)
        if isinstance(res, tuple):
            return res[0]
        else:
            return res
    
    def visitBinOpExpr(self, ctx: GopherParser.BinOpExprContext):
        op = str(ctx.OPERATOR())
        lef, rig = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        t1, t2 = lef['type'], rig['type']
        mid = op + ',' + t1 + ',' + t2
        try:
            blck = self.memory[mid]
        except KeyError:
            blck = self.memory[op]
        self.memory['left'], self.memory['right'] = lef, rig
        res = self.visit(blck)
        if isinstance(res, tuple):
            return res[0]
        else:
            return res
    
    def visitType_name(self, ctx: GopherParser.Type_nameContext):
        if ctx.DT() is not None:
            return str(ctx.DT())
        elif ctx.ID() is not None:
            return str(ctx.ID())
        else:
            return str(ctx.recID().ID()[-1])
    
    def visitBin_op_def_stmt(self, ctx: GopherParser.Bin_op_def_stmtContext):
        op = str(ctx.OPERATOR())
        t1 = self.visit(ctx.type_name(0))
        t2 = self.visit(ctx.type_name(1))
        if t1 == 'any' or t2 == 'any':
            mid = op
        else:
            mid = op+','+t1+','+t2
        self.memory[mid] = ctx.stmt_block()
    
    def visitPrfix_op_def_stmt(self, ctx: GopherParser.Prfix_op_def_stmtContext):
        op = str(ctx.OPERATOR())
        t1 = self.visit(ctx.type_name())
        if t1 == 'any':
            mid = op
        else:
            mid = op+','+t1
        self.memory[mid] = ctx.stmt_block()
    
    def visitMultFor(self, ctx: GopherParser.MultForContext):
        retval = {'val': None, 'type': 'null'}
        vars = ctx.ID()
        lis = self.visit(ctx.expr())
        for val in lis['val']:
            for i, var in enumerate(vars):
                fncalls.assgn(self, val['val'][i], str(var), 'any')
            retval = self.visit(ctx.stmt_block())
            if isinstance(retval, tuple):
                return retval
        return retval
    

if __name__ == '__main__':
    import GopherCompiler
