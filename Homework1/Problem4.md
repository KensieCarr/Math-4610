# Homework 1

## Problem 4

**Routine Name:**           Open MP Hello World

**Author:** Kensie Carr

**Language:** C++

**Description/Purpose:** 
Using OpenMP to learn more about how many processes you can run on cores included in your computer.

**Input:** 

```c++ 
#include <iostream>
#include <omp.h>
#include <stdlib.h>

using namespace std;

int main() {
	int a;
	int id, numThreads;
#pragma omp parallel private(numThreads, id)
	id = omp_get_thread_num();
	cout << "Hello World from thread " << id << endl;
	if (id == 0) {
		numThreads = omp_get_num_threads();
		cout << "There are " << numThreads << " threads!" << endl;
	}
	cin >> a;
	return 0;
}
```

**Output:** 
Hello World from thread 0

There are 1 threads!

**Last Modified:** September/2018
