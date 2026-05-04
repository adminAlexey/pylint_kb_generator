---
id: pylint-W0715
rule_code: "W0715"
rule_name: "raising-format-tuple"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/raising-format-tuple.html"
---
# raising-format-tuple / W0715

**Message emitted:**

`Exception arguments suggest string formatting might be intended`

**Description:**

*Used when passing multiple arguments to an exception constructor, the first of them a string literal containing what appears to be placeholders intended for formatting*

**Problematic code:**

```
raise RuntimeError("This looks wrong %s %s", ("a", "b"))  # [raising-format-tuple]
```

**Correct code:**

```
raise RuntimeError("This looks wrong %s %s" % ("a", "b"))
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.