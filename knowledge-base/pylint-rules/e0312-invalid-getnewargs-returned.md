---
id: pylint-E0312
rule_code: "E0312"
rule_name: "invalid-getnewargs-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-getnewargs-returned.html"
---
# invalid-getnewargs-returned / E0312

**Message emitted:**

`__getnewargs__ does not return a tuple`

**Description:**

*Used when a __getnewargs__ method returns something which is not a tuple*

**Problematic code:**

```
class CustomGetNewArgs:
    """__getnewargs__ returns an integer"""

    def __getnewargs__(self):  # [invalid-getnewargs-returned]
        return 1
```

**Correct code:**

```
class CustomGetNewArgs:
    """__getnewargs__ returns <type 'tuple'>"""

    def __getnewargs__(self):
        return (1, 2)
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.