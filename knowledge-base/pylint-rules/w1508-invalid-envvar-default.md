---
id: pylint-W1508
rule_code: "W1508"
rule_name: "invalid-envvar-default"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/invalid-envvar-default.html"
---
# invalid-envvar-default / W1508

**Message emitted:**

`%s default type is %s. Expected str or None.`

**Description:**

*Env manipulation functions return None or str values. Supplying anything different as a default may cause bugs. See https://docs.python.org/3/library/os.html#os.getenv.*

**Problematic code:**

```
import os

env = os.getenv("SECRET_KEY", 1)  # [invalid-envvar-default]
```

**Correct code:**

```
import os

env = os.getenv("SECRET_KEY", "1")
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.