#include <iostream>
#include <cmath>

using namespace std;

template<class T>
void test() {
  T ep = 1.0f;
  size_t countMantisa = 0;
  while (1.0f + ep / 2 != 1.0f) {
    ep /= 2;
    countMantisa++;
  }
  cout << "Size of mantise: " << countMantisa << "\n";
  cout << "Epsilon: " << ep << "\n";

  T a = 1.f;
  size_t countMax = 0;
  while (a < (1.0f / 0.0f)) {
    a *= 2;
    countMax++;
  }
  cout << "Max exponent: " << countMax - 1 << "\n";
  
  T b = 1.f;
  size_t countMin = 0;
  while (isnormal(b)) {
    b /= 2;
    countMin++;
  }
  cout << "Min exponent: " <<  countMin + 1 << "\n";
    
  cout << "1 < 1 + e/2 = " << (1.0f < 1.0f + ep / 2) << "\n";
  cout << "1 < 1 + e = " << (1.0f < 1.0f + ep) << "\n";
  cout << "1 + e/2 < 1 + e = " << (1.0f + ep / 2 < 1.0f + ep) << "\n";
  cout << "1 + e < 1 + e + e/2 =  " << (1.0f + ep < 1.0f + ep + ep / 2) << "\n";
}

int main() {
  cout << "------ Test for float -----\n";
  test<float>();
  cout << "----- Test for double -----\n";
  test<double>();
}
