---
id: pylint-F0011
rule_code: "F0011"
rule_name: "config-parse-error"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/fatal/config-parse-error.html"
---
# config-parse-error / F0011

**Message emitted:**

`error while parsing the configuration: %s`

**Description:**

*Used when an exception occurred while parsing a pylint configuration file.*

**Additional details:**

This is a message linked to a problem in your configuration not your code.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.