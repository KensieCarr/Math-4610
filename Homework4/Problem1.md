# Homework 4

## Problem 1

**Routine Name:**  
Gaussian Elimination on Square Matrix

**Author:** Kensie Carr

**Language:** Python

**Description/Purpose:** 
This routine will  take a square matrix and preform Gaussian elimination on said matrix and return the matrix in
reduced row echelon form.

**Input:**
square matrix

**Output:** 
reduced row echelon form matrix

**Usage/Example:**
<p>
  $ \left[ \begin{matrix} 
  1 &-3 & 1 \\
  2 & -8 & 8 \\
  -6 & 3 & -15
  \end{matrix} \right] \\
  \left[ \begin{matrix}
  1 & -3 & 1 \\
  0 & -2 & 6 \\
  0 & -15 & -9
  \end{matrix} \right] \\
  \left[ \begin{matrix}
  1 & -3 & 1 \\
  0 & -1 & 3 \\
  0 & -5 & -3
  \end{matrix} \right] \\
  \left[ \begin{matrix}
  1 & -3 & 1 \\
  0 & -1 & 2 \\
  0 & 0 & -18
  \end{matrix} \right] \\
  \left[ \begin{matrix}
  1 & -3 & 1 \\
  0 & -1 & 2 \\
  0 & 0 & 1
  \end{matrix} \right] \\
  \left[ \begin{matrix}
  1 & -3 & 1 \\
  0 & 1 & 0 \\
  0 & 0 & 1
  \end{matrix} \right] \\
  \left[ \begin{matrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1
  \end{matrix} 
 </p>

**Implementation/Code:** 
```python 
def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


if __name__ == "__main__":
    from fractions import Fraction
    n = input()

    A = [[0 for j in range(n+1)] for i in range(n)]

    # Read input data
    for i in range(0, n):
        line = map(Fraction, raw_input().split(" "))
        for j, el in enumerate(line):
            A[i][j] = el
    raw_input()

    line = raw_input().split(" ")
    lastLine = map(Fraction, line)
    for i in range(0, n):
        A[i][n] = lastLine[i]

    # Print input
    pprint(A)

    # Calculate solution
    x = gauss(A)

    # Print result
    line = "Result:\t"
    for i in range(0, n):
        line += str(x[i]) + "\t"
    print(line)
```
**Last Modified:** November/2018

