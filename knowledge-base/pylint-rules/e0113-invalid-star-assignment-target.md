---
id: pylint-E0113
rule_code: "E0113"
rule_name: "invalid-star-assignment-target"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-star-assignment-target.html"
---
# invalid-star-assignment-target / E0113

**Message emitted:**

`Starred assignment target must be in a list or tuple`

**Description:**

*Emitted when a star expression is used as a starred assignment target.*

**Problematic code:**

```
*fruit = ["apple", "banana", "orange"]  # [invalid-star-assignment-target]
```

**Correct code:**

```
fruit = ["apple", "banana", "orange"]
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.