---
id: pylint-E0238
rule_code: "E0238"
rule_name: "invalid-slots"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-slots.html"
---
# invalid-slots / E0238

**Message emitted:**

`Invalid __slots__ object`

**Description:**

*Used when an invalid __slots__ is found in class. Only a string, an iterable or a sequence is permitted.*

**Problematic code:**

```
class Person:  # [invalid-slots]
    __slots__ = 42
```

**Correct code:**

```
class Person:
    __slots__ = ("name", "age")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.