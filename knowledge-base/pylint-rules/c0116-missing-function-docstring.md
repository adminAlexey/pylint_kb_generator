---
id: pylint-C0116
rule_code: "C0116"
rule_name: "missing-function-docstring"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-function-docstring.html"
---
# missing-function-docstring / C0116

**Message emitted:**

`Missing function or method docstring`

**Description:**

*Used when a function or method has no docstring. Some special methods like __init__ do not require a docstring.*

**Problematic code:**

```
import sys

def print_python_version():  # [missing-function-docstring]
    print(sys.version)
```

**Correct code:**

```
import sys

def print_python_version():
    """Function printing python version."""
    print(sys.version)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/docstring_checker.py) checker.