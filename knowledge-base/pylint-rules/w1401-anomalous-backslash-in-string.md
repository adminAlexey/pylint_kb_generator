---
id: pylint-W1401
rule_code: "W1401"
rule_name: "anomalous-backslash-in-string"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/anomalous-backslash-in-string.html"
---
# anomalous-backslash-in-string / W1401

**Message emitted:**

`Anomalous backslash in string: '%s'. String constant might be missing an r prefix.`

**Description:**

*Used when a backslash is in a literal string but not as an escape.*

**Problematic code:**

```
string = "\z"  # [syntax-error]
```

**Correct code:**

`double_escape.py`:

```
string = "\\z"
```

`existing_escape_sequence.py`:

```
string = "\t"
```

`r_prefix.py`:

```
string = r"\z"
```

**Additional details:**

`\z` is same as `\\z` because there's no escape sequence for `z`. But it is not clear
for the reader of the code.

The only reason this is demonstrated to raise `syntax-error` is because
pylint's CI now runs on Python 3.12, where this truly raises a `SyntaxError`.
We hope to address this discrepancy in the documentation in the future.

**Related links:**

- [String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
- [Long form stackoverflow explanation](https://stackoverflow.com/a/19030982/2519059)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.