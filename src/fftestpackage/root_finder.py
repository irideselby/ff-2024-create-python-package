"""This module contains an algorithm for finding roots of 1D-functions."""


def _sign(number):

    return -1 if number < 0 else 1


def bisect_interval(func, lower_bound, upper_bound):

    if not lower_bound < upper_bound:

        raise ValueError('Lower bound is not smaller than upper bound.')

    f_min = func(lower_bound)
    f_max = func(upper_bound)

    if _sign(f_min) == _sign(f_max):

        raise ValueError('Function has same signs on interval boundaries.')

    interval_centre = (lower_bound + upper_bound) / 2
    f_centre = func(interval_centre)

    if abs(f_centre) < 1e-24:

        return interval_centre

    if not _sign(f_min) == _sign(f_centre):

        return bisect_interval(func, lower_bound, interval_centre)

    return bisect_interval(func, interval_centre, upper_bound)

