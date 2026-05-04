---
id: pylint-W1502
rule_code: "W1502"
rule_name: "boolean-datetime"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/boolean-datetime.html"
---
# boolean-datetime / W1502

**Message emitted:**

`Using datetime.time in a boolean context.`

**Description:**

*Using datetime.time in a boolean context can hide subtle bugs when the time they represent matches midnight UTC. This behaviour was fixed in Python 3.5. See https://bugs.python.org/issue13936 for reference.*

**Problematic code:**

```
import datetime

if datetime.time():  # [boolean-datetime]
    print("It is time.")

if datetime.datetime.now().time():  # [boolean-datetime]
    print("Now or never.")
```

**Correct code:**

```
import datetime

time_now_utc = datetime.datetime.now(tz=datetime.UTC).time()

if time_now_utc > datetime.time(6, 0):
    print("Daytime!")

if time_now_utc < datetime.time(6, 0):
    print("Nighttime!")
```

**Configuration file:**

```
[main]
py-version=3.4
```

**Related links:**

- [Python bug tracker](https://bugs.python.org/issue13936)

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.