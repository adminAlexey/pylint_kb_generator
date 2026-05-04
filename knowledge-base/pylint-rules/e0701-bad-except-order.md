---
id: pylint-E0701
rule_code: "E0701"
rule_name: "bad-except-order"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-except-order.html"
---
# bad-except-order / E0701

**Message emitted:**

`Bad except clauses order (%s)`

**Description:**

*Used when except clauses are not in the correct order (from the more specific to the more generic). If you don't fix the order, some exceptions may not be caught by the most specific handler.*

**Problematic code:**

```
try:
    print(int(input()))
except Exception:
    raise
except TypeError:  # [bad-except-order]
    # This block cannot be reached since TypeError exception
    # is caught by previous exception handler.
    raise
```

**Correct code:**

```
try:
    print(int(input()))
except TypeError:
    raise
except Exception:
    raise
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.