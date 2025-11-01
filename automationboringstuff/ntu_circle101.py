"""
Creation of circle class 
"""
import math


class Circle:
    def __init__(self, radius,color):  # initialzing the circle class with radius
        self.radius = radius
        self.color = color

    def calculate_area(self):  # calculating area
        return math.pi * self.radius ** 2

    def __repr__(self):  # string rep of class
        return f"Circle object with radius is :{self.radius} and of color {self.color}"


if __name__ == "__main__":
    c1 = Circle(23,'red')
    # printing area of circle with 2 decimal point
    print(
        f'Area of circle  of {c1.radius} radius is :{c1.calculate_area():.2f}, and of color {c1.color}')
