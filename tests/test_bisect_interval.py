"""Tests for the bisect_interval function from root_finder.py."""

from unittest import TestCase
from fftestpackage.root_finder import bisect_interval


class TestBisectInterval(TestCase):

    def test_bisect_interval(self) -> None:
        """Test correct output of bisect_interval function."""

        def test_func(x):

            return x**3

        self.assertRaises(ValueError, bisect_interval, test_func, 3, 2)
        self.assertRaises(ValueError, bisect_interval, test_func, 2, 3)

        result = bisect_interval(test_func, -2, 4)

        self.assertAlmostEqual(result, 0)

        def test_func_2(x):

            return x + 10

        result_2 = bisect_interval(test_func_2, -15, -2)

        self.assertAlmostEqual(result_2, -10)
