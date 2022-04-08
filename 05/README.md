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


