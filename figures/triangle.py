
import math
from .figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        # Проверка на существование треугольника
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise ValueError("С указанными сторонами треугольник не может существовать.")

    def area(self):
        # Полупериметр
        s = (self.a + self.b + self.c) / 2
        # Геронова формула
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        # Проверка на прямоугольность
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
