---
id: pylint-W2301
rule_code: "W2301"
rule_name: "unnecessary-ellipsis"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unnecessary-ellipsis.html"
---
# unnecessary-ellipsis / W2301

**Message emitted:**

`Unnecessary ellipsis constant`

**Description:**

*Used when the ellipsis constant is encountered and can be avoided. A line of code consisting of an ellipsis is unnecessary if there is a docstring on the preceding line or if there is a statement in the same scope.*

**Problematic code:**

```
def my_function():
    """My docstring"""
    ...  # [unnecessary-ellipsis]
```

**Correct code:**

```
def my_function():
    """My docstring"""
```

Created by the [unnecessary_ellipsis](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/ellipsis_checker.py) checker.