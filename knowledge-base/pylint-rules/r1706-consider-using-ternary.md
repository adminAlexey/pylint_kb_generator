---
id: pylint-R1706
rule_code: "R1706"
rule_name: "consider-using-ternary"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-ternary.html"
---
# consider-using-ternary / R1706

**Message emitted:**

`Consider using ternary (%s)`

**Description:**

*Used when one of known pre-python 2.5 ternary syntax is used.*

**Problematic code:**

```
x, y = 1, 2
maximum = x >= y and x or y  # [consider-using-ternary]
```

**Correct code:**

```
x, y = 1, 2
maximum = x if x >= y else y
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.