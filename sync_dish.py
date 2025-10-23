import time
from datetime import datetime

COEFF = 1  # 1 сек программы = 2 минуте реального времени


def dish(num, prepare, wait):
    """
    Функция имитирует приготовление блюда
    :param num: номер блюда по порядку
    :param prepare: минут на подготовку
    :param wait: ожидание готовности
    :return: None
    """
    print(f'Начало: {datetime.now().strftime('%HH:%MM:%SS')}: готовится блюдо №{num} в течении {prepare} мин.')
    time.sleep(COEFF * prepare)
    print(f'Начало: {datetime.now().strftime('%HH:%MM:%SS')}: ожидаем блюдо №{num} в течении {wait} мин.')
    time.sleep(COEFF * wait)
    print(f'Итак: {datetime.now().strftime('%HH:%MM:%SS')} блюдо №{num} готово')


def main():
    dish(1, 2, 3)
    dish(2, 5, 10)
    dish(3, 3, 5)


if __name__ == '__main__':
    ts = time.time()  # засекаем время начала
    main()  # запускаем готовку
    delta = int((time.time() - ts) / COEFF)  # подсчёт затраченного времени
    print(f'Готовка заняла {delta} мин. Сейчас: {datetime.now().strftime('%HH:%MM:%SS')}')
