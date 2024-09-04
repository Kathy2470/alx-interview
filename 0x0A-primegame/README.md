# Prime Game

## Description

The Prime Game is a two-player game where players take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including `n`. The chosen prime number and all its multiples are removed from the set. The player who cannot make a move loses the game. Maria always goes first, and both players play optimally.

The task is to determine who wins the most rounds when given multiple values of `n` for several rounds of the game.

## Task

Implement the `isWinner` function that determines who wins the most rounds given the number of rounds and the list of values for `n`.

### Function Prototype

```python
def isWinner(x: int, nums: List[int]) -> str:
