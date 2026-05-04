---
id: pylint-R0913
rule_code: "R0913"
rule_name: "too-many-arguments"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/too-many-arguments.html"
---
# too-many-arguments / R0913

**Message emitted:**

`Too many arguments (%s/%s)`

**Description:**

*Used when a function or method takes too many arguments.*

**Problematic code:**

```
def three_d_chess_move(  # [too-many-arguments]
    x_white,
    y_white,
    z_white,
    piece_white,
    x_black,
    y_black,
    z_black,
    piece_black,
    x_blue,
    y_blue,
    z_blue,
    piece_blue,
    current_player,
):
    pass
```

**Correct code:**

```
from dataclasses import dataclass

@dataclass
class ThreeDChessPiece:
    x: int
    y: int
    z: int
    type: str

def three_d_chess_move(
    white: ThreeDChessPiece,
    black: ThreeDChessPiece,
    blue: ThreeDChessPiece,
    current_player,
):
    pass
```

Created by the [design](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/design_analysis.py) checker.