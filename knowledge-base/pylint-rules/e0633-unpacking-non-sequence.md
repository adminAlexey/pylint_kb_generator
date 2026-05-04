---
id: pylint-E0633
rule_code: "E0633"
rule_name: "unpacking-non-sequence"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unpacking-non-sequence.html"
---
# unpacking-non-sequence / E0633

**Message emitted:**

`Attempting to unpack a non-sequence%s`

**Description:**

*Used when something which is not a sequence is used in an unpack assignment*

**Problematic code:**

```
a, b, c = 1  # [unpacking-non-sequence]
```

**Correct code:**

```
a, b, c = 1, 2, 3
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.