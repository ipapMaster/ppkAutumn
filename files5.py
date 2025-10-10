# Файлы и запись словаря
# Домашнее задание

# Есть словарь, который нужно сохранить
# в файл и потом уметь его оттуда прочитать

class SmartDict:
    def __init__(self):
        self._d = {'стол': 'table', 'стул': 'chair'}

    def print_dict(self):
        for k, v in self._d.items():
            print(f'{k} : {v}')

    def is_in_dict(self, key):
        return key in self._d  # вернёт True, если такой ключ есть в словаре

    def add_word(self, value, translate):
        self._d[value] = translate

    def save_dict(self):
        # Менеджер контекста (конструкция with ... as)
        # автоматически закрывает файл
        with open('./files/dict.txt', 'wt', encoding='utf-8') as f:
            for k, v in self._d.items():
                print(f'{k} : {v}', file=f)

    def read_dict(self):
        self._d.clear()
        with open('./files/dict.txt', 'rt', encoding='utf-8') as f:
            while line := f.readline().strip():
                k, v = line.split(' : ')
                self._d[k] = v

    def translate_word(self, word):
        return self._d[word]


sd = SmartDict()  # создаём экземпляр SmartDict

sd.read_dict()  # читаем из файла

while (w := input('Введите слово для перевода или "#" для выхода: ')) != '#':
    if sd.is_in_dict(w):
        print(f'Слово {w} переводится как {sd.translate_word(w)}')
    else:
        print('Я пока перевода не знаю.')
        t = input(f'А как "{w}" переводится? ')
        sd.add_word(w, t)

sd.save_dict()  # записываем "поумневший" словарь в файл
