from enum import Enum


class TokenKind(Enum):
    INTEGER = 0
    PLUS    = 1
    MINUS   = 2
    MULT    = 3
    DIV     = 4
    DOT     = 5
    LPAREN  = 6
    RPAREN  = 7
    EOF     = 8


class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __str__(self):
        return f'[{self.kind.name}, {self.value}]'

    def __repr__(self):
        return self.__str__()
