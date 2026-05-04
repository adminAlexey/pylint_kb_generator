---
id: pylint-E0118
rule_code: "E0118"
rule_name: "used-prior-global-declaration"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/used-prior-global-declaration.html"
---
# used-prior-global-declaration / E0118

**Message emitted:**

`Name %r is used prior to global declaration`

**Description:**

*Emitted when a name is used prior a global declaration, which results in an error since Python 3.6.*

**Problematic code:**

```
TOMATO = "black cherry"

def update_tomato():
    print(TOMATO)  # [used-prior-global-declaration]
    global TOMATO
    TOMATO = "cherry tomato"
```

**Correct code:**

```
TOMATO = "black cherry"

def update_tomato():
    global TOMATO
    TOMATO = "moneymaker"
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.