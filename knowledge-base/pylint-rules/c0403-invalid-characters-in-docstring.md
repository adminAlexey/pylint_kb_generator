---
id: pylint-C0403
rule_code: "C0403"
rule_name: "invalid-characters-in-docstring"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/invalid-characters-in-docstring.html"
---
# invalid-characters-in-docstring / C0403

**Message emitted:**

`Invalid characters %r in a docstring`

**Description:**

*Used when a word in docstring cannot be checked by enchant.*

**Additional details:**

This is a message linked to an internal problem in enchant. There's nothing to change in your code,
but maybe in pylint's configuration or the way you installed the 'enchant' system library.

Created by the [spelling](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/spelling.py) checker.