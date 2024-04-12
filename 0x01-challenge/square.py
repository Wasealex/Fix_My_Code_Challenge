#!/usr/bin/python3
"""documented for square
"""


class Square:
    """class square involving height
    """
    def __init__(self, width=0):
        """initializing"""
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_mysquare(self):
        """perimeter"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """str represtent"""
        return "{}".format(self.width)


if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_mysquare())
