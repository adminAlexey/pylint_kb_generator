---
id: pylint-W0244
rule_code: "W0244"
rule_name: "redefined-slots-in-subclass"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redefined-slots-in-subclass.html"
---
# redefined-slots-in-subclass / W0244

**Message emitted:**

`Redefined slots %r in subclass`

**Description:**

*Used when a slot is re-defined in a subclass.*

**Problematic code:**

```
class Base:
    __slots__ = ("a", "b")

class Subclass(Base):
    __slots__ = ("a", "d")  # [redefined-slots-in-subclass]
```

**Correct code:**

```
class Base:
    __slots__ = ("a", "b")

class Subclass(Base):
    __slots__ = ("d",)
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.