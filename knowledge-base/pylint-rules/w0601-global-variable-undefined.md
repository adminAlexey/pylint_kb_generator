---
id: pylint-W0601
rule_code: "W0601"
rule_name: "global-variable-undefined"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/global-variable-undefined.html"
---
# global-variable-undefined / W0601

**Message emitted:**

`Global variable %r undefined at the module level`

**Description:**

*Used when a variable is defined through the "global" statement but the variable is not defined in the module scope.*

**Problematic code:**

```
def update_tomato():
    global TOMATO  # [global-variable-undefined]
    TOMATO = "moneymaker"
```

**Correct code:**

```
TOMATO = "black cherry"

def update_tomato():
    global TOMATO
    TOMATO = "moneymaker"
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.