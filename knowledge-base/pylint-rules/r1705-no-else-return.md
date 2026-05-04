---
id: pylint-R1705
rule_code: "R1705"
rule_name: "no-else-return"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-else-return.html"
---
# no-else-return / R1705

**Message emitted:**

`Unnecessary "%s" after "return", %s`

**Description:**

*Used in order to highlight an unnecessary block of code following an if, or a try/except containing a return statement. As such, it will warn when it encounters an else following a chain of ifs, all of them containing a return statement.*

**Problematic code:**

```
def compare_numbers(a: int, b: int) -> int:
    if a == b:  # [no-else-return]
        return 0
    elif a < b:
        return -1
    else:
        return 1
```

**Correct code:**

```
def compare_numbers(a: int, b: int) -> int:
    if a == b:
        return 0
    if a < b:
        return -1
    return 1
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.