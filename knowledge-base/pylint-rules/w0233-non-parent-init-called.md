---
id: pylint-W0233
rule_code: "W0233"
rule_name: "non-parent-init-called"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/non-parent-init-called.html"
---
# non-parent-init-called / W0233

**Message emitted:**

`__init__ method from a non direct base class %r is called`

**Description:**

*Used when an __init__ method is called on a class which is not in the direct ancestors for the analysed class.*

**Problematic code:**

```
class Animal:
    def __init__(self):
        self.is_multicellular = True

class Vertebrate(Animal):
    def __init__(self):
        super().__init__()
        self.has_vertebrae = True

class Cat(Vertebrate):
    def __init__(self):
        Animal.__init__(self)  # [non-parent-init-called]
        self.is_adorable = True
```

**Correct code:**

```
class Animal:
    def __init__(self):
        self.is_multicellular = True

class Vertebrate(Animal):
    def __init__(self):
        super().__init__()
        self.has_vertebrae = True

class Cat(Vertebrate):
    def __init__(self):
        super().__init__()
        self.is_adorable = True
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.