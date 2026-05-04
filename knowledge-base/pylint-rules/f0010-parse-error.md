---
id: pylint-F0010
rule_code: "F0010"
rule_name: "parse-error"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/fatal/parse-error.html"
---
# parse-error / F0010

**Message emitted:**

`error while code parsing: %s`

**Description:**

*Used when an exception occurred while building the Astroid representation which could be handled by astroid.*

**Additional details:**

This is a message linked to an internal problem in pylint. There's nothing to change in your code.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.