# Неизменяемость строки (immutable)
# на хождение и подсчёт элементов

string = 'толокно'
counter = 0

count = string.count('о')
# index = string.find('о')

print('В слове', string, 'число букв "о" -', count)
# print(index)  # 1, 3, 6

# Способ 1
# for i in range(len(string)):
#     if string[i] == 'о':
#         print('Позиция -', i + 1)

# Способ 2 (доработать)
i = False  # Флаг, отвечающий за последующие итерации
for _ in range(count):
    if i:
        counter = string.find('о', counter + 1)
    else:
        counter = string.find('о')
        i = True
    print(counter + 1)
