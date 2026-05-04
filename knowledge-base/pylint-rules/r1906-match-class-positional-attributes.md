---
id: pylint-R1906
rule_code: "R1906"
rule_name: "match-class-positional-attributes"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/match-class-positional-attributes.html"
---
# match-class-positional-attributes / R1906

**Message emitted:**

`Use keyword attributes instead of positional ones (%s)`

**Description:**

*Keyword attributes are more explicit and slightly faster since CPython can skip the `__match_args__` lookup.*

**Problematic code:**

```
class Book:
    __match_args__ = ("title", "year")

    def __init__(self, title, year):
        self.title = title
        self.year = year

def func(item: Book):
    match item:
        case Book("abc", 2000):  # [match-class-positional-attributes]
            ...
```

**Correct code:**

```
class Book:
    __match_args__ = ("title", "year")

    def __init__(self, title, year):
        self.title = title
        self.year = year

def func(item: Book):
    match item:
        case Book(title="abc", year=2000):
            ...
```

**Related links:**

- [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#class-patterns)

Created by the [match_statements](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/match_statements_checker.py) checker.