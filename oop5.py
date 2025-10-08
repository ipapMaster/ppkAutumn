# Основные понятия в ООП
# Полиморфизм (polymorphism - продолжение)
# Свойство кода работать с разными типами данных
# Функция isinstance(объект, класс) -> True или False
# ДЗ - добавить необходимые поля, вывод об объекте,
# сеттеры и сеттеры

# Student, Employee, Person
class Student:
    def __init__(self, u=''):
        self.university = u


class Employee:
    def __init__(self, c=''):
        self.company = c


class Person:
    def __init__(self, n=''):
        self.name = n


s = Student('Техноложка')
e = Employee('Авангард')
p = Person('Дима')

persons = [s, e, p]

for person in persons:
    # if person is Student: # is идентичность, а не равенство
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
