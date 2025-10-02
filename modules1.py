# Встроенные модули
# Не импортируем то, чем не пользуемся
# print(dir(m))

# import math as m  # псевдоним через as
#
# # from math import pi, e, sqrt
# print(f'Число Пи:', m.pi)
# print('Применим ceil к Pi:', m.ceil(m.pi))
# print(f'Основание натурального логарифма:', m.e)
# print(f'Квадратный корень из 225:', m.sqrt(225))

# ord и chr - для работы только с символами
# Узнаём код по символу
letter = 'r'
code = ord(letter)
print(code)

# Узнаём символ по коду
# « - 171
# » - 187
# ⚀ - 9856
# ⚁ - 9857
# ⚅ - 9861
symbol = chr(9861)
print(symbol)
print(f'Кафе {chr(171)}Аист{chr(187)}')





