---
id: pylint-R6201
rule_code: "R6201"
rule_name: "use-set-for-membership"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/use-set-for-membership.html"
---
# use-set-for-membership / R6201

**Message emitted:**

`Consider using set for membership test`

**Description:**

*Membership tests are more efficient when performed on a lookup optimized datatype like ``sets``.*

**Problematic code:**

```
def fruit_is_dangerous_for_cat(fruit: str) -> bool:
    """This list is only a silly example, don't make decision regarding your cat diet based on it."""
    return fruit in ["cherry", "grapes"]  # [use-set-for-membership]
```

**Correct code:**

```
def fruit_is_dangerous_for_cat(fruit: str) -> bool:
    """This list is only a silly example, don't make decision regarding your cat diet based on it."""
    return fruit in {"cherry", "grapes"}
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.set_membership
```

Note

This message is emitted by the optional ['set_membership'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-set-membership)
checker, which requires the `pylint.extensions.set_membership` plugin to be loaded.

Created by the [set_membership](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/set_membership.py) checker.