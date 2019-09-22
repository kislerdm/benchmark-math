package main

import (
	"fmt"
	"math"
	rnd "math/rand"
	"time"
)

func sigmoid(arg float64) float64 {
	return 1. / (1. + math.Exp(-arg))
}

func tanh(arg float64) float64 {
	return (math.Exp(arg) - math.Exp(-arg)) / (math.Exp(arg) + math.Exp(-arg))
}

func main() {
	rnd.Seed(2019)
	length := 1000000
	random_max := 100
	var input = make([]int, length)
	var output = make([]float64, length)

	for i := 0; i < length; i++ {
		input[i] = rnd.Intn(random_max)
	}

	// multiplication
	t0 := time.Now()
	for i := 0; i < length; i++ {
		output[i] = float64(input[i] * 2.)
	}
	fmt.Println("Multiplication by 2:", time.Since(t0))

	// sum
	t0 = time.Now()
	for i := 0; i < length; i++ {
		if i == length-1 {
			output[i] = float64(input[i] + input[0])
		} else {
			output[i] = float64(input[i] + input[i+1])
		}
	}
	fmt.Println("Sum:", time.Since(t0))

	// power
	t0 = time.Now()
	for i := 0; i < length; i++ {
		output[i] = math.Pow(float64(input[i]), 2.)
	}
	fmt.Println("Power of 2:", time.Since(t0))

	// sigmoid
	t0 = time.Now()
	for i := 0; i < length; i++ {
		output[i] = sigmoid(float64(input[i]))
	}
	fmt.Println("Sigmoid:", time.Since(t0))

	// sigmoid
	t0 = time.Now()
	for i := 0; i < length; i++ {
		output[i] = tanh(float64(input[i]))
	}
	fmt.Println("Tanh:", time.Since(t0))

}
