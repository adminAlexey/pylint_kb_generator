---
id: pylint-W1507
rule_code: "W1507"
rule_name: "shallow-copy-environ"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/shallow-copy-environ.html"
---
# shallow-copy-environ / W1507

**Message emitted:**

`Using copy.copy(os.environ). Use os.environ.copy() instead.`

**Description:**

*os.environ is not a dict object but proxy object, so shallow copy has still effects on original object. See https://bugs.python.org/issue15373 for reference.*

**Problematic code:**

```
import copy
import os

copied_env = copy.copy(os.environ)  # [shallow-copy-environ]
```

**Correct code:**

```
import os

copied_env = os.environ.copy()
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.