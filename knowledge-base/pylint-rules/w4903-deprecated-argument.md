---
id: pylint-W4903
rule_code: "W4903"
rule_name: "deprecated-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/deprecated-argument.html"
---
# deprecated-argument / W4903

**Message emitted:**

`Using deprecated argument %s of method %s()`

**Description:**

*The argument is marked as deprecated and will be removed in the future.*

**Problematic code:**

```
int(x=1)  # [deprecated-argument]
```

**Correct code:**

```
int(1)
```

**Configuration file:**

```

```

**Additional details:**

The actual replacement needs to be studied on a case by case basis
by reading the deprecation warning or the release notes.

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.