# Project 7: 

## Parse Tree

A **parse tree** (sometimes called a **concrete syntax tree**) is a tree that represents the syntactic structure of a language construct according to our grammar definition. It basically shows how your parser recognized the language construct or, in other words, it shows how the start symbol of your grammar derives a certain string in the programming language.

![Parse Tree](Parse_Tree.png)

In the picture above you can see that:

- The parse tree records a sequence of rules the parser applies to recognize the input.
- The root of the parse tree is labeled with the grammar start symbol.
- Each interior node represents a non-terminal, that is it represents a grammar rule application, like expr, term, or factor in our case.
- Each leaf node represents a token.

## Abstract Syntax Tree (AST)

An **abstract syntax tree (AST)** is a tree that represents the abstract syntactic structure of a language construct where each interior node and the root node represents an operator, and the children of the node represent the operands of that operator.

The following diagram illustrates the AST and the parse tree for the expression `2 * 7 + 3`:

![AST](AST.png)

Here are the main differences between ASTs and Parse trees:

- ASTs uses operators/operations as root and interior nodes and it uses operands as their children.
- ASTs do not use interior nodes to represent a grammar rule, unlike the parse tree does.
- ASTs don't represent every detail from the real syntax (that's why they're called abstract) - no rule nodes and no parentheses, for example.
- ASTs are dense compared to a parse tree for the same language construct.


