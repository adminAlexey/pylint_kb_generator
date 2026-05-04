---
id: pylint-C0321
rule_code: "C0321"
rule_name: "multiple-statements"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/multiple-statements.html"
---
# multiple-statements / C0321

**Message emitted:**

`More than one statement on a single line`

**Description:**

*Used when more than one statement is found on the same line.*

**Problematic code:**

```
fruits = ["apple", "orange", "mango"]

if "apple" in fruits: pass  # [multiple-statements]
else:
    print("no apples!")
```

**Correct code:**

```
fruits = ["apple", "orange", "mango"]

if "apple" in fruits:
    pass
else:
    print("no apples!")
```

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.