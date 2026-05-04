---
id: pylint-E0011
rule_code: "E0011"
rule_name: "unrecognized-inline-option"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unrecognized-inline-option.html"
---
# unrecognized-inline-option / E0011

**Message emitted:**

`Unrecognized file option %r`

**Description:**

*Used when an unknown inline option is encountered.*

**Problematic code:**

```
# +1: [unrecognized-inline-option]
# pylint:applesoranges=1
```

**Correct code:**

```
# pylint: enable=too-many-public-methods
```

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.