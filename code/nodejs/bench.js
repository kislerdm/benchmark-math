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
  return (Math.exp(arg) - Math.exp(-arg)) / (Math.exp(arg) + Math.exp(-arg))
}


for (var i = 0; i < length; i++) {
  input.push(randomIntInc(0, random_max))
}

// multiplication
var t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  output[i] = input[i] * 2.
}
console.log("Multiplication by 2: %dms", process.hrtime(t0)[1] / 1000000)

// sum
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  if (i == length - 1) {
    output[i] = input[i] + input[0]
  } else {
    output[i] = input[i] + input[i+1]
  }
}
console.log("Sum: %dms", process.hrtime(t0)[1] / 1000000)

// power
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
    output[i] = Math.pow(input[i], 2)
}
console.log("Power of 2: %dms", process.hrtime(t0)[1] / 1000000)

// sigmoid
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  output[i] = sigmoid(input[i])
}
console.log("Sigmoid: %dms", process.hrtime(t0)[1] / 1000000)

// tanh
t0 = new process.hrtime();
for (var i = 0; i < length; i++) {
  output[i] = tanh(input[i])
}
console.log("Tanh: %dms", process.hrtime(t0)[1] / 1000000)