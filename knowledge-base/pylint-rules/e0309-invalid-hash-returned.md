---
id: pylint-E0309
rule_code: "E0309"
rule_name: "invalid-hash-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-hash-returned.html"
---
# invalid-hash-returned / E0309

**Message emitted:**

`__hash__ does not return int`

**Description:**

*Used when a __hash__ method returns something which is not an integer*

**Problematic code:**

```
class CustomHash:
    """__hash__ returns dict"""

    def __hash__(self):  # [invalid-hash-returned]
        return {}
```

**Correct code:**

```
class CustomHash:
    """__hash__ returns `int`"""

    def __hash__(self):
        return 19
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.