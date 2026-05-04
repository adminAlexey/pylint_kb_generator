---
id: pylint-W0104
rule_code: "W0104"
rule_name: "pointless-statement"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/pointless-statement.html"
---
# pointless-statement / W0104

**Message emitted:**

`Statement seems to have no effect`

**Description:**

*Used when a statement doesn't have (or at least seems to) any effect.*

**Problematic code:**

```
[1, 2, 3]  # [pointless-statement]
```

**Correct code:**

```
NUMBERS = [1, 2, 3]

print(NUMBERS)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.