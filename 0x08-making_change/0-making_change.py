#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Parameters:
    coins (list): A list of the values of the coins available.
    total (int): The total amount to be achieved.

    Returns:
    int: The fewest number of coins needed to meet the total,
         or -1 if the total cannot be met with the available coins.
    """
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount up to the total
    # We use float('inf') to represent an initially unreachable amount
    dp = [float('inf')] * (total + 1)

    # Base case: No coins are needed to make a total of 0
    dp[0] = 0

    # Loop through each coin in the coins list
    for coin in coins:
        # Update the dp array for all amounts from the value of the coin up to the total
        for i in range(coin, total + 1):
            # The minimum coins needed to make the amount i is either the current value
            # or 1 more than the number of coins needed to make the amount (i - coin)
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be met with the available coins
    return dp[total] if dp[total] != float('inf') else -1
