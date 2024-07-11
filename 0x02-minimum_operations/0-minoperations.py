#!/usr/bin/python3

"""
Module to calculate minimum operations needed to achieve a certain
number of 'H' using Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to achieve n characters using
    "Copy All" and "Paste" operations.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations needed to achieve n characters.
             If n is impossible to achieve, return 0.
    """
    if n < 2:
        return n

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        j = 1
        while j * j <= i:
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
            j += 1

    return dp[n] if dp[n] != float('inf') else 0
