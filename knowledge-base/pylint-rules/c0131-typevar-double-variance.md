---
id: pylint-C0131
rule_code: "C0131"
rule_name: "typevar-double-variance"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/typevar-double-variance.html"
---
# typevar-double-variance / C0131

**Message emitted:**

`TypeVar cannot be both covariant and contravariant`

**Description:**

*Emitted when both the "covariant" and "contravariant" keyword arguments are set to "True" in a TypeVar.*

**Problematic code:**

```
from typing import TypeVar

T = TypeVar("T", covariant=True, contravariant=True)  # [typevar-double-variance]
```

**Correct code:**

```
from typing import TypeVar

T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/name_checker/checker.py) checker.