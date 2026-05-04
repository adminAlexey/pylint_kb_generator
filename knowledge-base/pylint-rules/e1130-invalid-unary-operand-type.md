---
id: pylint-E1130
rule_code: "E1130"
rule_name: "invalid-unary-operand-type"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-unary-operand-type.html"
---
# invalid-unary-operand-type / E1130

**Message emitted:**

`%s`

**Description:**

*Emitted when a unary operand is used on an object which does not support this type of operation.*

**Problematic code:**

```
cherries = 10
eaten_cherries = int
cherries = -eaten_cherries  # [invalid-unary-operand-type]
```

**Correct code:**

```
cherries = 10
eaten_cherries = 2
cherries -= eaten_cherries
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.