---
id: pylint-E1138
rule_code: "E1138"
rule_name: "unsupported-delete-operation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unsupported-delete-operation.html"
---
# unsupported-delete-operation / E1138

**Message emitted:**

`%r does not support item deletion`

**Description:**

*Emitted when an object does not support item deletion (i.e. doesn't define __delitem__ method).*

**Problematic code:**

```
FRUITS = ("apple", "orange", "berry")

del FRUITS[0]  # [unsupported-delete-operation]
```

**Correct code:**

```
FRUITS = ["apple", "orange", "berry"]

del FRUITS[0]
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.