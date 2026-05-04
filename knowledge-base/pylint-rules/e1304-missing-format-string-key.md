---
id: pylint-E1304
rule_code: "E1304"
rule_name: "missing-format-string-key"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/missing-format-string-key.html"
---
# missing-format-string-key / E1304

**Message emitted:**

`Missing key %r in format string dictionary`

**Description:**

*Used when a format string that uses named conversion specifiers is used with a dictionary that doesn't contain all the keys required by the format string.*

**Problematic code:**

```
# +1: [missing-format-string-key]
fruit_prices = """
Apple: %(apple_price)d ¤
Orange: %(orange_price)d ¤
""" % {"apple_price": 42}
```

**Correct code:**

```
fruit_prices = """
Apple: %(apple_price)d ¤
Orange: %(orange_price)d ¤
""" % {
    "apple_price": 42,
    "orange_price": 87,
}
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.