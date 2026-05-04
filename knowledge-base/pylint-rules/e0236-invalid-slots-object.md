---
id: pylint-E0236
rule_code: "E0236"
rule_name: "invalid-slots-object"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-slots-object.html"
---
# invalid-slots-object / E0236

**Message emitted:**

`Invalid object %r in __slots__, must contain only non empty strings`

**Description:**

*Used when an invalid (non-string) object occurs in __slots__.*

**Problematic code:**

```
class Person:
    __slots__ = ("name", 3)  # [invalid-slots-object]
```

**Correct code:**

```
class Person:
    __slots__ = ("name", "surname")
```

**Related links:**

- [Documentation for __slots__](https://docs.python.org/3/reference/datamodel.html#slots)

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.