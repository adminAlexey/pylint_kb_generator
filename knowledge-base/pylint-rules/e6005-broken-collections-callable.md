---
id: pylint-E6005
rule_code: "E6005"
rule_name: "broken-collections-callable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/broken-collections-callable.html"
---
# broken-collections-callable / E6005

**Message emitted:**

`'collections.abc.Callable' inside Optional and Union is broken in 3.9.0 / 3.9.1 (use 'typing.Callable' instead)`

**Description:**

*``collections.abc.Callable`` inside Optional and Union is broken in Python 3.9.0 and 3.9.1. Use ``typing.Callable`` for these cases instead. https://bugs.python.org/issue42965*

**Problematic code:**

```
from collections.abc import Callable
from typing import Optional

def func() -> Optional[Callable[[int], None]]:  # [broken-collections-callable]
    ...
```

**Correct code:**

```
from typing import Callable, Optional

def func() -> Optional[Callable[[int], None]]: ...
```

**Configuration file:**

```
[main]
py-version=3.9
load-plugins=pylint.extensions.typing
```

**Related links:**

- [bpo-42965](https://bugs.python.org/issue42965)

Note

This message is emitted by the optional ['typing'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-typing)
checker, which requires the `pylint.extensions.typing` plugin to be loaded.

Created by the [typing](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/typing.py) checker.