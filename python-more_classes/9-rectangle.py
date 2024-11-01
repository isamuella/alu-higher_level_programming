#!/usr/bin/python3

"""Create an empty class Rectangle"""


class Rectangle:
    """Already created Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """created a getter method for the __width attribute"""
        return self.__width

    @property
    def height(self):
        """created a getter method for the __height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets a private attribute for the Rectangle width.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets a private attribute for the Rectangle height.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print the rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        sign = str(self.print_symbol)
        return "\n".join(sign * self.__width for i in range(self.__height))

    def __repr__(self):
        """A string representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """A delete message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Displays the biggest area.

        Raises:
             TypeError: if rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

        @classmethod
        def square(cls, size=0):
            """New instance that has width == height == size"""
            return cls(size, size)
