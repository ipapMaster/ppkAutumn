# Методы списков
# print(dir([]))
# lst = list(range(1, 11))
lst = []

for i in range(1, 11):
    lst.append(i)

lst2 = [11, 12]

# res = lst.extend(lst2)
res = lst + lst2 + [13, 14]

res.extend('Привет')  # в отличие от "+" преобразовывает "на лету"
res.extend({1, 2, 3})

print(res)
print(f'Длина итогового списка - {len(res)}')

res.insert(2, 2.5)

# Срезы такие же, как для строки
print(res[:5])  # до пятого элемента

# Удаление
res.remove(2.5)  # Удаляет если есть, или ошибка
res.pop()  # удаляет последний элемент и возвращает его (или по индексу)
print(res)
