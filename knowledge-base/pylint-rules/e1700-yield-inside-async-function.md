---
id: pylint-E1700
rule_code: "E1700"
rule_name: "yield-inside-async-function"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/yield-inside-async-function.html"
---
# yield-inside-async-function / E1700

**Message emitted:**

`Yield inside async function`

**Description:**

*Used when an `yield` or `yield from` statement is found inside an async function.*

**Problematic code:**

```
async def foo():
    yield from [1, 2, 3]  # [yield-inside-async-function]
```

**Correct code:**

```
async def foo():
    def _inner_foo():
        yield from [1, 2, 3]

async def foo():
    yield 42
```

**Additional details:**

The message can't be emitted when using Python < 3.5.

**Related links:**

- [PEP 525](https://peps.python.org/pep-0525/)

Created by the [async](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/async_checker.py) checker.