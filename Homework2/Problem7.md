# Homework 2

## Problem 7

**Routine Name:**           

**Author:** Kensie Carr

**Language:** C++

**Description/Purpose:** 

**Input:**

**Output:** 

**Usage/Example:**

**Implementation/Code:** 
```python
def secantMethod(fn, x0, x1, tol, maxIter):
    for i in range(0, maxIter):
        xtemp = x1
        if Abs(x0 - x1) < tol:
            return x1
        x1 = x1 - (fn(x1)*(x1-x0))/(fn(x1)-fn(x0))
        x0 = xtemp
    return float(x1)
```
[full code](https://KensieCarr.github.io/Math-4610/Homework2/Problem7.py)
**Last Modified:** September/2018
