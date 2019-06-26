import gen.*;
import jdk.nashorn.internal.runtime.regexp.joni.exception.SyntaxException;
import org.antlr.v4.runtime.misc.NotNull;
import java.util.*;
public class EvalVisitor extends GopherBaseVisitor<Value> {
    public static final double SMALL_VALUE=0.00000000001;
    private Map<String,Value> memory=new HashMap<>();
    private Scanner sc=new Scanner(System.in);
    @Override
    public Value visitVar(GopherParser.VarContext ctx) {
        String id=ctx.ID().getText();
        Value value=this.visit(ctx.expr());
        return memory.put(id,value);
    }

    @Override
    public Value visitIdAtom(GopherParser.IdAtomContext ctx) {
        String id=ctx.getText();
        Value value=memory.get(id);
        if(value==null){
            throw new RuntimeException("variable "+id+" has not yet been declared");
        }
        return value;
    }

    @Override
    public Value visitStringAtom(GopherParser.StringAtomContext ctx) {
        String str=ctx.getText();
        return new Value(str.substring(1,str.length()-1));
    }

    @Override
    public Value visitNumberAtom(GopherParser.NumberAtomContext ctx) {
        return new Value(Double.parseDouble(ctx.getText()));
    }

    @Override
    public Value visitBoolAtom(GopherParser.BoolAtomContext ctx) {
        return new Value(Boolean.parseBoolean(ctx.getText()));
    }

    @Override
    public Value visitNullAtom(GopherParser.NullAtomContext ctx) {
        return new Value(null);
    }

    @Override
    public Value visitParExpr(GopherParser.ParExprContext ctx) {
        return this.visit(ctx.expr());
    }

    @Override
    public Value visitPowExpr(GopherParser.PowExprContext ctx) {
        Value left=this.visit(ctx.expr(0));
        Value right=this.visit(ctx.expr(1));
        return new Value(Math.pow(left.toDouble(),right.toDouble()));
    }

    @Override
    public Value visitUminusExpr(GopherParser.UminusExprContext ctx) {
        Value value=this.visit(ctx.expr());
        return new Value(value.isDouble()?
        -value.toDouble():
                (value.isBool() ? !value.toBool() : reverse(value.toString())));
    }
    public String reverse(String inp){
        String ret="";
        for(int x=0;x<inp.length();x++){
            ret+=inp.charAt(inp.length()-x-1);
        }
        return ret;
    }
    public String ntimes(int times,String str){
        String ret="";
        for(int x=0;x<times;x++){
            ret.concat(str);
        }
        return ret;
    }
    @Override
    public Value visitUnotExpr(GopherParser.UnotExprContext ctx) {
        Value value=this.visit(ctx.expr());
        return new Value(!value.toBool());
    }

    @Override
    public Value visitMultExpr(@NotNull GopherParser.MultExprContext ctx) {
        Value left=this.visit(ctx.expr(0))
                ,right=this.visit(ctx.expr(1)),ret;
        switch (ctx.op.getType()){
            case GopherParser.MULT:
                ret=new Value(right.isDouble()?
                        left.toDouble()*right.toDouble():
                        ntimes((int)((double)left.toDouble()),right.toString()));
                break;
            case GopherParser.DIV:
                ret=new Value(left.toDouble()/right.toDouble());
                break;
            case GopherParser.MOD:
                ret=new Value(left.toDouble()%right.toDouble());
                break;
            default:
                throw new SyntaxException("unknown operator "+GopherParser.tokenNames[ctx.op.getType()]);
        }
        return ret;
    }

    @Override
    public Value visitAddExpr(@NotNull GopherParser.AddExprContext ctx) {
        Value left = this.visit(ctx.expr(0));
        Value right = this.visit(ctx.expr(1));

        switch (ctx.op.getType()) {
            case GopherParser.PLUS:
                return left.isDouble() && right.isDouble() ?
                        new Value(left.toDouble() + right.toDouble()) :
                        new Value(left.toString() + right.toString());
            case GopherParser.MINUS:
                return new Value(left.toDouble() - right.toDouble());
            default:
                throw new RuntimeException("unknown operator: " + GopherParser.tokenNames[ctx.op.getType()]);
        }
    }
        @Override
        public Value visitRelatExpr(@NotNull GopherParser.RelatExprContext ctx) {

            Value left = this.visit(ctx.expr(0));
            Value right = this.visit(ctx.expr(1));

            switch (ctx.op.getType()) {
                case GopherParser.LT:
                    return new Value(left.toDouble() < right.toDouble());
                case GopherParser.LTEQ:
                    return new Value(left.toDouble() <= right.toDouble());
                case GopherParser.GT:
                    return new Value(left.toDouble() > right.toDouble());
                case GopherParser.GTEQ:
                    return new Value(left.toDouble() >= right.toDouble());
                default:
                    throw new RuntimeException("unknown operator: " + GopherParser.tokenNames[ctx.op.getType()]);
            }
        }

        @Override
        public Value visitEqExpr(@NotNull GopherParser.EqExprContext ctx) {

            Value left = this.visit(ctx.expr(0));
            Value right = this.visit(ctx.expr(1));

            switch (ctx.op.getType()) {
                case GopherParser.EQ:
                    return left.isDouble() && right.isDouble() ?
                            new Value(Math.abs(left.toDouble() - right.toDouble()) < SMALL_VALUE) :
                            new Value(left.equals(right));
                case GopherParser.NEQ:
                    return left.isDouble() && right.isDouble() ?
                            new Value(Math.abs(left.toDouble() - right.toDouble()) >= SMALL_VALUE) :
                            new Value(!left.equals(right));
                default:
                    throw new RuntimeException("unknown operator: " + GopherParser.tokenNames[ctx.op.getType()]);
            }
        }

        @Override
        public Value visitAndExpr(GopherParser.AndExprContext ctx) {
            Value left = this.visit(ctx.expr(0));
            Value right = this.visit(ctx.expr(1));
            return new Value(left.toBool() && right.toBool());
        }

        @Override
        public Value visitOrExpr(GopherParser.OrExprContext ctx) {
            Value left = this.visit(ctx.expr(0));
            Value right = this.visit(ctx.expr(1));
            return new Value(left.toBool() || right.toBool());
        }

    @Override
    public Value visitPrint0(GopherParser.Print0Context ctx) {
        Value value=this.visit(ctx.expr());
        System.out.print(value);
        return value;
    }

    @Override
    public Value visitValueExpr(GopherParser.ValueExprContext ctx) {
        return this.visit(ctx.value());
    }

    @Override
    public Value visitPrintln(GopherParser.PrintlnContext ctx) {
        Value value=this.visit(ctx.expr());
        System.out.println(value);
        return value;
    }

    @Override
    public Value visitKey(GopherParser.KeyContext ctx) {
        sc.nextLine();
        return Value.VOID;
    }

    @Override
    public Value visitInputExpr(GopherParser.InputExprContext ctx) {
        Value value=this.visit(ctx.expr());
        System.out.print(value);
        return new Value(sc.nextLine());
    }
}



