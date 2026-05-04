---
id: pylint-W2901
rule_code: "W2901"
rule_name: "redefined-loop-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redefined-loop-name.html"
---
# redefined-loop-name / W2901

**Message emitted:**

`Redefining %r from loop (line %s)`

**Description:**

*Used when a loop variable is overwritten in the loop body.*

**Problematic code:**

```
def normalize_names(names):
    for name in names:
        name = name.lower()  # [redefined-loop-name]
```

**Correct code:**

```
def normalize_names(names):
    for name in names:
        lowercased_name = name.lower()
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.redefined_loop_name,
```

Note

This message is emitted by the optional ['redefined-loop-name'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-redefined-loop-name)
checker, which requires the `pylint.extensions.redefined_loop_name` plugin to be loaded.

Created by the [redefined-loop-name](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/redefined_loop_name.py) checker.