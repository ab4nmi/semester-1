# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Circle(Shape):
    """circle class"""
    def __init__(self, radius, position, colour="red"):
        super().__init__(position, colour)
        self.set_radius(radius)

    def set_radius(self, radius):
        """sets the radius"""
        # check if its a num
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        # cant be 0 or negative
        if radius <= 0:
            raise ValueError("radius must be bigger than 0")
        self.radius = radius

    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        # pi r squared
        return math.pi * self.radius * self.radius

    def perimeter(self):
        # 2 pi r
        return 2 * math.pi * self.radius