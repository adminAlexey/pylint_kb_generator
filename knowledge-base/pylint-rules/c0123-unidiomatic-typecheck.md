---
id: pylint-C0123
rule_code: "C0123"
rule_name: "unidiomatic-typecheck"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/unidiomatic-typecheck.html"
---
# unidiomatic-typecheck / C0123

**Message emitted:**

`Use isinstance() rather than type() for a typecheck.`

**Description:**

*The idiomatic way to perform an explicit typecheck in Python is to use isinstance(x, Y) rather than type(x) == Y, type(x) is Y. Though there are unusual situations where these give different results.*

**Problematic code:**

```
test_score = {"Biology": 95, "History": 80}
if type(test_score) is dict:  # [unidiomatic-typecheck]
    pass
```

**Correct code:**

```
test_score = {"Biology": 95, "History": 80}
if isinstance(test_score, dict):
    pass
```

**Related links:**

- [Builtin function type()](https://docs.python.org/3/library/functions.html#type)
- [Builtin function isinstance()](https://docs.python.org/3/library/functions.html#isinstance)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/comparison_checker.py) checker.