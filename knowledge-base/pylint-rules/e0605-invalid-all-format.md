---
id: pylint-E0605
rule_code: "E0605"
rule_name: "invalid-all-format"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-all-format.html"
---
# invalid-all-format / E0605

**Message emitted:**

`Invalid format for __all__, must be tuple or list`

**Description:**

*Used when __all__ has an invalid format.*

**Problematic code:**

```
__all__ = "CONST"  # [invalid-all-format]

CONST = 42
```

**Correct code:**

```
__all__ = ("CONST",)

CONST = 42
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.