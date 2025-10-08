# Основные понятия в ООП
# Инкапсуляция (encapsulation)
class Person:
    _counter = 0  # статичный член класса (счётчик персон, защищенный)

    def __init__(self, n='Noname', a=0, c='РФ'):
        self._name = n
        self._age = a
        self._nationality = c
        Person._counter += 1  # увеличиваем счётчик экземпляров

    def about_me(self):
        print(f'Я - "{self._name}", мой возраст {self._age}.')
        print(f'Я из: {self._nationality}.')

    # Setter (сеттер)
    def set_age(self, new_age):
        if 0 < new_age <= 125:
            self._age = new_age
        else:
            print('Недопустимое значение для возраста')

    def set_name(self, new_name):
        if len(new_name) > 3:
            self._name = new_name

    def set_nationality(self, new_nation):
        if len(new_nation) > 1:
            self._nationality = new_nation

    # Getter (геттеры)
    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    @staticmethod
    def get_count():
        return Person._counter


p1 = Person('John', 27, 'USA')
p1.set_age(-25)
p1.about_me()
print('Итак, его зовут -', p1.get_name())

print('Всего персон:', Person.get_count())  # We are all adults here
