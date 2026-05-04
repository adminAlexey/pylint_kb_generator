---
id: pylint-E0015
rule_code: "E0015"
rule_name: "unrecognized-option"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unrecognized-option.html"
---
# unrecognized-option / E0015

**Message emitted:**

`Unrecognized option found: %s`

**Description:**

*Used when we detect an option that we do not recognize.*

**Additional details:**

One of your options is not recognized. There's nothing to change in
your code, but your pylint configuration or the way you launch
pylint needs to be modified.

For example, this message would be raised when invoking pylint with
`pylint --unknown-option=yes test.py`. Or you might be launching
pylint with the following `toml` configuration:

```
[tool.pylint]
jars = "10"
```

When the following should be used:

```
[tool.pylint]
jobs = "10"
```

This warning was released in pylint 2.14: bad options were silently failing before.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.