---
id: pylint-E1136
rule_code: "E1136"
rule_name: "unsubscriptable-object"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unsubscriptable-object.html"
---
# unsubscriptable-object / E1136

**Message emitted:**

`Value '%s' is unsubscriptable`

**Description:**

*Emitted when a subscripted value doesn't support subscription (i.e. doesn't define __getitem__ method or __class_getitem__ for a class).*

**Problematic code:**

```
class Fruit:
    pass

Fruit()[1]  # [unsubscriptable-object]
```

**Correct code:**

```
class Fruit:
    def __init__(self):
        self.colors = ["red", "orange", "yellow"]

    def __getitem__(self, idx):
        return self.colors[idx]

Fruit()[1]
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.