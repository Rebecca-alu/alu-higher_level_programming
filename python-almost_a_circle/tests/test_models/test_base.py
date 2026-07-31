#!/usr/bin/python3
"""Unittests for models.base.Base"""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for the Base class"""

    def test_id_public(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_none_uses_counter(self):
        b = Base(None)
        self.assertIsInstance(b.id, int)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        result = Base.to_json_string([{"a": 1}])
        self.assertEqual(json.loads(result), [{"a": 1}])

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        result = Base.from_json_string('[{"a": 1}]')
        self.assertEqual(result, [{"a": 1}])


if __name__ == "__main__":
    unittest.main()
