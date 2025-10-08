# Основные понятия в ООП
# Инкапсуляция (encapsulation - продолжение)
class Car:
    _counter = 0  # статичный член класса (счётчик машин, защищенный)

    def __init__(self, b='Noname', m='Nomodel'):
        self._brand = b
        self._model = m
        self._engine_on = False
        Car._counter += 1  # увеличиваем счётчик машин в гараже

    # Сокрытие информации о внутреннем
    # устройстве за внешним интерфейсом
    # и есть инкапсуляция
    def engine_start(self):
        self._engine_on = True

    def drive(self, place):
        if self._engine_on:
            print('Пункт назначения:', place)
        else:
            print('Двигатель не заведён, никуда не едем!')

    # Геттеры
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    # Сеттеры
    def set_brand(self, new_brand):
        self._brand = new_brand

    def set_model(self, new_model):
        self._brand = new_model

    def about_car(self):
        print('Автомобиль:')
        print('\tМарка:', self._brand)
        print('\tМодель:', self._model)

    @staticmethod
    def get_count():
        return Car._counter
