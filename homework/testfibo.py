import unittest
from fibo import *
import time

value_for_timer = 1000000


class TestFibonachi(unittest.TestCase):
    def test_zero_if_number_is_zero(self):
        self.assertEqual(list(fibonachi(0)), [])

    def test_one_if_number_is_more_then_zero(self):
        self.assertEqual(list(fibonachi(1)), [0])

    def test_two_if_number_is_high(self):
        self.assertEqual(list(fibonachi(5)), [0, 1, 1, 2, 3])

    def test_time(self):
        start = time.time()
        a = fibonachi(value_for_timer)
        end = time.time()
        self.assertLess(end - start, 1)