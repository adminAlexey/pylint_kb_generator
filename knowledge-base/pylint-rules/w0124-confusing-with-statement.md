---
id: pylint-W0124
rule_code: "W0124"
rule_name: "confusing-with-statement"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/confusing-with-statement.html"
---
# confusing-with-statement / W0124

**Message emitted:**

`Following "as" with another context manager looks like a tuple.`

**Description:**

*Emitted when a `with` statement component returns multiple values and uses name binding with `as` only for a part of those values, as in with ctx() as a, b. This can be misleading, since it's not clear if the context manager returns a tuple or if the node without a name binding is another context manager.*

**Problematic code:**

```
with open("file.txt", "w") as fh1, fh2:  # [confusing-with-statement]
    pass
```

**Correct code:**

```
with open("file.txt", "w", encoding="utf8") as fh1:
    with open("file.txt", "w", encoding="utf8") as fh2:
        pass
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.