---
id: pylint-E1701
rule_code: "E1701"
rule_name: "not-async-context-manager"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/not-async-context-manager.html"
---
# not-async-context-manager / E1701

**Message emitted:**

`Async context manager '%s' doesn't implement __aenter__ and __aexit__.`

**Description:**

*Used when an async context manager is used with an object that does not implement the async context management protocol.*

**Problematic code:**

```
class ContextManager:
    def __enter__(self):
        pass

    def __exit__(self, *exc):
        pass

async def foo():
    async with ContextManager():  # [not-async-context-manager]
        pass
```

**Correct code:**

```
class AsyncContextManager:
    def __aenter__(self):
        pass

    def __aexit__(self, *exc):
        pass

async def foo():
    async with AsyncContextManager():
        pass
```

**Additional details:**

Async context manager doesn't implement `__aenter__` and `__aexit__`. It can't be emitted when using Python < 3.5.

Created by the [async](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/async_checker.py) checker.