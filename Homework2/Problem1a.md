# Homework 2

## Problem 1a

**Routine Name:**           Compute Absolute Error

**Author:** Kensie Carr

**Language:** C++

**Description/Purpose:** 
This routine computes the absolute error in the approximation of one number by another.

**Input:**
z = single value solution

y = numerical method produced solution

**Output:** 
E = Absolute Error

**Usage/Example:**
Suppose that z = 2.2, while some computed solution y = 2.20345. The absolute error can be computed using 
<p> 
    $|E| = |y - z| $
</p>
In this case the absolute error is 0.00345 or 3.45 x 10^{-3}

**Implementation/Code:** 
```c++
int absoluteError (int solution, int computedSolution) { 
    int absoluteError = abs(computedSolution - solution);
    return absoluteError;
}
```
[full code](https://KensieCarr.github.io/Math-4610/Homework2/absoluteError.cpp)

**Last Modified:** September/2018
