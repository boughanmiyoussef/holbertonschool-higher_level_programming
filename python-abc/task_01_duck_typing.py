from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            self.radius = 0  # Set radius to 0 for negative values
        else:
            self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":
    try:
        circle_negative_radius = Circle(radius=-5)
    except ValueError as e:
        print("Uncorrect output - Circle negative radius:", e)

    try:
        rectangle_negative_dimensions = Rectangle(width=-4, height=-7)
    except ValueError as e:
        print("Uncorrect output - Rectangle negative dimensions:", e)
