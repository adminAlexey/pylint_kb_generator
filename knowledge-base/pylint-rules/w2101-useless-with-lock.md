---
id: pylint-W2101
rule_code: "W2101"
rule_name: "useless-with-lock"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/useless-with-lock.html"
---
# useless-with-lock / W2101

**Message emitted:**

`'%s()' directly created in 'with' has no effect`

**Description:**

*Used when a new lock instance is created by using with statement which has no effect. Instead, an existing instance should be used to acquire lock.*

**Problematic code:**

```
import threading

with threading.Lock():  # [useless-with-lock]
    print("Make your bed.")
with threading.Lock():  # [useless-with-lock]
    print("Sleep in it")
```

**Correct code:**

```
import threading

lock = threading.Lock()
with lock:
    print("Make your bed.")
with lock:
    print("Sleep in it.")
```

Created by the [threading](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/threading_checker.py) checker.