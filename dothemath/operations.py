# encoding: utf-8


def int_sum(a, b):
    """
    Sums up two integers
    :param a: integer
    :param b: integer
    :return: sum of a and b
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise
    return a + b


def matrix_sum(v1, v2):
    """
    Sums up items in two vectors
    :param v1: vector of integers
    :param v2: vector of integers
    :return: vector of sums
    """
    if not all(isinstance(x, int) for x in v1) or not all(isinstance(x, int) for x in v2):
        raise
    return [sum(x) for x in zip(v1, v2)]
