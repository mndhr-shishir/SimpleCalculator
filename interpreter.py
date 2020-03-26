from tokens import TokenKind
import math


# More of a Parser/Interpreter
# Parses expression and interprets it at the same time ( without creating AST's)
class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, tokenKind):
        if self.current_token.kind == tokenKind:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception('Invalid Syntax!')

    def factor(self):
        token = self.current_token

        # resolve unary operation
        unary_op_resolve = 1
        unary_op_token_kinds = [TokenKind.PLUS, TokenKind.MINUS]

        while token.kind in unary_op_token_kinds:
            self.eat(token.kind)

            if token.kind == TokenKind.PLUS:
                unary_op_resolve *= 1
            else:
                unary_op_resolve *= -1

            token = self.current_token

        # get the whole number
        self.eat(TokenKind.INTEGER)
        whole_number = int(token.value)

        # append decimal values if they exist
        decimal_value = 0
        if self.current_token.kind == TokenKind.DOT:
            self.eat(TokenKind.DOT)

            token = self.current_token
            self.eat(TokenKind.INTEGER)

            # convert whole number(s) into decimal value(s)
            length        = len(token.value)
            decimal_value = int(token.value) / math.pow(10, length)

        # finally return the parsed number
        return (unary_op_resolve * (whole_number + decimal_value))

    def term(self):
        result = self.factor()

        op_token_kinds = [TokenKind.MULT, TokenKind.DIV]

        while self.current_token.kind in op_token_kinds:
            token = self.current_token

            self.eat(token.kind)

            if token.kind == TokenKind.MULT:
                result *= self.factor()
            else:
                result /= self.factor()

        return result

    def expr(self):
        result = self.term()

        op_token_kinds = [TokenKind.PLUS, TokenKind.MINUS]

        while self.current_token.kind in op_token_kinds:
            token = self.current_token

            self.eat(token.kind)

            if token.kind == TokenKind.PLUS:
                result += self.term()
            else:
                result -= self.term()

        return result

    def interpret(self):
        return self.expr()

