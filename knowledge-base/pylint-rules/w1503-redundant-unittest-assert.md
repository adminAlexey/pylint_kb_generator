---
id: pylint-W1503
rule_code: "W1503"
rule_name: "redundant-unittest-assert"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redundant-unittest-assert.html"
---
# redundant-unittest-assert / W1503

**Message emitted:**

`Redundant use of %s with constant value %r`

**Description:**

*The first argument of assertTrue and assertFalse is a condition. If a constant is passed as parameter, that condition will be always true. In this case a warning should be emitted.*

**Problematic code:**

```
import unittest

class DummyTestCase(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue("foo")  # [redundant-unittest-assert]
```

**Correct code:**

```
import unittest

class DummyTestCase(unittest.TestCase):
    def test_dummy(self):
        actual = "test_result"
        self.assertEqual(actual, "expected")
```

**Additional details:**

Directly asserting a string literal will always pass. The solution is to
test something that could fail, or not assert at all.

For assertions using `assert` there are similar messages: [assert-on-string-literal / W0129](https://pylint.readthedocs.io/en/latest/user_guide/messages/assert-on-string-literal.html#assert-on-string-literal) and [assert-on-tuple / W0199](https://pylint.readthedocs.io/en/latest/user_guide/messages/assert-on-tuple.html#assert-on-tuple).

**Related links:**

- [Tests without assertion](https://stackoverflow.com/a/137418/2519059)
- [Testing that there is no error raised](https://stackoverflow.com/questions/20274987)
- [Parametrizing conditional raising](https://docs.pytest.org/en/latest/example/parametrize.html#parametrizing-conditional-raising)

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.