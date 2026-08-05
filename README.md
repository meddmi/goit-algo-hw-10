# Change-Making Algorithms

This project implements two algorithms for calculating change using the following coin denominations:

```text
[50, 25, 10, 5, 2, 1]
```

The implementation is located in [`task01.py`](task01.py).

## Implemented functions

### `find_coins_greedy(amount)`

Uses a greedy strategy: it checks the denominations from largest to smallest and takes as many coins as possible at each step.

### `find_min_coins(amount)`

Uses dynamic programming. For every amount from `1` to the requested amount, it stores the smallest number of coins needed. The selected coins are then reconstructed from the stored results.

Both functions return a dictionary in the following format:

```python
{coin_denomination: number_of_coins}
```

For an amount of `0`, both functions return an empty dictionary: `{}`. The command-line interface accepts only non-negative integer amounts and asks for the input again when an invalid value is entered.

## Running the program

Run the script from the project directory:

```bash
python3 task01.py
```

The program asks for an amount and prints the result and average execution time for both algorithms. Each execution time is calculated as the average of 10 runs.

Example:

```text
Enter the amount of change (a non-negative integer): 4536133 
Greedy: {50: 90722, 25: 1, 5: 1, 2: 1, 1: 1}
Greedy average time: 1.3165990822017193e-06
Dynamic programming: {50: 90722, 25: 1, 5: 1, 2: 1, 1: 1}
Dynamic average time: 1.2499681500019506
```

## Complexity comparison

Let `n` be the requested amount and `k` be the number of coin denominations. In this implementation, `k = 6`.

| Algorithm   | Time complexity            | Space complexity | Main characteristic     |
|-------------|----------------------------|------------------|-------------------------|
| Greedy      | `O(k)`; `O(1)` for a fixed | `O(k)`           | Very fast and uses only |
|             |  set of denominations.     |                  | the result dictionary.  |
|-------------|----------------------------|------------------|-------------------------|
| Dynamic     | `O(n × k)`; `O(n)` for a   | `O(n)`           | Guarantees the minimum  |
| programming | fixed set of denominations |                  | number of coins.        |
|-------------|----------------------------|------------------|-------------------------|

### Performance for large amounts

The greedy algorithm processes the six denominations once, so its execution time is almost independent of the size of the amount. It is therefore especially efficient for large amounts and requires very little additional memory.

The dynamic programming algorithm calculates the best solution for every intermediate amount from `1` through `n`. As `n` increases, both its execution time and memory usage increase linearly. It can become significantly slower and use considerably more memory than the greedy approach for very large amounts.

For the current denominations `[50, 25, 10, 5, 2, 1]`, the coin system is canonical. Therefore, the greedy algorithm always produces an optimal solution, and it is the best choice for this particular cash-register system.
Dynamic programming is more general: it remains useful when the set of denominations changes and the greedy strategy may fail.

## Conclusion

For the fixed coin set used in this assignment, the greedy algorithm is preferable because it is faster, uses less memory, and still guarantees the minimum number of coins. Dynamic programming is the safer general-purpose solution when coin denominations are arbitrary or when optimality cannot be guaranteed by a greedy strategy.
