var length = 1000000,
  random_max = 100,
  input = [],
  output = [];


function randomIntInc(low, high) {
  return Math.floor(Math.random() * (high - low + 1) + low)
}

function sigmoid(arg) {
  return 1. / (1. + Math.exp(-arg))
}

function tanh(arg) {
  let a1 = Math.exp(arg)
  let a2 = Math.exp(-arg)
  return (a1 - a2) / (a1 + a2)
}


for (var i = 0; i < length; i++) {
  input.push(randomIntInc(0, random_max))
}

// multiplication
var t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  output[i] = input[i] * 2.
}
var t = process.hrtime(t0)[1] / 1000000
console.log("Multiplication by 2: %dms", t)

// sum
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  if (i == length - 1) {
    output[i] = input[i] + input[0]
  } else {
    output[i] = input[i] + input[i+1]
  }
}
t = process.hrtime(t0)[1] / 1000000
console.log("Sum: %dms", t)

// power
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
    output[i] = Math.pow(input[i], 2)
}
t = process.hrtime(t0)[1] / 1000000
console.log("Power of 2: %dms", t)

// sigmoid
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  output[i] = sigmoid(input[i])
}
t = process.hrtime(t0)[1] / 1000000
console.log("Sigmoid: %dms", t)

// tanh
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  output[i] = tanh(input[i])
}
t = process.hrtime(t0)[1] / 1000000
console.log("Tanh: %dms", t)
