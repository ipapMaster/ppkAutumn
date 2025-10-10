# Файлы, директории и операции с ними
import os

# Текущая рабочая директория
path = os.getcwd()  # get current working directory
print(path)

# os.mkdir('имя_директории') - создаёт директорию
# os.rename('старое_имя', 'новое_имя') - переименовывает файл или директорию
# os.remove('имя_файла') - удалить файл
# os.path.basename('путь') - получить имя файла (директории) из пути
# os.path.join('часть1', 'часть2', 'часть3' ...) - объединение частей пути
# os.path.exists('путь') - проверка, что путь существует

# Базовый элемент
name = os.path.basename(path)
print(name)

# собираем путь из частей
set_path = os.path.join('C:\\', 'Users', 'student', 'PycharmProjects')
set_path = os.path.join(set_path, 'Cycles')
print(set_path)

# Проверка файла перед открытием
if os.path.exists(os.path.join(path, 'files', 'dict.txt')):
    print('Файл можно открывать на чтение')

# или с явным указанием пути
if os.path.exists('./files/dict.txt'):
    print('Файл существует')

# Смена директории
os.chdir('files')  # "входим" в files
print(os.getcwd())
os.chdir('..')  # и выходим оттуда
print(os.getcwd())
# зайдём в images и распечатаем все файлы оттуда
os.chdir('images')
file_list = os.listdir()  # текущая директория - по умолчанию
# отфильтровали файлы, которы начинаются на pyth
new_list = [f for f in file_list if f.startswith('pyth')]
print(new_list)

# Проверка на пустоту директории
if os.path.exists(os.path.join(path, 'test')):  # сначала проверим есть ли такой путь
    if os.listdir(os.path.join(path, 'test')):
        print('В директории есть файлы')
    else:
        print('Директория пуста')
else:
    print(f'Такого пути {os.path.join(path, 'test')} нет')

# переименовали файлы с числом
# for name in new_list:
#     if name[6].isdigit():  # если число
#         os.rename(name, name[:6] + '_' + name[6] + name[7:])

# os.chdir('..')
