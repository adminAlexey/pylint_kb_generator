---
id: pylint-W1202
rule_code: "W1202"
rule_name: "logging-format-interpolation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/logging-format-interpolation.html"
---
# logging-format-interpolation / W1202

**Message emitted:**

`Use %s formatting in logging functions`

**Description:**

*Used when a logging statement has a call form of "logging.<logging method>(format_string.format(format_args...))". Use another type of string formatting instead. You can use % formatting but leave interpolation to the logging function by passing the parameters as arguments. If logging-fstring-interpolation is disabled then you can use fstring formatting. If logging-not-lazy is disabled then you can use % formatting as normal.*

**Problematic code:**

```
import logging
import sys

# +1: [logging-format-interpolation]
logging.error("Python version: {}".format(sys.version))
```

**Correct code:**

```
import logging
import sys

logging.error("Python version: %s", sys.version)
```

**Additional details:**

Another reasonable option is to use f-string. If you want to do that, you need to enable
`logging-format-interpolation` and disable `logging-fstring-interpolation`.

**Related links:**

- [logging variable data](https://docs.python.org/3/howto/logging.html#logging-variable-data)
- [Rationale for the message on stackoverflow](https://stackoverflow.com/a/34634301/2519059)

Created by the [logging](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/logging.py) checker.