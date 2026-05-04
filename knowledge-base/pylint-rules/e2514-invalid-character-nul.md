---
id: pylint-E2514
rule_code: "E2514"
rule_name: "invalid-character-nul"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-character-nul.html"
---
# invalid-character-nul / E2514

**Message emitted:**

`Invalid unescaped character nul, use "\0" instead.`

**Description:**

*Mostly end of input for python.*

**Additional details:**

There's no need to use end-of-string characters. String objects maintain their
own length.

**Related links:**

- [Null terminator in python](https://stackoverflow.com/a/24410304/2519059)

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.