---
id: pylint-E1145
rule_code: "E1145"
rule_name: "async-context-manager-with-regular-with"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/async-context-manager-with-regular-with.html"
---
# async-context-manager-with-regular-with / E1145

**Message emitted:**

`Context manager '%s' is async and should be used with 'async with'.`

**Description:**

*Used when an async context manager is used with a regular 'with' statement instead of 'async with'.*

**Problematic code:**

```
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_context():
    yield

with async_context():  # [async-context-manager-with-regular-with]
    print("This will cause an error at runtime")
```

**Correct code:**

```
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_context():
    yield

async def main():
    async with async_context():
        print("This works correctly")
```

**Related links:**

- [PEP 492 - Coroutines with async and await syntax](https://peps.python.org/pep-0492/)
- [contextlib.asynccontextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.