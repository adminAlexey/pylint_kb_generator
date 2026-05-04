---
id: pylint-C0328
rule_code: "C0328"
rule_name: "unexpected-line-ending-format"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/unexpected-line-ending-format.html"
---
# unexpected-line-ending-format / C0328

**Message emitted:**

`Unexpected line ending format. There is '%s' while it should be '%s'.`

**Description:**

*Used when there is different newline than expected.*

**Problematic code:**

```
print("I'm drinking tea!")  # CRLF (\r\n) # [unexpected-line-ending-format]
print("I'm drinking water!")  # CRLF (\r\n) # [unexpected-line-ending-format]
```

**Correct code:**

```
print("I'm drinking tea!")  # LF (\n)
print("I'm drinking water!")  # LF (\n)
```

**Configuration file:**

```
[FORMAT]
expected-line-ending-format=LF
```

**Related links:**

- [History of CRLF and LF](https://stackoverflow.com/a/6521730/2519059)
- [Dealing with line endings in Git](https://stackoverflow.com/a/10855862/2519059)
- [A Collection of Useful .gitattributes Templates](https://github.com/alexkaratarakis/gitattributes)

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.