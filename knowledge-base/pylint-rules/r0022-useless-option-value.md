---
id: pylint-R0022
rule_code: "R0022"
rule_name: "useless-option-value"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/useless-option-value.html"
---
# useless-option-value / R0022

**Message emitted:**

`Useless option value for '%s', %s`

**Description:**

*Used when a value for an option that is now deleted from pylint is encountered.*

**Problematic code:**

```
"""'bad-continuation' was removed from pylint in https://github.com/pylint-dev/pylint/pull/3571"""

# pylint: disable=bad-continuation  # [useless-option-value]
```

**Correct code:**

```
"""'bad-continuation' was removed from pylint in https://github.com/pylint-dev/pylint/pull/3571"""
```

**Additional details:**

You can disable this check if you don't want to cleanup your configuration of old messages.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.