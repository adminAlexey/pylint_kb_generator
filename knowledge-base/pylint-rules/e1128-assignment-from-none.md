---
id: pylint-E1128
rule_code: "E1128"
rule_name: "assignment-from-none"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/assignment-from-none.html"
---
# assignment-from-none / E1128

**Message emitted:**

`Assigning result of a function call, where the function returns None`

**Description:**

*Used when an assignment is done on a function call but the inferred function returns nothing but None.*

**Problematic code:**

```
def function():
    return None

f = function()  # [assignment-from-none]
```

**Correct code:**

```
def function():
    return None

f = function() if function() else 1
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.