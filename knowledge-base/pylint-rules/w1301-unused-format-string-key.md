---
id: pylint-W1301
rule_code: "W1301"
rule_name: "unused-format-string-key"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-format-string-key.html"
---
# unused-format-string-key / W1301

**Message emitted:**

`Unused key %r in format string dictionary`

**Description:**

*Used when a format string that uses named conversion specifiers is used with a dictionary that contains keys not required by the format string.*

**Problematic code:**

```
"The quick %(color)s fox jumps over the lazy dog." % {
    "color": "brown",
    "action": "hops",
}
# -4: [unused-format-string-key]
```

**Correct code:**

```
"The quick %(color)s fox %(action)s over the lazy dog." % {
    "color": "brown",
    "action": "hops",
}
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.