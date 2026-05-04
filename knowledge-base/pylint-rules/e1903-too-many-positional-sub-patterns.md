---
id: pylint-E1903
rule_code: "E1903"
rule_name: "too-many-positional-sub-patterns"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/too-many-positional-sub-patterns.html"
---
# too-many-positional-sub-patterns / E1903

**Message emitted:**

`%s expects %d positional sub-patterns (given %d)`

**Description:**

*Emitted when the number of allowed positional sub-patterns exceeds the number of allowed sub-patterns specified in `__match_args__`.*

**Problematic code:**

```
class Book:
    __match_args__ = ("title", "year")

    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

def func(item: Book):
    match item:
        case Book("title", 2000, "author"):  # [too-many-positional-sub-patterns]
            ...
```

**Correct code:**

```
class Book:
    __match_args__ = ("title", "year")

    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

def func(item: Book):
    match item:
        case Book("title", 2000, author="author"):
            ...
```

**Related links:**

- [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#class-patterns)

Created by the [match_statements](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/match_statements_checker.py) checker.