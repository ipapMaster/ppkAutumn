# Регулярные выражения (regular expression)
# Поиск по паттерну (по образцу)
# Квантификаторы (quantifiers)
import re

# . - любой символ
# {m, n} - встречается от m до n раз
# {m} - ровно m раз
# {m,} - от m b и более раз
# {,n} - не более n раз
# ? - аналог {0,1}
# * - от нуля до 32767, аналог {0,}
# + - аналог {0,1}
# () - группировка

# "Жадный" квантификатор (greedy quantifier)
# pattern = '<img.*>'
# test_string = 'Картинка <img src="bg.jpg"> и текст'

# Минорный квантификатор
# pattern = r'<img.*?>'
# test_string = 'Картинка <img src="bg.jpg"> и текст</p>'

# Только путь к картинке
pattern = r'<img[^>]+src="([^">]+)"'
test_string = 'Картинка <img src="bg.jpg"> и текст</p>'
result = re.findall(pattern, test_string)
print(result)


# pattern = 'Go{,2}gle'
#
# test_string = 'Gogle, Google, Gooogle'
#
# result = re.findall(pattern, test_string)
#
# print(result)
