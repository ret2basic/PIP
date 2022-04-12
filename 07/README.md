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

In order to encode the operator precedence in AST, that is, to represent that "X happens before Y" you just need to put X lower in the tree than Y. For example:

![Precedence 1](Precedence_1.png)

Another example:

![Precedence 2](Precedence_2.png)

## Postorder Traversal

To evaluate the expression represented by the AST, we use **postorder traversal**. For example, here is the AST for `2 * 7 + 3`:

![Postorder Traversal](Postorder_Traversal.png)

Postorder traversal gives `[2, 7, '*', 3, '+']`.

## Design


```python
class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method")
```



```python
class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) // self.visit(node.right)

    def visit_Num(self, node):
        return node.value
```

There are two interesting things about the code that are worth mentioning here:

1. First, the visitor code that manipulates AST nodes is decoupled from the AST nodes themselves. You can see that none of the `AST` node classes (`BinOp` and `Num`) provide any code to manipulate the data stored in those nodes. That logic is encapsulated in the Interpreter class that implements the NodeVisitor class.
2. Second, instead of a giant if statement in the NodeVisitor’s visit method like this, the `NodeVisitor`'s visit method is very generic and dispatches calls to the appropriate method based on the node type passed to it. As I've mentioned before, in order to make use of it, our interpreter inherits from the NodeVisitor class and implements necessary methods. So if the type of a node passed to the visit method is `BinOp`, then the visit method will dispatch the call to the `visit_BinOp` method, and if the type of a node is `Num`, then the visit method will dispatch the call to the `visit_Num` method, and so on.

## Exercises

- [ ] Write a translator (hint: node visitor) that takes as input an arithmetic expression and prints it out in postfix notation, also known as **Reverse Polish Notation (RPN)**. For example, if the input to the translator is the expression `(5 + 3) * 12 / 3` than the output should be `5 3 + 12 * 3 /`. See the answer here but try to solve it first on your own.
- [ ] Write a translator (node visitor) that takes as input an arithmetic expression and prints it out in LISP style notation, that is `2 + 3` would become `(+ 2 3)` and `(2 + 3 * 5)` would become `(+ 2 (* 3 5))`. You can find the answer here but again try to solve it first before looking at the provided solution.
