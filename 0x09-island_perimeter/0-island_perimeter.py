#!/usr/bin/python3
"""
island_perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of a grid island.
    """
    perimeter = 0
    for row in grid:
        for i, j in zip([0] + row, row + [0]):
            perimeter += int(i != j)
    for column in zip(*grid):
        for i, j in zip([0] + column, column + [0]):
            perimeter += int(i != j)
    return perimeter
