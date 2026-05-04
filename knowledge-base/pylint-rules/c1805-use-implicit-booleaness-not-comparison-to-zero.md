---
id: pylint-C1805
rule_code: "C1805"
rule_name: "use-implicit-booleaness-not-comparison-to-zero"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/use-implicit-booleaness-not-comparison-to-zero.html"
---
# use-implicit-booleaness-not-comparison-to-zero / C1805

**Message emitted:**

`"%s" can be simplified to "%s", if it is strictly an int, as 0 is falsey`

**Description:**

*0 is considered false in a boolean context. Following this check blindly in weakly typed code base can create hard to debug issues. If the value can be something else that is falsey but not an int (for example ``None``, an empty string, or an empty sequence) the code will not be equivalent.*

Caution

This message is disabled by default. To enable it, add `use-implicit-booleaness-not-comparison-to-zero` to the `enable` option.

**Problematic code:**

```
def important_math(x: int, y: int) -> None:
    if x == 0:  # [use-implicit-booleaness-not-comparison-to-zero]
        print("x is equal to zero")

    if y != 0:  # [use-implicit-booleaness-not-comparison-to-zero]
        print("y is not equal to zero")
```

**Correct code:**

```
def important_math(x: int, y: int) -> None:
    if not x:
        print("x is equal to zero")

    if y:
        print("y is not equal to zero")
```

**Configuration file:**

```
[main]
enable=use-implicit-booleaness-not-comparison-to-zero
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/implicit_booleaness_checker.py) checker.