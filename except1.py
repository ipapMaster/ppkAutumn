# Исключения - это не ошибка
# Исключение возникает run-time
# т.е. во время работы программы
# исключительная ситуация
# 1. NameError - имя не определено
a = 3

try:
    print(a)
except NameError:
    print('Переменная b не была определена!')

# 2. Деление на ноль
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print('На ноль делить нельзя')

# 3. Некорректный индекс
s = 'Python'
try:
    print(s[8])
except IndexError:
    print('Некорректный индекс')

# 4. Отсутствие файла для чтения
fname = 'non-exists.txt'

try:
    f = open(fname)
except FileNotFoundError:
    print(f'Файла {fname} не существует!')

# 5. Некорректная операция с типами
x = 4
y = '5'

try:
    print(x + y)
except TypeError:
    print('Нельзя выполнять операции с данными разного типа')

# 6. Ошибка преобразования
z = '4f'

try:
    print(int(z))
except ValueError:
    print('Некорректное приведение типа')

# 7. Не знаем какое исключение
try:
    a = 3 / 0
except Exception as exp:  # сообщение при выбросе исключения
    print(exp.__class__.__name__)  # получаем имя
