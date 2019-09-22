import random
from math import exp
import time


def sigmoid(arg: int) -> float:
    return 1. / (1. + exp(-arg))


def tanh(arg: int) -> float:
    arg1 = exp(arg)
    arg2 = exp(-arg)
    return (arg1 - arg2) / (arg1 + arg2)


if __name__ == "__main__":

    random.seed(2019)
    length = 1000000
    random_max = 100

    input = [random.randint(0, random_max) for _ in range(length)]

    # multiplication
    t0 = time.time()
    output = [i * 2. for i in input]
    t = (time.time() - t0) * 1e3
    print(f"Multiplication by 2: {t}ms")

    # sum
    t0 = time.time()
    output = input[:-1] + input[1:]
    output.append(input[-1] + input[0])
    t = (time.time() - t0) * 1e3
    print(f"Sum: {t}ms")

    # power
    t0 = time.time()
    output = [pow(i, 2) for i in input]
    t = (time.time() - t0) * 1e3
    print(f"Power of 2: {t}ms")

    # sigmoid
    t0 = time.time()
    output = [sigmoid(i) for i in input]
    t = (time.time() - t0) * 1e3
    print(f"Sigmoid: {t}ms")

    # tanh
    t0 = time.time()
    output = [tanh(i) for i in input]
    t = (time.time() - t0) * 1e3
    print(f"Tanh: {t}ms")
