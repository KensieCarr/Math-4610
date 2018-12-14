import numpy as np
from sympy import *

def absError(solution, computedSolution):
    return Abs(solution - computedSolution)

def relError(solution, computedSolution):
    return Abs((computedSolution - solution)/solution)

def derivative(fn, h):
    return (fn(x+h) - fn(x))/h

def f(x):
    return sin(x)

def g(x):
    return x - ((x**3)/6) + ((x**5)/120) - ((x**7)/5040) + ((x**9)/362880)

def solveWithH(fn, expectedSolution, value, histKey):
    h1 = 1
    makeHistory(fn, h1, expectedSolution, value, histKey)
    h1 = h1/2
    makeHistory(fn, h1, expectedSolution, value, histKey)
    
    while Ne(history[histKey][-1]['relError'] - history[histKey][-2]['relError'], 0) or Ne(history[histKey][-1]['absError'] - history[histKey][-2]['absError'], 0):
        h1 = h1/2
        makeHistory(fn, h1, expectedSolution, value, histKey)


def makeHistory(fn, h, expectedSolution, value, histKey):
    if histKey not in history:
        history[histKey] = []
    history[histKey].append(dict())
    approx = derivative(fn, h).subs(x,value)
    history[histKey][-1]['h'] = h
    history[histKey][-1]['approx'] = approx
    history[histKey][-1]['relError'] = relError(expectedSolution, approx)
    history[histKey][-1]['absError'] = absError(expectedSolution, approx)
    

def printHistory(funcHistory, nameOfFunc, expectedSolution):
    print("Function: ", nameOfFunc)
    print("======================")
    print("h                  | exactSolution      | approx             | relError           | absError             ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for item in funcHistory:
        print("{:<18} | {:<18} | {:<18} | {:<18e} | {:<18e}".format(N(item['h'], 10), expectedSolution, N(item['approx'], 10), float(N(item['relError'], 10)), float(N(item['absError'], 10))))


if __name__ == '__main__':
    x, h = symbols('x h')
    history = {}

    solveWithH(f, 1, 0, 'f')
    solveWithH(g, 1, 0, 'g')
    # print(history)
    printHistory(history['f'], "f(x) = sin(x)", 1)
    printHistory(history['g'], "g(x) = x - x^3/3! + x^5/5! - x^7/7! + x^9/9!", 1)
    import os
    os.system("pause")

