---
id: pylint-W4902
rule_code: "W4902"
rule_name: "deprecated-method"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/deprecated-method.html"
---
# deprecated-method / W4902

**Message emitted:**

`Using deprecated method %s()`

**Description:**

*The method is marked as deprecated and will be removed in the future.*

**Problematic code:**

```
import logging

logging.warn("I'm coming, world !")  # [deprecated-method]
```

**Correct code:**

```
import logging

logging.warning("I'm coming, world !")
```

**Additional details:**

The actual replacement needs to be studied on a case by case basis
by reading the deprecation warning or the release notes.

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.