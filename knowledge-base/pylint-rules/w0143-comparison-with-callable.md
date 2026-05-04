---
id: pylint-W0143
rule_code: "W0143"
rule_name: "comparison-with-callable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/comparison-with-callable.html"
---
# comparison-with-callable / W0143

**Message emitted:**

`Comparing against a callable, did you omit the parenthesis?`

**Description:**

*This message is emitted when pylint detects that a comparison with a callable was made, which might suggest that some parenthesis were omitted, resulting in potential unwanted behaviour.*

**Problematic code:**

```
def function_returning_a_fruit() -> str:
    return "orange"

def is_an_orange(fruit: str = "apple"):
    # apple == <function function_returning_a_fruit at 0x7f343ff0a1f0>
    return fruit == function_returning_a_fruit  # [comparison-with-callable]
```

**Correct code:**

```
def function_returning_a_fruit() -> str:
    return "orange"

def is_an_orange(fruit: str = "apple"):
    # apple == orange
    return fruit == function_returning_a_fruit()
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/comparison_checker.py) checker.