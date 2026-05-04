---
id: pylint-R1732
rule_code: "R1732"
rule_name: "consider-using-with"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-with.html"
---
# consider-using-with / R1732

**Message emitted:**

`Consider using 'with' for resource-allocating operations`

**Description:**

*Emitted if a resource-allocating assignment or call may be replaced by a 'with' block. By using 'with' the release of the allocated resources is ensured even in the case of an exception.*

**Problematic code:**

`close.py`:

```
file = open("apple.txt", "r", encoding="utf8")  # [consider-using-with]
contents = file.read()
file.close()
```

`not_even_close.py`:

```
contents = open("apple.txt", "r", encoding="utf8").read()  # [consider-using-with]
```

**Correct code:**

```
with open("apple.txt", "r", encoding="utf8") as file:
    contents = file.read()
```

**Additional details:**

Calling `write()` without using the `with` keyword or calling `close()` might
result in the arguments of `write()` not being completely written to the disk,
even if the program exits successfully.

This message applies to callables of Python's stdlib which can be replaced by a `with` statement.
It is suppressed in the following cases:

- the call is located inside a context manager
- the call result is returned from the enclosing function
- the call result is used in a `with` statement itself

**Related links:**

- [Python doc: Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [PEP 343](https://peps.python.org/pep-0343/)
- [Context managers in Python](https://johnlekberg.com/blog/2020-10-11-ctx-manage.html) by John Lekberg
- [Rationale](https://stackoverflow.com/a/73181877/2519059)

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.