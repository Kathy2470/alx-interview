#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of a prime game.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing the upper limit for each round.

    Returns:
    str: The name of the player who won the most rounds, or None if the winner cannot be determined.
    """

    def is_prime(n):
        """
        Check if a number is prime.

        Parameters:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Create a set of numbers from 1 to n
        numbers = set(range(1, n + 1))
        maria_turn = True

        while numbers:
            # Find the smallest prime number in the set
            prime = next((num for num in numbers if is_prime(num)), None)
            if prime is None:
                # If no prime numbers are left, the current player loses
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Remove the prime number and its multiples from the set
            numbers -= set(range(prime, n + 1, prime))
            maria_turn = not maria_turn

    # Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
