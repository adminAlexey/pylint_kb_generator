---
id: pylint-E2510
rule_code: "E2510"
rule_name: "invalid-character-backspace"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-character-backspace.html"
---
# invalid-character-backspace / E2510

**Message emitted:**

`Invalid unescaped character backspace, use "\b" instead.`

**Description:**

*Moves the cursor back, so the character after it will overwrite the character before.*

**Problematic code:**

```
STRING = "Invalid character backspace "  # [invalid-character-backspace]
```

**Correct code:**

```
STRING = "Valid character backspace \b"
```

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.