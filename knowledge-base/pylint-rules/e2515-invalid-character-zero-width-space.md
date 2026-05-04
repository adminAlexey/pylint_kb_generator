---
id: pylint-E2515
rule_code: "E2515"
rule_name: "invalid-character-zero-width-space"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-character-zero-width-space.html"
---
# invalid-character-zero-width-space / E2515

**Message emitted:**

`Invalid unescaped character zero-width-space, use "\u200B" instead.`

**Description:**

*Invisible space character could hide real code execution.*

**Problematic code:**

```
STRING = "Invalid character zero-width-space ​"  # [invalid-character-zero-width-space]
```

**Correct code:**

```
STRING = "Valid character zero-width-space u200B"
```

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.