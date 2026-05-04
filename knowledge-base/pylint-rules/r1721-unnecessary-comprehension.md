---
id: pylint-R1721
rule_code: "R1721"
rule_name: "unnecessary-comprehension"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/unnecessary-comprehension.html"
---
# unnecessary-comprehension / R1721

**Message emitted:**

`Unnecessary use of a comprehension, use %s instead.`

**Description:**

*Instead of using an identity comprehension, consider using the list, dict or set constructor. It is faster and simpler.*

**Problematic code:**

```
NUMBERS = [1, 1, 2, 2, 3, 3]

UNIQUE_NUMBERS = {number for number in NUMBERS}  # [unnecessary-comprehension]
```

**Correct code:**

```
NUMBERS = [1, 1, 2, 2, 3, 3]

UNIQUE_NUMBERS = set(NUMBERS)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.