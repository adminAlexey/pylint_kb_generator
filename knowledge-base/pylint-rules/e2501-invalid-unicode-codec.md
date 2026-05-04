---
id: pylint-E2501
rule_code: "E2501"
rule_name: "invalid-unicode-codec"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-unicode-codec.html"
---
# invalid-unicode-codec / E2501

**Message emitted:**

`UTF-16 and UTF-32 aren't backward compatible. Use UTF-8 instead`

**Description:**

*For compatibility use UTF-8 instead of UTF-16/UTF-32. See also https://bugs.python.org/issue1503789 for a history of this issue. And https://softwareengineering.stackexchange.com/questions/102205/ for some possible problems when using UTF-16 for instance.*

**Additional details:**

This message is a placeholder for a potential future issue with unicode codecs.

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.