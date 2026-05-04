---
id: pylint-E2512
rule_code: "E2512"
rule_name: "invalid-character-sub"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-character-sub.html"
---
# invalid-character-sub / E2512

**Message emitted:**

`Invalid unescaped character sub, use "\x1A" instead.`

**Description:**

*Ctrl+Z "End of text" on Windows. Some programs (such as type) ignore the rest of the file after it.*

**Problematic code:**

```
STRING = "Invalid character sub "  # [invalid-character-sub]
```

**Correct code:**

```
STRING = "Valid character sub x1A"
```

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.