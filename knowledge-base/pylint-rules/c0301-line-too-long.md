---
id: pylint-C0301
rule_code: "C0301"
rule_name: "line-too-long"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/line-too-long.html"
---
# line-too-long / C0301

**Message emitted:**

`Line too long (%s/%s)`

**Description:**

*Used when a line is longer than a given number of characters.*

**Problematic code:**

```
# +1: [line-too-long]
FRUIT = ["apricot", "blackcurrant", "cantaloupe", "dragon fruit", "elderberry", "fig", "grapefruit", ]
```

**Correct code:**

```
FRUIT = [
    "apricot",
    "blackcurrant",
    "cantaloupe",
    "dragon fruit",
    "elderberry",
    "fig",
    "grapefruit",
]
```

**Configuration file:**

```
[MAIN]
max-line-length=100
```

**Additional details:**

Pragma controls such as `# pylint: disable=all` are not counted toward line length for the purposes of this message.

If you attempt to disable this message via `# pylint: disable=line-too-long` in a module with no code, you may receive a message for `useless-suppression`. This is a false positive of `useless-suppression` we can't easily fix.

See [https://github.com/pylint-dev/pylint/issues/3368](https://github.com/pylint-dev/pylint/issues/3368) for more information.

Created by the [format](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/format.py) checker.