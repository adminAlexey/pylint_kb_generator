---
id: pylint-E1134
rule_code: "E1134"
rule_name: "not-a-mapping"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/not-a-mapping.html"
---
# not-a-mapping / E1134

**Message emitted:**

`Non-mapping value %s is used in a mapping context`

**Description:**

*Used when a non-mapping value is used in place where mapping is expected*

**Problematic code:**

```
def print_colors(**colors):
    print(colors)

print_colors(**list("red", "black"))  # [not-a-mapping]
```

**Correct code:**

```
def print_colors(**colors):
    print(colors)

print_colors(**dict(red=1, black=2))
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.