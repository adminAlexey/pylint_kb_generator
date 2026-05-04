---
id: pylint-C0415
rule_code: "C0415"
rule_name: "import-outside-toplevel"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/import-outside-toplevel.html"
---
# import-outside-toplevel / C0415

**Message emitted:**

`Import outside toplevel (%s)`

**Description:**

*Used when an import statement is used anywhere other than the module toplevel. Move this import to the top of the file.*

**Problematic code:**

```
def print_python_version():
    import sys  # [import-outside-toplevel]

    print(sys.version_info)
```

**Correct code:**

```
import sys

def print_python_version():
    print(sys.version_info)
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.