---
id: pylint-E1125
rule_code: "E1125"
rule_name: "missing-kwoa"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/missing-kwoa.html"
---
# missing-kwoa / E1125

**Message emitted:**

`Missing mandatory keyword argument %r in %s call`

**Description:**

*Used when a function call does not pass a mandatory keyword-only argument.*

**Problematic code:**

```
def target(pos, *, keyword):
    return pos + keyword

def not_forwarding_kwargs(*args, **kwargs):
    target(*args)  # [missing-kwoa]
```

**Correct code:**

```
def target(pos, *, keyword):
    return pos + keyword

def not_forwarding_kwargs(*args, **kwargs):
    target(*args, **kwargs)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.