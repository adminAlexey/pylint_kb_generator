---
id: pylint-E0110
rule_code: "E0110"
rule_name: "abstract-class-instantiated"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/abstract-class-instantiated.html"
---
# abstract-class-instantiated / E0110

**Message emitted:**

`Abstract class %r with abstract methods instantiated`

**Description:**

*Used when an abstract class with `abc.ABCMeta` as metaclass has abstract methods and is instantiated.*

**Problematic code:**

```
import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass

sheep = Animal()  # [abstract-class-instantiated]
```

**Correct code:**

```
import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass

class Sheep(Animal):
    def make_sound(self):
        print("bhaaaaa")

sheep = Sheep()
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.