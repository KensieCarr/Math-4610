# Homework 2

## Problem 5

**Routine Name:**  Bisection Method         

**Author:** Kensie Carr

**Language:** Python

**Description/Purpose:** 

**Input:**
<p>
  $f_1(x) = x^2 - 3$
  <br>
  $g_1(x) = x - \dfrac{x^2-3}{10}$
  <br>
  
  <br>
  $f_2(x) = \sin(\pi x)$
  <br>
  Point A: 1 Point B: 3
  <br>
  $g_2(x) = x - \dfrac{\sin{\pi x}}{2}$
  <br>
  Point A: 0.35 Point B: 1.5
  <br>
  Tolerance: 1.0e-5
</p>

Tolerance: 1.0xe-5

**Output:** 
<pre>
1.7320480346679688
1.0
</pre>

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
```
[full code](https://KensieCarr.github.io/Math-4610/Homework2/Problem5.py)

**Last Modified:** September/2018
