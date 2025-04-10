import math
from .figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус не может быть <= 0.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
