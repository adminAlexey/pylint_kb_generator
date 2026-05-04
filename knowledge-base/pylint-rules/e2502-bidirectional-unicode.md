---
id: pylint-E2502
rule_code: "E2502"
rule_name: "bidirectional-unicode"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bidirectional-unicode.html"
---
# bidirectional-unicode / E2502

**Message emitted:**

`Contains control characters that can permit obfuscated code executed differently than displayed`

**Description:**

*bidirectional unicode are typically not displayed characters required to display right-to-left (RTL) script (i.e. Chinese, Japanese, Arabic, Hebrew, ...) correctly. So can you trust this code? Are you sure it displayed correctly in all editors? If you did not write it or your language is not RTL, remove the special characters, as they could be used to trick you into executing code, that does something else than what it looks like.
More Information:
https://en.wikipedia.org/wiki/Bidirectional_text
https://trojansource.codes/*

**Problematic code:**

```
# +1: [bidirectional-unicode]
example = "x‏" * 100  #    "‏x" is assigned
```

**Correct code:**

```
example = "x[U+2194]" * 100
```

Created by the [unicode_checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unicode.py) checker.