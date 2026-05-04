---
id: pylint-R6101
rule_code: "R6101"
rule_name: "consider-using-namedtuple-or-dataclass"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-namedtuple-or-dataclass.html"
---
# consider-using-namedtuple-or-dataclass / R6101

**Message emitted:**

`Consider using namedtuple or dataclass for dictionary values`

**Description:**

*Emitted when dictionary values can be replaced by namedtuples or dataclass instances.*

**Problematic code:**

```
FELIDAES = {  # [consider-using-namedtuple-or-dataclass]
    "The queen's cymric, fragile furry friend": {
        "tail_length_cm": 1,
        "paws": 4,
        "eyes": 2,
        "Elizabethan collar": 1,
    },
    "Rackat the red, terror of the sea": {
        "tail_length_cm": 13,
        "paws": 3,
        "eyes": 1,
        "Red Hat": 1,
    },
}
```

**Correct code:**

```
from typing import NamedTuple

class FelidaeCharacteristics(NamedTuple):
    tail_length_cm: int
    paws: int
    eyes: int
    hat: str | None

FELIDAES = {
    "The queen's cymric, fragile furry friend": FelidaeCharacteristics(
        tail_length_cm=1, paws=4, eyes=2, hat="Elizabethan collar"
    ),
    "Rackat the red, terror of the sea": FelidaeCharacteristics(
        tail_length_cm=21, paws=3, eyes=1, hat="Red Hat"
    ),
}
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.code_style
```

Note

This message is emitted by the optional ['code_style'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-code-style)
checker, which requires the `pylint.extensions.code_style` plugin to be loaded.

Created by the [code_style](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/code_style.py) checker.