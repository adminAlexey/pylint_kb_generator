---
id: pylint-W0223
rule_code: "W0223"
rule_name: "abstract-method"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/abstract-method.html"
---
# abstract-method / W0223

**Message emitted:**

`Method %r is abstract in class %r but is not overridden in child class %r`

**Description:**

*Used when an abstract method (i.e. raise NotImplementedError) is not overridden in concrete class.*

**Problematic code:**

`abstract_method.py`:

```
import abc

class WildAnimal:
    @abc.abstractmethod
    def make_sound(self):
        pass

class Panther(WildAnimal):  # [abstract-method]
    pass
```

`function_raising_not_implemented_error.py`:

```
class Pet:
    def make_sound(self):
        raise NotImplementedError

class Cat(Pet):  # [abstract-method]
    pass
```

**Correct code:**

`abstract_method.py`:

```
import abc

class WildAnimal:
    @abc.abstractmethod
    def make_sound(self):
        pass

class Panther(WildAnimal):
    def make_sound(self):
        print("MEEEOW")
```

`function_raising_not_implemented_error.py`:

```
class Pet:
    def make_sound(self):
        raise NotImplementedError

class Cat(Pet):
    def make_sound(self):
        print("Meeeow")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.