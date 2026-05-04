---
id: pylint-E1904
rule_code: "E1904"
rule_name: "multiple-class-sub-patterns"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/multiple-class-sub-patterns.html"
---
# multiple-class-sub-patterns / E1904

**Message emitted:**

`Multiple sub-patterns for attribute %s`

**Description:**

*Emitted when there is more than one sub-pattern for a specific attribute in a class pattern.*

**Problematic code:**

```
class Book:
    __match_args__ = ("title", "year")

    def __init__(self, title, year):
        self.title = title
        self.year = year

def func(item: Book):
    match item:
        case Book("abc", title="abc"):  # [multiple-class-sub-patterns]
            ...
        case Book(year=2000, year=2001):  # [multiple-class-sub-patterns]
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
        case Book(title="abc"):
            ...
        case Book(year=2000):
            ...
```

**Related links:**

- [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#class-patterns)

Created by the [match_statements](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/match_statements_checker.py) checker.