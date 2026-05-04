---
id: pylint-W0149
rule_code: "W0149"
rule_name: "while-used"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/while-used.html"
---
# while-used / W0149

**Message emitted:**

`Used `while` loop`

**Description:**

*Unbounded `while` loops can often be rewritten as bounded `for` loops. Exceptions can be made for cases such as event loops, listeners, etc.*

**Problematic code:**

```
import requests

def fetch_data():
    i = 1
    while i < 6:  # [while-used]
        print(f"Attempt {i}...")
        try:
            return requests.get("https://example.com/data")
        except requests.exceptions.RequestException:
            pass
        i += 1
```

**Correct code:**

```
import requests

def fetch_data():
    for i in range(1, 6):
        print(f"Attempt {i}...")
        try:
            return requests.get("https://example.com/data")
        except requests.exceptions.RequestException:
            pass
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.while_used
```

**Related links:**

- [Stackoverflow discussion](https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python)

Note

This message is emitted by the optional ['while_used'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-while-used)
checker, which requires the `pylint.extensions.while_used` plugin to be loaded.

Created by the [while_used](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/while_used.py) checker.