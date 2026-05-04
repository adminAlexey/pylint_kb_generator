---
id: pylint-W1117
rule_code: "W1117"
rule_name: "kwarg-superseded-by-positional-arg"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/kwarg-superseded-by-positional-arg.html"
---
# kwarg-superseded-by-positional-arg / W1117

**Message emitted:**

`%r will be included in %r since a positional-only parameter with this name already exists`

**Description:**

*Emitted when a function is called with a keyword argument that has the same name as a positional-only parameter and the function contains a keyword variadic parameter dict.*

**Problematic code:**

```
def print_name(name="Sarah", /, **kwds):
    print(name)

print_name(name="Jacob")  # [kwarg-superseded-by-positional-arg]
# Will print "Sarah"
```

**Correct code:**

```
def print_name(name="Sarah", /, **kwds):
    print(name)

print_name("Jacob")
# Will print "Jacob"
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.