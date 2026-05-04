---
id: pylint-E0102
rule_code: "E0102"
rule_name: "function-redefined"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/function-redefined.html"
---
# function-redefined / E0102

**Message emitted:**

`%s already defined line %s`

**Description:**

*Used when a function / class / method is redefined.*

**Problematic code:**

```
def get_email():
    pass

def get_email():  # [function-redefined]
    pass
```

**Correct code:**

```
def get_email():
    pass
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.