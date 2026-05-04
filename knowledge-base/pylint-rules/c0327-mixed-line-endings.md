---
id: pylint-C0327
rule_code: "C0327"
rule_name: "mixed-line-endings"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/mixed-line-endings.html"
---
# mixed-line-endings / C0327

**Message emitted:**

`Mixed line endings LF and CRLF`

**Description:**

*Used when there are mixed (LF and CRLF) newline signs in a file.*

**Problematic code:**

```
print("Hello")  # CRLF (\r\n)
print("World")  # LF (\n) # [mixed-line-endings]
```

**Correct code:**

`full_crlf.py`:

```
print("Hello")  # CRLF (\r\n)
print("World")  # CRLF (\r\n)
```

`full_lf.py`:

```
print("Hello")  # LF (\n)
print("World")  # LF (\n)
```

**Related links:**

- [History of CRLF and LF](https://stackoverflow.com/a/6521730/2519059)
- [Dealing with line endings in Git](https://stackoverflow.com/a/10855862/2519059)
- [A Collection of Useful .gitattributes Templates](https://github.com/alexkaratarakis/gitattributes)

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.