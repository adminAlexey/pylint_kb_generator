---
id: pylint-E0712
rule_code: "E0712"
rule_name: "catching-non-exception"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/catching-non-exception.html"
---
# catching-non-exception / E0712

**Message emitted:**

`Catching an exception which doesn't inherit from Exception: %s`

**Description:**

*Used when a class which doesn't inherit from Exception is used as an exception in an except clause.*

**Problematic code:**

```
class FooError:
    pass

try:
    1 / 0
except FooError:  # [catching-non-exception]
    pass
```

**Correct code:**

```
class FooError(Exception):
    pass

try:
    1 / 0
except FooError:
    pass
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.