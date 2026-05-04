---
id: pylint-R6105
rule_code: "R6105"
rule_name: "prefer-typing-namedtuple"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/prefer-typing-namedtuple.html"
---
# prefer-typing-namedtuple / R6105

**Message emitted:**

`Prefer 'typing.NamedTuple' over 'collections.namedtuple'`

**Description:**

*'typing.NamedTuple' uses the well-known 'class' keyword with type-hints for readability (it's also faster as it avoids an internal exec call).
Disabled by default!*

Caution

This message is disabled by default. To enable it, add `prefer-typing-namedtuple` to the `enable` option.

**Problematic code:**

```
from collections import namedtuple

Philosophy = namedtuple(  # [prefer-typing-namedtuple]
    "Philosophy", ("goodness", "truth", "beauty")
)
```

**Correct code:**

```
from typing import NamedTuple

class Philosophy(NamedTuple):
    goodness: str
    truth: bool
    beauty: float
```

**Configuration file:**

```
[MAIN]
load-plugins = pylint.extensions.code_style
```

**Related links:**

- [typing.NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Note

This message is emitted by the optional ['code_style'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-code-style)
checker, which requires the `pylint.extensions.code_style` plugin to be loaded.

Created by the [code_style](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/code_style.py) checker.