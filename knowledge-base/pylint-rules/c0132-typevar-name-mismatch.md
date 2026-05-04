---
id: pylint-C0132
rule_code: "C0132"
rule_name: "typevar-name-mismatch"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/typevar-name-mismatch.html"
---
# typevar-name-mismatch / C0132

**Message emitted:**

`TypeVar name "%s" does not match assigned variable name "%s"`

**Description:**

*Emitted when a TypeVar is assigned to a variable that does not match its name argument.*

**Problematic code:**

```
from typing import TypeVar

X = TypeVar("T")  # [typevar-name-mismatch]
```

**Correct code:**

```
from typing import TypeVar

T = TypeVar("T")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/name_checker/checker.py) checker.