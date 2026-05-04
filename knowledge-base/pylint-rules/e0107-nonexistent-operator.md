---
id: pylint-E0107
rule_code: "E0107"
rule_name: "nonexistent-operator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/nonexistent-operator.html"
---
# nonexistent-operator / E0107

**Message emitted:**

`Use of the non-existent %s operator`

**Description:**

*Used when you attempt to use the C-style pre-increment or pre-decrement operator -- and ++, which doesn't exist in Python.*

**Problematic code:**

```
i = 0

while i <= 10:
    print(i)
    ++i  # [nonexistent-operator]
```

**Correct code:**

```
i = 0

while i <= 10:
    print(i)
    i += 1
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.