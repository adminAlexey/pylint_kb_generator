---
id: pylint-R1905
rule_code: "R1905"
rule_name: "match-class-bind-self"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/match-class-bind-self.html"
---
# match-class-bind-self / R1905

**Message emitted:**

`Use '%s() as %s' instead`

**Description:**

*Match class patterns are faster if the name binding happens for the whole pattern and any lookup for `__match_args__` can be avoided.*

**Problematic code:**

```
class Book:
    __match_args__ = ("title", "year")

    def __init__(self, title, year):
        self.title = title
        self.year = year

def func(item: Book):
    match item:
        case Book(title=str(title)):  # [match-class-bind-self]
            ...
        case Book(year=int(year)):  # [match-class-bind-self]
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
        case Book(title=str() as title):
            ...
        case Book(year=int() as year):
            ...
```

**Related links:**

- [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#class-patterns)

Created by the [match_statements](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/match_statements_checker.py) checker.