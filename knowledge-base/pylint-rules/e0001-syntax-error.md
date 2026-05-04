---
id: pylint-E0001
rule_code: "E0001"
rule_name: "syntax-error"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/syntax-error.html"
---
# syntax-error / E0001

**Message emitted:**

`%s`

**Description:**

*Used when a syntax error is raised for a module.*

**Problematic code:**

```
fruit_stock = {
    'apple': 42,
    'orange': 21  # [syntax-error]
    'banana': 12
}
```

**Correct code:**

```
fruit_stock = {"apple": 42, "orange": 21, "banana": 12}
```

**Additional details:**

The python's ast builtin module cannot parse your code if there's a syntax error, so
if there's a syntax error other messages won't be available at all.

**Related links:**

- [Why can't pylint recover from a syntax error ?](https://stackoverflow.com/a/78419051/2519059)

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.