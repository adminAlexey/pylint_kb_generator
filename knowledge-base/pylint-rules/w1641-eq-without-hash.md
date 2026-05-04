---
id: pylint-W1641
rule_code: "W1641"
rule_name: "eq-without-hash"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/eq-without-hash.html"
---
# eq-without-hash / W1641

**Message emitted:**

`Implementing __eq__ without also implementing __hash__`

**Description:**

*Used when a class implements __eq__ but not __hash__. Objects get None as their default __hash__ implementation if they also implement __eq__.*

**Problematic code:**

```
class Fruit:  # [eq-without-hash]
    def __init__(self) -> None:
        self.name = "apple"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Fruit) and other.name == self.name
```

**Correct code:**

```
class Fruit:
    def __init__(self) -> None:
        self.name = "apple"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Fruit) and other.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.eq_without_hash,
```

Note

This message is emitted by the optional ['eq-without-hash'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-eq-without-hash)
checker, which requires the `pylint.extensions.eq_without_hash` plugin to be loaded.

Created by the [eq-without-hash](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/eq_without_hash.py) checker.