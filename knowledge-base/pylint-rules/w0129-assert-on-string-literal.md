---
id: pylint-W0129
rule_code: "W0129"
rule_name: "assert-on-string-literal"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/assert-on-string-literal.html"
---
# assert-on-string-literal / W0129

**Message emitted:**

`Assert statement has a string literal as its first argument. The assert will %s fail.`

**Description:**

*Used when an assert statement has a string literal as its first argument, which will cause the assert to always pass.*

**Problematic code:**

```
def test_division():
    a = 9 / 3
    assert "No ZeroDivisionError were raised"  # [assert-on-string-literal]
```

**Correct code:**

```
def test_division():
    a = 9 / 3
    assert a == 3
```

**Additional details:**

Directly asserting a string literal will always pass. The solution is to
test something that could fail, or not assert at all.

For `unittest` assertions there is the similar [redundant-unittest-assert / W1503](https://pylint.readthedocs.io/en/latest/user_guide/messages/redundant-unittest-assert.html#redundant-unittest-assert) message.

**Related links:**

- [Tests without assertion](https://stackoverflow.com/a/137418/2519059)
- [Testing that there is no error raised](https://stackoverflow.com/questions/20274987)
- [Parametrizing conditional raising](https://docs.pytest.org/en/latest/example/parametrize.html#parametrizing-conditional-raising)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.