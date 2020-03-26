from tokens import TokenKind, Token


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1

        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while (self.current_char is not None) and (self.current_char.isspace()):
            self.advance()

    def integer(self):
        final = ''

        while (self.current_char is not None) and (self.current_char.isdigit()):
            final += self.current_char
            self.advance()

        return final

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenKind.INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(TokenKind.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TokenKind.MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(TokenKind.MULT, '*')

            if self.current_char == '/':
                self.advance()
                return Token(TokenKind.DIV, '/')

            if self.current_char == '.':
                self.advance()
                return Token(TokenKind.DOT, '.')

            if self.current_char == '(':
                self.advance()
                return Token(TokenKind.LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(TokenKind.RPAREN, ')')

            raise Exception(f"Unrecognized character '{self.current_char}'!")

        return Token(TokenKind.EOF, None)

