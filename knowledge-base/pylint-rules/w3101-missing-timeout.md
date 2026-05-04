---
id: pylint-W3101
rule_code: "W3101"
rule_name: "missing-timeout"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-timeout.html"
---
# missing-timeout / W3101

**Message emitted:**

`Missing timeout argument for method '%s' can cause your program to hang indefinitely`

**Description:**

*Used when a method needs a 'timeout' parameter in order to avoid waiting for a long time. If no timeout is specified explicitly the default value is used. For example for 'requests' the program will never time out (i.e. hang indefinitely).*

**Problematic code:**

```
import requests

requests.post("http://localhost")  # [missing-timeout]
```

**Correct code:**

```
import requests

requests.post("http://localhost", timeout=10)
```

**Additional details:**

You can add new methods that should have a defined ``timeout` argument as qualified names
in the `timeout-methods` option, for example:

- `requests.api.get`
- `requests.api.head`
- `requests.api.options`
- `requests.api.patch`
- `requests.api.post`
- `requests.api.put`
- `requests.api.request`

Created by the [method_args](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/method_args.py) checker.