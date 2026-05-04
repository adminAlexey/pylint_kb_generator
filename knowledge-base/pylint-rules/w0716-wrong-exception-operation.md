---
id: pylint-W0716
rule_code: "W0716"
rule_name: "wrong-exception-operation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/wrong-exception-operation.html"
---
# wrong-exception-operation / W0716

**Message emitted:**

`Invalid exception operation. %s`

**Description:**

*Used when an operation is done against an exception, but the operation is not valid for the exception in question. Usually emitted when having binary operations between exceptions in except handlers.*

**Problematic code:**

```
try:
    1 / 0
except ValueError + TypeError:  # [wrong-exception-operation]
    pass
```

**Correct code:**

```
try:
    1 / 0
except (ValueError, TypeError):
    pass
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.