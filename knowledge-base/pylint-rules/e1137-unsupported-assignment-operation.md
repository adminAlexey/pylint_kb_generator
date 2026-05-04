---
id: pylint-E1137
rule_code: "E1137"
rule_name: "unsupported-assignment-operation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unsupported-assignment-operation.html"
---
# unsupported-assignment-operation / E1137

**Message emitted:**

`%r does not support item assignment`

**Description:**

*Emitted when an object does not support item assignment (i.e. doesn't define __setitem__ method).*

**Problematic code:**

```
def pick_fruits(fruits):
    for fruit in fruits:
        print(fruit)

pick_fruits(["apple"])[0] = "orange"  # [unsupported-assignment-operation]
```

**Correct code:**

```
def pick_fruits(fruits):
    for fruit in fruits:
        print(fruit)

    return []

pick_fruits(["apple"])[0] = "orange"
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.