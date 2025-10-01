# Функции с переменным числом именованных аргументов
# Аргумент с двумя звездочками означает, что функция
# может использовать переменное число именованных аргументов
# пример **kwargs - keyword arguments

# Ternary if (Тернарный if)
def weather(temp):
    return 'тепло' if temp > 15 else 'холодно'


def cook(*ingredients, action='f'):  # b - варить
    print('Ингредиенты', end=': ')
    print(', '.join(ingredients), end='.\n')
    print('Их мы будем', end=': ')
    print('жарить.' if action == 'f' else 'варить.')


def about_man(name: str, surname: str, age: int, *children, **additional):
    translate = {
        'profession': 'Профессия',
        'birth': 'Дата рождения',
        'hobby': 'Хобби'
    }
    print(f'Человек: {surname} {name}.')
    print(f'Возраст: {age}.')
    print('Дети', end=': ')
    if len(children) > 0:
        print(', '.join(children))
    if additional:
        print('Дополнительная информация:')
        for k, v in additional.items():
            print(f'\t{translate.get(k, '')}: {v}')


# about_man('Дмитрий', 'Донской', 38, 'Петя', 'Маша',
#           profession='Писатель', birth='20/09/1987', hobby='Плавание', lang='Русский')

cook('лук', 'картофель', action='f')
