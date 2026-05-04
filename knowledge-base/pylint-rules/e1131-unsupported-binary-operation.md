---
id: pylint-E1131
rule_code: "E1131"
rule_name: "unsupported-binary-operation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unsupported-binary-operation.html"
---
# unsupported-binary-operation / E1131

**Message emitted:**

`%s`

**Description:**

*Emitted when a binary arithmetic operation between two operands is not supported.*

**Problematic code:**

```
drink = "water" | None  # [unsupported-binary-operation]
result = [] | None  # [unsupported-binary-operation]
```

**Correct code:**

```
masked = 0b111111 & 0b001100
result = 0xAEFF | 0x0B99
```

**Configuration file:**

```
[main]
py-version=3.9
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.