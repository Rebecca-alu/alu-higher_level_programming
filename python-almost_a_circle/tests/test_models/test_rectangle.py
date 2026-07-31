#!/usr/bin/python3
"""Unittests for models.rectangle.Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for the Rectangle class"""

    def test_width_height(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_x_y_set(self):
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_width_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {}, 0)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4, id=99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/3 - 4/2")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 5, "width": 10,
                              "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_type(self):
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertIsInstance(r.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
