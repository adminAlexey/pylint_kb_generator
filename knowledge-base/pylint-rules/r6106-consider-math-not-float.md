---
id: pylint-R6106
rule_code: "R6106"
rule_name: "consider-math-not-float"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-math-not-float.html"
---
# consider-math-not-float / R6106

**Message emitted:**

`Consider %smath.%s instead of %s`

**Description:**

*Using math.inf or math.nan permits to benefit from typing and it is up to 4 times faster than a float call (after the initial import of math). This check also catches typos in float calls as a side effect.*

**Problematic code:**

```
swag = float("inf")  # [consider-math-not-float]
```

**Correct code:**

```
import math

swag = math.inf
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.code_style
```

**Additional details:**

This is an extension check because the typing advantage could be fixed.

Regarding performance, float("nan") and float("inf") are slower than their counterpart math.inf and math.nan by a factor of 4 after the initial import of math.

```
import math
import timeit

time_math_inf = timeit.timeit('math.nan', globals=globals(), number=10**8)
print(f'math.nan: {time_math_inf:.2f} seconds')

import timeit
time_inf_str = timeit.timeit('float("nan")', number=10**8)
print(f'float("nan"): {time_inf_str:.2f} seconds')
```

Result:

```
math.nan: 1.24 seconds
float("nan"): 5.15 seconds
```

But if we take the initial import into account it's worse.

```
import timeit

time_math_inf = timeit.timeit('import math;math.nan', globals=globals(), number=10**8)
print(f'math.nan: {time_math_inf:.2f} seconds')

import timeit
time_inf_str = timeit.timeit('float("nan")', number=10**8)
print(f'float("nan"): {time_inf_str:.2f} seconds')
```

Result:

```
math.nan: 9.08 seconds
float("nan"): 5.33 seconds
```

So the decision depends on how and how often you need to use it and what matter to you.

Note

This message is emitted by the optional ['code_style'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-code-style)
checker, which requires the `pylint.extensions.code_style` plugin to be loaded.

Created by the [code_style](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/code_style.py) checker.