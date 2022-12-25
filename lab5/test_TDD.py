import pytest
from main import *


def test_0_if_zero_root():
    assert len(get_roots(1, -1, 1)) == 0


def test_1_if_one_root():
    assert len(get_roots(1, 0, 0)) == 1


def test_2_if_two_roots():
    assert len(get_roots(1, -2, -8)) == 2


def test_3_if_three_roots():
    assert len(get_roots(10, -5, 0)) == 3


def test_4_if_four_roots():
    assert len(get_roots(4, -5, 1)) == 4
