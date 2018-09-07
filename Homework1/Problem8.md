# Homework 1

## Problem 8

Compute the solutions for the following simple initial value problems:
<p>
a. $ \frac{dx}{dt} = 3x $ and $x(0) = 1.0 \\
 dx = 3x dt \\
 \frac{1}{x}dx = 3dt \\
 \int \frac{1}{x}dx = \int 3dt \\
 \ln(x) = 3t + c\\
 x = e^{3t + c} \\
 x(0) = 1.0 \\
 1 = e^{3(0) + c} \\
 1 = e^c \\
 c = 0 \\
 x = e^{3t}
 $
 <br>
 b. $\frac{dx}{dt} = 3tx$ and $x(0) = 1.0 \\
 dx = 3tx dt \\
 \frac{1}{x}dx = 3t dt \\
 \int \frac{1}{x}dx = \int 3t dt \\
 \ln(x) = \frac{3}{2}t^2 + c \\
 x = e^{\frac{3}{2}t^2 + c} \\
 x(0) = 1 \\
 1 = e^{\frac{3}{2}(0)^2 + c} \\
 c = 0 \\
 x = e^{\frac{3}{2}t^2}
 $
 <br>
 c. $\frac{dx}{dt} = 0.1x - 0.003x^2$ and $x(0) = 4 \\
 dx = 0.1x - 0.003x^2 dt \\
 \frac{1}{0.1x - 0.003x^2}dx = dt \\
 \frac{1}{x(0.1 - 0.003x)} = \frac{A}{x} + \frac{B}{0.1 - 0.003x} \\
 1 = A(0.1 - 0.003x) + B(x) \\
1 = 0.1A - 0.003xA + Bx \\
1 = 0.1A + x(-0.003A + B) \\
1 = 0.1A \\
A = 10 \\
0 = -0.003A + B \\
0 = -0.003(10) + B \\
0 = -0.03 + B \\
B = 0.03 \\
\frac{10}{x} + \frac{0.03}{0.1 - 0.003x} dx = dt \\
\int \frac{10}{x} + \frac{0.03}{0.1 - 0.003x} dx = \int dt \\
10\ln(x) -10\ln(3x - 100)  = t + c \\
\ln(x) - \ln(3x - 100) = \frac{t}{10} + c\\
x - 3x + 100 = e^{\frac{t}{10} + c} \\
-2x = e^{\frac{t}{10} + c} - 100 \\
x = -\frac{1}{2}e^{\frac{t}{10} + c} + 50 \\
x(0) = 4 \\
4 = -\frac{1}{2}e^{\frac{0}{10} + c} + 50 \\
-46 = -\frac{1}{2}e^c \\
92 = e^c \\
\ln(92) = c \\
c \approx 4.5 \\
x = -\frac{1}{2}e^{\frac{t}{10} + 4.5} + 50 
 $ 
 <br>
 d. $\frac{dx}{dt} = 0.1x - 0.003x^2$ and $x(0) = 400 \\
   dx = 0.1x - 0.003x^2 dt \\
 \frac{1}{0.1x - 0.003x^2}dx = dt \\
 \frac{1}{x(0.1 - 0.003x)} = \frac{A}{x} + \frac{B}{0.1 - 0.003x} \\
 1 = A(0.1 - 0.003x) + B(x) \\
1 = 0.1A - 0.003xA + Bx \\
1 = 0.1A + x(-0.003A + B) \\
1 = 0.1A \\
A = 10 \\
0 = -0.003A + B \\
0 = -0.003(10) + B \\
0 = -0.03 + B \\
B = 0.03 \\
\frac{10}{x} + \frac{0.03}{0.1 - 0.003x} dx = dt \\
\int \frac{10}{x} + \frac{0.03}{0.1 - 0.003x} dx = \int dt \\
10\ln(x) -10\ln(3x - 100)  = t + c \\
\ln(x) - \ln(3x - 100) = \frac{t}{10} + c\\
x - 3x + 100 = e^{\frac{t}{10} + c} \\
-2x = e^{\frac{t}{10} + c} - 100 \\
x = -\frac{1}{2}e^{\frac{t}{10} + c} + 50 \\
x(0) = 400 \\
400 = -\frac{1}{2}e^{\frac{0}{10} + c} + 50 \\
350 = -\frac{1}{2}e^{c} \\
700 = e^c \\
c = \ln(700) \\
c \approx 6.6 \\
x = -\frac{1}{2}e^{\frac{t}{10} + 6.6} + 50 $
  </p>
