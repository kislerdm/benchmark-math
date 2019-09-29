# Math pperations benchmark

## Tested languages

```yaml
- cpp:
  - g++: 8.3.0-r0
- golang: 1.11
- python: 3.7.4
  - numpy: 1.17.2
- R: 3.6.1
```

## Benchmark procedure

Run a cycle/program 100 repetitions and measure elapsed time of every math operation

### Cycle

1. Generate an array of <em>1M</em> elements, each element <em>is a random int between 0 and 100</em>
2. Multiply generated array elementwise by 2
3. Add to the <em>i-th</em> element of array it's <em>(i+1)-th</em> value, last element of array to be summed up with the 0-th element
4. Get generated array elementwise to the power of 2
5. Calculate <em>sigmoid</em> function elementwise
6. Calculate <em>tanh</em> function elementwise

# Result (WIP)

# Contribution

Feel free to add more benchmark tests and open a pull request