---
id: pylint-I0013
rule_code: "I0013"
rule_name: "file-ignored"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/file-ignored.html"
---
# file-ignored / I0013

**Message emitted:**

`Ignoring entire file`

**Description:**

*Used to inform that the file will not be checked*

Caution

This message is disabled by default. To enable it, add `file-ignored` to the `enable` option.

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I0013` option
or `--fail-on=I` to fail on all enabled informational messages.

**Problematic code:**

```
# pylint: skip-file
# -1: [file-ignored]
```

**Correct code:**

```

```

**Additional details:**

There's no checks at all for a file if it starts by `# pylint: skip-file`.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.