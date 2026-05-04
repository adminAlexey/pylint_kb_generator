---
id: pylint-E0304
rule_code: "E0304"
rule_name: "invalid-bool-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-bool-returned.html"
---
# invalid-bool-returned / E0304

**Message emitted:**

`__bool__ does not return bool`

**Description:**

*Used when a __bool__ method returns something which is not a bool*

**Problematic code:**

```
class CustomBool:
    """__bool__ returns an int"""

    def __bool__(self):  # [invalid-bool-returned]
        return 1
```

**Correct code:**

```
class CustomBool:
    """__bool__ returns `bool`"""

    def __bool__(self):
        return True
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.