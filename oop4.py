# Основные понятия в ООП
# Полиморфизм (polymorphism)
# Свойство кода работать с разными типами данных
from math import pi


# Полиморфная функция
def print_shape_info(shape: object) -> None:
    """
    Распечатывает информацию о площади и периметре объекта
    :param shape: объект: квадрат, круг, прямоугольник, ...
    :return: None
    """
    figure = None
    if shape.__class__.__name__ == 'Square':
        figure = 'квадрата'
    if shape.__class__.__name__ == 'Circle':
        figure = 'круга'
    if shape.__class__.__name__ == 'Rectangle':
        figure = 'прямоугольника'
    print(f'Площадь {figure}: {shape.square()}\nПериметр {figure}: {shape.perimeter()}')


class Rectangle:
    def __init__(self, a=1, b=1):
        self._a = a
        self._b = b

    def perimeter(self):
        return 2 * (self._a + self._b)

    def square(self):
        return self._a * self._b


class Circle:
    def __init__(self, r=1):
        self._radius = r

    def perimeter(self):
        return 2 * pi * self._radius

    def square(self):
        return pi * (self._radius ** 2)


class Square:
    def __init__(self, s=1):
        self._side = s

    def perimeter(self):
        return 4 * self._side

    def square(self):
        return self._side ** 2


s = Square(5)  # Квадрат со стороной 5
c = Circle(5)  # Окружность с радиусом 5
r = Rectangle(3, 4)

print_shape_info(s)
print_shape_info(c)
print_shape_info(r)

# print(dir(s))
# print(dir(c))
