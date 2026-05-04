---
id: pylint-E0307
rule_code: "E0307"
rule_name: "invalid-str-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-str-returned.html"
---
# invalid-str-returned / E0307

**Message emitted:**

`__str__ does not return str`

**Description:**

*Used when a __str__ method returns something which is not a string*

**Problematic code:**

```
class CustomStr:
    """__str__ returns int"""

    def __str__(self):  # [invalid-str-returned]
        return 1
```

**Correct code:**

```
class CustomStr:
    """__str__ returns <type 'str'>"""

    def __str__(self):
        return "oranges"
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.