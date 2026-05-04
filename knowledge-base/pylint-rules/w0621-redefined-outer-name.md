---
id: pylint-W0621
rule_code: "W0621"
rule_name: "redefined-outer-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redefined-outer-name.html"
---
# redefined-outer-name / W0621

**Message emitted:**

`Redefining name %r from outer scope (line %s)`

**Description:**

*Used when a variable's name hides a name defined in an outer scope or except handler.*

**Problematic code:**

```
count = 10

def count_it(count):  # [redefined-outer-name]
    for i in range(count):
        print(i)
```

**Correct code:**

```
count = 10

def count_it(limit):
    for i in range(limit):
        print(i)
```

**Additional details:**

A common issue is that this message is triggered when using pytest [fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html):

```
import pytest

@pytest.fixture
def setup():
    ...

def test_something(setup):  # [redefined-outer-name]
    ...
```

One solution to this problem is to explicitly name the fixture:

```
@pytest.fixture(name="setup")
def setup_fixture():
    ...
```

Alternatively pylint plugins like [pylint-pytest](https://pypi.org/project/pylint-pytest/) can be used.

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.