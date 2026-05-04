---
id: pylint-W0201
rule_code: "W0201"
rule_name: "attribute-defined-outside-init"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/attribute-defined-outside-init.html"
---
# attribute-defined-outside-init / W0201

**Message emitted:**

`Attribute %r defined outside __init__`

**Description:**

*Used when an instance attribute is defined outside the __init__ method.*

**Problematic code:**

```
class Student:
    def register(self):
        self.is_registered = True  # [attribute-defined-outside-init]
```

**Correct code:**

```
class Student:
    def __init__(self):
        self.is_registered = False

    def register(self):
        self.is_registered = True
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.