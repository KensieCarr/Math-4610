import numpy as np
from sympy import *

def f(x):
    #x^2 - 3
    return x**2 - 3

def g(x):
    #sin(pi x)
    return sin(pi*x)

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
    
if __name__ == '__main__':
    x = symbols('x')
    print(bisectionMethod(f, 1, 3, 1.0e-5))
    print(bisectionMethod(g, 0.25, 1.5,.0e-5))
    
