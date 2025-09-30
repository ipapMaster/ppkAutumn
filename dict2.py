# Методы словаря

d = {
    'питомец': 'кошка',
    'имя':  'Мурка'
}

# Получить список ключей
print(list(d.keys()))

# получить список значений
print(list(d.values()))

if 'Мурка' in d.values():
    print('Мурка есть')

# получить список пар
print(list(d.items()))

for k, v in d.items():
    print(k, v)

print('Как зовут кошку:', d.get('име', 'Такого ключа нет'))