# Множества
# Неупорядоченная коллекция данных
# Исключает повторы
# Может содержать любой тип данных (смешанно)
from gettext import find

s = set()  # Пустое множество
filled = {'cat', 'dog', 1, 2, 37.8, 'dog', 'dog', 1}
letters_num = '1234567890qwertyuiopasdfghjkl'

if 'dog' in filled:
    print('"dog" присутствует в множестве')

ln = set(letters_num)
print(ln)

print(f'Длина множества "filled" - {len(filled)}')

for item in filled:
    print(item)
