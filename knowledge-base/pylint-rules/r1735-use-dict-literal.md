---
id: pylint-R1735
rule_code: "R1735"
rule_name: "use-dict-literal"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/use-dict-literal.html"
---
# use-dict-literal / R1735

**Message emitted:**

`Consider using '%s' instead of a call to 'dict'.`

**Description:**

*Emitted when using dict() to create a dictionary instead of a literal '{ ... }'. The literal is faster as it avoids an additional function call.*

**Problematic code:**

`empty_dict.py`:

```
empty_dict = dict()  # [use-dict-literal]
```

`init_dict_from_another.py`:

```
original_dict = {"name": "Sunny", "age": 10, "favorite_color": "yellow"}
copied_dict = dict(**original_dict)  # [use-dict-literal]
```

`init_with_keyword.py`:

```
response_dict = dict(answer="No")  # [use-dict-literal]
```

**Correct code:**

`empty_dict.py`:

```
empty_dict = {}
```

`init_dict_from_another.py`:

```
original_dict = {"name": "Sunny", "age": 10, "favorite_color": "yellow"}
# shallow copy a dict
copied_dict = {**original_dict}
```

`init_with_literal.py`:

```
response_dict = {"answer": "No"}
```

**Additional details:**

[https://gist.github.com/hofrob/ad143aaa84c096f42489c2520a3875f9](https://gist.github.com/hofrob/ad143aaa84c096f42489c2520a3875f9)

This example script shows an 18% increase in performance when using a literal over the
constructor in python version 3.10.6.

**Related links:**

- [Performance Analysis of Python’s dict() vs dict literal](https://madebyme.today/blog/python-dict-vs-curly-brackets/)

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.