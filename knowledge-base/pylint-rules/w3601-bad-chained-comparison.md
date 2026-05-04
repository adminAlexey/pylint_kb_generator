---
id: pylint-W3601
rule_code: "W3601"
rule_name: "bad-chained-comparison"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-chained-comparison.html"
---
# bad-chained-comparison / W3601

**Message emitted:**

`Suspicious %s-part chained comparison using semantically incompatible operators (%s)`

**Description:**

*Used when there is a chained comparison where one expression is part of two comparisons that belong to different semantic groups ("<" does not mean the same thing as "is", chaining them in "0 < x is None" is probably a mistake).*

**Problematic code:**

`parrot.py`:

```
shop = {
    # animal: (specie, descriptions)
    "parrot": ("Norvegian blue", ("restin'", "remarkable", "beautiful plumage")),
}

if "parrot" in shop is "restin'":  # [bad-chained-comparison]
    print("Hellooooo, Pooolllllyyy ! WAAAAKEEY, WAKKEEEY !")
```

`xor.py`:

```
def xor_check(*, left=None, right=None):
    if left is None != right is None:  # [bad-chained-comparison]
        raise ValueError(
            "Either both left= and right= need to be provided or none should."
        )
```

**Correct code:**

`parrot.py`:

```
shop = {
    # animal: (specie, descriptions)
    "parrot": ("Norvegian blue", ("restin'", "remarkable", "beautiful plumage")),
}

if "parrot" in shop and "restin'" in shop["parrot"][1]:
    print("Hellooooo, Pooolllllyyy ! WAAAAKEEY, WAKKEEEY !")
```

`xor.py`:

```
def xor_check(*, left=None, right=None):
    if (left is None) != (right is None):
        raise ValueError(
            "Either both left= and right= need to be provided or none should."
        )
```

**Related links:**

- [Comparison Chaining](https://docs.python.org/3/reference/expressions.html#comparisons)

Created by the [bad-chained-comparison](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/bad_chained_comparison.py) checker.