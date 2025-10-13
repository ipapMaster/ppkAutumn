# Регулярные выражения (regular expression)
# Поиск по паттерну (по образцу)
# Split и RegExp
import re

pattern = r'[,.!? ]+'
test_string = "Hello,    world! How are you? It is me."
result = re.split(pattern, test_string)

print(result)
