---
id: pylint-W0150
rule_code: "W0150"
rule_name: "lost-exception"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/lost-exception.html"
---
# lost-exception / W0150

**Message emitted:**

`%s statement in finally block may swallow exception`

**Description:**

*Used when a break or a return statement is found inside the finally clause of a try...finally block: the exceptions raised in the try clause will be silently swallowed instead of being re-raised.*

**Problematic code:**

```
class FasterThanTheSpeedOfLightError(ZeroDivisionError):
    def __init__(self):
        super().__init__("You can't go faster than the speed of light !")

def calculate_speed(distance: float, time: float) -> float:
    try:
        return distance / time
    except ZeroDivisionError as e:
        raise FasterThanTheSpeedOfLightError() from e
    finally:
        return 299792458  # [lost-exception]
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

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.