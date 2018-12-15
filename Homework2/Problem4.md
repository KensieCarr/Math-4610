# Homework 2

## Problem 4

**Routine Name:**  Fixed Point Iteration         

**Author:** Kensie Carr

**Language:** Python

**Description/Purpose:** 
Fixed point iteration searches for a root of a given function. Given a scalar continuous function in one variable, *f(x)*, select a function *g(x)* such that *x* satisfies *f(x) = 0* if and only if *g(x) = x*. Then:

1. Start from ann initial guess *x0*.

2. For *k - 0,1,2,..., set*
<p>
  $x_{k+1} = g(x_k)
</p>
until <p>$x_{k+1}$</p> satisfies termination criteria
**Input:**
<p>
  $g_1(x) = x - \dfrac{x^2-3}{10}$
  <br>
  Initial Guess: 0
  <br>
  $g_2(x) = x - \dfrac{\sin{\pi x}}{2}$
  <br>
  Initial Guess: 5.9
</p>
Max Iterations: 100

Tolerance: 1.0xe-5

**Output:** 
<pre>
1.7320508075688772
6.000000000000001
</pre>

**Usage/Example:**

**Implementation/Code:** 
```python
def fixedPointIteration(fn, x0, tol, maxIter):
    x1 = fn(x0)
    for i in range(0, maxIter):
        if Abs(x0 - x1) < tol:
            return x1
        x1 = fn(float(x1))
    return float(x1)
```
[full code](https://KensieCarr.github.io/Math-4610/Homework2/Problem4.py)
**Last Modified:** September/2018
