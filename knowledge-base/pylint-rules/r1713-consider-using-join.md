---
id: pylint-R1713
rule_code: "R1713"
rule_name: "consider-using-join"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-join.html"
---
# consider-using-join / R1713

**Message emitted:**

`Consider using str.join(sequence) for concatenating strings from an iterable`

**Description:**

*Using str.join(sequence) is faster, uses less memory and increases readability compared to for-loop iteration.*

**Problematic code:**

```
def fruits_to_string(fruits):
    formatted_fruit = ""
    for fruit in fruits:
        formatted_fruit += fruit  # [consider-using-join]
    return formatted_fruit

print(fruits_to_string(["apple", "pear", "peach"]))
```

**Correct code:**

```
print("".join(["apple", "pear", "peach"]))
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.