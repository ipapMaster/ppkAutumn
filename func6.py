# Функция, как объект и функции высшего порядка
# map(функция как объект, iterable)
# filter(критерий отбора, iterable)

words = ['Только', 'длинные', 'слова', 'пройдут', 'дальше']


def double(x):
    return x * 2


def long_word(word):  # слова, длина которых больше 10
    return len(word) > 6


a = (1, 2, 3)
lst = ['один', 'два', 'три']
print(a)

b = map(double, a)
print(list(b))

cap = map(str.upper, lst)
print(list(cap))

res = filter(long_word, words)
print(list(res))
# b = map(str, a)
# print('-'.join(b))
