---
id: pylint-C0303
rule_code: "C0303"
rule_name: "trailing-whitespace"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/trailing-whitespace.html"
---
# trailing-whitespace / C0303

**Message emitted:**

`Trailing whitespace`

**Description:**

*Used when there is whitespace between the end of a line and the newline.*

**Problematic code:**

```
print("Hello")  # [trailing-whitespace]   
#                                       ^^^ trailing whitespaces
```

**Correct code:**

```
print("Hello")
```

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.