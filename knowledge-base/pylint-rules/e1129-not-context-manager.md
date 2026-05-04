---
id: pylint-E1129
rule_code: "E1129"
rule_name: "not-context-manager"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/not-context-manager.html"
---
# not-context-manager / E1129

**Message emitted:**

`Context manager '%s' doesn't implement __enter__ and __exit__.`

**Description:**

*Used when an instance in a with statement doesn't implement the context manager protocol(__enter__/__exit__).*

**Problematic code:**

```
class MyContextManager:
    def __enter__(self):
        pass

with MyContextManager() as c:  # [not-context-manager]
    pass
```

**Correct code:**

```
class MyContextManager:
    def __enter__(self):
        pass

    def __exit__(self, *exc):
        pass

with MyContextManager() as c:
    pass
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.