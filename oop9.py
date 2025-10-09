# Основные понятия в ООП
# Наследование (Inheritance)
# Базовый класс (super-class, родительский)
# Производный (наследник, дочерний)
import math


class Rectangle:
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


t = EquilateralTriangle(3)

print(t)
print(t.perimetr())
print(t.square())
