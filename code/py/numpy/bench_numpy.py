import numpy as np
import time


def sigmoid(arg: int) -> float:
    return np.divide(1., 1. + np.exp(-arg))


def tanh(arg: int) -> float:
    arg1 = np.exp(arg)
    arg2 = np.exp(-arg)
    return np.divide(arg1 - arg2, arg1 + arg2)


if __name__ == "__main__":

    np.random.seed(2019)
    length = 1000000
    random_max = 100

    input = np.random.randint(0, random_max, length)

    # multiplication
    t0 = time.time()
    output = np.multiply(input, 2)
    print(f"Multiplication by 2: {(time.time() - t0)*1e3}ms")

    # sum
    t0 = time.time()
    output = input[:-1] + input[1:]
    output = np.append(output, input[-1] + input[0])
    print(f"Sum: {(time.time() - t0)*1e3}ms")

    # power
    t0 = time.time()
    output = np.power(input, 2)
    print(f"Power of 2: {(time.time() - t0)*1e3}ms")
    
    # sigmoid
    t0 = time.time()
    output = sigmoid(input)
    print(f"Sigmoid: {(time.time() - t0)*1e3}ms")

    # tanh
    t0 = time.time()
    output = tanh(input)
    print(f"Tanh: {(time.time() - t0)*1e3}ms")
