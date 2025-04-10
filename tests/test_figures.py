import unittest
from figures.circle import Circle
from figures.triangle import Triangle

class TestFigures(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.00, places=2)

    def test_triangle_invalid(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_triangle_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

    def test_triangle_not_right_angle(self):
        triangle = Triangle(3, 5, 7)
        self.assertFalse(triangle.is_right_angle())

