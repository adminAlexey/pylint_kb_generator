---
id: pylint-R6104
rule_code: "R6104"
rule_name: "consider-using-augmented-assign"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-augmented-assign.html"
---
# consider-using-augmented-assign / R6104

**Message emitted:**

`Use '%s' to do an augmented assign directly`

**Description:**

*Emitted when an assignment is referring to the object that it is assigning to. This can be changed to be an augmented assign.
Disabled by default!*

Caution

This message is disabled by default. To enable it, add `consider-using-augmented-assign` to the `enable` option.

**Problematic code:**

```
x = 1
x = x + 1  # [consider-using-augmented-assign]
```

**Correct code:**

```
x = 1
x += 1
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.code_style
enable=consider-using-augmented-assign
```

Note

This message is emitted by the optional ['code_style'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-code-style)
checker, which requires the `pylint.extensions.code_style` plugin to be loaded.

Created by the [code_style](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/code_style.py) checker.