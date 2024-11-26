#!/usr/bin/python3
""" A test file for base.py"""


import unittest
from models.base import Base
class TestBase(unittest.TestBase):
    def test_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_custom_id(self):
        b3 = Base(42)
        self.assertEqual(b3.id, 42)

    if __name__ == "__main__":
        unittest.main()
