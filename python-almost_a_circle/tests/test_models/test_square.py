#!/usr/bin/python3
"""Unittests for models.square.Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for the Square class"""

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_str(self):
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_update_args(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})


if __name__ == "__main__":
    unittest.main()
