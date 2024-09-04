#!/usr/bin/python3
"""Prime Game Algorithm Python"""


def sieve_of_eratosthenes(max_num):
    """
    Generate a list of primes up to max_num using Sieve of Eratosthenes.
    """
    is_prime = [True] * (max_num + 1)
    p = 2

    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    primes = [p for p in range(2, max_num + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """
    Determine who the winner is based on the number of rounds played.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        """
        Simulate a single game for value n and return the winner.
        """
        if n < 2:
            return "Ben"

        remaining = [True] * (n + 1)
        turn = 0  # Maria starts, so Maria = 0, Ben = 1

        for prime in primes:
            if prime > n:
                break
            if remaining[prime]:
                for multiple in range(prime, n + 1, prime):
                    remaining[multiple] = False
                turn = 1 - turn  # Toggle player

        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
