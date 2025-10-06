# Встроенные модули
# Не импортируем то, чем не пользуемся
# Дата и время
import datetime as dt

# Получения текущих даты и времени из операционной системы
print(dt.datetime.now())  # выводит дату и время
print(dt.datetime.now().date())  # вычленяем только дату
print(dt.datetime.now().time())  # вычленяем только время

# Для вывода строки из формата времени используем
raw_time = dt.datetime.now()  # в формате datetime
date_as_string = raw_time.strftime('Сегодня: %d.%m.%Y')
time_as_string = raw_time.strftime('А время: %H : %M : %S')
print(date_as_string)
print(time_as_string)

# Создание объекта с датой
weekdays = ['понедельник', 'вторник']
new_date = dt.date(2021, 11, 27)
print(dt.date.today())
# целое число от 0 - понедельник, до 6 - воскресенье
weekday = dt.date.today().weekday()
print(weekdays[weekday])
print(type(weekday))
print(type(new_date))
date_as_string = new_date.strftime('%d.%m.%Y')
print(date_as_string)
print(type(date_as_string))

# Создание объекта с временем
new_time = dt.time(11, 30, 15)
print(new_time)
print(type(new_time))

# Создаём две даты и получаем разницу
first_date = dt.date(1941, 6, 22)
second_date = dt.date(1945, 5, 9)

diff = second_date - first_date
temp = diff.days
print(type(temp))
print()


# используем random() (от 0,000000...1 до 0,99999999....)
# from random import random, randint
#
# result = []
#
# for i in range(6):
#     temp = random() + randint(0, 5)
#     # result.append(round(temp, 1))
#     result.append(f'{temp:.1f}')
#
# print(*result, sep=', ')
