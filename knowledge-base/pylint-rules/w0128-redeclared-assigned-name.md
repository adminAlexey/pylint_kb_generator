---
id: pylint-W0128
rule_code: "W0128"
rule_name: "redeclared-assigned-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redeclared-assigned-name.html"
---
# redeclared-assigned-name / W0128

**Message emitted:**

`Redeclared variable %r in assignment`

**Description:**

*Emitted when we detect that a variable was redeclared in the same assignment.*

**Problematic code:**

```
FIRST, FIRST = (1, 2)  # [redeclared-assigned-name]
```

**Correct code:**

```
FIRST, SECOND = (1, 2)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.