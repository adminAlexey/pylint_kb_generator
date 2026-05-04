---
id: pylint-C2503
rule_code: "C2503"
rule_name: "bad-file-encoding"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/bad-file-encoding.html"
---
# bad-file-encoding / C2503

**Message emitted:**

`PEP8 recommends UTF-8 as encoding for Python files`

**Description:**

*PEP8 recommends UTF-8 default encoding for Python files. See https://peps.python.org/pep-0008/#source-file-encoding*

**Problematic code:**

```
# coding: latin_1 # [bad-file-encoding]
```

**Correct code:**

```

```

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.