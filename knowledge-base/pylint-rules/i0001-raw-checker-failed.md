---
id: pylint-I0001
rule_code: "I0001"
rule_name: "raw-checker-failed"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/raw-checker-failed.html"
---
# raw-checker-failed / I0001

**Message emitted:**

`Unable to run raw checkers on built-in module %s`

**Description:**

*Used to inform that a built-in module has not been checked using the raw checkers.*

Caution

This message is disabled by default. To enable it, add `raw-checker-failed` to the `enable` option.

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I0001` option
or `--fail-on=I` to fail on all enabled informational messages.

**Additional details:**

This warns you that a builtin module was impossible to analyse (an ast node is not pure python).
There's nothing to change in your code, this is a warning about astroid and pylint's limitations.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.