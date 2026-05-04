---
id: pylint-R0205
rule_code: "R0205"
rule_name: "useless-object-inheritance"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/useless-object-inheritance.html"
---
# useless-object-inheritance / R0205

**Message emitted:**

`Class %r inherits from object, can be safely removed from bases in python3`

**Description:**

*Used when a class inherit from object, which under python3 is implicit, hence can be safely removed from bases.*

**Problematic code:**

```
class Banana(object):  # [useless-object-inheritance]
    ...
```

**Correct code:**

```
class Banana: ...
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.