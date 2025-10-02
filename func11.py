# Потоковый ввод stdin
# Потоки, которые поддерживает python: stdin, stdout, stderr
# Прекращение потока: Ctrl + D (Pycharm и Linux)
# Прекращение потока: Ctrl + Z и Enter (консоль Windows)
import sys

data = sys.stdin.readlines()

data = list(map(lambda x: x.rstrip('\n'), data))

print(data)

# for s in sys.stdin:
#     print(s.rstrip('\n'))



# sys.stdout.write('Привет\n')
# sys.stdout.write('Пока\n')
# sys.stderr.write('Ошибка\n')
#
# print('Сообщение', file=sys.stderr)
