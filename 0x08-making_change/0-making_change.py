#!/usr/bin/python3
"""
Making Change
"""
import sys


def makeChange(coins, total):
    """
    Given a total and a pile of coins of different values,
    determine the fewest number of coins needed to meet the
    given amount total.
    """
    if total <= 0:
        return 0

    table = [0] + [sys.maxsize] * total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                sub_res = table[i - coin]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1

    return -1 if table[total] == sys.maxsize else table[total]
