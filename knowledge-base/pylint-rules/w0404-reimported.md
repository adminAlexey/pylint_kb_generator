---
id: pylint-W0404
rule_code: "W0404"
rule_name: "reimported"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/reimported.html"
---
# reimported / W0404

**Message emitted:**

`Reimport %r (imported line %s)`

**Description:**

*Used when a module is imported more than once.*

**Problematic code:**

```
import re
import re  # [reimported]
```

**Correct code:**

```
import re
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.