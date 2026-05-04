---
id: pylint-W0707
rule_code: "W0707"
rule_name: "raise-missing-from"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/raise-missing-from.html"
---
# raise-missing-from / W0707

**Message emitted:**

`Consider explicitly re-raising using %s'%s from %s'`

**Description:**

*Python's exception chaining shows the traceback of the current exception, but also of the original exception. When you raise a new exception after another exception was caught it's likely that the second exception is a friendly re-wrapping of the first exception. In such cases `raise from` provides a better link between the two tracebacks in the final error.*

**Problematic code:**

```
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("Rectangle Area cannot be zero")  # [raise-missing-from]
```

**Correct code:**

```
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("Rectangle Area cannot be zero") from e
```

**Related links:**

- [PEP 3134](https://peps.python.org/pep-3134/)

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.