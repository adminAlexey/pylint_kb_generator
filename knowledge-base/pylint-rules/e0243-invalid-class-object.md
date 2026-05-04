---
id: pylint-E0243
rule_code: "E0243"
rule_name: "invalid-class-object"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-class-object.html"
---
# invalid-class-object / E0243

**Message emitted:**

`Invalid assignment to '__class__'. Should be a class definition but got a '%s'`

**Description:**

*Used when an invalid object is assigned to a __class__ property. Only a class is permitted.*

**Problematic code:**

```
class Apple:
    pass

Apple.__class__ = 1  # [invalid-class-object]
```

**Correct code:**

```
class Apple:
    pass

class RedDelicious:
    pass

Apple.__class__ = RedDelicious
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.