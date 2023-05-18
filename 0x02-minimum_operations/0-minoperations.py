#!/usr/bin/python3
"""
Minumum operation Model
"""


def minOperations(n):
    """
Given a number n, calculate the fewest number of operations
needed to result in exactly n H characters in a text file.
Returns an integer.
If n is impossible to achieve, return 0.
"""
    if type(n) is not int or n < 2:
        return 0
    result = 0
    iteration = 2
    while n > 1:
        if n % iteration == 0:
            result += iteration
            n /= iteration
        else:
            iteration += 1
    return result
