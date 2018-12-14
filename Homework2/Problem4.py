import numpy as np
from sympy import *

def f(x):
    #x^2 - 3
    return x - ((x**2 - 3)/10)

def g(x):
    #sin(pi x)
    return x - (sin(pi * x)/2)

def fixedPointIteration(fn, x0, tol, maxIter):
    x1 = fn(x0)
    for i in range(0, maxIter):
        if Abs(x0 - x1) < tol:
            return x1
        x1 = fn(float(x1))
    return float(x1)
    
if __name__ == '__main__':
    x = symbols('x')
    print(fixedPointIteration(f, 0, 1.0e-5, 100))
    print(fixedPointIteration(g, 5.9, 1.0e-5, 100))