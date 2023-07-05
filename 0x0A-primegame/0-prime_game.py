#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """ Check if n is a prime number """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def add_prime(n, primes):
    """ Add primes up to n to the list """
    last_prime = primes[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """ Determine the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the upper limit for each round.

    Returns:
        str: The name of the player who won the most rounds (either "Maria" or "Ben").
             If the winner cannot be determined, returns None.
    """
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]  # Initialize with pre-calculated primes up to 2.
    add_prime(max(nums), primes)

    for round_num in range(x):
        _sum = sum((i != 0 and i <= nums[round_num]) for i in primes[:nums[round_num] + 1])
        if _sum % 2:
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
