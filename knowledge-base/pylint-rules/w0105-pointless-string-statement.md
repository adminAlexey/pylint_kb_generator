---
id: pylint-W0105
rule_code: "W0105"
rule_name: "pointless-string-statement"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/pointless-string-statement.html"
---
# pointless-string-statement / W0105

**Message emitted:**

`String statement has no effect`

**Description:**

*Used when a string is used as a statement (which of course has no effect). This is a particular case of W0104 with its own message so you can easily disable it if you're using those strings as documentation, instead of comments.*

**Problematic code:**

```
"""This is a docstring which describes the module"""

"""This is not a docstring"""  # [pointless-string-statement]
```

**Correct code:**

```
"""This is a docstring which describes the module"""

# This is comment which describes a particular part of the module.
```

**Related links:**

- [Discussion thread re: docstrings on assignments](https://discuss.python.org/t/docstrings-for-new-type-aliases-as-defined-in-pep-695/39816)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.