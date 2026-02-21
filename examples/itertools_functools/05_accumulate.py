"""itertools.accumulate for running totals and cumulative operations."""

import itertools
import operator


def running_total(numbers):
    """Compute the running total of a list of numbers."""
    return list(itertools.accumulate(numbers))


def running_product(numbers):
    """Compute the running product of a list of numbers."""
    return list(itertools.accumulate(numbers, operator.mul))


def running_max(numbers):
    """Track the running maximum."""
    return list(itertools.accumulate(numbers, max))


def cumulative_balance(transactions):
    """Calculate cumulative balance from transactions."""
    return list(itertools.accumulate(transactions, lambda bal, tx: bal + tx))


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Running total:", running_total(nums))
    print("Running product:", running_product(nums))

    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("\nRunning max:", running_max(data))

    transactions = [1000, -200, 50, -75, 300]
    print(f"\nTransactions: {transactions}")
    print(f"Balance:      {cumulative_balance(transactions)}")

    # With initial value (Python 3.8+)
    result = list(itertools.accumulate([1, 2, 3], initial=100))
    print(f"\nWith initial=100: {result}")
