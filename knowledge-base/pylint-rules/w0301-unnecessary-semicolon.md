---
id: pylint-W0301
rule_code: "W0301"
rule_name: "unnecessary-semicolon"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unnecessary-semicolon.html"
---
# unnecessary-semicolon / W0301

**Message emitted:**

`Unnecessary semicolon`

**Description:**

*Used when a statement is ended by a semi-colon (";"), which isn't necessary (that's python, not C ;).*

**Problematic code:**

```
print("Hello World!");  # [unnecessary-semicolon]
```

**Correct code:**

```
print("Hello World!")
```

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.