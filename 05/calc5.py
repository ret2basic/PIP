class Token:
    def __init__(self, type, value):
        # Token type: INTEGER, PLUS, MINUS, MUL, DIV, or EOF
        self.type = type
        # Token value: non-negative integer value, '+', '-', '*', '/', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()

class Lexer:
    def __init__(self, text):
        # client string input, e.g. "3 * 5", "12 / 3 * 4", etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char:
                if self.current_char.isspace():
                    self.skip_whitespace()
                    continue
                elif self.current_char.isdigit():
                    # No self.advance() here. It was invoked in self.integer().
                    return Token('INTEGER', self.integer())
                elif self.current_char == '+':
                    self.advance()
                    return Token('PLUS', '+')
                elif self.current_char == '-':
                    self.advance()
                    return Token('MINUS', '-')
                elif self.current_char == '*':
                    self.advance()
                    return Token('MUL', '*')
                elif self.current_char == '/':
                    self.advance()
                    return Token('DIV', '/')
                else:
                    self.error()
        
        return Token('EOF', None)

class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        # Set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        self.eat('INTEGER')
        return token.value

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.type in ('MUL', 'DIV'):
            token = self.current_token
            if token.type == 'MUL':
                self.eat('MUL')
                result *= self.factor()
            elif token.type == 'DIV':
                self.eat('DIV')
                result //= self.factor()

        return result

    def expr(self):
        """Arithmetic expression parser / interpreter.

        calc>  14 + 2 * 3 - 6 / 2
        17

        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER
        """
        result = self.term()

        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
                result += self.term()
            elif token.type == 'MINUS':
                self.eat('MINUS')
                result -= self.term()

        return result

if __name__ == '__main__':
    # REPL
    while True:
        # Print prompt and record user input
        try:
            text = input('calc> ')
        except EOFError:
            break
        if text == 'exit':
            exit()
        if not text:
            continue
        # Interpret and print user input
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)
