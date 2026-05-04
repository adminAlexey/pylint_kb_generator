---
id: pylint-W0101
rule_code: "W0101"
rule_name: "unreachable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unreachable.html"
---
# unreachable / W0101

**Message emitted:**

`Unreachable code`

**Description:**

*Used when there is some code behind a "return" or "raise" statement, which will never be accessed.*

**Problematic code:**

```
def say_hello():
    return True
    print("Hello World!, Outside function.")  # [unreachable]
```

**Correct code:**

```
def say_hello():
    print("Hello World!, Inside function.")
    return True
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.