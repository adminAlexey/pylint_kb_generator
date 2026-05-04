---
id: pylint-E0101
rule_code: "E0101"
rule_name: "return-in-init"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/return-in-init.html"
---
# return-in-init / E0101

**Message emitted:**

`Explicit return in __init__`

**Description:**

*Used when the special class method __init__ has an explicit return value.*

**Problematic code:**

```
class Sum:
    def __init__(self, a, b):  # [return-in-init]
        return a + b
```

**Correct code:**

```
class Sum:
    def __init__(self, a, b) -> None:
        self.result = a + b
```

**Related links:**

- [__init__ method documentation](https://docs.python.org/3/reference/datamodel.html#object.__init__)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.