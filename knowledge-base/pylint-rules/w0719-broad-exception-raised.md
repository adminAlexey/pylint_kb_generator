---
id: pylint-W0719
rule_code: "W0719"
rule_name: "broad-exception-raised"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/broad-exception-raised.html"
---
# broad-exception-raised / W0719

**Message emitted:**

`Raising too general exception: %s`

**Description:**

*Raising exceptions that are too generic force you to catch exceptions generically too. It will force you to use a naked ``except Exception:`` clause. You might then end up catching exceptions other than the ones you expect to catch. This can hide bugs or make it harder to debug programs when unrelated errors are hidden.*

**Problematic code:**

```
def small_apple(apple, length):
    if len(apple) < length:
        raise Exception("Apple is too small!")  # [broad-exception-raised]
    print(f"{apple} is proper size.")
```

**Correct code:**

```
def small_apple(apple, length):
    if len(apple) < length:
        raise ValueError("Apple is too small!")
    print(f"{apple} is proper size.")
```

**Related links:**

- [Programming recommendation in PEP8](https://peps.python.org/pep-0008/#programming-recommendations)

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.