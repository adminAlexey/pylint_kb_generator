---
id: pylint-W1406
rule_code: "W1406"
rule_name: "redundant-u-string-prefix"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redundant-u-string-prefix.html"
---
# redundant-u-string-prefix / W1406

**Message emitted:**

`The u prefix for strings is no longer necessary in Python >=3.0`

**Description:**

*Used when we detect a string with a u prefix. These prefixes were necessary in Python 2 to indicate a string was Unicode, but since Python 3.0 strings are Unicode by default.*

**Problematic code:**

```
def print_fruit():
    print(u"Apple")  # [redundant-u-string-prefix]
```

**Correct code:**

```
def print_fruit():
    print("Apple")
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.