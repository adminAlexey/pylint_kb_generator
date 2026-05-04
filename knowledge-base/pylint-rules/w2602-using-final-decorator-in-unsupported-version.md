---
id: pylint-W2602
rule_code: "W2602"
rule_name: "using-final-decorator-in-unsupported-version"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/using-final-decorator-in-unsupported-version.html"
---
# using-final-decorator-in-unsupported-version / W2602

**Message emitted:**

`typing.final is not supported by all versions included in the py-version setting`

**Description:**

*Used when the py-version set by the user is lower than 3.8 and pylint encounters a ``typing.final`` decorator.*

**Problematic code:**

```
from typing import final

@final  # [using-final-decorator-in-unsupported-version]
class Playtypus(Animal):
    @final  # [using-final-decorator-in-unsupported-version]
    def lay_egg(self): ...
```

**Correct code:**

```
class Playtypus(Animal):
    def lay_egg(self): ...
```

**Configuration file:**

```
[main]
py-version=3.7
```

**Additional details:**

The message is emitted when the `final` decorator is used with a Python version less than 3.8.
The `final` decorator was introduced in Python version 3.8.

**Related links:**

- [PEP 591](https://peps.python.org/pep-0591/#the-final-decorator)

Created by the [unsupported_version](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unsupported_version.py) checker.