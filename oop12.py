# Основные понятия в ООП
# Абстракция

from abc import ABC, abstractmethod


def get_shape_info(shape):
    if not isinstance(shape, (Shape, Rectangle)):
        print(f'Про фигуру {shape} я ничего не знаю!')
    else:
        print('Это объект класса', shape.__class__.__name__)
        print('Периметр этой фигуры:', shape.perimeter())
        print('Площадь этой фигуры:', shape.square())


class Shape(ABC):  # абстрактный базовый класс
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self._w = w
        self._h = h

    def square(self):
        return self._w * self._h

    def perimeter(self):
        return 2 * (self._w + self._h)


get_shape_info(Rectangle(4, 5))
get_shape_info('Шестиугольник')
