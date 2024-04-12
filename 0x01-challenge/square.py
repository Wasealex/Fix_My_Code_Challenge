#!/usr/bin/python3
"""documented for square
"""


class Square:
    """class square involving height
    """
    def __init__(self, width=0, height=0):
        """initializing"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """perimeter"""
        self.height = self.width
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """str represtent"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
