---
id: pylint-W0012
rule_code: "W0012"
rule_name: "unknown-option-value"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unknown-option-value.html"
---
# unknown-option-value / W0012

**Message emitted:**

`Unknown option value for '%s', expected a valid pylint message and got '%s'`

**Description:**

*Used when an unknown value is encountered for an option.*

**Problematic code:**

```
# pylint: disable=missnig-docstring  # [unknown-option-value]
```

**Correct code:**

```
# pylint: disable=missing-docstring
```

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.