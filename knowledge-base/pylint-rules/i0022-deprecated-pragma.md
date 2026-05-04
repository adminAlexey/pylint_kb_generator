---
id: pylint-I0022
rule_code: "I0022"
rule_name: "deprecated-pragma"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/deprecated-pragma.html"
---
# deprecated-pragma / I0022

**Message emitted:**

`Pragma "%s" is deprecated, use "%s" instead`

**Description:**

*Some inline pylint options have been renamed or reworked, only the most recent form should be used. NOTE:skip-all is only available with pylint >= 0.26*

Caution

This message is disabled by default. To enable it, add `deprecated-pragma` to the `enable` option.

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I0022` option
or `--fail-on=I` to fail on all enabled informational messages.

**Problematic code:**

```
# pylint: disable-msg=eval-used # [deprecated-pragma]
```

**Correct code:**

```
# pylint: disable = eval-used
```

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.