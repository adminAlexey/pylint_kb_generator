---
id: pylint-E0308
rule_code: "E0308"
rule_name: "invalid-bytes-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-bytes-returned.html"
---
# invalid-bytes-returned / E0308

**Message emitted:**

`__bytes__ does not return bytes`

**Description:**

*Used when a __bytes__ method returns something which is not bytes*

**Problematic code:**

```
class CustomBytes:
    """__bytes__ returns <type 'str'>"""

    def __bytes__(self):  # [invalid-bytes-returned]
        return "123"
```

**Correct code:**

```
class CustomBytes:
    """__bytes__ returns <type 'bytes'>"""

    def __bytes__(self):
        return b"some bytes"
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.