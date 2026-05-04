---
id: pylint-F0002
rule_code: "F0002"
rule_name: "astroid-error"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/fatal/astroid-error.html"
---
# astroid-error / F0002

**Message emitted:**

`%s: %s`

**Description:**

*Used when an unexpected error occurred while building the Astroid  representation. This is usually accompanied by a traceback. Please report such errors !*

**Additional details:**

This is a message linked to an internal problem in pylint. There's nothing to change in your code,
but maybe in pylint's configuration or installation.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.