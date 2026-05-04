---
id: pylint-C0105
rule_code: "C0105"
rule_name: "typevar-name-incorrect-variance"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/typevar-name-incorrect-variance.html"
---
# typevar-name-incorrect-variance / C0105

**Message emitted:**

`Type variable name does not reflect variance%s`

**Description:**

*Emitted when a TypeVar name doesn't reflect its type variance. According to PEP8, it is recommended to add suffixes '_co' and '_contra' to the variables used to declare covariant or contravariant behaviour respectively. Invariant (default) variables do not require a suffix. The message is also emitted when invariant variables do have a suffix.*

**Problematic code:**

```
from typing import TypeVar

T_co = TypeVar("T_co")  # [typevar-name-incorrect-variance]
```

**Correct code:**

```
from typing import TypeVar

T = TypeVar("T")
```

**Additional details:**

When naming type vars, only use a `_co` suffix when indicating covariance or `_contra` when indicating contravariance.

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/name_checker/checker.py) checker.