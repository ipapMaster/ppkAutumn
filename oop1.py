# Основные понятия в ООП
# 1. Класс - описание модели будущего объекта
# 2. Экземпляр - экземпляр (объект) класс
# 3. Объект - конкретное воплощение класса
# 4. Атрибуты - свойства и действия, присущие объекту
# 5. Метод - действия над собой и другими объектами
class Fruit:
    def __init__(self, n='Фрукт', w=0, c='Белый'):
        self.name = n
        self.weight = w
        self.color = c

    def washed(self):
        print(f'Фрукт "{self.name}" помыт')

    def about_me(self):
        print(f'Я фрукт "{self.name}", который весит {self.weight} грамм.')
        print(f'А цвет у меня: {self.color}.')


f1 = Fruit('Груша', 150, 'Зелёный')  # вызван конструктор
# f1.name = 'Груша'
# f1.weight = 150
f1.about_me()
# print(f'Фрукт "{f1.name}" весит {f1.weight} грамм.')
f1.washed()

f2 = Fruit('Яблоко', 180, 'Красный')  # вызван конструктор
# f2.name = 'Яблоко'
# f2.weight = 180

# print(f'Фрукт "{f2.name}" весит {f2.weight} грамм.')

f3 = Fruit('Лемон', 160, 'Жёлтый')  # вызван конструктор
# f3.name = 'Лемон'
# f3.weight = 160
# f3.color = 'Жёлтый'
#
# print(f'Фрукт "{f3.name}", цвет: {f3.color} весит {f3.weight} грамм.')

# print(f1.color) #  у f1 цвет не назначался

f4 = Fruit('Ананас', 650)
f4.about_me()
