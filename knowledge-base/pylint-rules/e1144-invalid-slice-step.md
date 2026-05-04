---
id: pylint-E1144
rule_code: "E1144"
rule_name: "invalid-slice-step"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-slice-step.html"
---
# invalid-slice-step / E1144

**Message emitted:**

`Slice step cannot be 0`

**Description:**

*Used when a slice step is 0 and the object doesn't implement a custom __getitem__ method.*

**Problematic code:**

```
LETTERS = ["a", "b", "c", "d"]

LETTERS[::0]  # [invalid-slice-step]
```

**Correct code:**

```
LETTERS = ["a", "b", "c", "d"]

LETTERS[::2]
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.