---
id: pylint-R0902
rule_code: "R0902"
rule_name: "too-many-instance-attributes"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/too-many-instance-attributes.html"
---
# too-many-instance-attributes / R0902

**Message emitted:**

`Too many instance attributes (%s/%s)`

**Description:**

*Used when class has too many instance attributes, try to reduce this to get a simpler (and so easier to use) class.*

**Problematic code:**

```
class Fruit:  # [too-many-instance-attributes]
    def __init__(self):
        # max of 7 attributes by default, can be configured
        self.worm_name = "Jimmy"
        self.worm_type = "Codling Moths"
        self.worm_color = "light brown"
        self.fruit_name = "Little Apple"
        self.fruit_color = "Bright red"
        self.fruit_vitamins = ["A", "B1"]
        self.fruit_antioxidants = None
        self.secondary_worm_name = "Kim"
        self.secondary_worm_type = "Apple maggot"
        self.secondary_worm_color = "Whitish"
```

**Correct code:**

```
import dataclasses

@dataclasses.dataclass
class Worm:
    name: str
    type: str
    color: str

class Fruit:
    def __init__(self):
        self.name = "Little Apple"
        self.color = "Bright red"
        self.vitamins = ["A", "B1"]
        self.antioxidants = None
        self.worms = [
            Worm(name="Jimmy", type="Codling Moths", color="light brown"),
            Worm(name="Kim", type="Apple maggot", color="Whitish"),
        ]
```

Created by the [design](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/design_analysis.py) checker.