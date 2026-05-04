---
id: pylint-E0237
rule_code: "E0237"
rule_name: "assigning-non-slot"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/assigning-non-slot.html"
---
# assigning-non-slot / E0237

**Message emitted:**

`Assigning to attribute %r not defined in class slots`

**Description:**

*Used when assigning to an attribute not defined in the class slots.*

**Problematic code:**

```
class Student:
    __slots__ = ("name",)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname  # [assigning-non-slot]
        self.setup()

    def setup(self):
        pass
```

**Correct code:**

```
class Student:
    __slots__ = ("name", "surname")

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.setup()

    def setup(self):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.