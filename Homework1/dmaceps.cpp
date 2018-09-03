#include <iostream>
using namespace std;

void machineEpsilon(double EPS);

int main() {
  machineEpsilon(0.5);
  return 0;
}

void machineEpsilon(double EPS) {
  double prev_epsilon;
  while ((1 + EPS) != 1) {
    prev_epsilon = EPS;
    EPS /= 2;
  }
  cout << "Machine Epsilon is: " << prev_epsilon << endl;
}
