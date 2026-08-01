#!/usr/bin/python3
"""Unittests for Base.save_to_file_csv and Base.load_from_file_csv"""
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square


class TestBaseCsvRectangle(unittest.TestCase):
    """Unittests for CSV serialization with Rectangle"""

    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

    def test_save_to_file_csv_none(self):
        Rectangle.save_to_file_csv(None)
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_save_to_file_csv_empty(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv") as f:
            self.assertEqual(f.read(), "")

    def test_load_from_file_csv_no_file(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_save_and_load_round_trip(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        result = Rectangle.load_from_file_csv()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))

    def test_csv_field_order(self):
        r1 = Rectangle(10, 7, 2, 8, 99)
        Rectangle.save_to_file_csv([r1])
        with open("Rectangle.csv") as f:
            row = f.read().strip()
        self.assertEqual(row, "99,10,7,2,8")


class TestBaseCsvSquare(unittest.TestCase):
    """Unittests for CSV serialization with Square"""

    def tearDown(self):
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_save_to_file_csv_none(self):
        Square.save_to_file_csv(None)
        self.assertTrue(os.path.exists("Square.csv"))

    def test_save_to_file_csv_empty(self):
        Square.save_to_file_csv([])
        with open("Square.csv") as f:
            self.assertEqual(f.read(), "")

    def test_load_from_file_csv_no_file(self):
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        self.assertEqual(Square.load_from_file_csv(), [])

    def test_save_and_load_round_trip(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        result = Square.load_from_file_csv()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(s1))
        self.assertEqual(str(result[1]), str(s2))

    def test_csv_field_order(self):
        s1 = Square(7, 9, 1, 99)
        Square.save_to_file_csv([s1])
        with open("Square.csv") as f:
            row = f.read().strip()
        self.assertEqual(row, "99,7,9,1")


if __name__ == "__main__":
    unittest.main()
