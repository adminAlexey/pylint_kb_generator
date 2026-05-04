---
id: pylint-E0310
rule_code: "E0310"
rule_name: "invalid-length-hint-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-length-hint-returned.html"
---
# invalid-length-hint-returned / E0310

**Message emitted:**

`__length_hint__ does not return non-negative integer`

**Description:**

*Used when a __length_hint__ method returns something which is not a non-negative integer*

**Problematic code:**

```
class CustomLengthHint:
    """__length_hint__ returns non-int"""

    def __length_hint__(self):  # [invalid-length-hint-returned]
        return 3.0
```

**Correct code:**

```
class CustomLengthHint:
    """__length_hint__ returns <type 'int'>"""

    def __length_hint__(self):
        return 10
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.