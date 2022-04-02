# Project 4: Calculator v4

## Objective

Let the interpreter parse and interpret arithmetic expressions with any number of multiplication and division operators in them, for example "7 * 4 / 2 * 3".




## Context-Free Grammars (CFG) and Backus-Naur Form (BNF)

Motivation of using grammars:

- A grammar specifies the syntax of a programming language in a concise manner. Unlike syntax diagrams, grammars are very compact.
- A grammar can serve as great documentation.
- A grammar is a good starting point even if you manually write your parser from scratch. Quite often you can just convert the grammar to code by following a set of simple rules.
- There is a set of tools, called **parser generators**, which accept a grammar as an input and automatically generate a parser for you based on that grammar.




## Design




## Exercises

- [ ] Write a grammar that describes arithmetic expressions containing any number of +, -, *, or / operators. With the grammar you should be able to derive expressions like "2 + 7 * 4", "7 - 8 / 4", "14 + 2 * 3 - 6 / 2", and so on.
- [ ] Using the grammar, write an interpreter that can evaluate arithmetic expressions containing any number of +, -, *, or / operators. Your interpreter should be able to handle expressions like "2 + 7 * 4", "7 - 8 / 4", "14 + 2 * 3 - 6 / 2", and so on.
