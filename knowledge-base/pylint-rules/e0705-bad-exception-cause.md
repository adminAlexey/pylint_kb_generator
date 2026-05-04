---
id: pylint-E0705
rule_code: "E0705"
rule_name: "bad-exception-cause"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-exception-cause.html"
---
# bad-exception-cause / E0705

**Message emitted:**

`Exception cause set to something which is not an exception, nor None`

**Description:**

*Used when using the syntax "raise ... from ...", where the exception cause is not an exception, nor None.*

**Problematic code:**

```
def divide(x, y):
    result = 0
    try:
        result = x / y
    except ZeroDivisionError:
        # +1: [bad-exception-cause]
        raise ValueError(f"Division by zero when dividing {x} by {y} !") from result
    return result
```

**Correct code:**

```
def divide(x, y):
    result = 0
    try:
        result = x / y
    except ZeroDivisionError as exc:
        raise ValueError(f"Division by zero when dividing {x} by {y} !") from exc
    return result
```

**Related links:**

- [The raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)
- [Explicit Exception Chaining](https://peps.python.org/pep-3134/#explicit-exception-chaining) per PEP 3134

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.