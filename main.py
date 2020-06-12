import lur_lexer
import lur_parser
import lur_interpreter

from sys import *

#DENGAN MASUKAN .px
lexer = lur_lexer.BasicLexer()
parser = lur_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    lur_interpreter.BasicExecute(tree, env)
