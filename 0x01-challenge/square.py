#!/usr/bin/python3
"""module that contains one class square"""


class Square:
    """class square """

    def __init__(self, width=0):
        """initializing square paramteres"""
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """perimeter of the square"""
        return (self.width * 4)

    def __str__(self):
        """string representation"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
