# Cловари (key: value)
# d = dict()
d = {
    'стол': 'table',
    'стул': 'chair',
    'яблоко': 'apple',
    'питомец': 'собака',
    'имя': 'Рекс',
    'еда': ['Royal Canin', 'мясо']
}

print(d['стол'])
d['стол'] = 'из дерева'
d['name'] = 'имя'
print(d['name'])
d.pop('стол')
if d.pop('фамилия', None):
    print(f'Ключ "фамилия" удалён')
else:
    print(f'Ключа "фамилия" не существует')
print(d)

if 'стол' in d:
    print('Такой ключ есть в словаре')

for key in d:
    print(key, d[key])

