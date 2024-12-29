import math


class Circle:
    def __init__(self, radius):  # Радиус круга
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # Площадь круга

    def perimeter(self):
        return 2 * math.pi * self.radius  # Периметр круга


r = int(input("Введите радиус круга: "))
obj = Circle(r)
print("Площадь круга:", round(obj.area(), 2))
print("Длина окружности:", round(obj.perimeter(), 2))
