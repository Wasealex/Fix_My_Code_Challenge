#!/usr/bin/python3
"""module that contains one class square"""


class Square:
    def __init__(self, width=0):
        """initializing square"""
        self._width = width

    @property
    def width(self):
        """property"""
        return self._width

    @width.setter
    def width(self, value):
        """accurate value"""
        if value >= 0:
            self._width = value
        else:
            raise ValueError("Width cannot be negative.")

    def calculate_area(self):
        """area of square"""
        return self._width ** 2

    def calculate_perimeter(self):
        """perimeter"""
        return self._width * 4

    def __str__(self):
        """string represtnation"""
        return f"{self._width}/{self._width}"


if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print(s.calculate_area())
    print(s.calculate_perimeter())
