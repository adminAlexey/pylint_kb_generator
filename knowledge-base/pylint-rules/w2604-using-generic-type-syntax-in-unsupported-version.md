---
id: pylint-W2604
rule_code: "W2604"
rule_name: "using-generic-type-syntax-in-unsupported-version"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/using-generic-type-syntax-in-unsupported-version.html"
---
# using-generic-type-syntax-in-unsupported-version / W2604

**Message emitted:**

`Generic type syntax (PEP 695) is not supported by all versions included in the py-version setting`

**Description:**

*Used when the py-version set by the user is lower than 3.12 and pylint encounters generic type syntax.*

**Problematic code:**

```
type Vector = list[float]  # [using-generic-type-syntax-in-unsupported-version]
```

**Correct code:**

```
from typing import TypeAlias

Vector: TypeAlias = list[float]
```

**Configuration file:**

```
[main]
py-version=3.11
```

**Additional details:**

Generic type syntax was introduced in Python 3.12; to use it, please use a more recent version of Python.

Created by the [unsupported_version](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unsupported_version.py) checker.