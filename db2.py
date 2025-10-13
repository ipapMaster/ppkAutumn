# Базы данных
# Архиватор или структурированное хранение и передача
# JSON - Java Script Object Notation
# Чтение JSON:
# json.load() - читаем прямо из файлы
# json.loads() - json как строка
import json

with open('data/pets.json', 'rt', encoding='utf-8') as f:
    data = json.load(f)

    # Если объект один (один условный словарь)
    # for key, value in data.items():
    #     if type(value) is list:
    #         print(f'{key}: {', '.join(value)}')
    #     else:
    #         print(f'{key}: {value}')

    # А если список объектов (словарей)
    # print('----------------------------')
    # for item in data:
    #     for key, value in item.items():
    #         if type(value) is list:
    #             print(f'{key}: {', '.join(value)}')
    #         else:
    #             print(f'{key}: {value}')
    #     print('----------------------------')

    # А если ключу соответствует список
    pets_list = data['pets']

    print('----------------------------')
    for item in pets_list:
        for key, value in item.items():
            if type(value) is list:
                print(f'{key}: {', '.join(value)}')
            else:
                print(f'{key}: {value}')
        print('----------------------------')
