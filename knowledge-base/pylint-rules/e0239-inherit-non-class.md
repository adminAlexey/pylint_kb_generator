---
id: pylint-E0239
rule_code: "E0239"
rule_name: "inherit-non-class"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/inherit-non-class.html"
---
# inherit-non-class / E0239

**Message emitted:**

`Inheriting %r, which is not a class.`

**Description:**

*Used when a class inherits from something which is not a class.*

**Problematic code:**

```
class Fruit(bool):  # [inherit-non-class]
    pass
```

**Correct code:**

```
class Fruit:
    def __bool__(self):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.