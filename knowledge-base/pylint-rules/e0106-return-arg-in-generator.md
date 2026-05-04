---
id: pylint-E0106
rule_code: "E0106"
rule_name: "return-arg-in-generator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/return-arg-in-generator.html"
---
# return-arg-in-generator / E0106

**Message emitted:**

`Return with argument inside generator`

**Description:**

*Used when a "return" statement with an argument is found in a generator function or method (e.g. with some "yield" statements).*

**Correct code:**

```
def yield_numbers():
    for number in range(10):
        yield number
        return "I am now allowed!"  # This was not allowed in Python 3.3 and earlier.
```

**Additional details:**

This is a message that isn't going to be raised for python > 3.3. It was raised
for code like:

```
def interrogate_until_you_find_jack(pirates):
    for pirate in pirates:
        if pirate == "Captain Jack Sparrow":
            return "Arrr! We've found our captain!"
        yield pirate
```

Which is now valid and equivalent to the previously expected:

```
def interrogate_until_you_find_jack(pirates):
    for pirate in pirates:
        if pirate == "Captain Jack Sparrow":
            raise StopIteration("Arrr! We've found our captain!")
        yield pirate
```

**Related links:**

- [PEP380](https://peps.python.org/pep-0380/)
- [Stackoverflow explanation](https://stackoverflow.com/a/16780113/2519059)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.