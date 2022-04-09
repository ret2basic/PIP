# Project 6: Calculator v6

## Objective

Add parenthesized expressions to our grammar and implement an interpreter that will be able to evaluate parenthesized expressions with arbitrarily deep nesting, like the expression 7 + 3 * (10 / (12 / (3 + 1) - 1)).

## Design

- The Lexer has been modified to return two more tokens: `LPAREN` for a left parenthesis and `RPAREN` for a right parenthesis.
- The Interpreter's factor method has been slightly updated to parse parenthesized expressions in addition to integers.

## Exercises

- [x] Write your own version of the interpreter of arithmetic expressions.
