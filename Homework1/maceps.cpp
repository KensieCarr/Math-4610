#include <iostream>
#include <cfloat>
using namespace std;

void machineEpsilon(float EPS);
void doubleMachineEpsilon(double EPS);

int main() {
  machineEpsilon(0.5);
  doubleMachineEpsilon(0.5);
  return 0;
}

void machineEpsilon(float EPS) {
  float prev_epsilon;
  while ((1 + EPS) != 1) {
    prev_epsilon = EPS;
    EPS /= 2;
  }
  cout << "Machine Epsilon is: " << prev_epsilon << endl;
}

void doubleMachineEpsilon(double EPS) {
  double prev_epsilon;
  while ((1 + EPS) != 1) {
    prev_epsilon = EPS;
    EPS /= 2;
  }
  cout << "Double Precision Machine Epsilon is: " << prev_epsilon << endl;
}
