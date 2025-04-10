import unittest
from unittest.mock import patch
import tkinter as tk
from gui.app import App
from figures.circle import Circle
from figures.triangle import Triangle

class TestApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = App(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.messagebox.showinfo')
    def test_calculate_circle_area_positive(self, mock_showinfo):
        self.app.entry_radius.insert(0, '5')
        self.app.calculate_circle_area()
        mock_showinfo.assert_called_with("Площадь круга", "Площадь круга: 78.54")

    @patch('tkinter.messagebox.showerror')
    def test_calculate_circle_area_negative(self, mock_showerror):
        self.app.entry_radius.insert(0, '-5')
        self.app.calculate_circle_area()
        mock_showerror.assert_called_with("Ошибка", "Радиус не может быть отрицательным.")

    @patch('tkinter.messagebox.showerror')
    def test_calculate_circle_area_invalid_input(self, mock_showerror):
        self.app.entry_radius.insert(0, 'abc')
        self.app.calculate_circle_area()
        mock_showerror.assert_called_with("Ошибка", "Некорректный ввод радиуса.")

    @patch('tkinter.messagebox.showinfo')
    def test_calculate_triangle_area_positive(self, mock_showinfo):
        self.app.entry_a.insert(0, '3')
        self.app.entry_b.insert(0, '4')
        self.app.entry_c.insert(0, '5')
        self.app.calculate_triangle_area()
        mock_showinfo.assert_called_with(
            "Площадь треугольника",
            "Площадь треугольника: 6.00\nЭто прямоугольный треугольник."
        )

    @patch('tkinter.messagebox.showerror')
    def test_calculate_triangle_area_invalid(self, mock_showerror):
        self.app.entry_a.insert(0, '1')
        self.app.entry_b.insert(0, '2')
        self.app.entry_c.insert(0, '3')
        self.app.calculate_triangle_area()
        mock_showerror.assert_called_with("Ошибка", "Некорректный ввод сторон треугольника.")

if __name__ == '__main__':
    unittest.main()
