#!/usr/bin/env python3
"""
This module demonstrates Abstract Base Classes and Duck Typing in Python.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract Base Class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete implementation of a Circle.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete implementation of a Rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    
    This function does not check if 'shape' inherits from Shape.
    It simply assumes the object provides area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
