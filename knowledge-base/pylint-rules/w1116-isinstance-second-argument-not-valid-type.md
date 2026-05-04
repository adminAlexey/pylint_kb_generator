---
id: pylint-W1116
rule_code: "W1116"
rule_name: "isinstance-second-argument-not-valid-type"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/isinstance-second-argument-not-valid-type.html"
---
# isinstance-second-argument-not-valid-type / W1116

**Message emitted:**

`Second argument of isinstance is not a type`

**Description:**

*Emitted when the second argument of an isinstance call is not a type.*

**Problematic code:**

```
isinstance("apples and oranges", hex)  # [isinstance-second-argument-not-valid-type]
```

**Correct code:**

```
isinstance("apples and oranges", str)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.