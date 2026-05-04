---
id: pylint-E0643
rule_code: "E0643"
rule_name: "potential-index-error"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/potential-index-error.html"
---
# potential-index-error / E0643

**Message emitted:**

`Invalid index for iterable length`

**Description:**

*Emitted when an index used on an iterable goes beyond the length of that iterable.*

**Problematic code:**

```
print([1, 2, 3][3])  # [potential-index-error]
```

**Correct code:**

```
print([1, 2, 3][2])
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.