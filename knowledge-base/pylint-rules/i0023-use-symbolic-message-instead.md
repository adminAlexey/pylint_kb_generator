---
id: pylint-I0023
rule_code: "I0023"
rule_name: "use-symbolic-message-instead"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/use-symbolic-message-instead.html"
---
# use-symbolic-message-instead / I0023

**Message emitted:**

`%s`

**Description:**

*Used when a message is enabled or disabled by id.*

Caution

This message is disabled by default. To enable it, add `use-symbolic-message-instead` to the `enable` option.

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I0023` option
or `--fail-on=I` to fail on all enabled informational messages.

**Problematic code:**

```
fruit_name = "plum"

# pylint: disable-next=W0621
def eat(fruit_name: str):  # [use-symbolic-message-instead]
    ...
```

**Correct code:**

```
fruit_name = "plum"

# pylint: disable-next=redefined-outer-name
def eat(fruit_name: str): ...
```

Created by the [miscellaneous](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/misc.py) checker.