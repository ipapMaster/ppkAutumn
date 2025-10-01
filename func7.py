# Лямбда-функции
# анонимные функции, безымянные функции
# функции-однострочники
words = ['Только', 'длинные', 'слова', 'пройдут', 'дальше', 'гидроэлектростанция']
a = (1, 2, 3)

b = map(lambda x: x * 2, a)
print(list(b))

long_word = filter(lambda w: len(w) > 6, words)
print(list(long_word))
