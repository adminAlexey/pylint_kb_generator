---
id: pylint-E1132
rule_code: "E1132"
rule_name: "repeated-keyword"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/repeated-keyword.html"
---
# repeated-keyword / E1132

**Message emitted:**

`Got multiple values for keyword argument %r in function call`

**Description:**

*Emitted when a function call got multiple values for a keyword.*

**Problematic code:**

```
def func(a, b, c):
    return a, b, c

func(1, 2, c=3, **{"c": 4})  # [repeated-keyword]
func(1, 2, **{"c": 3}, **{"c": 4})  # [repeated-keyword]
```

**Correct code:**

```
def func(a, b, c):
    return a, b, c

func(1, 2, c=3)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.