---
id: pylint-E1310
rule_code: "E1310"
rule_name: "bad-str-strip-call"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-str-strip-call.html"
---
# bad-str-strip-call / E1310

**Message emitted:**

`Suspicious argument in %s.%s call`

**Description:**

*The argument to a str.{l,r,}strip call contains a duplicate character,*

**Problematic code:**

`hello_world.py`:

```
"Hello World".strip("Hello")  # [bad-str-strip-call]
# >>> ' World'
```

`remove_abc_from_both_side.py`:

```
"abcbc def bacabc".strip("abcbc ")  # [bad-str-strip-call]
# >>> 'def'
```

**Correct code:**

`hello_world.py`:

```
"Hello World".strip("Helo")
# >>> ' World'
```

`remove_abc_from_both_side.py`:

```
"abcbc def bacabc".strip("abc ")
# >>> 'def'
```

**Additional details:**

A common misconception is that `str.strip('Hello')` removes the *substring* `'Hello'` from the beginning and end of the string.
This is **not**  the case.
From the [documentation](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip):

> The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped

Duplicated characters in the `str.strip` call, besides not having any effect on the actual result, may indicate this misunderstanding.

**Related links:**

- Documentation: [str.strip([chars])](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.