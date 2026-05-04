---
id: pylint-C0401
rule_code: "C0401"
rule_name: "wrong-spelling-in-comment"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/wrong-spelling-in-comment.html"
---
# wrong-spelling-in-comment / C0401

**Message emitted:**

`Wrong spelling of a word '%s' in a comment:
%s
%s
Did you mean: '%s'?`

**Description:**

*Used when a word in comment is not spelled correctly.*

**Problematic code:**

```
# There's a mistkae in this string  # [wrong-spelling-in-comment]
```

**Correct code:**

```
# There's no mistake in this string
```

**Configuration file:**

```
[main]
# This might not run in your env if you don't have the en_US dict installed.
spelling-dict=en_US
```

Created by the [spelling](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/spelling.py) checker.