#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_attributes(self):
        """Test that attributes are set correctly."""
        r = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_rectangle_basic(self):
        """Test Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_rectangle_with_x(self):
        """Test Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_rectangle_with_xy(self):
        """Test Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_rectangle_with_id(self):
        """Test Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_too_many_args(self):
        """Test Rectangle with too many positional arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_type_error(self):
        """Test width raises TypeError on non-int."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_type_error(self):
        """Test height raises TypeError on non-int."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_type_error(self):
        """Test x raises TypeError on non-int."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_type_error(self):
        """Test y raises TypeError on non-int."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_value_error(self):
        """Test width raises ValueError when not > 0."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_width_zero(self):
        """Test width raises ValueError when 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_value_error(self):
        """Test height raises ValueError when not > 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_height_zero(self):
        """Test height raises ValueError when 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_negative(self):
        """Test x raises ValueError when negative."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_value_error(self):
        """Test y raises ValueError when < 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        """Test the __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_no_y(self):
        """Test display() with x and y at defaults."""
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            r.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """Test display() without y set."""
        r = Rectangle(2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            r.display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

    def test_display_full(self):
        """Test display() with x and y both set."""
        r = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            r.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """Test to_dictionary output."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_args_id(self):
        """Test update(89)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_width(self):
        """Test update(89, 1)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_args_height(self):
        """Test update(89, 1, 2)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_args_x(self):
        """Test update(89, 1, 2, 3)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_args_full(self):
        """Test update(89, 1, 2, 3, 4)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kwargs_id(self):
        """Test update(id=89)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual(r.id, 89)

    def test_update_kwargs_width(self):
        """Test update(id=89, width=1)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_height(self):
        """Test update(id=89, width=1, height=2)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_x(self):
        """Test update(id=89, width=1, height=2, x=3)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_full(self):
        """Test update(id=89, width=1, height=2, x=3, y=4)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create_kwargs_id(self):
        """Test Rectangle.create(id=89)."""
        r = Rectangle.create(id=89)
        self.assertEqual(r.id, 89)

    def test_create_kwargs_width(self):
        """Test Rectangle.create(id=89, width=1)."""
        r = Rectangle.create(id=89, width=1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_kwargs_height(self):
        """Test Rectangle.create(id=89, width=1, height=2)."""
        r = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_create_kwargs_x(self):
        """Test Rectangle.create(id=89, width=1, height=2, x=3)."""
        r = Rectangle.create(id=89, width=1, height=2, x=3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_create_kwargs_full(self):
        """Test Rectangle.create(id=89, width=1, height=2, x=3, y=4)."""
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file_none(self):
        """Test save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        """Test save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):
        """Test save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"width": 1', content)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file() when the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test load_from_file() when the file exists."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        self.assertEqual(str(rects[0]), str(r1))
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
