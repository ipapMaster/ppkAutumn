# Исключения и конструкция их обработки
# try:
#     пробуем провести операцию
# except ИмяИсключения:
#     если исключени было, то обработчик
# else: # если исключения не было (не обязательно)
#     тогда отдельный блок кода
# finally: # блок кода, который выполнится
#     # в любом случае

# Пример 1
# try:
#     f = open('file.txt')
#     # какие-то действия с файлом
# except FileNotFoundError:
#     print('Файл не найден')
# else:
#     f.close()

# Пример 2
# try:
#     number = int(input('Введите число: '))
# except ValueError as exp:
#     print('Это не число, а', exp.args[0].split()[-1])
# else:
#     print('Вот введённое число:', number)
# finally:
#     print('Ну, что-то в любом случае вводилось...')

# Пример 3 - несколько исключений
# a = [0, 1, 2, 3]
# try:
#     index = int(input('Введите индекс: '))
#     result = 5 / a[index]
# except ZeroDivisionError:
#     print('Попытка деления на ноль!')
# except IndexError:
#     print('Такого индекса нет')
# except ValueError:
#     print('Индекс должен быть целым числом')
# except Exception as exp:
#     print('Тут вот что:', exp)
#     print('Отработало исключение:', exp.__class__.__name__)
# else:
#     print('Удачно угадали индекс')
#     print('И получили результат -', result)
# finally:
#     try:
#         print('А индекс вводился такой:', index)
#     except NameError:
#         print('Не смогли назначить индекс')

# Пример 4. Бросаем исключение
# try:
#     age = int(input('Введите возраст человека: '))
#     if age < 0:
#         raise ValueError('Возраст не может быть отрицательным.')
#     elif age > 125:
#         raise ValueError('Возраст не может быть больше 125.')
# except ValueError as exp:
#     if exp.args[0].startswith('invalid'):
#         print('Надо вводить целое число, а не', exp.args[0].split()[-1])
#     else:
#         print(exp)
# # На всякий случай, для отладки (not production)
# except Exception as e:
#     print('Непредвиденная ситуация:', e)
# else:
#     print('Введен возраст:', age)

# Пример 5
# class Example:
#     pass
#
#
# example = Example()
#
# try:  # попытка обращения к несуществующему атрибуту объекта
#     print(example.info())
# except AttributeError:
#     print('Такого атрибута нет')

# Пример 6. Утверждение (Assertion)
# try:
#     password = input('Введите пароль: ')
#     assert len(password) > 8
# except AssertionError:  # используют чаще в целях тестирования и отладки
#     print('Пароль слишком короткий.')
# else:
#     print('Успешный ввод.')

# Пример тестирования функции через assert
# Функция
def validate_email(email):
    assert '@' in email, 'E-mail должен содержать символ @'
    assert email.endswith(('.ru', '.org', '.com')), 'Домен для E-mail не указан'
    return True


# Сам тест
try:
    validate_email('test@example.com')
    # validate_email('test#example.com')
    validate_email('test@example')
except AssertionError as e:
    print('Не прошёл проверку:', e)
