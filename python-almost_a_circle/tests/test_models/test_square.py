#!/usr/bin/python3
"""Unittests for models.square.Square"""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for the Square class"""

    def tearDown(self):
        """Remove Square.json if it was created during a test"""
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_1(self):
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 0, 0))

    def test_square_1_2(self):
        s = Square(1, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 0))

    def test_square_1_2_3(self):
        s = Square(1, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 3))

    def test_square_1_2_3_4(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id),
                          (1, 1, 2, 3, 4))

    def test_size_not_int(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_not_int(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

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

    def test_update_kwargs_size_id(self):
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_update_kwargs_id_size_x(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_id_size_x_y(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_create_id_only(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_id_size_x_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file_no_file(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        Square.save_to_file([Square(1), Square(2, 1, 1)])
        result = Square.load_from_file()
        self.assertEqual(len(result), 2)
        for s in result:
            self.assertIsInstance(s, Square)


if __name__ == "__main__":
    unittest.main()
