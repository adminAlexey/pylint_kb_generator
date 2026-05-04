---
id: pylint-E2513
rule_code: "E2513"
rule_name: "invalid-character-esc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-character-esc.html"
---
# invalid-character-esc / E2513

**Message emitted:**

`Invalid unescaped character esc, use "\x1B" instead.`

**Description:**

*Commonly initiates escape codes which allow arbitrary control of the terminal.*

**Problematic code:**

```
STRING = "Invalid escape character "  # [invalid-character-esc]
```

**Correct code:**

```
STRING = "Valid escape character \x1b"
```

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.