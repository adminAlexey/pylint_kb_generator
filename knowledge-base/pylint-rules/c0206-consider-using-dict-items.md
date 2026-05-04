---
id: pylint-C0206
rule_code: "C0206"
rule_name: "consider-using-dict-items"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/consider-using-dict-items.html"
---
# consider-using-dict-items / C0206

**Message emitted:**

`Consider iterating with .items()`

**Description:**

*Emitted when iterating over the keys of a dictionary and accessing the value by index lookup. Both the key and value can be accessed by iterating using the .items() method of the dictionary instead.*

**Problematic code:**

```
ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}

for instrument in ORCHESTRA:  # [consider-using-dict-items]
    print(f"{instrument}: {ORCHESTRA[instrument]}")
```

**Correct code:**

```
ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}

for instrument, section in ORCHESTRA.items():
    print(f"{instrument}: {section}")
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/recommendation_checker.py) checker.