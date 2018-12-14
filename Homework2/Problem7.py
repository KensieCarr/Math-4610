import numpy as np
from sympy import *

def f(x):
    #x^2 - 3
    return x**2-3

def g(x):
    #sin(pi x)
    return float(sin(pi*x))

def secantMethod(fn, x0, x1, tol, maxIter):
    for i in range(0, maxIter):
        xtemp = x1
        if Abs(x0 - x1) < tol:
            return x1
        x1 = x1 - (fn(x1)*(x1-x0))/(fn(x1)-fn(x0))
        x0 = xtemp
    return float(x1)
    
if __name__ == '__main__':
    x = symbols('x')
    print(secantMethod(f, 1, 1.6, 1.0e-5, 100))
    print(secantMethod(g, 5.5, 5.8, 1.0e-5, 100))