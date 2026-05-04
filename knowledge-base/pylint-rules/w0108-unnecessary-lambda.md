---
id: pylint-W0108
rule_code: "W0108"
rule_name: "unnecessary-lambda"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unnecessary-lambda.html"
---
# unnecessary-lambda / W0108

**Message emitted:**

`Lambda may not be necessary`

**Description:**

*Used when the body of a lambda expression is a function call on the same argument list as the lambda itself; such lambda expressions are in all but a few cases replaceable with the function being called in the body of the lambda.*

**Problematic code:**

`pandas.py`:

```
df.apply(lambda x: str(x))  # [unnecessary-lambda]
```

`print.py`:

```
function = lambda x: print(x)  # [unnecessary-lambda]

function("Hello world !")
```

**Correct code:**

`pandas.py`:

```
df.apply(str)
```

`print.py`:

```
print("Hello world !")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.