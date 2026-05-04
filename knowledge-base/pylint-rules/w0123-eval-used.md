---
id: pylint-W0123
rule_code: "W0123"
rule_name: "eval-used"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/eval-used.html"
---
# eval-used / W0123

**Message emitted:**

`Use of eval`

**Description:**

*Used when you use the "eval" function, to discourage its usage. Consider using `ast.literal_eval` for safely evaluating strings containing Python expressions from untrusted sources.*

**Problematic code:**

```
eval("[1, 2, 3]")  # [eval-used]
```

**Correct code:**

```
from ast import literal_eval

literal_eval("[1, 2, 3]")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.