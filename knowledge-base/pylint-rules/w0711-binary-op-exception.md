---
id: pylint-W0711
rule_code: "W0711"
rule_name: "binary-op-exception"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/binary-op-exception.html"
---
# binary-op-exception / W0711

**Message emitted:**

`Exception to catch is the result of a binary "%s" operation`

**Description:**

*Used when the exception to catch is of the form "except A or B:".  If intending to catch multiple, rewrite as "except (A, B):"*

**Problematic code:**

```
try:
    1 / 0
except ZeroDivisionError or ValueError:  # [binary-op-exception]
    pass
```

**Correct code:**

```
try:
    1 / 0
except (ZeroDivisionError, ValueError):
    pass
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.