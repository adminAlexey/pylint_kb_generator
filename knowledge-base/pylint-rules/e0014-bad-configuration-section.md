---
id: pylint-E0014
rule_code: "E0014"
rule_name: "bad-configuration-section"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-configuration-section.html"
---
# bad-configuration-section / E0014

**Message emitted:**

`Out-of-place setting encountered in top level configuration-section '%s' : '%s'`

**Description:**

*Used when we detect a setting in the top level of a toml configuration that shouldn't be there.*

**Additional details:**

This error was raised when we encountered an unexpected value type in a toml
configuration between pylint 2.12 and pylint 2.14 (before the argparse refactor).

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.