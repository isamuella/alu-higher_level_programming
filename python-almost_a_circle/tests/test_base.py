#!/usr/bin/python3
""" A test file for base.py"""


import unittest
from models.base import Base
class TestBase(unittest.TestCase):
    def test_base_no_id(self):
        b1 = Base()
        b2 = Base()
        self.assertIsNotNone(b1.id)
        self.assertNotEqual(b1.id, b2.id)

    def test_base_has_id(self):
        b = Base(55)
        self.assertEqual(b.id, 55)

    def test_base_more_instances(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_id_types(self):
        b1 = Base(1)
        b2 = Base("String")
        b3 = Base(0.5)
        self.assertequal(b1.id, 1)
        self.assertEqual(b2.id, "String")
        self.assertequal(b3.id, 0.5)

if __name__ == "__main__":
    unittest.main()
