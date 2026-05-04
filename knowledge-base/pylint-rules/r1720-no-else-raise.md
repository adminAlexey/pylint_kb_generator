---
id: pylint-R1720
rule_code: "R1720"
rule_name: "no-else-raise"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-else-raise.html"
---
# no-else-raise / R1720

**Message emitted:**

`Unnecessary "%s" after "raise", %s`

**Description:**

*Used in order to highlight an unnecessary block of code following an if, or a try/except containing a raise statement. As such, it will warn when it encounters an else following a chain of ifs, all of them containing a raise statement.*

**Problematic code:**

```
def integer_sum(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):  # [no-else-raise]
        raise ValueError("Function supports only integer parameters.")
    else:
        return a + b
```

**Correct code:**

```
def integer_sum(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Function supports only integer parameters.")
    return a + b
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.