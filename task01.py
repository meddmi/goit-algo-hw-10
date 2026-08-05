"""Algorithms for finding an optimal set of coins for a given amount."""

from __future__ import annotations

from numbers import Integral
from timeit import timeit

COINS: tuple[int, ...] = (50, 25, 10, 5, 2, 1)
REPEAT_COUNT = 10


def find_coins_greedy(amount: int) -> dict[int, int]:
    """Return the coin counts produced by the greedy algorithm.

    Denominations are considered from largest to smallest.  The supplied
    denominations form a canonical coin system, so this result also uses the
    minimum possible number of coins.
    """
    if amount == 0:
        return {}

    remaining = amount
    result: dict[int, int] = {}

    for coin in COINS:
        count, remaining = divmod(remaining, coin)
        if count:
            result[coin] = count

    return result


def find_min_coins(amount: int) -> dict[int, int]:
    """Return a minimum-coin representation using dynamic programming.

    ``min_coins[current]`` stores the smallest number of coins needed for
    ``current``.  ``last_coin[current]`` stores the coin used to reconstruct
    the corresponding solution.
    """

    if amount == 0:
        return {}

    min_coins_required = [amount + 1] * (amount + 1)
    coin_used = [0] * (amount + 1)
    min_coins_required[0] = 0

    for current in range(1, amount + 1):
        for coin in COINS:
            if coin > current:
                continue

            candidate = min_coins_required[current - coin] + 1
            if candidate < min_coins_required[current]:
                min_coins_required[current] = candidate
                coin_used[current] = coin

    result: dict[int, int] = {}
    remaining = amount
    while remaining:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin

    return dict(sorted(result.items(), reverse=True))


def benchmark_algorithm(search_function, amount: int) -> float:
    """Measure the average execution time for one search function."""
    total_time = timeit(lambda: search_function(amount), number=REPEAT_COUNT)
    return total_time / REPEAT_COUNT


def main() -> None:
    """Read an amount from the console and print both solutions."""

    while True:
        value = input("Enter the amount of change (a non-negative integer): ")
        try:
            amount = int(value)

            if isinstance(amount, bool) or not isinstance(amount, Integral):
                raise ValueError("Amount must be a non-negative integer")
            if amount < 0:
                raise ValueError("Amount must be a non-negative integer")

            print(f"Greedy: {find_coins_greedy(amount)}")
            print(f"Greedy average time: {benchmark_algorithm(find_coins_greedy, amount)}")
            print(f"Dynamic programming: {find_min_coins(amount)}")
            print(f"Dynamic average time: {benchmark_algorithm(find_min_coins, amount)}")
            break
        except ValueError:
            print("incorrect amount. Please, input a non-negative integer.")


if __name__ == "__main__":
    main()
