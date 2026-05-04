---
id: pylint-E0245
rule_code: "E0245"
rule_name: "declare-non-slot"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/declare-non-slot.html"
---
# declare-non-slot / E0245

**Message emitted:**

`No such name %r in __slots__`

**Description:**

*Raised when a type annotation on a class is absent from the list of names in __slots__, and __slots__ does not contain a __dict__ entry.*

**Problematic code:**

```
class Student:
    __slots__ = ("name",)

    name: str
    surname: str  # [declare-non-slot]
```

**Correct code:**

```
class Student:
    __slots__ = ("name", "surname")

    name: str
    surname: str
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.