# Базы данных
# Простые таблицы
# Comma Separated Values - *.csv
import csv

# with open('data/example.csv', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     cheap = filter(lambda x: int(x[3]) < 3000, list(reader)[1:])
#     for row in cheap:
#         print(row)

with open('data/example.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    expensive = sorted(reader, key=lambda x: int(x['цена']), reverse=True)

    print(expensive)

    for item in expensive:
        for k, v in item.items():
            print(f'{k}: {v}')
