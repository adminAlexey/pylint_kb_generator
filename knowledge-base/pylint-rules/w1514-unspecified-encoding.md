---
id: pylint-W1514
rule_code: "W1514"
rule_name: "unspecified-encoding"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unspecified-encoding.html"
---
# unspecified-encoding / W1514

**Message emitted:**

`Using open without explicitly specifying an encoding`

**Description:**

*It is better to specify an encoding when opening documents. Using the system default implicitly can create problems on other operating systems. See https://peps.python.org/pep-0597/*

**Problematic code:**

```
def foo(file_path):
    with open(file_path) as file:  # [unspecified-encoding]
        contents = file.read()
```

**Correct code:**

```
def foo(file_path):
    with open(file_path, encoding="utf-8") as file:
        contents = file.read()
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.