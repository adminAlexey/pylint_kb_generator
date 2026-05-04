---
id: pylint-W2601
rule_code: "W2601"
rule_name: "using-f-string-in-unsupported-version"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/using-f-string-in-unsupported-version.html"
---
# using-f-string-in-unsupported-version / W2601

**Message emitted:**

`F-strings are not supported by all versions included in the py-version setting`

**Description:**

*Used when the py-version set by the user is lower than 3.6 and pylint encounters an f-string.*

**Problematic code:**

```
f"python {3.5} is past end of life"  # [using-f-string-in-unsupported-version]
```

**Correct code:**

```
"python {} is past end of life".format(3.5)
```

**Configuration file:**

```
[main]
py-version=3.5
```

**Additional details:**

f-strings were introduced in Python version 3.6; to use them, please use a more recent version of Python.

Created by the [unsupported_version](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/unsupported_version.py) checker.