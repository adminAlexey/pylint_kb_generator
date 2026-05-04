---
id: pylint-E2511
rule_code: "E2511"
rule_name: "invalid-character-carriage-return"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-character-carriage-return.html"
---
# invalid-character-carriage-return / E2511

**Message emitted:**

`Invalid unescaped character carriage-return, use "\r" instead.`

**Description:**

*Moves the cursor to the start of line, subsequent characters overwrite the start of the line.*

**Correct code:**

```
STRING = "Valid carriage return: \r"
```

**Additional details:**

This message exists because one of our checkers is very generic, but it's never going to
raise during normal use as it's a `syntax-error` that would prevent the python ast
(and thus pylint) from constructing a code representation of the file.

You could encounter it by feeding a properly constructed node directly to the checker.

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.