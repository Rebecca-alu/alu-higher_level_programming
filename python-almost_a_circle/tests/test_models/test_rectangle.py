#!/usr/bin/python3
"""Unittests for models.rectangle.Rectangle"""
import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for the Rectangle class"""

    def tearDown(self):
        """Remove Rectangle.json if it was created during a test"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

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

    def test_rectangle_1_2_3_4_5(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                          (1, 2, 3, 4, 5))

    def test_width_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_y_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {}, 0)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        r.display()

    def test_display_without_y(self):
        r = Rectangle(2, 2, 1)
        r.display()

    def test_display(self):
        r = Rectangle(2, 2, 1, 1)
        r.display()

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

    def test_create_id_only(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_create_id_width_height_x(self):
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                          (89, 1, 2, 3, 4))

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file_no_file(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        for r in result:
            self.assertIsInstance(r, Rectangle)


if __name__ == "__main__":
    unittest.main()
