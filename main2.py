import lur_lexer
import lur_parser
import lur_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = lur_lexer.BasicLexer()
    parser = lur_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('>> ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            lur_interpreter.BasicExecute(tree, env)
