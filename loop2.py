# Моржовый оператор (walrus operator - :=) c версии 3.8

while (string := input('Введите любую строку или exit для завершения: ')) != 'exit':
    print('Вы ввели: ' + string)

print('Вы ввели: exit. Программа завершена.')
