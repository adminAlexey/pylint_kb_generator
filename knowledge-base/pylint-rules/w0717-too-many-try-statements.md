---
id: pylint-W0717
rule_code: "W0717"
rule_name: "too-many-try-statements"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/too-many-try-statements.html"
---
# too-many-try-statements / W0717

**Message emitted:**

`%s`

**Description:**

*Try clause contains too many statements.*

**Problematic code:**

```
FRUITS = {"apple": 1, "orange": 10}

def pick_fruit(name):
    try:  # [too-many-try-statements]
        count = FRUITS[name]
        count += 1
        print(f"Got fruit count {count}")
    except KeyError:
        return
```

**Correct code:**

```
FRUITS = {"apple": 1, "orange": 10}

def pick_fruit(name):
    try:
        count = FRUITS[name]
    except KeyError:
        return

    count += 1
    print(f"Got fruit count {count}")
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.broad_try_clause,
```

Note

This message is emitted by the optional ['broad_try_clause'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-broad-try-clause)
checker, which requires the `pylint.extensions.broad_try_clause` plugin to be loaded.

Created by the [broad_try_clause](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/broad_try_clause.py) checker.