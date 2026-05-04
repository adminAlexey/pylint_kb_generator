---
id: pylint-C0205
rule_code: "C0205"
rule_name: "single-string-used-for-slots"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/single-string-used-for-slots.html"
---
# single-string-used-for-slots / C0205

**Message emitted:**

`Class __slots__ should be a non-string iterable`

**Description:**

*Used when a class __slots__ is a simple string, rather than an iterable.*

**Problematic code:**

```
class Fruit:  # [single-string-used-for-slots]
    __slots__ = "name"

    def __init__(self, name):
        self.name = name
```

**Correct code:**

```
class Fruit:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.