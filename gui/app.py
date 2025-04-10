import tkinter as tk
from tkinter import messagebox
from figures.circle import Circle
from figures.triangle import Triangle

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Геометрический калькулятор")

        # Раздел для круга
        self.label_circle = tk.Label(root, text="Радиус круга")
        self.label_circle.pack()

        self.entry_radius = tk.Entry(root)
        self.entry_radius.pack()

        self.button_circle = tk.Button(root, text="Вычислить площадь круга", command=self.calculate_circle_area)
        self.button_circle.pack()

        # Раздел для треугольника
        self.label_triangle = tk.Label(root, text="Стороны треугольника (a, b, c)")
        self.label_triangle.pack()

        self.entry_a = tk.Entry(root)
        self.entry_b = tk.Entry(root)
        self.entry_c = tk.Entry(root)
        self.entry_a.pack()
        self.entry_b.pack()
        self.entry_c.pack()

        self.button_triangle = tk.Button(root, text="Вычислить площадь треугольника", command=self.calculate_triangle_area)
        self.button_triangle.pack()

    def calculate_circle_area(self):
        try:
            radius = float(self.entry_radius.get())
            if radius < 0:
                messagebox.showerror("Ошибка", "Радиус не может быть отрицательным.")
                return

            circle = Circle(radius)
            area = circle.area()
            messagebox.showinfo("Площадь круга", f"Площадь круга: {area:.2f}")
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод радиуса.")

    def calculate_triangle_area(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            triangle = Triangle(a, b, c)
            area = triangle.area()
            if triangle.is_right_angle():
                right_angle_info = "Это прямоугольный треугольник."
            else:
                right_angle_info = "Это не прямоугольный треугольник."

            messagebox.showinfo("Площадь треугольника", f"Площадь треугольника: {area:.2f}\n{right_angle_info}")
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод сторон треугольника.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
