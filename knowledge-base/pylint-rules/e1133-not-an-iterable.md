---
id: pylint-E1133
rule_code: "E1133"
rule_name: "not-an-iterable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/not-an-iterable.html"
---
# not-an-iterable / E1133

**Message emitted:**

`Non-iterable value %s is used in an iterating context`

**Description:**

*Used when a non-iterable value is used in place where iterable is expected*

**Problematic code:**

```
for i in 10:  # [not-an-iterable]
    pass
```

**Correct code:**

```
for i in "10":
    pass
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.