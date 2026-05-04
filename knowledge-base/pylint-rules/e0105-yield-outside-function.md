---
id: pylint-E0105
rule_code: "E0105"
rule_name: "yield-outside-function"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/yield-outside-function.html"
---
# yield-outside-function / E0105

**Message emitted:**

`Yield outside function`

**Description:**

*Used when a "yield" statement is found outside a function or method.*

**Problematic code:**

```
for i in range(10):
    yield i  # [yield-outside-function]
```

**Correct code:**

```
def one_to_ten():
    for i in range(10):
        yield i
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.