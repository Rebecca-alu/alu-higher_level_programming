#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an Exception since area() is not implemented here."""
        raise Exception("area() is not implemented")
