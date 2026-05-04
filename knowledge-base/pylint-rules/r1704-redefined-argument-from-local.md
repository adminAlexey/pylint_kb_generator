---
id: pylint-R1704
rule_code: "R1704"
rule_name: "redefined-argument-from-local"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/redefined-argument-from-local.html"
---
# redefined-argument-from-local / R1704

**Message emitted:**

`Redefining argument with the local name %r`

**Description:**

*Used when a local name is redefining an argument, which might suggest a potential error. This is taken in account only for a handful of name binding operations, such as for iteration, with statement assignment and exception handler assignment.*

**Problematic code:**

```
def show(host_id=10.11):
    # +1: [redefined-argument-from-local]
    for host_id, host in [[12.13, "Venus"], [14.15, "Mars"]]:
        print(host_id, host)
```

**Correct code:**

```
def show(host_id=10.11):
    for inner_host_id, host in [[12.13, "Venus"], [14.15, "Mars"]]:
        print(host_id, inner_host_id, host)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.