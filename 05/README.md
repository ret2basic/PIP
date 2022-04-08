# Project 5: Calculator v5

Write an interpreter that will be able to evaluate expressions like "14 + 2 * 3 - 6 / 2".

## Associativity and Precedence

In ordinary arithmetic and most programming languages addition, subtraction, multiplication, and division are **left-associative**. For example:

- 7 + 3 + 1 is equivalent to (7 + 3) + 1
- 7 - 3 - 1 is equivalent to (7 - 3) - 1
- 8 * 4 * 2 is equivalent to (8 * 4) * 2
- 8 / 4 / 2 is equivalent to (8 / 4) / 2

Multiplication and division have **higher precedence** than addition and subtraction. For example:

- 7 + 5 * 2 is equivalent to 7 + (5 * 2)
- 7 - 8 / 4 is equivalent to 7 - (8 / 4)

Precedence table:

![Precedence Table](Precedence_Table.png)

Here are the rules for how to construct a grammar from the precedence table:

1. For each level of precedence define a non-terminal. The body of a production for the non-terminal should contain arithmetic operators from that level and non-terminals for the next higher level of precedence.
2. Create an additional non-terminal factor for basic units of expression, in our case, integers. The general rule is that if you have N levels of precedence, you will need N + 1 non-terminals in total: one non-terminal for each level plus one non-terminal for basic units of expression.

According to Rule 1 we will define two non-terminals: a non-terminal called expr for level 2 and a non-terminal called term for level 1. And by following Rule 2 we will define a factor non-terminal for basic units of arithmetic expressions, integers:

```
expr   : term ((PLUS | MINUS) factor)*
term   : factor ((MUL | DIV) factor)*
factor : INTEGER
```

## Design

- The Lexer class can now tokenize `+`, `-`, `*`, and `/` (Nothing new here, we just combined code from previous articles into one class that supports all those tokens)
- Recall that each rule (production), `R`, defined in the grammar, becomes a method with the same name, and references to that rule become a method call: `R()`. As a result the Interpreter class now has three methods that correspond to non-terminals in the grammar: `expr`, `term`, and `factor`.

## Exercises

- [x] Write an interpreter as described in this article off the top of your head, without peeking into the code from the article. Write some tests for your interpreter, and make sure they pass.
- [x] Extend the interpreter to handle arithmetic expressions containing parentheses so that your interpreter could evaluate deeply nested arithmetic expressions like: 7 + 3 * (10 / (12 / (3 + 1) - 1))
