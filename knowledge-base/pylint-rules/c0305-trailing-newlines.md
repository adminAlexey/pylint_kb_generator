---
id: pylint-C0305
rule_code: "C0305"
rule_name: "trailing-newlines"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/trailing-newlines.html"
---
# trailing-newlines / C0305

**Message emitted:**

`Trailing newlines`

**Description:**

*Used when there are trailing blank lines in a file.*

**Problematic code:**

```
print("apple")
# The file ends with 2 lines that are empty # +1: [trailing-newlines]
```

**Correct code:**

```
print("apple")
```

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.