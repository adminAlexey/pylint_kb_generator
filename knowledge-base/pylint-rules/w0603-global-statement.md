---
id: pylint-W0603
rule_code: "W0603"
rule_name: "global-statement"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/global-statement.html"
---
# global-statement / W0603

**Message emitted:**

`Using the global statement`

**Description:**

*Used when you use the "global" statement to update a global variable. Pylint discourages its usage. That doesn't mean you cannot use it!*

**Problematic code:**

```
var = 1

def foo():
    global var  # [global-statement]
    var = 10
    print(var)

foo()
print(var)
```

**Correct code:**

```
var = 1

def foo():
    print(var)
    return 10

var = foo()
print(var)
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.