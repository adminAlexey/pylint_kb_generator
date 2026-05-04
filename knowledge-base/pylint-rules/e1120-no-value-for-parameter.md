---
id: pylint-E1120
rule_code: "E1120"
rule_name: "no-value-for-parameter"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/no-value-for-parameter.html"
---
# no-value-for-parameter / E1120

**Message emitted:**

`No value for argument %s in %s call`

**Description:**

*Used when a function call passes too few arguments.*

**Problematic code:**

```
def add(x, y):
    return x + y

add(1)  # [no-value-for-parameter]
```

**Correct code:**

```
def add(x, y):
    return x + y

add(1, 2)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.