---
id: pylint-W0130
rule_code: "W0130"
rule_name: "duplicate-value"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/duplicate-value.html"
---
# duplicate-value / W0130

**Message emitted:**

`Duplicate value %r in set`

**Description:**

*This message is emitted when a set contains the same value two or more times.*

**Problematic code:**

```
incorrect_set = {"value1", 23, 5, "value1"}  # [duplicate-value]
```

**Correct code:**

```
correct_set = {"value1", 23, 5}
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.