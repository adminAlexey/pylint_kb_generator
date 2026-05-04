---
id: pylint-W2606
rule_code: "W2606"
rule_name: "using-positional-only-args-in-unsupported-version"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/using-positional-only-args-in-unsupported-version.html"
---
# using-positional-only-args-in-unsupported-version / W2606

**Message emitted:**

`Positional-only arguments are not supported by all versions included in the py-version setting`

**Description:**

*Used when the py-version set by the user is lower than 3.8 and pylint encounters positional-only arguments.*

**Problematic code:**

```
def add(x, y, /):  # [using-positional-only-args-in-unsupported-version]
    return x + y
```

**Correct code:**

```
# pylint: disable=missing-function-docstring, missing-module-docstring
def add(x, y):
    return x + y
```

**Configuration file:**

```
[main]
py-version=3.7
```

**Additional details:**

Positional-only arguments were introduced in Python 3.8; to use them, please use a more recent version of Python.

Created by the [unsupported_version](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unsupported_version.py) checker.