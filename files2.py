# Файлы и работа с ними
# Запись

f = open('./files/info.txt', 'at', encoding='utf8')  # файловый объект

num = f.write('Привет\n')

print(f'В файл было записано {num} байт')
print(f.readable())

f.close()
