grammar Gopher;
program: block EOF;
block: (stmt)*;
stmt:
	incl_stmt (';')?
	| load_stmt (';')?
	| var (';')?
	| multivar (';')?
	| decl (';')?
	| class_stmt
	| impl_stmt
	| print_stmt (';')?
	| key (';')?
	| exit (';')?
	| preproc
	| if_stmt
	| while_stmt
	| until_stmt
	| for_stmt
	| switch_stmt
	| label_def
	| def_func_stmt
	| bin_op_def_stmt
	| prfix_op_def_stmt
	| id_call (';')?
	| ext_call (';')?
	| goto_stmt (';')?
	| return_stmt (';')?
	| expr (';')?
	| assexpr (';')?;
key: 'key';
exit: 'exit' expr;
preproc: '~#' .* '~';
var: (
		(ID (':' type_name)? CONSTASSIGN expr)
		| ((VAR)? ID (':' type_name)? '=' expr)
		| (expr ASSIGN (type_name ':')? ID)
	)											# valdVar
	| '@' DT ID (',' ID)*						# novalVar
	| '@' (CLASS)? (ID | recID) ID (',' ID)*	# novalClass;
multivar: (ID (',' ID)+ (COL)? (DT)? '=' expr)
	| (expr ASSIGN (DT)? (COL?) ID (',' ID)+);
assexpr:
	ID POWEQ expr							# powAssgn
	| ID op = (MULTEQ | DIVEQ | MODEQ) expr	# multAssgn
	| ID op = (PLUSEQ | MINUSEQ) expr		# addAssgn
	| ID APPENDEQ expr						# appendAssgn
	| expr POP ID							# popandAssgn
	| expr '[' expr ']' '=' expr			# indexAssgn;
decl: recID '=' expr;
print_stmt:
	PRINT expr				# print0
	| PRINTLN expr			# println
	| OUTS expr expr expr	# fileouts;
label_def: LABEL ID stmt_block;
goto_stmt: GOTO ID;
class_stmt: CLASS ID (UNDER (EID = ID)+)? OBRACE var* CBRACE;
impl_stmt: 'impl' ID OBRACE def_func_stmt* CBRACE;
class_inst: (ID | recID) OBRACE (expr (',' expr)*)? CBRACE;
def_func_stmt:
	FUNCTION type_name? (FUNCID = ID) OPAR (ID (',' ID)*)? (
		(',' var)*
	)? CPAR stmt_block;
def_func_expr:
	'|' (ID (',' ID)*)? ((',' var)*)? '|' '=>' stmt_block;
type_name: DT | ID | recID;
bin_op_def_stmt:
	OP OPERATOR XFX type_name ',' type_name stmt_block;
prfix_op_def_stmt: OP OPERATOR FX type_name stmt_block;
id_call: (
		(ID | recID | exprID) /* REF_OP*/ OPAR (expr (',' expr)*)? CPAR
	)
	| (
		('.' expr '.') (ID | recID | exprID) (
			/* REF_OP*/ OPAR (expr (',' expr)*)? CPAR
		)?
	);
ext_call: EXTCALL OPAR (expr (',' expr)*)? CPAR (ID | recID);
recID: ID (REF_OP ID)+;
exprID: OPAR expr CPAR REF_OP (ID | recID);
value:
	OPAR expr CPAR			# parExpr
	| DECIMAL				# numberAtom
	| EXPDECIMAL			# expnumberAtom
	| BOOL					# boolAtom
	| (ID | recID | exprID)	# idAtom
	| STRING				# stringAtom
	| list_var				# listAtom
	| linspace				# listspaceAtom
	| NULL					# nullAtom;
expr:
	DT OBRACE expr CBRACE										# typeCastExpr
	| INPUT expr												# inputExpr
	| switch_stmt												# switchExpr
	| ext_call													# ext_callExpr
	| id_call													# id_callExpr
	| class_inst												# class_instExpr
	| def_func_expr												# def_funcExpr
	| len_expr													# lenExpr
	| expr '[' expr ']'											# listIndexExpr
	| expr '[' expr COL expr ']'								# listSliceExpr
	| <assoc = right>expr POW expr								# powExpr
	| MINUS expr												# uminusExpr
	| NOT expr													# unotExpr
	| expr op = (MULT | DIV | MOD) expr							# multExpr
	| expr op = (PLUS | MINUS) expr								# addExpr
	| expr APPEND expr											# appendExpr
	| expr op = (LTEQ | GTEQ | LT | GT) expr					# relatExpr
	| expr op = (EQ | NEQ) expr									# eqExpr
	| expr AND expr												# andExpr
	| expr OR expr												# orExpr
	| expr XOR expr												# xorExpr
	| expr IN expr												# containsExpr
	| expr OPERATOR expr										# binOpExpr
	| OPERATOR expr												# prefixOpExpr
	| TYPEOF expr												# typeOfExpr
	| condexpr = expr '?' truexpr = expr ':' falsexpr = expr	# tern_opExpr
	| '`' expr '`'												# strcnvrtExpr
	| value														# valueExpr;
len_expr: LEN expr;
incl_stmt: INCLUDE (ID | recID);
load_stmt: LOAD (ID | recID);
for_stmt:
	FOR (type_name)? ID OF expr stmt_block	# singlFor
	| FOR ID (',' ID)+ OF expr stmt_block	# multFor;
switch_stmt:
	SWITCH expr OBRACE condition_block* CBRACE (ELSE stmt_block)?;
until_stmt: UNTIL expr stmt_block;
while_stmt: WHILE expr stmt_block;
if_stmt:
	IF condition_block ((ELSE IF | ELSIF) condition_block)* (
		ELSE stmt_block
	)?;
condition_block: expr stmt_block;
stmt_block: OBRACE block CBRACE | '\t' stmt;
return_stmt: RET expr;
DT: 'float' | 'str' | 'bool' | 'list' | 'any';
LEN: 'len';
COL: ':';
PRINT: 'print';
OUTS: 'outs';
INCLUDE: 'incl';
LOAD: 'load';
EXTCALL: 'extcall';
PRINTLN: 'println';
INPUT: 'gets' | 'input';
FUNCTION: 'fn';
RET: 'ret';
LABEL: 'label';
CLASS: 'type';
UNDER: 'under';
GOTO: 'goto';
VAR: 'var';
IF: 'if';
ELSE: 'else';
ELSIF: 'elsif';
UNTIL: 'until';
WHILE: 'while';
FOR: 'for';
SWITCH: 'switch';
list_var: '[' (expr (',' expr)*)? ']';
linspace: 'l[' expr ',' expr ':' expr ']';
BOOL: (TRUE | FALSE);
DECIMAL: [0-9]+ ('.' [0-9]*)? | '.' [0-9]+;
EXPDECIMAL: DECIMAL 'e' ('+' | '-') [0-9]+;
TRUE: 'true';
FALSE: 'false';
NULL: 'null';
TYPEOF: 'typeof';
REF_OP: '::';
OP: 'op';
XFX: 'xfx';
FX: 'fx';
OR: 'or';
XOR: 'xor';
IN: 'in';
OF: 'of';
AND: ('and' | '&');
EQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
GTEQ: '>=';
LTEQ: '<=';
POW: '**';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%' | 'rem';
NOT: 'not';
ASSIGN: '->';
APPEND: '<-';
POP: '=>';
CONSTASSIGN: 'is';
POWEQ: '**=';
PLUSEQ: '+=';
MINUSEQ: '-=';
MULTEQ: '*=';
DIVEQ: '/=';
MODEQ: '%=';
APPENDEQ: '<-=';
OPAR: '(';
CPAR: ')';
OBRACE: '{';
CBRACE: '}';
STRING: ('"' (~["\n\r] | ESCAPE)* '"')
	| ('\'' (~["\n\r] | ESCAPE)* '\'');
ESCAPE: '\\' .;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
OPERATOR: ('$' | '^' | '%%' | '@@' | '&&' | '<<' | '>>') (
		(~[ \t\r\n])*
	)?;
COMMENT: ('#' ~[\r\n]* | '#*' .* '*#') -> skip;
WS: [ \t\n\r]+ -> skip;