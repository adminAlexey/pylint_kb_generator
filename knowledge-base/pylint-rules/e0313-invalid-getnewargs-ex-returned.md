---
id: pylint-E0313
rule_code: "E0313"
rule_name: "invalid-getnewargs-ex-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-getnewargs-ex-returned.html"
---
# invalid-getnewargs-ex-returned / E0313

**Message emitted:**

`__getnewargs_ex__ does not return a tuple containing (tuple, dict)`

**Description:**

*Used when a __getnewargs_ex__ method returns something which is not of the form tuple(tuple, dict)*

**Problematic code:**

```
class CustomGetNewArgsEx:
    """__getnewargs_ex__ returns tuple with incorrect arg length"""

    def __getnewargs_ex__(self):  # [invalid-getnewargs-ex-returned]
        return (tuple(1), dict(x="y"), 1)
```

**Correct code:**

```
class CustomGetNewArgsEx:
    """__getnewargs_ex__ returns <type 'tuple'>"""

    def __getnewargs_ex__(self):
        return ((1,), {"2": 2})
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.