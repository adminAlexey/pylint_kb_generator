---
id: pylint-E1902
rule_code: "E1902"
rule_name: "invalid-match-args-definition"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-match-args-definition.html"
---
# invalid-match-args-definition / E1902

**Message emitted:**

``__match_args__` must be a tuple of strings.`

**Description:**

*Emitted if `__match_args__` isn't a tuple of strings required for match.*

**Problematic code:**

```
class Book:
    __match_args__ = ["title", "year"]  # [invalid-match-args-definition]

    def __init__(self, title, year):
        self.title = title
        self.year = year
```

**Correct code:**

```
class Book:
    __match_args__ = ("title", "year")

    def __init__(self, title, year):
        self.title = title
        self.year = year
```

**Related links:**

- [Python documentation](https://docs.python.org/3/reference/datamodel.html#customizing-positional-arguments-in-class-pattern-matching)

Created by the [match_statements](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/match_statements_checker.py) checker.