# Student, Employee, Person
# Домашнее задание
# Модификаторы доступа
# public - публичный, доступный всем и отовсюду (self.name)
# private - закрытый, доступный только внутри класса (self.__name)
# protected - защищённый, доступный внутри класса и его наследникам (self._name)
class Student:
    def __init__(self, u=''):
        self.university = u


class Employee:
    def __init__(self, c=''):
        self.company = c


class Person:
    def __init__(self, n='', a=0):
        self.__name = n
        if not isinstance(a, int):
            raise TypeError('Возраст должен быть целым числом!')
        if not (0 <= a <= 125):
            raise ValueError('Возраст должен быть в диапазоне 0...125')
        self.__age = a

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Возраст должен быть целым числом!')
        if not (0 <= new_age <= 125):
            raise ValueError('Возраст должен быть в диапазоне 0...125')
        self.__age = new_age

    def get_info(self):
        return self.__str__()

    def __str__(self):
        return f'<Person({self.__name}, {self.__age})>'

    def __repr__(self):
        return f'<Person({self.__name}, {self.__age})>'


s = Student('Техноложка')
e = Employee('Авангард')
p = Person('Дима', 23)

persons = [s, e, p]

for person in persons:
    # if type(person) is Student: # is идентичность, а не равенство
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name, person.age)

print(p.get_info())
