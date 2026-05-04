---
id: pylint-W2605
rule_code: "W2605"
rule_name: "using-assignment-expression-in-unsupported-version"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/using-assignment-expression-in-unsupported-version.html"
---
# using-assignment-expression-in-unsupported-version / W2605

**Message emitted:**

`Assignment expression is not supported by all versions included in the py-version setting`

**Description:**

*Used when the py-version set by the user is lower than 3.8 and pylint encounters an assignment expression (walrus) operator.*

**Problematic code:**

```
import random

# +1: [using-assignment-expression-in-unsupported-version]
if zero_or_one := random.randint(0, 1):
    assert zero_or_one == 1
```

**Correct code:**

```
import random

zero_or_one = random.randint(0, 1)
if zero_or_one:
    assert zero_or_one == 1
```

**Configuration file:**

```
[main]
py-version=3.7
```

**Additional details:**

The assignment expression (walrus) operator (:=) was introduced in Python 3.8; to use it, please use a more recent version of Python.

Created by the [unsupported_version](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unsupported_version.py) checker.