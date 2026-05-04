---
id: pylint-E0702
rule_code: "E0702"
rule_name: "raising-bad-type"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/raising-bad-type.html"
---
# raising-bad-type / E0702

**Message emitted:**

`Raising %s while only classes or instances are allowed`

**Description:**

*Used when something which is neither a class nor an instance is raised (i.e. a `TypeError` will be raised).*

**Problematic code:**

```
class FasterThanTheSpeedOfLightError(ZeroDivisionError):
    def __init__(self):
        super().__init__("You can't go faster than the speed of light !")

def calculate_speed(distance: float, time: float) -> float:
    try:
        return distance / time
    except ZeroDivisionError as e:
        raise None  # [raising-bad-type]
```

**Correct code:**

```
class FasterThanTheSpeedOfLightError(ZeroDivisionError):
    def __init__(self):
        super().__init__("You can't go faster than the speed of light !")

def calculate_speed(distance: float, time: float) -> float:
    try:
        return distance / time
    except ZeroDivisionError as e:
        raise FasterThanTheSpeedOfLightError() from e
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.