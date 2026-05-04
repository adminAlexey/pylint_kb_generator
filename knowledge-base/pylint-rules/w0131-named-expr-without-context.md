---
id: pylint-W0131
rule_code: "W0131"
rule_name: "named-expr-without-context"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/named-expr-without-context.html"
---
# named-expr-without-context / W0131

**Message emitted:**

`Named expression used without context`

**Description:**

*Emitted if named expression is used to do a regular assignment outside a context like if, for, while, or a comprehension.*

**Problematic code:**

```
(a := 42)  # [named-expr-without-context]
```

**Correct code:**

```
if a := 42:
    print("Success")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.