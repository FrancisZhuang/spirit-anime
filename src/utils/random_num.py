"""This function can generate n digits number"""

from random import randint


def random_number(n_digits):
    """Generate random n digits number"""
    range_start = 10 ** (n_digits - 1)
    range_end = (10 ** n_digits) - 1
    return randint(range_start, range_end)
