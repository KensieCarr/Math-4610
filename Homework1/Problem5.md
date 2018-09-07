# Homework 1

## Problem 5

<p>
Expand the following functions about the given center $x_0$ and find the radius of convergence of each of the series.
  <br>
a. $f(x) = \sin(2x)$ and $x_0 = 0 \\
f'(x) = 2\cos(2x),\ f''(x) = -4\sin(2x),\ f'''(x) = -8\cos(2x),\ f^{4} = 16\sin(2x) \\
f(0) = 0,\ f'(0) = 2,\ f''(0) = 0,\ f'''(x) = -8,\ f^4 = 0 \\
f(x) = \sum^\infty_{n=0} \dfrac{f^n(0)}{n!}x^n\\
\sin(2x) = \dfrac{2}{1!}x - \dfrac{8}{3!}x^3 + ... \\
\sin(2x) = \sum^\infty_{n=0}\dfrac{(-1)^n(2x)^{2n+1}}{(2n+1)!} 
$ 
  <br>
b. $f(x) = \ln(2x)$ and $x_0 = 1 \\
f'(x) = \frac{1}{x},\ f''(x) = - x^{-2},\ f'''(x) = 2x^{-3},\ f^4 = -6x^{-4} \\
f(1) = 0,\ f'(1) = 1,\ f''(1) = -1,\ f'''(1) = 2,\ f^4(1) = -6 \\
f(x) = \sum^\infty_{n=0} \dfrac{f^n(0)}{n!}x^n \\
\ln(2x) = \dfrac{1}{1!}x - \dfrac{1}{2!}x^2 + \dfrac{2}{3!}x^3 - \dfrac{6}{4!}x^4 + ...\\
\ln(2x) = \sum^\infty_{n=0}\dfrac{(-1)^{n+1}(x-1)^n}{n!} 
$ 
  <br>
c. $f(x) = e^{2x}$ and $x_0 = 1 \\
f'(x) = 2e^{2x},\ f''(x) = 4e^{2x},\ f'''(x) = 8e^{2x},\ f^4(x) = 16e^{2x} 
$ 
  <br>
d. $f(x) = 3x^2 - 2x + 5$ and $x_0 = 0 \\
f'(x) = 6x - 2,\ f''(x) = 6,\ f'''(x) = 0 \\
f(0) = 5,\ f'(0) = -2,\ f''(0) = 6,\ f'''(0) = 0 \\
f(x) = \sum^\infty_{n=0} \dfrac{f^n(0)}{n!}x^n \\
f(x) = \dfrac{5}{0!} - \dfrac{2}{1!}x + \dfrac{6}{2!}x^2 \\
f(x) = 5 - 2x + 3x^2 
$ 
  <br>
e. $f(x) = 3x^2 - 2x + 5$ and $x_0 = 1 \\
f'(x) = 6x - 2,\ f''(x) = 6,\ f'''(x) = 0 \\
f(1) = 6,\ f'(1) = 4,\ f''(1) = 6,\ f'''(x) = 0 \\
f(x) = \sum^\infty_{n=0} \dfrac{f^n(0)}{n!}x^n \\
f(x) = \dfrac{6}{0!} + \dfrac{4}{1!}x + \dfrac{6}{2!}x^2 \\
f(x) = 6 + 4x + 3x^2 
$ 
  <br>
f. $f(x) = (3x^2 - 2x + 5)^{-1}$ and $x_0 = 1 \\
f'(x) = -\dfrac{6x-2}{(3x^2 - 2x + 5)^2},\ f''(x) = \dfrac{2\left(6x-2\right)^2}{\left(3x^2-2x+5\right)^3}-\dfrac{6}{\left(3x^2-2x+5\right)^2} = \dfrac{2\left(27x^2-18x-11\right)}{\left(3x^2-2x+5\right)^3} \\
f'''(x) = \dfrac{2\left(54x-18\right)}{\left(3x^2-2x+5\right)^3}-\dfrac{6\left(6x-2\right)\left(27x^2-18x-11\right)}{\left(3x^2-2x+5\right)^4} = -\dfrac{24\left(3x-1\right)\left(9x^2-6x-13\right)}{\left(3x^2-2x+5\right)^4} 
$
  <br>
g. $f(x) = \cosh(x-3)$ and $x_0 = 1 \\
f'(x) = \sinh(x-3),\ f''(x) = cosh(x-3),\ f'''(x) = \sinh(x-3) 
$ 
  <br>
h. $f(x)$ and $x_0 = a \\
f(x) = f(a) + \dfrac{f'(a)}{1!}(x-1)' + \dfrac{f''(a)}{2!}(x-a)^2 + ...  $
<br>
i. $f(a)$ and $x_0 = x \\
f(x) = f(x) + \dfrac{f'(x)}{1!}(x-x)' +... \\
f(x) = f(x) $
  <br>
j. $f(a + h)$ and $x_0 = a \\
f(a) + \dfrac{f'(a)}{1!}(a + h - a) + ... \\
= f(a) + \dfrac{f'(a)}{1!}(h) + \frac{f''(a)}{2!}(h)^2 + ...$
</p>
