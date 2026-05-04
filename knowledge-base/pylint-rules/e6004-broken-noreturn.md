---
id: pylint-E6004
rule_code: "E6004"
rule_name: "broken-noreturn"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/broken-noreturn.html"
---
# broken-noreturn / E6004

**Message emitted:**

`'NoReturn' inside compound types is broken in 3.7.0 / 3.7.1`

**Description:**

*``typing.NoReturn`` inside compound types is broken in Python 3.7.0 and 3.7.1. If not dependent on runtime introspection, use string annotation instead. E.g. ``Callable[..., 'NoReturn']``. https://bugs.python.org/issue34921*

**Problematic code:**

```
from typing import NoReturn, Union

def exploding_apple(apple) -> Union[None, NoReturn]:  # [broken-noreturn]
    print(f"{apple} is about to explode")
```

**Correct code:**

```
from typing import NoReturn

def exploding_apple(apple) -> NoReturn:
    print(f"{apple} is about to explode")
    raise Exception("{apple} exploded !")
```

**Configuration file:**

```
[main]
py-version=3.7
load-plugins=pylint.extensions.typing
```

Note

This message is emitted by the optional ['typing'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-typing)
checker, which requires the `pylint.extensions.typing` plugin to be loaded.

Created by the [typing](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/typing.py) checker.