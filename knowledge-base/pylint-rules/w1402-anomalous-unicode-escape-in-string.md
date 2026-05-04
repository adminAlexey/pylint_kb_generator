---
id: pylint-W1402
rule_code: "W1402"
rule_name: "anomalous-unicode-escape-in-string"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/anomalous-unicode-escape-in-string.html"
---
# anomalous-unicode-escape-in-string / W1402

**Message emitted:**

`Anomalous Unicode escape in byte string: '%s'. String constant might be missing an r or u prefix.`

**Description:**

*Used when an escape like u is encountered in a byte string where it has no effect.*

**Problematic code:**

```
print(b"\u%b" % b"0394")  # [syntax-error]
```

**Correct code:**

```
print(b"\\u%b" % b"0394")
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.