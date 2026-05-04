---
id: pylint-C0304
rule_code: "C0304"
rule_name: "missing-final-newline"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-final-newline.html"
---
# missing-final-newline / C0304

**Message emitted:**

`Final newline missing`

**Description:**

*Used when the last line in a file is missing a newline.*

**Problematic code:**

`crlf.py`:

```
print("Hello")  # CRLF (\r\n)
print("world")  # End-of-file (EOF)
# [missing-final-newline]
```

`lf.py`:

```
print("Hello")  # LF (\n)
print("world")  # End-of-file (EOF)
# [missing-final-newline]
```

**Correct code:**

`crlf.py`:

```
print("Hello")  # CRLF (\r\n)
print("world")  # CRLF (\r\n)
# End-of-file (EOF)
```

`lf.py`:

```
print("Hello")  # LF (\n)
print("world")  # LF (\n)
# End-of-file (EOF)
```

**Additional details:**

**The POSIX standard defines a line as:**
: "A sequence of zero or more non- <newline> characters plus a terminating <newline> character."

**Related links:**

- [POSIX Standard](https://pubs.opengroup.org/onlinepubs/9699919799/)
- [POSIX Standard Chapter 3.206 Line](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206)

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.