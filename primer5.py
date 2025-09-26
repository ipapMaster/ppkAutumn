# попросить пользователя 11 раз ввести числа
# подсчитать количество положительных и количество отрицательных

counter_positive = 0
counter_negative = 0
i = 0
while i < 11:
    number = int(input('введите число '))
    if number > 0:
        counter_positive += 1
    if number < 0:
        counter_negative += 1
    i += 1                      #увеличиваем счетчик шагов цикла
print(f'количество положительных чисел {counter_positive}')
print(f'количество отрицательных чисел {counter_negative}')
