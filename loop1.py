# Циклы (DRY - Don't repeat Yourself)
# for count in range(s, s, s)
# s - start (0 - по умолчанию)
# s - stop (не включая)
# s - step (1 - по умолчанию)
# for i in range(10) -> ... in range(0, 10, 1)

loop = True

while loop:
    string = input('Введите любую строку: ')
    if not string:
        loop = False

print('Вы ничего не ввели. Программа завершена')


