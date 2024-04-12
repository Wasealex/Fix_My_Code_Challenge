#!/usr/bin/python3
"""class module"""


class Square:
    """class square"""
    width = 0

    def __init__(self, *args, **kwargs):
        """init"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """perimiter"""
        return (self.width * 4)

    def __str__(self):
        """str"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """comment me"""
    s = Square(width=12, height=10)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
