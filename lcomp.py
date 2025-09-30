# Списочные выражения (list comprehension)
lst = []

# for i in range(1, 11):
#     lst.append(i ** 2)

# lst = [i ** 2 for i in range(1, 11)]
# lst = [i for i in range(1, 101) if i % 2 == 0]
ip = '192.168.1.0'
lst = [int(i) for i in ip.split('.')]

print(*lst, sep=', ')
