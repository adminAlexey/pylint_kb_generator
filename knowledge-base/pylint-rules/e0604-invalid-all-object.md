---
id: pylint-E0604
rule_code: "E0604"
rule_name: "invalid-all-object"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-all-object.html"
---
# invalid-all-object / E0604

**Message emitted:**

`Invalid object %r in __all__, must contain only strings`

**Description:**

*Used when an invalid (non-string) object occurs in __all__.*

**Problematic code:**

```
__all__ = (
    None,  # [invalid-all-object]
    Fruit,
    Worm,
)

class Fruit:
    pass

class Worm:
    pass
```

**Correct code:**

```
__all__ = ["Fruit", "Worm"]

class Fruit:
    pass

class Worm:
    pass
```

**Additional details:**

**FromThe Python Language Reference – The import statement:**
: "Thepublic namesdefined by a module are determined by checking the module's namespace for a variable named__all__; if defined, it must be a sequence of strings which are names defined or imported by that module."

**Related links:**

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#module-level-dunder-names)

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.