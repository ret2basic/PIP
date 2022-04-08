# Project 4: Calculator v4

## Objective

Let the interpreter parse and interpret arithmetic expressions with any number of multiplication and division operators in them, for example "7 * 4 / 2 * 3".

## Context-Free Grammars (CFG) and Backus-Naur Form (BNF)

### Motivation

- A grammar specifies the syntax of a programming language in a concise manner. Unlike syntax diagrams, grammars are very compact.
- A grammar can serve as great documentation.
- A grammar is a good starting point even if you manually write your parser from scratch. Quite often you can just convert the grammar to code by following a set of simple rules.
- There is a set of tools, called **parser generators**, which accept a grammar as an input and automatically generate a parser for you based on that grammar.

### Example

Here is a grammar that describes arithmetic expressions like "7 * 4 / 2 * 3":

```
expr   : factor ((MUL | DIV) factor)*
factor : INTEGER
```

### Terminologies

- Each line is called a **rule** or **production**. The left-hand side of a rule is called **head** and the right-hand side of a rule is called **body**.
- Tokens with all capital letters such as `MUL/DIV/INTEGER` are called **terminals**. Other tokens such as `expr/factor` are called **non-terminals**. Non-terminals usually consist of a sequence of terminals and/or non-terminals.
- The non-terminal symbol on the left side of the first rule is called the **start symbol**. In the case of our grammar, the start symbol is `expr`.
  
### Symbols

- `|`: Alternatives. A bar means "or". So `(MUL | DIV)` means either `MUL` or `DIV`.
- `( ... )`: An open and closing parentheses mean grouping of terminals and/or non-terminals as in `(MUL | DIV)`.
- `( ... )*`: The wildcard `*` matches contents within the group zero or more times.

### Derivation

A grammar defines a **language** by explaining what sentences it can form. This is how you can **derive** an arithmetic expression using the grammar: first you begin with the start symbol expr and then repeatedly replace a non-terminal by the body of a rule for that non-terminal until you have generated a sentence consisting solely of terminals. Those sentences form a language defined by the grammar.

This is how the grammar derives the expression 3:

![Derive1](Derive1.png)

This is how the grammar derives the expression 3 * 7:

![Derive2](Derive2.png)

And this is how the grammar derives the expression 3 * 7 / 2:

![Derive3](Derive3.png)

## Design

### Grammar => Code

- Each rule, `R`, defined in the grammar, becomes a method with the same name, and references to that rule become a method call: `R()`. The body of the method follows the flow of the body of the rule using the very same guidelines.
- Alternatives `(a1 | a2 | aN)` become an if-elif-else statement
- An optional grouping `(...)*` becomes a while statement that can loop over zero or more times
- Each token reference T becomes a call to the method eat: `eat(T)`. The way the eat method works is that it consumes the token T if it matches the current lookahead token, then it gets a new token from the lexer and assigns that token to the current_token internal variable.

Pictorially:

![Rules](Rules.png)

These steps reduce to the following code:

```python
def factor(self):
    self.eat(INTEGER)

def expr(self):
    self.factor()

    while self.current_token.type in (MUL, DIV):
        token = self.current_token
        if token.type == MUL:
            self.eat(MUL)
            self.factor()
        elif token.type == DIV:
            self.eat(DIV)
            self.factor()
```

The trophy of this project includes two files:

- `parser.py`: class Token + class Lexer + class Parser.
- `calc4.py`: class Token + class Lexer + class Interpreter.

## Exercises

- [x] Write a grammar that describes arithmetic expressions containing any number of +, -, *, or / operators. With the grammar you should be able to derive expressions like "2 + 7 * 4", "7 - 8 / 4", "14 + 2 * 3 - 6 / 2", and so on.
- [x] Using the grammar, write an interpreter that can evaluate arithmetic expressions containing any number of +, -, *, or / operators. Your interpreter should be able to handle expressions like "2 + 7 * 4", "7 - 8 / 4", "14 + 2 * 3 - 6 / 2", and so on.
