---
id: pylint-W0311
rule_code: "W0311"
rule_name: "bad-indentation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-indentation.html"
---
# bad-indentation / W0311

**Message emitted:**

`Bad indentation. Found %s %s, expected %s`

**Description:**

*Used when an unexpected number of indentation's tabulations or spaces has been found.*

**Problematic code:**

```
if input():
   print('yes')  # [bad-indentation]
```

**Correct code:**

```
if input():
    print("yes")
```

**Additional details:**

The option `--indent-string` can be used to set the indentation unit for this check.

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.