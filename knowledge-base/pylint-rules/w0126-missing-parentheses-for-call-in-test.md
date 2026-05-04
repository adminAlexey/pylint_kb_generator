---
id: pylint-W0126
rule_code: "W0126"
rule_name: "missing-parentheses-for-call-in-test"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-parentheses-for-call-in-test.html"
---
# missing-parentheses-for-call-in-test / W0126

**Message emitted:**

`Using a conditional statement with potentially wrong function or method call due to missing parentheses`

**Description:**

*Emitted when a conditional statement (If or ternary if) seems to wrongly call a function due to missing parentheses*

**Problematic code:**

```
import random

def is_it_a_good_day():
    return random.choice([True, False])

if is_it_a_good_day:  # [missing-parentheses-for-call-in-test]
    print("Today is a good day!")
```

**Correct code:**

```
import random

def is_it_a_good_day():
    return random.choice([True, False])

if is_it_a_good_day():
    print("Today is a good day!")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.