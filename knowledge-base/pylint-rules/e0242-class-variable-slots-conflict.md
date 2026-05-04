---
id: pylint-E0242
rule_code: "E0242"
rule_name: "class-variable-slots-conflict"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/class-variable-slots-conflict.html"
---
# class-variable-slots-conflict / E0242

**Message emitted:**

`Value %r in slots conflicts with class variable`

**Description:**

*Used when a value in __slots__ conflicts with a class variable, property or method.*

**Problematic code:**

```
class Person:
    # +1: [class-variable-slots-conflict, class-variable-slots-conflict, class-variable-slots-conflict]
    __slots__ = ("age", "name", "say_hi")
    name = None

    def __init__(self, age, name):
        self.age = age
        self.name = name

    @property
    def age(self):
        return self.age

    def say_hi(self):
        print(f"Hi, I'm {self.name}.")
```

**Correct code:**

```
class Person:
    __slots__ = ("_age", "name")

    def __init__(self, age, name):
        self._age = age
        self.name = name

    @property
    def age(self):
        return self._age

    def say_hi(self):
        print(f"Hi, I'm {self.name}.")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.