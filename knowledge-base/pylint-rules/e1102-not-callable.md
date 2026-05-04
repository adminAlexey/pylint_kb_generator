---
id: pylint-E1102
rule_code: "E1102"
rule_name: "not-callable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/not-callable.html"
---
# not-callable / E1102

**Message emitted:**

`%s is not callable`

**Description:**

*Used when an object being called has been inferred to a non callable object.*

**Problematic code:**

```
NUMBER = 42
print(NUMBER())  # [not-callable]
```

**Correct code:**

```
NUMBER = 42
print(NUMBER)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.