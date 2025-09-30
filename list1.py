# Знакомство со списками
# lst = list()  # Пустой список
# lst = []  # Пустой список (способ 2)

lst = [11, '27' * 3, 43.4, 24, 5, True]
print(lst)
lst[0] = 55
print(lst[0] + 1)
zero_list = [0] * 10
print(zero_list)

from_1_10 = list(range(1, 11))
print(from_1_10)

s = {1, 2, 3}
s = list(s)
print(s[0])

num = [1, 2, 3, 3, 1, 2, 3, 2, 3, 1, 2]
num = set(num)
num = list(num)
print(num)

string = 'Python'
lst = list(string)
print(lst)

res = str(lst)
print(res)

if 'P' in lst:
    print('Есть в списке')
