---
id: pylint-C0325
rule_code: "C0325"
rule_name: "superfluous-parens"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/superfluous-parens.html"
---
# superfluous-parens / C0325

**Message emitted:**

`Unnecessary parens after %r keyword`

**Description:**

*Used when a single item in parentheses follows an if, for, or other keyword.*

**Problematic code:**

`example_1.py`:

```
x = input()
y = input()
if (x == y):  # [superfluous-parens]
    pass
```

`example_2.py`:

```
i = 0
exclude = []
if (i - 0) in exclude:  # [superfluous-parens]
    pass
```

**Correct code:**

`example_1.py`:

```
x = input()
y = input()
if x == y:
    pass
```

`example_2.py`:

```
i = 0
exclude = []
if i - 0 in exclude:
    pass
```

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.