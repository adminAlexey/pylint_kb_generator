---
id: pylint-R0916
rule_code: "R0916"
rule_name: "too-many-boolean-expressions"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/too-many-boolean-expressions.html"
---
# too-many-boolean-expressions / R0916

**Message emitted:**

`Too many boolean expressions in if statement (%s/%s)`

**Description:**

*Used when an if statement contains too many boolean expressions.*

**Problematic code:**

```
def can_be_divided_by_two_and_are_not_zero(x, y, z):
    # Maximum number of boolean expressions in an if statement (by default 5)
    # +1: [too-many-boolean-expressions]
    if (x and y and z) and (x % 2 == 0 and y % 2 == 0 and z % 2 == 0):
        pass
```

**Correct code:**

```
def can_be_divided_by_two_and_are_not_zero(x, y, z):
    if all(i and i % 2 == 0 for i in [x, y, z]):
        pass
```

Created by the [design](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/design_analysis.py) checker.