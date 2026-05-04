---
id: pylint-E0305
rule_code: "E0305"
rule_name: "invalid-index-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-index-returned.html"
---
# invalid-index-returned / E0305

**Message emitted:**

`__index__ does not return int`

**Description:**

*Used when an __index__ method returns something which is not an integer*

**Problematic code:**

```
class CustomIndex:
    """__index__ returns a dict"""

    def __index__(self):  # [invalid-index-returned]
        return {"19": "19"}
```

**Correct code:**

```
class CustomIndex:
    """__index__ returns <type 'int'>"""

    def __index__(self):
        return 19
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.