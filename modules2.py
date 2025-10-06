# Встроенные модули
# Не импортируем то, чем не пользуемся
from random import choice, choices, shuffle


# Ctrl + Alt + O - оптимизировать импорт

# print(random.randint(1, 10))
# print(random.randrange(1, 10, 2))
# zars = list(range(9856, 9862))
# print(chr(choice(zars)), chr(choice(zars)))

# lst = ['Вероятней всего', 'Наверное', 'Пока не точно', 'Даже не думай',
#        'Хорошие перспективы']

# while (question := input('Ваш вопрос: ').lower()) != 'хватит':
#     print(choice(lst))

# if len(lst) > 0:
#     print(choices(lst, k=3))  # с повторами
#     print(sample(lst, k=2))  # без повторов

# пароль из 8-символов (маленькие и большие буквы, как минимум один спец-символ и одна цифра)
def random_password() -> str:
    """
    Возвращает 8-значный случайный пароль
    :return: строка, которая состоит из больших,
    маленьких букв, одной цифры и одного спец-символа
    """
    letters = list('qwertyuiopasdfghjklzxcvbnm')
    digits = list('0123456789')
    special = list('@_#$^')
    big_letters = list(map(lambda x: x.upper(), letters))

    three_letters = choices(letters, k=3)  # выбор 3-х случайных маленьких букв
    three_big_letters = choices(big_letters, k=3)  # выбор 3-х случайных больших букв
    one_digit = choice(digits)  # выбор одной случайной цифры
    one_special = choice(special)  # выбор одного случайного спецсимвола

    # складываем случайные выборки
    result = three_letters + three_big_letters + [one_special] + [one_digit]
    # и "замешиваем" их
    shuffle(result)

    return ''.join(result)  # возвращаем результат в виде строки


print('Пять случайных паролей:')
for _ in range(5):
    print('\t', random_password())
