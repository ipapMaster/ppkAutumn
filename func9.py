# Декораторы
import time

# 1. Функцию можно переопределить
language = 'ru'

if language == 'en':
    def greet(name):
        print('Hello,', name)
else:
    def greet(name):
        print('Привет,', name)


# greet('Дмитрий')


# Лучше пользоваться декоратором
# Функция, которая принимает другую функцию
# в качестве аргумента и меняет её поведение

# определяем простой декоратор
def my_decorator(func):
    def wrapper():  # обёртка без параметров
        print('Действия до вызова переданной функции')
        func()  # вызов переданной функции
        print('Действия после вызова переданной функции')

    return wrapper


# декоратор с параметрами
def params_decorator(func):
    def wrapper(*args, **kwargs):
        print('Задекорированная функция вызвана с параметрами: ', args, kwargs)
        result = func(*args, **kwargs)
        print('Результат функции', result)
        return result

    return wrapper


# Измерение времени работы функции
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # время старта
        result = func(*args, **kwargs)
        end_time = time.time()  # время окончания
        print(f'Функция {func.__name__} выполнялась {end_time - start_time:.2f} сек.')
        return result

    return wrapper


@my_decorator
def called_func():
    print('Вызываемая функция')


@params_decorator
def summ(a, b, action='s'):
    if action == 's':
        return a + b
    return a * b


@timing_decorator
def fill_list():
    a = []
    print('Начало работы')
    # time.sleep(2)  # задержка в 2 сек
    for i in range(10000000):
        a.append(i)
    print('Окончание работы')


fill_list()
# res = summ(3, 4, action='m')
# print(res)
# called_func()
