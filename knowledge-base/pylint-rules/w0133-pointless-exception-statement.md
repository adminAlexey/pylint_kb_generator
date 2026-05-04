---
id: pylint-W0133
rule_code: "W0133"
rule_name: "pointless-exception-statement"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/pointless-exception-statement.html"
---
# pointless-exception-statement / W0133

**Message emitted:**

`Exception statement has no effect`

**Description:**

*Used when an exception is created without being assigned, raised or returned for subsequent use elsewhere.*

**Problematic code:**

```
Exception("This exception is a statement.")  # [pointless-exception-statement]
```

**Correct code:**

```
raise Exception("This will raise.")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.