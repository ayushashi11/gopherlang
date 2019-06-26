grammar Gopher;
program: block EOF;
block:(stmt)*;
stmt:incl_stmt ';'
|load_stmt ';'
|var ';'
|print_stmt ';'
|key ';'
|preproc
|if_stmt
|while_stmt
|until_stmt
|for_stmt
|label_def
|def_func_stmt
|id_call';'
|ext_call ';'
|goto_stmt';'
|return_stmt ';'
|expr ';';
key: 'key';
var: (VAR ID (ASSIGN|CONSTASSIGN) expr)|(ID '=' expr);
preproc:'$#\n' '\t'block '\n#$';//TODO:implement preprocessing
print_stmt: PRINT expr #print0
|PRINTLN expr #println;
label_def:LABEL ID stmt_block;
goto_stmt:GOTO ID;
def_func_stmt:FUNCTION FUNCID=ID OPAR (ID(','ID)*)?((','NID=ID '=' value)*)? CPAR stmt_block;
id_call: (ID|recID) REF_OP OPAR (expr(','expr)*) CPAR;
ext_call: EXTCALL OPAR (expr(','expr)*) CPAR (ID|recID);
recID: ID (REF_OP ID)+;
value:OPAR expr CPAR #parExpr
|DECIMAL #numberAtom
|BOOL #boolAtom
|(ID|recID) #idAtom
|STRING #stringAtom
|list_var #listAtom
|NULL #nullAtom
;
expr:<assoc=right>INPUT expr #inputExpr
|expr POW expr #powExpr
|MINUS expr #uminusExpr
|NOT expr #unotExpr
|expr op=(MULT|DIV|MOD) expr #multExpr
|expr op=(PLUS|MINUS) expr #addExpr
|expr op=(LTEQ|GTEQ|LT|GT) expr #relatExpr
|expr op=(EQ|NEQ) expr #eqExpr
|expr AND expr #andExpr
|expr OR expr #orExpr
|condexpr=expr '?' truexpr=expr ':' falsexpr=expr #tern_opExpr
|id_call #id_callExpr
|ext_call #ext_callExpr
|value #valueExpr
;
incl_stmt:INCLUDE (ID|recID);
load_stmt:LOAD (ID|recID);
for_stmt:FOR ID COL expr stmt_block;
until_stmt:UNTIL expr stmt_block;
while_stmt:WHILE expr stmt_block;
if_stmt:IF condition_block ((ELSE IF|ELSIF) condition_block)* (ELSE stmt_block)?;
condition_block:expr stmt_block;
stmt_block:OBRACE block CBRACE
|'\t'stmt
;
COL:':';
return_stmt:RET expr ;
PRINT: 'print'|'outs';
INCLUDE: 'incl';
LOAD: 'load';
EXTCALL: 'extcall';
PRINTLN: 'println';
INPUT: 'gets'|'input';
FUNCTION: 'function';
RET: 'ret';
LABEL: 'label';
GOTO: 'goto';
VAR: 'var';
IF: 'if';
ELSE:'else';
ELSIF: 'elsif';
UNTIL: 'until';
WHILE: 'while';
FOR: 'for';
list_var: '['expr(','expr)*']';
BOOL:(TRUE|FALSE);
DECIMAL: [0-9]+('.'[0-9]*)?
|'.' [0-9]+;
TRUE:'true';
FALSE:'false';
NULL:'null';
REF_OP:'::';
OR:'or';
AND:'and';
EQ:'==';
NEQ:'!=';
GT:'>';
LT:'<';
GTEQ:'>=';
LTEQ:'<=';
POW: '**';
PLUS:'+';
MINUS:'-';
MULT:'*';
DIV:'/';
MOD:'%'|'rem';
NOT:'not';
ASSIGN:'->';
CONSTASSIGN:'is';
OPAR:'(';
CPAR:')';
OBRACE:'{';
CBRACE:'}';
STRING:'"'~['"\n\r]*'"';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
COMMENT:('#' ~[\r\n]* | '#*' .* '*#')->skip;
WS: [ \t\n\r]+ -> skip;