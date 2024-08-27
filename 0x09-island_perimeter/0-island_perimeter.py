#!/usr/bin/python3
"""
This module contains the function `island_perimeter`
to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by 1s in a grid.

    Args:
        grid (list of list of int): The grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check each side of the cell
                if i == 0 or grid[i-1][j] == 0:  # Top
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1

    return perimeter
