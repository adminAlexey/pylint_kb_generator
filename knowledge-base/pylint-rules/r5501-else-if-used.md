---
id: pylint-R5501
rule_code: "R5501"
rule_name: "else-if-used"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/else-if-used.html"
---
# else-if-used / R5501

**Message emitted:**

`Consider using "elif" instead of "else" then "if" to remove one indentation level`

**Description:**

*Used when an else statement is immediately followed by an if statement and does not contain statements that would be unrelated to it.*

**Problematic code:**

```
if input():
    pass
else:
    if len(input()) >= 10:  # [else-if-used]
        pass
    else:
        pass
```

**Correct code:**

```
if input():
    pass
elif len(input()) >= 10:
    pass
else:
    pass
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.check_elif
```

Note

This message is emitted by the optional ['else_if_used'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-check-elif)
checker, which requires the `pylint.extensions.check_elif` plugin to be loaded.

Created by the [else_if_used](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/check_elif.py) checker.