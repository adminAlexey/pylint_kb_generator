---
id: pylint-W0410
rule_code: "W0410"
rule_name: "misplaced-future"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/misplaced-future.html"
---
# misplaced-future / W0410

**Message emitted:**

`__future__ import is not the first non docstring statement`

**Description:**

*Python 2.5 and greater require __future__ import to be the first non docstring statement in the module.*

**Problematic code:**

```
import sys

from __future__ import print_function  # [misplaced-future]
```

**Correct code:**

```
from __future__ import print_function

import sys
```

**Additional details:**

A bare raise statement will re-raise the last active exception in the current scope. If the `raise` statement is not in an `except` or `finally` block, a RuntimeError will be raised instead.

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.