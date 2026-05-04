---
id: pylint-W4904
rule_code: "W4904"
rule_name: "deprecated-class"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/deprecated-class.html"
---
# deprecated-class / W4904

**Message emitted:**

`Using deprecated class %s of module %s`

**Description:**

*The class is marked as deprecated and will be removed in the future.*

**Problematic code:**

```
from collections import Iterable  # [deprecated-class]
```

**Correct code:**

```
from collections.abc import Iterable
```

**Additional details:**

The actual replacement needs to be studied on a case by case basis
by reading the deprecation warning or the release notes.

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.