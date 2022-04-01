# Project 2: Calculator v2

## Objective

In this project, we are going to improve the `cacl1.py` interpreter. In particular, `calc2.py` is able to:

- Handle whitespace characters anywhere in the input string
- Consume multi-digit integers from the input
- Subtract two integers (currently it can only add integers)

## Lexme

A **lexeme** is a sequence of characters that form a token. For example:

![Lexme.png](Lexme.png)

## Design

The major code changes compared with `calc1.py` are:

- The `get_next_token` method was refactored a bit. The logic to increment the pos pointer was factored into a separate method advance.
- Two more methods were added: `skip_whitespace` to ignore whitespace characters and `integer` to handle multi-digit integers in the input.
- The `expr` method was modified to recognize `INTEGER -> MINUS -> INTEGER` phrase in addition to `INTEGER -> PLUS -> INTEGER` phrase. The method now also interprets both addition and subtraction after having successfully recognized the corresponding phrase.
