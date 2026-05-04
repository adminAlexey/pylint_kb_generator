---
id: pylint-E1003
rule_code: "E1003"
rule_name: "bad-super-call"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-super-call.html"
---
# bad-super-call / E1003

**Message emitted:**

`Bad first argument %r given to super()`

**Description:**

*Used when another argument than the current class is given as first argument of the super builtin.*

**Problematic code:**

```
class Animal:
    pass

class Tree:
    pass

class Cat(Animal):
    def __init__(self):
        super(Tree, self).__init__()  # [bad-super-call]
        super(Animal, self).__init__()
```

**Correct code:**

```
class Animal:
    pass

class Tree:
    pass

class Cat(Animal):
    def __init__(self):
        super(Animal, self).__init__()
```

**Additional details:**

In Python 2.7, `super()` has to be called with its own class and `self` as arguments (`super(Cat, self)`), which can
lead to a mix up of parent and child class in the code.

In Python 3 the recommended way is to call `super()` without arguments (see also `super-with-arguments`).

One exception is calling `super()` on a non-direct parent class. This can be used to get a method other than the default
method returned by the `mro()`.

**Related links:**

- [Documentation for super()](https://docs.python.org/3/library/functions.html#super)

Created by the [newstyle](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/newstyle.py) checker.