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
	a1 := math.Exp(arg)
	a2 := math.Exp(-arg)
	return (a1 - a2) / (a1 + a2)
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
	t := time.Since(t0)
	fmt.Println("Multiplication by 2:", t)

	// sum
	t0 = time.Now()
	for i := 0; i < length; i++ {
		if i == length-1 {
			output[i] = float64(input[i] + input[0])
		} else {
			output[i] = float64(input[i] + input[i+1])
		}
	}
	t = time.Since(t0)
	fmt.Println("Sum:", t)

	// power
	t0 = time.Now()
	for i := 0; i < length; i++ {
		output[i] = math.Pow(float64(input[i]), 2.)
	}
	t = time.Since(t0)
	fmt.Println("Power of 2:", t)

	// sigmoid
	t0 = time.Now()
	for i := 0; i < length; i++ {
		output[i] = sigmoid(float64(input[i]))
	}
	t = time.Since(t0)
	fmt.Println("Sigmoid:", t)

	// sigmoid
	t0 = time.Now()
	for i := 0; i < length; i++ {
		output[i] = tanh(float64(input[i]))
	}
	t = time.Since(t0)
	fmt.Println("Tanh:", t)
}
