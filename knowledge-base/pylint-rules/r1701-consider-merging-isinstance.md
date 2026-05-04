---
id: pylint-R1701
rule_code: "R1701"
rule_name: "consider-merging-isinstance"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-merging-isinstance.html"
---
# consider-merging-isinstance / R1701

**Message emitted:**

`Consider merging these isinstance calls to isinstance(%s, (%s))`

**Description:**

*Used when multiple consecutive isinstance calls can be merged into one.*

**Problematic code:**

```
from typing import Any

def is_number(value: Any) -> bool:
    # +1: [consider-merging-isinstance]
    return isinstance(value, int) or isinstance(value, float)
```

**Correct code:**

```
from typing import Any

def is_number(value: Any) -> bool:
    return isinstance(value, (int, float))
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.