---
id: pylint-W0602
rule_code: "W0602"
rule_name: "global-variable-not-assigned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/global-variable-not-assigned.html"
---
# global-variable-not-assigned / W0602

**Message emitted:**

`Using global for %r but no assignment is done`

**Description:**

*When a variable defined in the global scope is modified in an inner scope, the 'global' keyword is required in the inner scope only if there is an assignment operation done in the inner scope.*

**Problematic code:**

```
TOMATO = "black cherry"

def update_tomato():
    global TOMATO  # [global-variable-not-assigned]
    print(TOMATO)
```

**Correct code:**

```
TOMATO = "black cherry"

def update_tomato():
    global TOMATO
    TOMATO = "moneymaker"
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.