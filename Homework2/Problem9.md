# Homework 2

## Problem 9

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

def secantMethod(fn, x0, x1, tol, maxIter):
    for i in range(0, maxIter):
        xtemp = x1
        if Abs(x0 - x1) < tol:
            return x1
        x1 = float(x1 - (fn(x1)*(x1-x0))/(fn(x1)-fn(x0)))
        x0 = xtemp
    return float(x1)
    
if __name__ == '__main__':
    x = symbols('x')
    print(secantMethod(f, 1, bisectionMethod(f, 1, 3, 1.0e-1), 1.0e-10, 100))
    print(secantMethod(g, 1.75, bisectionMethod(g, 1.25, 2.5, 1.0e-1), 1.0e-10,100))
```
[full code](https://KensieCarr.github.io/Math-4610/Homework2/Problem9.py)

**Last Modified:** September/2018
