---
id: pylint-W0406
rule_code: "W0406"
rule_name: "import-self"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/import-self.html"
---
# import-self / W0406

**Message emitted:**

`Module import itself`

**Description:**

*Used when a module is importing itself.*

**Additional details:**

Say you have a file called `my_file.py`. `import-self` would be raised on the following code:

```
from my_file import a_function  # [import-self]

def a_function():
    pass
```

The solution would be to remove the import:

```
def a_function():
    pass
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.