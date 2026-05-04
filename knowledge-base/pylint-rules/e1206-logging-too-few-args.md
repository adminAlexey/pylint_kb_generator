---
id: pylint-E1206
rule_code: "E1206"
rule_name: "logging-too-few-args"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/logging-too-few-args.html"
---
# logging-too-few-args / E1206

**Message emitted:**

`Not enough arguments for logging format string`

**Description:**

*Used when a logging format string is given too few arguments.*

**Problematic code:**

```
import logging

try:
    function()
except Exception as e:
    logging.error("%s error occurred: %s", e)  # [logging-too-few-args]
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