# Функции и область видимости
# Local scope (локальная область)
# Global scope (глобальная область)
import math

a = 3  # Глобальная область (a - глобальная переменная)


def square(x):  # x - из локальной области (локальная переменная)
    return x ** 2


def round_length(radius=0):
    return round(2 * math.pi * radius, 2)


def main():  # encapsulated
    radius = 5
    result = round_length(radius)
    print(result)


def print_array(array):
    for item in array:
        print(item)


def change_a():
    global a  # разрешаем менять значение глобальной переменной
    a = a + 1
    return a


def greet(name):
    print('Здравствуй,', name)
    name = 'товарищ'
    print('Здравствуй,', name)


arr = [1, 2, 3]
main()
greet('Петя')
print('Значение а до:', a)
print()
print('Вызов change_a:', change_a())
print('Значение а после:', a)
print(square(a))
print_array(arr)
