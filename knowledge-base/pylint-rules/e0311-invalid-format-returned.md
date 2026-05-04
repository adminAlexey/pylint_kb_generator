---
id: pylint-E0311
rule_code: "E0311"
rule_name: "invalid-format-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-format-returned.html"
---
# invalid-format-returned / E0311

**Message emitted:**

`__format__ does not return str`

**Description:**

*Used when a __format__ method returns something which is not a string*

**Problematic code:**

```
class CustomFormat:
    """__format__ returns <type 'int'>"""

    def __format__(self, format_spec):  # [invalid-format-returned]
        return 1
```

**Correct code:**

```
class CustomFormat:
    """__format__ returns <type 'str'>"""

    def __format__(self, format_spec):
        return "hello!"
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.