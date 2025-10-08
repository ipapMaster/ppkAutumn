# Основные понятия в ООП
# Специальные методы
# __init__ - создание объекта
# __name__ - возвращает имя объекта(экземпляра) или модуля
# __sizeof__() - размер объекта в байтах
# __class__ - имя класса объекта


# Всё есть объект - манипуляции с объектами
# a, b = 3, 4
#
# c = a + b  # "под капотом" -> a.__add__(b)
# c = a / b  # "под капотом" -> a.__div__(b)
# c = str(a) # "под капотом" -> a.__str__()

class A:
    def __init__(self, a=0):
        self.a = a

    # Переопределяем (override)
    # преобразование в строку
    def __str__(self):
        return f'<Объект класса A со значением a = {self.a}>'

    # Представление (representation) сложного объекта
    def __repr__(self):
        return f'<Объект класса A со значением a = {self.a}>'

    def __add__(self, other):
        return A(self.a + other.a)


class B:
    def __init__(self, b=0):
        self.b = b

    # Переопределяем (override)
    # преобразование в строку
    def __str__(self):
        return f'<Объект класса B со значением b = {self.b}>'

    # Представление (representation) сложного объекта
    def __repr__(self):
        return f'<Объект класса B со значением b = {self.b}>'

    def __sub__(self, other):
        return B(self.b - other.b)


a1 = A(10)
a2 = A(15)
c = a1 + a2

b1 = B(15)
b2 = B(10)

d = b1 - b2

print(c)
print(d)
