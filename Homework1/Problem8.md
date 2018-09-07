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
10\ln(x) -10\ln(-3x + 100)  = t + c \\
\ln(x) - \ln(-3x + 100) = \frac{t}{10} + c\\
\ln(\frac{x}{-3x + 100}) = \frac{t}{10} + c \\
\frac{x}{-3x+100} = e^{\frac{t}{10} + c} \\
x = e^{\frac{t}{10} + c}(-3x + 100) \\
x = -3xe^{\frac{t}{10} + c} + 100e^{\frac{t}{10} + c} \\
x + 3xe^{\frac{t}{10} + c} = 100e^{\frac{t}{10} + c} \\
x(1 + 3e^{\frac{t}{10} + c}) = 100e^{\frac{t}{10} + c} \\
x = \frac{100e^{\frac{t}{10} + c}}{1 + 3e^{\frac{t}{10} + c}} \\
x(0) = 4 \\
4 = \frac{100e^{\frac{0}{10} + c}}{1 + 3e^{\frac{0}{10} + c}} \\
4 = \frac{100e^c}{1+3e^c} \\
4(1+3e^c) = 100e^c \\
4 + 12e^c = 100e^c \\
4 = 88e^c \\
\frac{1}{22} = e^c \\
c = \ln(\frac{1}{22}) = -\ln(22) \\
c \approx -3.09 \\
x = \frac{100e^{\frac{t}{10} - \ln(22)}}{1 + 3e^{\frac{t}{10} - \ln(22)}} \\
x = \left[ \frac{(100e^{\frac{t}{10}})\frac{1}{22}}{1+ 3e^{\frac{t}{10}}\frac{1}{22}} \right] \times \frac{22}{22} \\
x = \frac{100e^{\frac{t}{10}}}{22 + 3e^{\frac{t}{10}}} 
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
10\ln(x) -10\ln(-3x + 100)  = t + c \\
\ln(x) - \ln(-3x + 100) = \frac{t}{10} + c\\
\ln(\frac{x}{-3x + 100}) = \frac{t}{10} + c \\
\frac{x}{-3x+100} = e^{\frac{t}{10} + c} \\
x = e^{\frac{t}{10} + c}(-3x + 100) \\
x = -3xe^{\frac{t}{10} + c} + 100e^{\frac{t}{10} + c} \\
x + 3xe^{\frac{t}{10} + c} = 100e^{\frac{t}{10} + c} \\
x(1 + 3e^{\frac{t}{10} + c}) = 100e^{\frac{t}{10} + c} \\
x = \frac{100e^{\frac{t}{10} + c}}{1 + 3e^{\frac{t}{10} + c}} \\
x(0) = 400 \\
400 = \frac{100e^{\frac{0}{10} + c}}{1 + 3e^{\frac{0}{10} + c}} \\
400 = \frac{100e^c}{1+3e^c} \\
400(1+3e^c) = 100e^c \\
400 + 1200e^c = 100e^c \\
400 = -1100e^c \\
-e^c = \frac{400}{1100} \\
c = -\ln(\frac{4}{11})  \\
x = \frac{100e^{\frac{t}{10} -\ln(\frac{4}{11})}}{1 + 3e^{\frac{t}{10} -\ln(\frac{4}{11})}} \\
x = \left[ \frac{100e^{\frac{t}{10}}\frac{11}{4}}{1 + 3e^{\frac{t}{10}}\frac{11}{4}} \right] \times \frac{4}{4} \\
x = \frac{1100e^{\frac{t}{10}}}{4 + 33e^{\frac{t}{10}}}
$
</p>
