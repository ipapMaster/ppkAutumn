# Строки, индексы
string = input('Введите любую строку: ')
length = len(string)  # число элементов итерируемого объекта (число символов в строке)

print('Строка "' + string + '" имеет длину:', length)

symb = string[-1]  # string[length - 1]

for index in reversed(string):
    print(index, end='')
