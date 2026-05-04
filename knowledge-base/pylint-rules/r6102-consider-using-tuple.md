---
id: pylint-R6102
rule_code: "R6102"
rule_name: "consider-using-tuple"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-tuple.html"
---
# consider-using-tuple / R6102

**Message emitted:**

`Consider using an in-place tuple instead of list`

**Description:**

*Only for style consistency! Emitted where an in-place defined ``list`` can be replaced by a ``tuple``. Due to optimizations by CPython, there is no performance benefit from it.*

**Problematic code:**

```
for i in [1, 2, 3]:  # [consider-using-tuple]
    print(i)
```

**Correct code:**

```
for i in (1, 2, 3):
    print(i)
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.code_style
```

Note

This message is emitted by the optional ['code_style'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-code-style)
checker, which requires the `pylint.extensions.code_style` plugin to be loaded.

Created by the [code_style](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/code_style.py) checker.