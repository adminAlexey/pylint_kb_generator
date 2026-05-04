---
id: pylint-I0021
rule_code: "I0021"
rule_name: "useless-suppression"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/useless-suppression.html"
---
# useless-suppression / I0021

**Message emitted:**

`Useless suppression of %s`

**Description:**

*Reported when a message is explicitly disabled for a line or a block of code, but never triggered.*

Caution

This message is disabled by default. To enable it, add `useless-suppression` to the `enable` option.

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I0021` option
or `--fail-on=I` to fail on all enabled informational messages.

**Problematic code:**

```
fruit_counter = 0

# pylint: disable-next=redefined-outer-name
def eat(fruit_name: str):  # [useless-suppression]
    ...
```

**Correct code:**

```
fruit_counter = 0

def eat(fruit_name: str): ...
```

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.