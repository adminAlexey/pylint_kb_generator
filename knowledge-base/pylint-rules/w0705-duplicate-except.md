---
id: pylint-W0705
rule_code: "W0705"
rule_name: "duplicate-except"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/duplicate-except.html"
---
# duplicate-except / W0705

**Message emitted:**

`Catching previously caught exception type %s`

**Description:**

*Used when an except catches a type that was already caught by a previous handler.*

**Problematic code:**

```
try:
    1 / 0
except ZeroDivisionError:
    pass
except ZeroDivisionError:  # [duplicate-except]
    pass
```

**Correct code:**

```
try:
    1 / 0
except ZeroDivisionError:
    pass
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.