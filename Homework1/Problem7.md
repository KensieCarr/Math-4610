# Homework 1

## Problem 7
**Routine Name:**           Find Roots of A Quadratic Polynomial

**Author:** Kensie Carr

**Language:** C++

**Description/Purpose:** 
This routine will take a quadratic polynomial $ax^2 + bx + c = 0 $ and find the existing solutions.

**Input:** 
The inputs are the coefficients of the polynomial $a,b,c$ .

**Output:** 
The outputs are the solutions to the quadratic polynomial, otherwise known as the roots. The solutions will be output as an array.

**Usage/Example:**
Say for example you had the quadratic polynomial 
<p>
  $$6x^2 - 7x - 3 = 0 $$  
</p>
you can use the quadratic formula to find the roots
<p>
 $ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \\
   x = \frac{-(-7) \pm \sqrt{(-7)^2 - 4(6)(-3)}[2(6)} \\
   x = \frac{7 \pm \sqrt{49 + 72}}{12} \\
   x = \frac{7 \pm \sqrt{121}}{12} \\
   x = \frac{7 \pm 11}{12} \\
   x = \frac{7 + 11}{12},\ \ \ \ \ x = \frac{7 - 11}{12} \\
   x = \frac{18}{12},\ \ \ \ \ x = \frac{-4}{12} \\
   x = \frac{3}{2},\ \ \ \ \ x = \frac{-1}{3}$
</p>
therefore the roots of the polynomial are
<p>
  $$ \frac{3}{2} \text{ and } \frac{-1}{3} $$
</p>
 
**Implementation/Code:** 
```c
#include <iostream>
#include <array>
#include <math.h>
using namespace std;

void quadForm(int a, int b, int c);
float* imaginaryRoots(int a, int b, int c);
float* realRoots(int a, int b, int c);
void printReal(float*);
void printImaginary(float*);

int main() {
	int t;
	int a;
	int b;
	int c;

	cout << "a = " << endl;
	cin >> a;
	if (a == 0) {
		cout << "This is not a quadratic polynomial." << endl;
		return 0;
	}
	cout << "b = " << endl;
	cin >> b;
	cout << "c = " << endl;
	cin >> c;
	quadForm(a, b, c);
	cin >> t;
}

void quadForm(int a, int b, int c) {
	float *roots;
	if (sqrt(b) - (4 * a * c) >= 0) {
		roots = realRoots(a, b, c);
		printImaginary(roots);
	}
	else {
		roots = realRoots(a, b, c);
		printReal(roots);
	}
	
}

float* imaginaryRoots(int a, int b, int c) {
	float roots[2];
	cout << "You have entered the imaginaryRoots function " << endl;
	roots[0] = (-b + sqrt(-(b ^ 2 - (4 * a*c)))) / (2 * a);
	roots[1] = (-b - sqrt(-(b ^ 2 - (4 * a*c)))) / (2 * a);
		return roots;
}

float* realRoots(int a, int b, int c) {
	float roots[2];
	cout << "You have entered the realRoots function " << endl;
	roots[0] = (-b + sqrt(b^2 - (4*a*c))) / (2 * a);
	roots[1] = (-b - sqrt(b^2 - (4*a*c))) / (2 * a);
	return roots;
}

void printReal(float* roots) {
	cout << "The roots are ";
	for (int i = 0; i < 2; i++) {
		cout << roots[i] << " ";
	}
}

void printImaginary(float* roots) {
	cout << "The roots are ";
	for (int i = 0; i < 2; i++) {
		cout << roots[i] << "i ";
	}
}
```
**Last Modified:** September/2018
