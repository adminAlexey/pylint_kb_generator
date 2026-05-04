---
id: pylint-W0107
rule_code: "W0107"
rule_name: "unnecessary-pass"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unnecessary-pass.html"
---
# unnecessary-pass / W0107

**Message emitted:**

`Unnecessary pass statement`

**Description:**

*Used when a "pass" statement can be removed without affecting the behaviour of the code.*

**Problematic code:**

```
class DataEntryError(Exception):
    """This exception is raised when a user has provided incorrect data."""

    pass  # [unnecessary-pass]
```

**Correct code:**

```
class DataEntryError(Exception):
    """This exception is raised when a user has provided incorrect data."""
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/pass_checker.py) checker.