# Список (имитация стека)
stack = []

for i in range(5):
    stack.append(f'Простыня_{i + 1}')

print('Наполняем стек:')
for item in stack:
    print(item)

print('Удаляем стек:')
while stack:  # пока список не пустой
    print(stack.pop())
