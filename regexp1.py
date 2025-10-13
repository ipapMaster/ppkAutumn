# Регулярные выражения (regular expression)
# Поиск по паттерну (по образцу)
import re

# \b - начало искомой последовательности и её окончание
# \w - все буквы, цифры и символ подчёркивания (@ - уже не подойдёт)
# {N} - точное количество совпадений
# \Z - заканчивается на текущий контекст
# [есн] - присутствуют ли в строке эти буквы
# [^aб] - всё, кроме а и б
# [а-яА-Я] - все буквы: от а до я и от А до Я
# findall - все совпадения в виде списка
# search - находит первое совпадение во всей строке
# match - совпадение в начале строки

pattern = '[0-5][0-9]'
test_string = 'Московское время: 07:45'

result = re.findall(pattern, test_string)

print(result)


# pattern = '[^те]'
#
# test_string = 'Телевизор и сеть и антенна'
#
# result = re.findall(pattern, test_string, re.IGNORECASE)
#
# print(result)

# заканчивается ли строка на искомую последовательность
# pattern = r'сначала\Z'
#
# test_string = 'эта песня хороша, начинай сначала'

# result = re.search(pattern, test_string)
#
# print(result.group())

# Найти три подряд идущие цифры
# pattern = r'\d{3}'
# test_string = 'Для записи в МФЦ звоните 122, но не 112'
#
# result = re.findall(pattern, test_string)
#
# print(result)

# pattern = r'\d'  # только цифры
# test_string = 'Для экстренных вызовов звоните 112'
# есть ли цифры в строке
# result = re.search(pattern, test_string)
#
# print('Цифры есть') if result else print('Цифр нет')

# pattern = r'\b\w{4}\b'  # raw string, все слова из 4-х букв
# test_string = 'Мама мыла раму, а папа был на пилораме'
#
# result = re.findall(pattern, test_string)

