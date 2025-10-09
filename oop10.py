# Основные понятия в ООП
# Наследование (Inheritance)
# Иерархия на примере геометрических фигур
import math


class Shape:
    def __repr__(self):
        return f'Класс: {self.__class__.__name__}'


class Rectangle(Shape):
    def __init__(self, a=1, b=1):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, new_a):
        if not isinstance(new_a, int):
            raise TypeError('Сторона прямоугольника должна быть целым числом')
        self._a = new_a

    @b.setter
    def b(self, new_b):
        if not isinstance(new_b, int):
            raise TypeError('Сторона прямоугольника должна быть целым числом')
        self._b = new_b

    def __str__(self):
        return f'<{self.__class__.__name__}({self._a}, {self._b})>'

    def __repr__(self):
        return self._a, self._b

    def square(self):
        return self._a * self._b

    def perimetr(self):
        return 2 * (self._a + self._b)


class Square(Rectangle):
    def __init__(self, a=1):
        super().__init__(a, a)


class Circle(Square):
    def __init__(self, d):
        super().__init__(d)
        self.radius = d / 2

    def square(self):
        return math.pi * self.radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'<Circle(Radius: {self.radius})>'


class EquilateralTriangle(Square):
    def __init__(self, side):
        if not isinstance(side, (int, float)) or side < 0:
            raise ValueError('Сторона должна быть положительным числом')

        self.side = side  # сохраняю сторону
        super().__init__(side)  # скорее всего не используем

    # Override (переопределение методов)
    def square(self):
        return round((math.sqrt(3) / 4) * self.side ** 2, 3)

    def perimetr(self):
        return 3 * self.side

    def __str__(self):
        return f'EquilateralTriangle({self.side}, {self.side}, {self.side})>'


t = Circle(3)

print(t.__class__.__bases__)  # кто родитель
print(t.__class__.__mro__)  # полная иерархия
print(t.radius)
print(t.perimetr())
print(t.square())
