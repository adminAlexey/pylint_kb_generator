---
id: pylint-C0114
rule_code: "C0114"
rule_name: "missing-module-docstring"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-module-docstring.html"
---
# missing-module-docstring / C0114

**Message emitted:**

`Missing module docstring`

**Description:**

*Used when a module has no docstring. Empty modules do not require a docstring.*

**Problematic code:**

```
import sys  # [missing-module-docstring]

def print_python_version():
    print(sys.version)
```

**Correct code:**

```
"""Module providing a function printing python version."""

import sys

def print_python_version():
    print(sys.version)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/docstring_checker.py) checker.