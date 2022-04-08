# PIP

"PIP" stands for "Pascal Interpreter in Python". This project is a simple interpreter for a large subset of Pascal language. The underlying language is Python. For example, pip is able to interpret the following Pascal program:

```pascal
program factorial;

function factorial(n: integer): longint;
begin
    if n = 0 then
        factorial := 1
    else
        factorial := n * factorial(n - 1);
end;

var
    n: integer;

begin
    for n := 0 to 16 do
        writeln(n, '! = ', factorial(n));
end.
```

## Compiler vs. Interpreter

- If a translator translates a source program into machine language, it is a **compiler**.
- If a translator processes and executes the source program without translating it into machine language first, it is an **interpreter**.

Pictorially:

![Compilervs. Interpreter](Compiler_vs_Interpreter.png)
