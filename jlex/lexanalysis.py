from jlex.lexer import lex_source_file
from jlex.type import Type

tokens = lex_source_file('Example.java')

for token in tokens:
    if token.type not in [Type.SPACE, Type.NEW_LINE]:
        print(token)
