---
id: pylint-R2004
rule_code: "R2004"
rule_name: "magic-value-comparison"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/magic-value-comparison.html"
---
# magic-value-comparison / R2004

**Message emitted:**

`Consider using a named constant or an enum instead of '%s'.`

**Description:**

*Using named constants instead of magic values helps improve readability and maintainability of your code, try to avoid them in comparisons.*

**Problematic code:**

```
import random

measurement = random.randint(0, 200)
above_threshold = False
i = 0
while i < 5:  # [magic-value-comparison]
    above_threshold = measurement > 100  # [magic-value-comparison]
    if above_threshold:
        break
    measurement = random.randint(0, 200)
```

**Correct code:**

```
import random

MAX_NUM_OF_ITERATIONS = 5
THRESHOLD_VAL = 100
MIN_MEASUREMENT_VAL = 0
MAX_MEASUREMENT_VAL = 200

measurement = random.randint(MIN_MEASUREMENT_VAL, MAX_MEASUREMENT_VAL)
above_threshold = False
i = 0
while i < MAX_NUM_OF_ITERATIONS:
    above_threshold = measurement > THRESHOLD_VAL
    if above_threshold:
        break
    measurement = random.randint(MIN_MEASUREMENT_VAL, MAX_MEASUREMENT_VAL)
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.magic_value
```

Note

This message is emitted by the optional ['magic-value'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-magic-value)
checker, which requires the `pylint.extensions.magic_value` plugin to be loaded.

Created by the [magic-value](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/magic_value.py) checker.