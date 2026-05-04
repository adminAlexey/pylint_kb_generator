---
id: pylint-R1709
rule_code: "R1709"
rule_name: "simplify-boolean-expression"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/simplify-boolean-expression.html"
---
# simplify-boolean-expression / R1709

**Message emitted:**

`Boolean expression may be simplified to %s`

**Description:**

*Emitted when redundant pre-python 2.5 ternary syntax is used.*

**Problematic code:**

```
def has_oranges(oranges, apples=None) -> bool:
    return apples and False or oranges  # [simplify-boolean-expression]
```

**Correct code:**

```
def has_oranges(oranges, apples=None) -> bool:
    return oranges
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.