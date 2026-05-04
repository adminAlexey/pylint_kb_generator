---
id: pylint-W1510
rule_code: "W1510"
rule_name: "subprocess-run-check"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/subprocess-run-check.html"
---
# subprocess-run-check / W1510

**Message emitted:**

`'subprocess.run' used without explicitly defining the value for 'check'.`

**Description:**

*The ``check`` keyword  is set to False by default. It means the process launched by ``subprocess.run`` can exit with a non-zero exit code and fail silently. It's better to set it explicitly to make clear what the error-handling behavior is.*

**Problematic code:**

```
import subprocess

proc = subprocess.run(["ls"])  # [subprocess-run-check]
```

**Correct code:**

```
import subprocess

proc = subprocess.run(["ls"], check=False)
```

**Related links:**

- [subprocess.run documentation](https://docs.python.org/3/library/subprocess.html#subprocess.run)

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.