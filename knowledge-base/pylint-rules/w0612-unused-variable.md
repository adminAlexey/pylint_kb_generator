---
id: pylint-W0612
rule_code: "W0612"
rule_name: "unused-variable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-variable.html"
---
# unused-variable / W0612

**Message emitted:**

`Unused variable %r`

**Description:**

*Used when a variable is defined but not used.*

**Problematic code:**

```
def print_fruits():
    fruit1 = "orange"
    fruit2 = "apple"  # [unused-variable]
    print(fruit1)
```

**Correct code:**

```
def print_fruits():
    fruit1 = "orange"
    fruit2 = "apple"
    print(fruit1, fruit2)
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.