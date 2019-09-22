#include <iostream>
#include <chrono>
#include <cmath>

using namespace std;
using namespace chrono;

float sigmoid(int arg) {
    return 1/(1 + exp(-arg));
}

float tanh(int arg) {
    return (exp(arg) - exp(-arg))/(exp(arg) + exp(-arg));
}

int main() {
  srand(2019);
  int length = 1000000;
  int random_max = 100;
  int input[length];
  float output[length];

  for (int32_t i = 0; i < length; i++) {
    input[i] = rand() % ( random_max + 1 );
  }

  // multiplication
  auto t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    output[i] = input[i] * 2.0;
  }
  double t = duration<double, std::milli>(high_resolution_clock::now() - t0).count();
  cout << "Multiplication by 2: " << t << "ms" << endl;

  // sum
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    if (i == length - 1 ) {
      output[i] = float(input[i] + input[0]);
    } else {
      output[i] = float(input[i] + input[i+1]);
    }
  }
  t = duration<double, std::milli>(high_resolution_clock::now() - t0).count();
  cout << "Sum: " << t << "ms" << endl;

  // power
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    output[i] = pow(float(input[i]), 2);
  }
  t = duration<double, std::milli>(high_resolution_clock::now() - t0).count();
  cout << "Power of 2: " << t << "ms" << endl;

  // sigmoid
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    output[i] = sigmoid(input[i]);
  }
  t = duration<double, std::milli>(high_resolution_clock::now() - t0).count();
  cout << "Sigmoid: " << t << "ms" << endl;    

  // tanh
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    output[i] = tanh(input[i]);
  }
  t = duration<double, std::milli>(high_resolution_clock::now() - t0).count();
  cout << "Tanh: " << t << "ms" << endl;    

  return 0;
}