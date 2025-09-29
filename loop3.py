# else и while
# else выполняется, если цикл завершился естественно
import random

num = random.randint(0, 10)  # 0 ... 10
attempts = 0

while attempts < 3:
    guess = int(input('Введите число: '))
    attempts += 1
    if guess == num:
        print('Ура, угадали!')
        break
    elif guess > num:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')
else:
    print('Попытки закончились! А число было:', num)  # если цикл завершился естественно
