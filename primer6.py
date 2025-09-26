counter_positive = 0
counter_negative = 0
for i in range( 11):
    number = int(input('введите число '))
    if number > 0:
        counter_positive += 1
    if number < 0:
        counter_negative += 1

print(f'количество положительных чисел {counter_positive}')
print(f'количество отрицательных чисел {counter_negative}')