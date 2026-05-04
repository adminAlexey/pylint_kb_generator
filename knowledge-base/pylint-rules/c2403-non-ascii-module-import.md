---
id: pylint-C2403
rule_code: "C2403"
rule_name: "non-ascii-module-import"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/non-ascii-module-import.html"
---
# non-ascii-module-import / C2403

**Message emitted:**

`%s name "%s" contains a non-ASCII character, use an ASCII-only alias for import.`

**Description:**

*Used when the name contains at least one non-ASCII unicode character. See https://peps.python.org/pep-0672/#confusing-features for a background why this could be bad.
If your programming guideline defines that you are programming in English, then there should be no need for non ASCII characters in Python Names. If not you can simply disable this check.*

**Problematic code:**

```
from os.path import join as łos  # [non-ascii-module-import]

foo = łos("a", "b")
```

**Correct code:**

```
from os.path import join as os_join

foo = os_join("a", "b")
```

Created by the [nonascii-checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/non_ascii_names.py) checker.