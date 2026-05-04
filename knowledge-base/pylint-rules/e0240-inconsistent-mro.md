---
id: pylint-E0240
rule_code: "E0240"
rule_name: "inconsistent-mro"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/inconsistent-mro.html"
---
# inconsistent-mro / E0240

**Message emitted:**

`Inconsistent method resolution order for class %r`

**Description:**

*Used when a class has an inconsistent method resolution order.*

**Problematic code:**

```
class A:
    pass

class B(A):
    pass

class C(A, B):  # [inconsistent-mro]
    pass
```

**Correct code:**

```
class A:
    pass

class B(A):
    pass

class C(B):  # or 'B, A' or 'A' but not 'A, B'
    pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.