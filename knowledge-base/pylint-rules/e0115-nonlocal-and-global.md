---
id: pylint-E0115
rule_code: "E0115"
rule_name: "nonlocal-and-global"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/nonlocal-and-global.html"
---
# nonlocal-and-global / E0115

**Message emitted:**

`Name %r is nonlocal and global`

**Description:**

*Emitted when a name is both nonlocal and global.*

**Problematic code:**

```
NUMBER = 42

def update_number(number):  # [nonlocal-and-global]
    global NUMBER
    nonlocal NUMBER
    NUMBER = number
    print(f"New global number is: {NUMBER}")

update_number(24)
```

**Correct code:**

```
NUMBER = 42

def update_number(number):
    global NUMBER
    NUMBER = number
    print(f"New global number is: {NUMBER}")

update_number(24)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.