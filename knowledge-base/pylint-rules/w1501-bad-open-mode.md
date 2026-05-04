---
id: pylint-W1501
rule_code: "W1501"
rule_name: "bad-open-mode"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-open-mode.html"
---
# bad-open-mode / W1501

**Message emitted:**

`"%s" is not a valid mode for open.`

**Description:**

*Python supports: r, w, a[, x] modes with b, +, and U (only with r) options. See https://docs.python.org/3/library/functions.html#open*

**Problematic code:**

```
def open_and_get_content(file_path):
    with open(file_path, "rwx") as file:  # [bad-open-mode]
        return file.read()
```

**Correct code:**

```
def open_and_get_content(file_path):
    with open(file_path, "r") as file:
        return file.read()
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.