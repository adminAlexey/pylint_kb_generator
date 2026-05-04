---
id: pylint-W1506
rule_code: "W1506"
rule_name: "bad-thread-instantiation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-thread-instantiation.html"
---
# bad-thread-instantiation / W1506

**Message emitted:**

`threading.Thread needs the target function`

**Description:**

*The warning is emitted when a threading.Thread class is instantiated without the target function being passed as a kwarg or as a second argument. By default, the first parameter is the group param, not the target param.*

**Problematic code:**

```
import threading

def thread_target(n):
    print(n**2)

thread = threading.Thread(lambda: None)  # [bad-thread-instantiation]
thread.start()
```

**Correct code:**

```
import threading

def thread_target(n):
    print(n**2)

thread = threading.Thread(target=thread_target, args=(10,))
thread.start()
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.