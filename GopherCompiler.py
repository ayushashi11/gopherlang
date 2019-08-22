from antlr4 import *
from GopherLexer import GopherLexer
from GopherParser import GopherParser
from Gophisitor import Gophisitor
import fmt
import sys
if len(sys.argv) > 1 and sys.argv[1] == '-c':
    lexer = GopherLexer(InputStream(input('>>')))
elif len(sys.argv) > 1 and\
                (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print('Gopher Interpreter\n' +
          'usage: Comp.py [Options] {file}\n' +
          '[Options]:\n' +
          '-c              Run a command\n' +
          '-h              Show this help\n' +
          'NO OPTIONS      run from a .gopr file')
    exit(0)
elif len(sys.argv) > 1:
    lexer = GopherLexer(FileStream(sys.argv[1]))
else:
    lexer = GopherLexer(FileStream('d:/games/lang_hello/Gopher/test2.gopr'))
stream = CommonTokenStream(lexer)
parser = GopherParser(stream)
tree = parser.program()
gophisitor = Gophisitor()
val = gophisitor.visit(tree)
if fmt.printitem(val) == 12:
    print(val)
