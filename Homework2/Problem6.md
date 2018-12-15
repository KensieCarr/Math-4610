# Homework 2

## Problem 6

**Routine Name:**           

**Author:** Kensie Carr

**Language:** Python

**Description/Purpose:** 

**Input:**

**Output:** 

**Usage/Example:**

**Implementation/Code:** 
```python
def newtonMethod(fn, x0, tol, maxIter):
    x1 = fn(x0)
    for i in range(0, maxIter):
        if Abs(x0 - x1) < tol:
            return x1
        if (fn is f):
            x1 = float(x1 - fn(x1)/(2*x1))
        if (fn is g):
            x1 = float(x1 - fn(x1)/(pi*cos(pi*x1)))
        
    return float(x1)
```
[full code](https://KensieCarr.github.io/Math-4610/Homework2/Problem5.py)

**Last Modified:** September/2018
