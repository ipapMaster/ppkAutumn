# Функции
import statistics
import math

temperatures = [13, 11, 7, -1, 7, 9, 10]


def hello(name):
    print('Привет,', name)


def goodbye(name):
    print('Пока,', name)


def min_value(t):
    min_val = t[0]  # присваиваем минимуму значение первого элемента
    for num in t:
        if num < min_val:
            min_val = num
    return min_val  # возврат значения и завершение работы


def max_value(t):
    max_val = t[0]  # присваиваем минимуму значение первого элемента
    for num in t:
        if num > max_val:
            max_val = num
    return max_val  # возврат значения и завершение работы


def average(t):
    count = len(t)  # число элементов в списке
    summ = 0  # изначально сумма нулевая
    for num in t:
        summ += num
    return summ / count


def round_len_and_square(radius):
    print(f'Площадь круга с радиусом {radius} = '
          f'{radius ** 2 * math.pi}')
    print(f'Длина окружности с радиусом {radius} = '
          f'{radius * 2 * math.pi}')


print(min_value(temperatures))
print(max_value(temperatures))
print(average(temperatures))

print()

# Тоже самое, но встроенными функциями
print(min(temperatures))
print(max(temperatures))
print(sum(temperatures) / len(temperatures))
print(statistics.mean(temperatures))  # встроенной нет, но есть библиотека
round_len_and_square(5)

# hello('Пётр')
# goodbye('Дима')
