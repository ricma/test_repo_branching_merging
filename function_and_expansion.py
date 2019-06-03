"""
Provide functions and their Taylor expansions around x₀ = 0
"""
import math


def f1(x):
    """
    The sine function

    Parameters
    ----------
    x : double
        Argument to evaluate sin at.

    Returns
    -------
    y : double
        Value of sin(x)
    """
    return math.sin(x)


def Taylor_f1(x, order=2):
    """
    Return Taylor polynomial of order `order` of `f1`.

    Parameters
    ----------
    x : double
        Value at which we want to evaluate th Taylor series
    order : integer, optional
        Order up to which we want to evaluate the series

    Returns
    -------
    y : double
        Value of the Taylor series at `x`.
    """
    if order == 0:
        return 0
    elif order == 1:
        return x
    elif order == 2:
        return x
    elif order == 3:
        return x - x ** 3 / (3 * 2 * 1)
    else:
        raise NotImplementedError(
            "Can't create Taylor series of order={0}".format(
                order))
