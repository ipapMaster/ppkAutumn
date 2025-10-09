# Файлы и работа с ними
# Построчное чтение

f = open('./files/info.txt', 'at+', encoding='utf8')  # файловый объект

f.seek(0)  # если открыт как at+, то нужно сместиться в начало

lines = f.readlines()

# Через map
# lines = list(map(lambda x: x.strip(), lines))

# Через списочное выражение
lines = [x.strip() for x in lines]

for line in lines:
    if line:
        print(line)

# print(lines)

# Оптимальный способ (если нет пустых строк до конца файла)
# while line := f.readline().strip():
#     print(line)

f.close()


"""
Плохая практика:
line = None

while True:
    line = f.readline().strip()
    if line:
        print(line)
    else:
        break
"""
