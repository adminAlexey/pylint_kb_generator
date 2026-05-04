---
id: pylint-W1515
rule_code: "W1515"
rule_name: "forgotten-debug-statement"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/forgotten-debug-statement.html"
---
# forgotten-debug-statement / W1515

**Message emitted:**

`Leaving functions creating breakpoints in production code is not recommended`

**Description:**

*Calls to breakpoint(), sys.breakpointhook() and pdb.set_trace() should be removed from code that is not actively being debugged.*

**Problematic code:**

```
import pdb

def find_the_treasure(clues):
    for clue in clues:
        pdb.set_trace()  # [forgotten-debug-statement]
        if "treasure" in clue:
            return True
    return False

treasure_hunt = [
    "Dead Man's Chest",
    "X marks the spot",
    "The treasure is buried near the palm tree",
]
find_the_treasure(treasure_hunt)
```

**Correct code:**

```
def find_the_treasure(clues):
    for clue in clues:
        if "treasure" in clue:
            return True
    return False

treasure_hunt = [
    "Dead Man's Chest",
    "X marks the spot",
    "The treasure is buried near the palm tree",
]
find_the_treasure(treasure_hunt)
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.