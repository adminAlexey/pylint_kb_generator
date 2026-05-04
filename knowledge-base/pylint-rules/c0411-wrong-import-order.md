---
id: pylint-C0411
rule_code: "C0411"
rule_name: "wrong-import-order"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/wrong-import-order.html"
---
# wrong-import-order / C0411

**Message emitted:**

`%s should be placed before %s`

**Description:**

*Used when PEP8 import order is not respected (standard imports first, then third-party libraries, then local imports).*

**Problematic code:**

```
import os
from . import utils
import pylint  # [wrong-import-order]
import sys  # [wrong-import-order]
```

**Correct code:**

```
import os
import sys

import pylint

from . import utils
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.