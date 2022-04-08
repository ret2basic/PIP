INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EOF'

class Token():
    def __init__(self, type, value):
        # Token types: 'INTEGER', 'PLUS', or 'EOF'
        self.type = type
        # Token values: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
            Token(INTEGER, 5)
        """
        return f"Token({self.type}, {repr(self.value)})"

class Interpreter(object):
    def __init__(self, text):
        # The input string, e.g. "3+5"
        self.text = text
        # The "pointer"
        self.pos = 0
        # The current token. e.g. '3' or '+' or '5'
        self.current_token = None
        # The current character pointed by the "pointer"
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input.')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""

        self.pos += 1
        if self.pos > len(self.text) - 1:
            # Indicates end of input
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """If the current character is whitespace, advance."""

        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""

        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_next_token(self):
        """This is the tokenizer."""

        while self.current_char != None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            elif self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            elif self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            elif self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')
            elif self.current_char == '/':
                self.advance()
                return Token(DIVIDE, '/')
            else:
                self.error()

        # If the current character is None, return the EOF token.
        return Token(EOF, None)

    def eat(self, token_type):
        """Verify the current toke type and move to the next token."""
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        """Return an INTEGER token value."""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """Parsing and interpreting."""

        self.current_token = self.get_next_token()

        result = self.term()
        while self.current_token.type in (PLUS, MINUS, MULTIPLY, DIVIDE):
            token = self.current_token

            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
            elif token.type == MULTIPLY:
                self.eat(MULTIPLY)
                result = result * self.term()
            elif token.type == DIVIDE:
                self.eat(DIVIDE)
                try:
                    result = result / self.term()
                except ZeroDivisionError:
                    result = "The divisor must be non-zero."
            else:
                self.error()

        return result

if __name__ == "__main__":
    # REPL
    while True:
        # Print a prompt and wait for user input
        try:
            text = input("calc> ")
        except EOFError:
            break
        # If the user input nothing and pressed enter, print the prompt again and wait
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
