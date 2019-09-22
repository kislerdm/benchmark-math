# Math pperations benchmark

```yaml
languages:
- cpp
- golang
- python:
  - vanila
  - numpy
- R
```

## Benchmark procedure

Run a cycle/program 100 repetitions and measure time of every math operation

### Cycle

1. Generate an array of <em>1M</em> elements, each element <em>is a random int between 0 and 100</em>
2. Multiply generated array elementwise by 2
3. 
4. Square generated array
5. Calculate <em>sigmoid</em> function elementwise
6. Calculate <em>tanh</em> function elementwise