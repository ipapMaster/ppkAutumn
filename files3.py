# Файлы и работа с ними
# Запись через print

text = """Однажды в студёную зимнюю пору,
Я из лесу вышел,
Был сильный мороз."""

f = open('./files/info.txt', 'wt', encoding='utf8')  # файловый объект

print(text, end='...', file=f)

f.close()
