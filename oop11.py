# Основные понятия в ООП
# Наследование через dataclasses
from dataclasses import dataclass


@dataclass
class Cat:
    # Более лаконично (методы __init__ и __repr__ уже есть)
    name: str
    age: int
    weight: float
    color: str

    def speak(self):
        return f'{self.name} сказал "Мяу"'

    def eat(self):
        return f'{self.name} ест "Wiskas"'

    def sleep(self):
        return f'{self.name} спит'


@dataclass
class Kitten(Cat):
    mother_name: str
    is_vaccinated: bool = False

    def speak(self):
        return f'{self.name} сказал "Пиииии!"'

    def play(self):
        return f'{self.name} играет с клубком!'

    def grow(self):
        self.age += 1
        self.weight *= 1.2
        return f'{self.name} подрос. Теперь ему {self.age} лет.'


cat = Cat(
    name='Барсик',
    age=3,
    weight=4.5,
    color='Рыжий'
)

kitten = Kitten(
    name='Снежок',
    age=0,
    weight=0.8,
    color='Белый',
    mother_name='Мурка'
)

print(kitten)
print(kitten.grow())
