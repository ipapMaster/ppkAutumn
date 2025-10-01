# Функции с переменным число аргументов

# Распаковка с помощью *
x, *ostatok, y = 1, 2, 3, 4, 5, 6


def multiply(first=1, *rest):
    result = first
    for value in rest:
        result *= value
    return result


def div(a, b):
    return a / b


def multiply2(*rest: int, action='m') -> int or None:
    """
    Действия над переменным числом аргументов
    если задан неверный аргумент, то вернёт None
    :param rest: позиционные аргументы (числа)
    :param action: m - произведение, s - сумма
    :return: сумму или произведение аргументов
    """
    match action:
        case 'm':
            result = 1
            for value in rest:
                result *= value
        case 's':
            result = 0
            for value in rest:
                result += value
        case _:
            result = None
    return result


print(x, y)
print(ostatok)
print(multiply(2, 3, 4, 5))
print(multiply2(1, 2, 3, 4, 5, action='w'))
print(div(b=6, a=18))
