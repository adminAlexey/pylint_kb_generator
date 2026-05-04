---
id: pylint-W1302
rule_code: "W1302"
rule_name: "bad-format-string"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-format-string.html"
---
# bad-format-string / W1302

**Message emitted:**

`Invalid format string`

**Description:**

*Used when a PEP 3101 format string is invalid.*

**Problematic code:**

```
print("{a[0] + a[1]}".format(a=[0, 1]))  # [bad-format-string]
```

**Correct code:**

```
print("{a[0]} + {a[1]}".format(a=[0, 1]))
```

**Related links:**

- [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
- [PyFormat](https://pyformat.info/)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.