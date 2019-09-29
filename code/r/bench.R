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
t <- (Sys.time() - t0) * 1e3
cat(paste0("Multiplication by 2: ", t, "ms\n"))

# sum
t0 <- Sys.time()
output <- input + input[c(2:length, 1)]
t <- (Sys.time() - t0) * 1e3
cat(paste0("Sum: ", t, "ms\n"))

# power
t0 <- Sys.time()
output <- input^2
t <- (Sys.time() - t0) * 1e3
cat(paste0("Power of 2: ", t, "ms\n"))

# sigmoid
t0 <- Sys.time()
output <- sigmoid(input)
t <- (Sys.time() - t0) * 1e3
cat(paste0("Sigmoid: ", t, "ms\n"))

# tanh
t0 <- Sys.time()
output <- tanh(input)
t <- (Sys.time() - t0) * 1e3
cat(paste0("Tanh: ", t, "ms\n"))
