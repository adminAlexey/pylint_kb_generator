---
id: pylint-E0241
rule_code: "E0241"
rule_name: "duplicate-bases"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/duplicate-bases.html"
---
# duplicate-bases / E0241

**Message emitted:**

`Duplicate bases for class %r`

**Description:**

*Duplicate use of base classes in derived classes raise TypeErrors.*

**Problematic code:**

```
class Animal:
    pass

class Cat(Animal, Animal):  # [duplicate-bases]
    pass
```

**Correct code:**

```
class Animal:
    pass

class Bird(Animal):
    pass

class Cat(Animal):
    pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.