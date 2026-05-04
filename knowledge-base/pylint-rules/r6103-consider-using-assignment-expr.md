---
id: pylint-R6103
rule_code: "R6103"
rule_name: "consider-using-assignment-expr"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-assignment-expr.html"
---
# consider-using-assignment-expr / R6103

**Message emitted:**

`Use '%s' instead`

**Description:**

*Emitted when an if assignment is directly followed by an if statement and both can be combined by using an assignment expression ``:=``. Requires Python 3.8 and ``py-version >= 3.8``.*

**Problematic code:**

```
apples = 2

if apples:  # [consider-using-assignment-expr]
    print("God apples!")
```

**Correct code:**

```
if apples := 2:
    print("God apples!")
```

**Configuration file:**

```
[MAIN]
py-version=3.8
load-plugins=pylint.extensions.code_style
```

Note

This message is emitted by the optional ['code_style'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-code-style)
checker, which requires the `pylint.extensions.code_style` plugin to be loaded.

Created by the [code_style](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/code_style.py) checker.