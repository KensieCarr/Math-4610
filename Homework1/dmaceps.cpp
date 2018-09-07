#include <iostream>
using namespace std;

void doubleMachineEpsilon(double EPS);

int main() {
  doubleMachineEpsilon(0.5);
  return 0;
}

void doubleMachineEpsilon(double EPS) {
  double prev_epsilon;
  while ((1 + EPS) != 1) {
    prev_epsilon = EPS;
    EPS /= 2;
  }
  cout << "Double Precision Machine Epsilon is: " << prev_epsilon << endl;
}
