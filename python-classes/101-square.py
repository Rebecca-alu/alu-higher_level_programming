#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size (int): The size of the new square
            position (tuple): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): The new size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): The new position
        """
        if (type(value) is not tuple or len(value) != 2 or
                not all(type(n) is int for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Print the square instance, same behavior as my_print()"""
        result = ""
        if self.__size == 0:
            return ""
        for i in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                result += "\n"
        return result
