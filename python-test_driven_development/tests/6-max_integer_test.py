#!/usr/bin/python3


import unittest
max_integer = __import__('6-max_integer').max_integer

class TextMaxInteger(unittest.TestCase):
    def test_integer(self):
        # Test if the list is empty
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1,5,3,9]), 9)
        self.assertAlmostEqual(max_integer([10,5,2,8]), 10)
        self.assertAlmostEqual(max_integer([5,8,3]), 8)
        self.assertAlmostEqual(max_integer([4,-8,19,2]), 19)
        self.assertAlmostEqual(max_integer([-101,-45,-78,-96,-10,-175]), -10)
        self.assertAlmostEqual(max_integer([6]), 6)
