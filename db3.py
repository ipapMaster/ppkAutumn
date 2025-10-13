# Базы данных
# Архиватор или структурированное хранение и передача
# JSON - Java Script Object Notation
# Запись в JSON:
# json.dump() - пишем прямо в файлы
# json.dumps() - отправляем JSON как строку
# Сохраним двух котов в JSON
import json

cats = {
    'name': 'Мурзик',
    'age': 1,
    'food': ['Wiskas', 'Hills'],
    'owner': {
        'f_name': 'Дмитрий',
        's_name': 'Петров',
    },
}

with open('data/cats.json', 'wt', encoding='utf-8') as cat_file:
    json.dump(cats, cat_file, indent=2, ensure_ascii=False)
