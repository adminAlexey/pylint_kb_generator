---
id: pylint-I0010
rule_code: "I0010"
rule_name: "bad-inline-option"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/bad-inline-option.html"
---
# bad-inline-option / I0010

**Message emitted:**

`Unable to consider inline option %r`

**Description:**

*Used when an inline option is either badly formatted or can't be used inside modules.*

Caution

This message is disabled by default. To enable it, add `bad-inline-option` to the `enable` option.

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I0010` option
or `--fail-on=I` to fail on all enabled informational messages.

**Problematic code:**

```
# 2:[bad-inline-option]
# pylint: disable line-too-long
```

**Correct code:**

```
# pylint: disable=line-too-long
```

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.