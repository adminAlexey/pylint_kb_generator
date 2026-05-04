---
id: pylint-E1507
rule_code: "E1507"
rule_name: "invalid-envvar-value"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-envvar-value.html"
---
# invalid-envvar-value / E1507

**Message emitted:**

`%s does not support %s type argument`

**Description:**

*Env manipulation functions support only string type arguments. See https://docs.python.org/3/library/os.html#os.getenv.*

**Problematic code:**

```
import os

os.getenv(1)  # [invalid-envvar-value]
```

**Correct code:**

```
import os

os.getenv("1")
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.