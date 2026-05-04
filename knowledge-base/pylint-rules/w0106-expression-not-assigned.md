---
id: pylint-W0106
rule_code: "W0106"
rule_name: "expression-not-assigned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/expression-not-assigned.html"
---
# expression-not-assigned / W0106

**Message emitted:**

`Expression "%s" is assigned to nothing`

**Description:**

*Used when an expression that is not a function call is assigned to nothing. Probably something else was intended.*

**Problematic code:**

```
str(42) == "42"  # [expression-not-assigned]
```

**Correct code:**

```
are_equal: bool = str(42) == "42"
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.