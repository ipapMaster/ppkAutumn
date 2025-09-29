# Циклы (DRY - Don't repeat Yourself)
# for count in range(s, s, s)
# s - start (0 - по умолчанию)
# s - stop (не включая)
# s - step (1 - по умолчанию)
# for i in range(10) -> ... in range(0, 10, 1)

# string = input('Введите любую строку или exit для завершения: ')

loop = True

while loop:
    string = input('Введите любую строку или exit для завершения: ')
    if string == 'exit':
        loop = False  # 0
    print('Вы ввели: ' + string)

print('Вы ввели: exit. Программа завершена.')
