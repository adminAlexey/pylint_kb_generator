---
id: pylint-W0160
rule_code: "W0160"
rule_name: "consider-ternary-expression"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/consider-ternary-expression.html"
---
# consider-ternary-expression / W0160

**Message emitted:**

`Consider rewriting as a ternary expression`

**Description:**

*Multiple assign statements spread across if/else blocks can be rewritten with a single assignment and ternary expression*

**Problematic code:**

```
x, y = input(), input()
if x >= y:  # [consider-ternary-expression]
    maximum = x
else:
    maximum = y
```

**Correct code:**

```
x, y = input(), input()
maximum = x if x >= y else y
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.consider_ternary_expression
```

Note

This message is emitted by the optional ['consider_ternary_expression'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-consider-ternary-expression)
checker, which requires the `pylint.extensions.consider_ternary_expression` plugin to be loaded.

Created by the [consider_ternary_expression](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/consider_ternary_expression.py) checker.