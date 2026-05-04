---
id: pylint-E0108
rule_code: "E0108"
rule_name: "duplicate-argument-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/duplicate-argument-name.html"
---
# duplicate-argument-name / E0108

**Message emitted:**

`Duplicate argument name %r in function definition`

**Description:**

*Duplicate argument names in function definitions are syntax errors.*

**Problematic code:**

```
def get_fruits(apple, banana, apple):  # [duplicate-argument-name]
    pass
```

**Correct code:**

```
def get_fruits(apple, banana, orange):
    pass
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.