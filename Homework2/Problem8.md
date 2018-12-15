# Homework 2

## Problem 8

**Routine Name:**           

**Author:** Kensie Carr

**Language:** Python

**Description/Purpose:** 

**Input:**

**Output:** 

**Usage/Example:**

**Implementation/Code:** 
```python
def bisectionMethod(fn, a, b, tol):
    mid = (a+b)/2
    while (b-a)/2 > tol:
        if fn(mid) == 0:
            return mid
        elif fn(a)*fn(mid) < 0:
            b = mid
        else:
            a = mid
        mid = (a+b)/2
    return mid

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
    
if __name__ == '__main__':
    x = symbols('x')
    print(newtonMethod(f, bisectionMethod(f, 1, 3, 1.0e-1), 1.0e-5, 100))
    print(newtonMethod(g, bisectionMethod(g, 1.25, 2.5, 1.0e-1), 1.0e-5, 100))
```
[full code](https://KensieCarr.github.io/Math-4610/Homework2/Problem8.py)

**Last Modified:** September/2018
