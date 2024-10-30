"""Tests for the multiply_numbers function from common.py."""

from fftestpackage.common import divide_numbers


def test_divide_numbers():
    """Test correct output of divide_numbers function."""

    assert divide_numbers(2, 4) == 0.5

