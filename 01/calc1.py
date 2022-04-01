# 
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

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

    def error(self):
        raise Exception('Error parsing input.')

    def get_next_token(self):
        """Tokenizer"""

        text = self.text

        # If the "pointer" is pointing to EOF
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        elif current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        else:
            self.error()

    def eat(self, token_type):
        """Verify the current toke type and move to the next token."""
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """Verify the input format, compute and print the result."""

        self.current_token = self.get_next_token()

        # An integer, for example, 3
        left = self.current_token
        self.eat(INTEGER)
        # A plus sign, +
        op = self.current_token
        self.eat(PLUS)
        # An integer, for example, 5
        right = self.current_token
        self.eat(INTEGER)
        # After the above call, self.current_token is set to the EOF token

        # Once we verify that the input format is correct, compute and print the result
        result = left.value + right.value
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