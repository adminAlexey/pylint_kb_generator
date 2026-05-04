---
id: pylint-W0177
rule_code: "W0177"
rule_name: "nan-comparison"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/nan-comparison.html"
---
# nan-comparison / W0177

**Message emitted:**

`Comparison %s should be %s`

**Description:**

*Used when an expression is compared to NaN values like numpy.NaN and float('nan').*

**Problematic code:**

```
import numpy as np

def both_nan(x, y) -> bool:
    return x == np.NaN and y == float("nan")  # [nan-comparison, nan-comparison]
```

**Correct code:**

```
import numpy as np

def both_nan(x, y) -> bool:
    return np.isnan(x) and np.isnan(y)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/comparison_checker.py) checker.