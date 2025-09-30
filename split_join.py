# Методы строки split и join
s = '   один     два    три'
ip = '192.168.0.1'

d = ip.split('.')
print(d)

lst = s.split()
print(lst)

s = 'сабака'

lst = list(s)
lst[1] = 'о'
s = ''.join(lst)
print(s)

s = 'однажды      в     студёную     зимнюю      пору'
print(' '.join(s.split()))

name = '     Д   м  и  т   р    и     й     '
print(''.join(name.split()))  # убрать все пробелы
