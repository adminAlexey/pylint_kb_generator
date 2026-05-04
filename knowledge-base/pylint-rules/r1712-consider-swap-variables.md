---
id: pylint-R1712
rule_code: "R1712"
rule_name: "consider-swap-variables"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-swap-variables.html"
---
# consider-swap-variables / R1712

**Message emitted:**

`Consider using tuple unpacking for swapping variables`

**Description:**

*You do not have to use a temporary variable in order to swap variables. Using "tuple unpacking" to directly swap variables makes the intention more clear.*

**Problematic code:**

```
a = 1
b = 2

temp = a  # [consider-swap-variables]
a = b
b = temp
```

**Correct code:**

```
a = 1
b = 2

a, b = b, a
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.