---
id: pylint-C0402
rule_code: "C0402"
rule_name: "wrong-spelling-in-docstring"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/wrong-spelling-in-docstring.html"
---
# wrong-spelling-in-docstring / C0402

**Message emitted:**

`Wrong spelling of a word '%s' in a docstring:
%s
%s
Did you mean: '%s'?`

**Description:**

*Used when a word in docstring is not spelled correctly.*

**Problematic code:**

```
"""There's a mistkae in this string"""  # [wrong-spelling-in-docstring]
```

**Correct code:**

```
"""There's no mistake in this string"""
```

**Configuration file:**

```
[main]
# This might not run in your env if you don't have the en_US dict installed.
spelling-dict=en_US
```

Created by the [spelling](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/spelling.py) checker.