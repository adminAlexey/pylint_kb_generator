---
id: pylint-C3001
rule_code: "C3001"
rule_name: "unnecessary-lambda-assignment"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/unnecessary-lambda-assignment.html"
---
# unnecessary-lambda-assignment / C3001

**Message emitted:**

`Lambda expression assigned to a variable. Define a function using the "def" keyword instead.`

**Description:**

*Used when a lambda expression is assigned to variable rather than defining a standard function with the "def" keyword.*

**Problematic code:**

```
foo = lambda x: x**2 + 2 * x + 1  # [unnecessary-lambda-assignment]
```

**Correct code:**

```
def foo(x):
    return x**2 + 2 * x + 1
```

Created by the [lambda-expressions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/lambda_expressions.py) checker.