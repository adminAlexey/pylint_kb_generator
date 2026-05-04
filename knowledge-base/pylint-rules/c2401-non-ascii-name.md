---
id: pylint-C2401
rule_code: "C2401"
rule_name: "non-ascii-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/non-ascii-name.html"
---
# non-ascii-name / C2401

**Message emitted:**

`%s name "%s" contains a non-ASCII character, consider renaming it.`

**Description:**

*Used when the name contains at least one non-ASCII unicode character. See https://peps.python.org/pep-0672/#confusing-features for a background why this could be bad.
If your programming guideline defines that you are programming in English, then there should be no need for non ASCII characters in Python Names. If not you can simply disable this check.*

**Problematic code:**

```
ápple_count = 4444  # [non-ascii-name]
```

**Correct code:**

```
apple_count = 4444
```

Created by the [nonascii-checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/non_ascii_names.py) checker.