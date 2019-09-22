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
  cout << "Multiplication by 2: "
       << duration<double, milli>(high_resolution_clock::now() - t0).count() << "ms" << endl;

  // sum
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    if (i == length - 1 ) {
      output[i] = float(input[i] + input[0]);
    } else {
      output[i] = float(input[i] + input[i+1]);
    }
  }
  cout << "Sum: "
       << duration<double, std::milli>(high_resolution_clock::now() - t0).count() << "ms" << endl;

  // power
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    output[i] = pow(float(input[i]), 2);
  }
  cout << "Power of 2: "
       << duration<double, std::milli>(high_resolution_clock::now() - t0).count() << "ms" << endl;

  // sigmoid
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    output[i] = sigmoid(input[i]);
  }
  cout << "Sigmoid: "
       << duration<double, std::milli>(high_resolution_clock::now() - t0).count() << "ms" << endl;    

  // tanh
  t0 = high_resolution_clock::now();
  for (int32_t i = 0; i < length; i++) {
    output[i] = tanh(input[i]);
  }
  cout << "Tanh: "
       << duration<double, std::milli>(high_resolution_clock::now() - t0).count() << "ms" << endl;    

  return 0;
}