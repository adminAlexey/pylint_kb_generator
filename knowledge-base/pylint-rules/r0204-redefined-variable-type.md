---
id: pylint-R0204
rule_code: "R0204"
rule_name: "redefined-variable-type"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/redefined-variable-type.html"
---
# redefined-variable-type / R0204

**Message emitted:**

`Redefinition of %s type from %s to %s`

**Description:**

*Used when the type of a variable changes inside a method or a function.*

**Problematic code:**

```
x = 1
x = "2"  # [redefined-variable-type]
```

**Correct code:**

```
x = 1
x = 2
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.redefined_variable_type,
```

Note

This message is emitted by the optional ['multiple_types'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-redefined-variable-type)
checker, which requires the `pylint.extensions.redefined_variable_type` plugin to be loaded.

Created by the [multiple_types](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/redefined_variable_type.py) checker.