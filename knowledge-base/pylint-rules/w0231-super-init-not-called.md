---
id: pylint-W0231
rule_code: "W0231"
rule_name: "super-init-not-called"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/super-init-not-called.html"
---
# super-init-not-called / W0231

**Message emitted:**

`__init__ method from base class %r is not called`

**Description:**

*Used when an ancestor class method has an __init__ method which is not called by a derived class.*

**Problematic code:**

```
class Fruit:
    def __init__(self, name="fruit"):
        self.name = name
        print("Creating a {self.name}")

class Apple(Fruit):
    def __init__(self):  # [super-init-not-called]
        print("Creating an apple")
```

**Correct code:**

```
class Fruit:
    def __init__(self, name="fruit"):
        self.name = name
        print("Creating a {self.name}")

class Apple(Fruit):
    def __init__(self):
        super().__init__("apple")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.