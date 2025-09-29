# Циклы (DRY - Don't repeat Yourself)
# for count in range(s, s, s)
# s - start (0 - по умолчанию)
# s - stop (не включая)
# s - step (1 - по умолчанию)
# for i in range(10) -> ... in range(0, 10, 1)

N = 10

for i in range(1, N + 1):
    if i % 2 == 0:
        print('Второй')
    else:
        print('Первый')

