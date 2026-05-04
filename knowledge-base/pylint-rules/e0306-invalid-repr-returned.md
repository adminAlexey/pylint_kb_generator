---
id: pylint-E0306
rule_code: "E0306"
rule_name: "invalid-repr-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-repr-returned.html"
---
# invalid-repr-returned / E0306

**Message emitted:**

`__repr__ does not return str`

**Description:**

*Used when a __repr__ method returns something which is not a string*

**Problematic code:**

```
class CustomRepr:
    """__repr__ returns <type 'int'>"""

    def __repr__(self):  # [invalid-repr-returned]
        return 1
```

**Correct code:**

```
class CustomRepr:
    """__repr__ returns <type 'str'>"""

    def __repr__(self):
        return "apples"
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.