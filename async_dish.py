import time
import os
import asyncio
from datetime import datetime

COEFF = 1  # 1 сек программы = 2 минуте реального времени


async def dish(num, prepare, wait):
    """
    Функция имитирует приготовление блюда
    в асинхронном режиме
    :param num: номер блюда по порядку
    :param prepare: минут на подготовку
    :param wait: ожидание готовности
    :return: None
    """
    print(f'Начало: {datetime.now().strftime('%H:%M:%S')}: готовится блюдо №{num} в течении {prepare} мин.')
    time.sleep(COEFF * prepare)
    print(f'Начало: {datetime.now().strftime('%H:%M:%S')}: ожидаем блюдо №{num} в течении {wait} мин.')
    await asyncio.sleep(COEFF * wait)
    print(f'Итак: {datetime.now().strftime('%H:%M:%S')} блюдо №{num} готово')


async def main():
    # создаём задачи
    tasks = [
        asyncio.create_task(dish(1, 2, 3)),
        asyncio.create_task(dish(2, 5, 10)),
        asyncio.create_task(dish(3, 3, 5))
    ]
    # группируем (собираем) задачи
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    ts = time.time()  # засекаем время начала
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())  # запускаем готовку в асинхронном режиме
    delta = int((time.time() - ts) / COEFF)  # подсчёт затраченного времени
    print(f'Готовка заняла {delta} мин. Сейчас: {datetime.now().strftime('%H:%M:%S')}')
