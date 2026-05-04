---
id: pylint-W0239
rule_code: "W0239"
rule_name: "overridden-final-method"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/overridden-final-method.html"
---
# overridden-final-method / W0239

**Message emitted:**

`Method %r overrides a method decorated with typing.final which is defined in class %r`

**Description:**

*Used when a method decorated with typing.final has been overridden.*

**Problematic code:**

```
from typing import final

class Animal:
    @final
    def can_breathe(self):
        return True

class Cat(Animal):
    def can_breathe(self):  # [overridden-final-method]
        pass
```

**Correct code:**

```
from typing import final

class Animal:
    @final
    def can_breathe(self):
        return True

class Cat(Animal):
    def can_purr(self):
        return True
```

**Configuration file:**

```
[MAIN]
py-version=3.8
```

**Additional details:**

The message can't be emitted when using Python < 3.8.

**Related links:**

- [PEP 591](https://peps.python.org/pep-0591/)

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.