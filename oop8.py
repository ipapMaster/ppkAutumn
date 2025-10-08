# Основные понятия в ООП
# Специальный метод __call__
# позволяет делать объект вызываемым

import time


class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, step=1):
        self.counter += step
        return self.counter

    def __str__(self):
        return str(self.counter)


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Начало работы медленной функции...')
        start = time.time_ns()
        result = self.func(*args, **kwargs)
        end = time.time_ns()
        print('Работа медленной функции завершена.')
        print(f'Выполнялось: {(end - start) / 10 ** 9:.4f} сек.')
        return result


@Timer
def slow_func(x):
    time.sleep(x)
    return 'Функция завершила работу'


slow_func(3)

# c = Counter()
# c(5)
# c(5)
# print(c)
