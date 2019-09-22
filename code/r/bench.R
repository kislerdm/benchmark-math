sigmoid <- function(arg) {
  1 / (1 + exp(arg))
}

tanh <- function(arg) {
  arg1 <- exp(arg)
  arg2 <- exp(-arg)

  return ( (arg1 - arg2)/(arg1 + arg2) )
}

set.seed(2019)
length <- 1000000
random_max <- 100

input <- sample(0:random_max, length, replace = TRUE)

# multiplication
t0 <- Sys.time()
output <- input * 2.
cat(paste0("Multiplication by 2: ", (Sys.time() - t0)*1e3, "ms\n"))

# sum
t0 <- Sys.time()
output <- input + input[c(2:length, 1)]
cat(paste0("Sum: ", (Sys.time() - t0)*1e3, "ms\n"))

# power
t0 <- Sys.time()
output <- input^2
cat(paste0("Power of 2: ", (Sys.time() - t0)*1e3, "ms\n"))

# sigmoid
t0 <- Sys.time()
output <- sigmoid(input)
cat(paste0("Sigmoid: ", (Sys.time() - t0)*1e3, "ms\n"))

# tanh
t0 <- Sys.time()
output <- tanh(input)
cat(paste0("Tanh: ", (Sys.time() - t0)*1e3, "ms\n"))
