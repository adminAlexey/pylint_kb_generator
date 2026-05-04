---
id: pylint-R6301
rule_code: "R6301"
rule_name: "no-self-use"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-self-use.html"
---
# no-self-use / R6301

**Message emitted:**

`Method could be a function`

**Description:**

*Used when a method doesn't use its bound instance, and so could be written as a function.*

**Problematic code:**

```
class Person:
    def greeting(self):  # [no-self-use]
        print("Greetings pythonista!")
```

**Correct code:**

`function.py`:

```
def greeting():
    print("Greetings pythonista!")
```

`staticmethod.py`:

```
class Person:
    @staticmethod
    def greeting():
        print("Greetings pythonista!")
```

`use_self.py`:

```
class Person:
    name: str = "Amelia"

    def greeting(self):
        print(f"Greetings {self.name} the pythonista!")
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.no_self_use,
```

**Additional details:**

If a function is not using any class attribute it can be a `@staticmethod`,
or a function outside the class.

Note

This message is emitted by the optional ['no_self_use'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-no-self-use)
checker, which requires the `pylint.extensions.no_self_use` plugin to be loaded.

Created by the [no_self_use](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/no_self_use.py) checker.