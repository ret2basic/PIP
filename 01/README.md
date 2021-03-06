# Project 1: Calculator v1

## Objective

In this project, we are going to implement a minimal interpreter for a calculator that handles addition only. For example:

```shell
$ python calc1.py
calc> 3+4
7
calc> 3+5
8
calc> 3+9
12
calc>
```

The input needs to follow certain rules:

- Only single digit integers are allowed in the input
- The only arithmetic operation supported at the moment is addition
- No whitespace characters are allowed anywhere in the input

## The Interpretation Process

From source code to machine code, the interpretation process is divided into the following steps:

1. **Scanning**
  - The first step is **scanning**, also known as **lexing**, or **lexical analysis**.
  - A **scanner** (or **lexer**) takes in the linear stream of characters and chunks them together into a series of something more akin to "words". In programming languages, each of these words is called a **token**.
  - For example, an input string "3+5" has the following tokens:
     - An integer `3`
     - An operator `+`
     - An integer `5`
2. **Parsing**
  - The next step is **parsing**, or **syntax analysis**. This is where our syntax gets a **grammar**—the ability to compose larger expressions and statements out of smaller parts.
  - A **parser** takes the flat sequence of tokens and builds an **abstract syntax tree (AST)** that mirrors the nested nature of the grammar.
  - In `calc1.py`, the function `expr()` will handle both parsing and interpreting.
3. Static Analysis
4. Intermediate Representations
5. Optimization
6. Code Generation
7. Virtual Machine
8. Runtime

We only implement scanning and parsing in the first few projects. Pictorially:

![Mountain](Mountain.png)

## Design

Think of the input string as a char array. A pointer starts from the left and handles each character one by one. Pictorially:

![Lexer1.png](Lexer1.png)

![Lexer2.png](Lexer2.png)

![Lexer3.png](Lexer3.png)

![Lexer4.png](Lexer4.png)

We define two classes:

- The `Token` class
  - Defines **token type** and **token value**.
  - Token type can be 'INTEGER', 'PLUS', or 'EOF'.
  - Token value can be 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or `None`.
- The `Interpreter` class
  - Defines a **"pointer"** `pos` (this is actually an index) and a few useful methods for interpreting the input string.
  - `get_next_token()`: recognizes the current token and move the pointer to the right.
  - `eat()`: Verify the current toke type and move to the next token.
  - `expr()`: Parsing and interpreting.

## Exercises

- [x] Modify the code to allow multiple-digit integers in the input, for example "12+3"
- [x] Add a method that skips whitespace characters so that your calculator can handle inputs with whitespace characters like "12 + 3"
- [x] Modify the code and instead of '+' handle '-' to evaluate subtractions like "7-5"
