---
id: pylint-R1722
rule_code: "R1722"
rule_name: "consider-using-sys-exit"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-sys-exit.html"
---
# consider-using-sys-exit / R1722

**Message emitted:**

`Consider using 'sys.exit' instead`

**Description:**

*Contrary to 'exit()' or 'quit()', 'sys.exit' does not rely on the site module being available (as the 'sys' module is always available).*

**Problematic code:**

```
if __name__ == "__main__":
    user = input("Enter user name: ")
    print(f"Hello, {user}")
    exit(0)  # [consider-using-sys-exit]
```

**Correct code:**

```
import sys

if __name__ == "__main__":
    user = input("Enter user name: ")
    print(f"Hello, {user}")
    sys.exit(0)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.