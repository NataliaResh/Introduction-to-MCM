#include <iostream>
#include <cmath>
#include <complex>

using namespace std;

template <typename T> int sgn(T val) {
    return (T(0) < val) - (val < T(0));
}

const double e = 1e-10;

double f(double x) {
  return tan(x) - x;
}

double tan_(double x) {
  return 1 / (cos(x) * cos(x));
}

double f_(double x) {
  return tan_(x) - 1;
}

double f__(double x) {
  return 2 * sin(x) / pow(cos(x), 3);
}

void bisectionMethod() {
  cout << "Метод бисекции:\n";
  double a, b;
  cout << "a: ";
  cin >> a;
  cout << "b: ";
  cin >> b;
  double fa = f(a), fb = f(b);
  if (sgn(fa) == sgn(fb) || a > b) {
    cout << "Некорректный отрезок\n";
    return;
  }
  while(abs(b - a) > e) {
    double c = (a + b) / 2;
    double fc = f(c);
    if (sgn(fa) != sgn(fc)) {
      fb = fc;
      b = c;
    } else {
      fa = fc;
      a = c;
    }
  }
  cout << "Промежуток: [" << a << ", " << b << "]" << "\n";
  cout << "Корень: " << (a + b) / 2 << "\n";
}

void fixedPointIteration() {
  cout << "Метод простых итераций:\n";
  double x;
  cout << "x: ";
  cin >> x;
  double a = 1e-2;
  cout << a;
  if (a >= 1) {
    cout << "Некотрректная начальная точка!\n";
    return;
  }
  double f1 = tan(x);
  double x1 = x - a * f1;
  while (abs(x1 - x) > e) {
    //cout << x << " " << f1 << "\n";
    x = x1;
    f1 = f(x);
    x1 = x - a * f1;
    
  }
  cout << "Корень: " << x << "\n";
}

void newtonsMethod() {
  cout << "Метод Ньютона (метод секущих)\n";
  cout << "x: ";
  double x;
  cin >> x;
  //if (abs(f(x) * f__(x)) >= f_(x) * f_(x)) {
   // cout << "Некорректная начальная точка!\n";
    //return;
  //}
  double x1 = x - f(x) / f_(x);
  while (abs(x1 - x) > e) {
    x = x1;
    x1 = x - f(x) / f_(x);
  }
  cout << "Корень: " << x1 << "\n";
}

void secantMethod() {
  cout << "Метод секущих\n";
  cout << "x1: ";
  double x1;
  cin >> x1;
  cout << "x2: ";
  double x2;
  cin >> x2;
  if (abs(f(x1) * f__(x1)) >= f_(x1) * f_(x1)) {
    cout << "Некорректная начальная точка!\n";
    return;
  }
  double f1 = f(x1), f2 = f(x2);
  double x3 = x2 - f2 * (x2 - x1) / (f2 - f1);
  cout << x3 << "\n";
  double f3 = f(x3);
  while (abs(x3 - x2) > e) {
    x1 = x2;
    x2 = x3;
    f1 = f2;
    f2 = f3;
    x3 = x2 - f2 * (x2 - x1) / (f2 - f1);
    f3 = f(x3);
  }
  cout << "Корень: " << x3 << "\n";
}

complex<double> fc(complex<double> z) {
  return z * z * z - (complex<double>)1;
}

complex<double> fc_(complex<double> z) {
  return (complex<double>)3 * z * z;
}

complex<double> fc__(complex<double> z) {
  return (complex<double>)6 * z;
}

void newtonsMethod1() {
  cout << "Метод Ньютона для нахождения корней полинома z**3 - 1\n";
  cout << "x: ";
  complex<double> xs[] = {0.5, complex<double>(-1, 1), complex<double>(-1, -1)};
  //if (abs(fc(x) * fc__(x)) >= abs(fc_(x) * fc_(x))) {
    //cout << "Некорректная начальная точка!\n";
    //return;
  //}
  for (auto x: xs) {
  complex<double> x1 = x - fc(x) / fc_(x);
  cout << x1;
  while (abs(x1 - x) > e) {
    x = x1;
    x1 = x - fc(x) / fc_(x);
  }
  cout << "Корень: " << x1 << "\n";
  }
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(5);
  //bisectionMethod();
  //fixedPointIteration();
  //newtonsMethod();
  secantMethod();
  newtonsMethod1();
}
