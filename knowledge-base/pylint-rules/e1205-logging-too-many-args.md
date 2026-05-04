---
id: pylint-E1205
rule_code: "E1205"
rule_name: "logging-too-many-args"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/logging-too-many-args.html"
---
# logging-too-many-args / E1205

**Message emitted:**

`Too many arguments for logging format string`

**Description:**

*Used when a logging format string is given too many arguments.*

**Problematic code:**

```
import logging

try:
    function()
except Exception as e:
    logging.error("Error occurred: %s", type(e), e)  # [logging-too-many-args]
    raise
```

**Correct code:**

```
import logging

try:
    function()
except Exception as e:
    logging.error("%s error occurred: %s", type(e), e)
    raise
```

Created by the [logging](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/logging.py) checker.