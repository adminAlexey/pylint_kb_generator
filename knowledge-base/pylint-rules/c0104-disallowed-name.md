---
id: pylint-C0104
rule_code: "C0104"
rule_name: "disallowed-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/disallowed-name.html"
---
# disallowed-name / C0104

**Message emitted:**

`Disallowed name "%s"`

**Description:**

*Used when the name matches bad-names or bad-names-rgxs- (unauthorized names).*

**Problematic code:**

```
def foo():  # [disallowed-name]
    print("apples")
```

**Correct code:**

```
def print_fruit():
    print("apples")
```

**Configuration file:**

```
[MAIN]
bad-names=foo,bar,baz
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/name_checker/checker.py) checker.