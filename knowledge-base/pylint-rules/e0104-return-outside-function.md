---
id: pylint-E0104
rule_code: "E0104"
rule_name: "return-outside-function"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/return-outside-function.html"
---
# return-outside-function / E0104

**Message emitted:**

`Return outside function`

**Description:**

*Used when a "return" statement is found outside a function or method.*

**Problematic code:**

```
return 42  # [return-outside-function]
```

**Correct code:**

```
def get_the_answer():
    return 42
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.