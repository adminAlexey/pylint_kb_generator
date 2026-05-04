---
id: pylint-E1142
rule_code: "E1142"
rule_name: "await-outside-async"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/await-outside-async.html"
---
# await-outside-async / E1142

**Message emitted:**

`'await' should be used within an async function`

**Description:**

*Emitted when await is used outside an async function.*

**Problematic code:**

```
import asyncio

def main():
    await asyncio.sleep(1)  # [await-outside-async]
```

**Correct code:**

```
import asyncio

async def main():
    await asyncio.sleep(1)
```

**Related links:**

- [PEP 492](https://peps.python.org/pep-0492/#await-expression)

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.