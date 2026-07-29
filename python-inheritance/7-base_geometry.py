#!/usr/bin/python3
"""Defines the BaseGeometry class"""


class BaseGeometry:
    """Represent a base geometry object"""

    def area(self):
        """Raise an Exception since area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer

        Args:
            name (str): The name of the attribute being validated
            value: The value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
